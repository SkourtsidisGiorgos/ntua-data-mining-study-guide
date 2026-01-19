"""
Safe SQL query execution utilities.
"""
import sqlite3
import pandas as pd
import re
from pathlib import Path
from typing import Tuple, Optional

# Blocked keywords for safety
BLOCKED_KEYWORDS = [
    'INSERT', 'UPDATE', 'DELETE', 'DROP', 'CREATE', 'ALTER',
    'TRUNCATE', 'REPLACE', 'ATTACH', 'DETACH', 'VACUUM',
    'PRAGMA', 'REINDEX', 'ANALYZE'
]


def is_safe_query(query: str) -> Tuple[bool, str]:
    """
    Check if a query is safe (read-only).

    Args:
        query: The SQL query to check.

    Returns:
        Tuple of (is_safe, error_message). If safe, error_message is empty.
    """
    # Remove comments and normalize whitespace
    query_clean = re.sub(r'--.*$', '', query, flags=re.MULTILINE)
    query_clean = re.sub(r'/\*.*?\*/', '', query_clean, flags=re.DOTALL)
    query_upper = query_clean.upper().strip()

    # Check for multiple statements (semicolon in middle)
    statements = [s.strip() for s in query_clean.split(';') if s.strip()]
    if len(statements) > 1:
        return False, "Μόνο ένα ερώτημα επιτρέπεται κάθε φορά."

    # Check for blocked keywords
    for keyword in BLOCKED_KEYWORDS:
        pattern = r'\b' + keyword + r'\b'
        if re.search(pattern, query_upper):
            return False, f"Η εντολή '{keyword}' δεν επιτρέπεται. Μόνο SELECT ερωτήματα επιτρέπονται."

    # Must start with SELECT or WITH (for CTEs)
    if not (query_upper.startswith('SELECT') or query_upper.startswith('WITH')):
        return False, "Μόνο SELECT ερωτήματα επιτρέπονται."

    return True, ""


def execute_query(query: str, db_path: str = None) -> Tuple[Optional[pd.DataFrame], str]:
    """
    Execute a SQL query and return results as a DataFrame.

    Args:
        query: The SQL query to execute.
        db_path: Path to the database. If None, uses default location.

    Returns:
        Tuple of (DataFrame or None, error_message).
        If successful, error_message is empty and DataFrame contains results.
        If failed, DataFrame is None and error_message contains the error.
    """
    if db_path is None:
        db_path = Path(__file__).parent.parent / "database" / "university.db"

    # First check if query is safe
    is_safe, error_msg = is_safe_query(query)
    if not is_safe:
        return None, error_msg

    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA query_only = ON")  # Extra safety

        df = pd.read_sql_query(query, conn)
        conn.close()

        return df, ""

    except sqlite3.Error as e:
        return None, f"Σφάλμα SQL: {str(e)}"
    except Exception as e:
        return None, f"Σφάλμα: {str(e)}"


def get_table_info(db_path: str = None) -> dict:
    """
    Get information about all tables in the database.

    Returns:
        Dictionary with table names and their column info.
    """
    if db_path is None:
        db_path = Path(__file__).parent.parent / "database" / "university.db"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]

    table_info = {}
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table})")
        columns = cursor.fetchall()
        table_info[table] = [
            {
                'name': col[1],
                'type': col[2],
                'notnull': col[3],
                'pk': col[5]
            }
            for col in columns
        ]

    conn.close()
    return table_info


def get_row_counts(db_path: str = None) -> dict:
    """
    Get row counts for all tables.

    Returns:
        Dictionary with table names and their row counts.
    """
    if db_path is None:
        db_path = Path(__file__).parent.parent / "database" / "university.db"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]

    counts = {}
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        counts[table] = cursor.fetchone()[0]

    conn.close()
    return counts
