"""
Grading logic for SQL query results.
"""
import pandas as pd
from typing import Tuple


def normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize a DataFrame for comparison.
    - Convert all columns to string
    - Strip whitespace
    - Handle None/NULL values consistently
    """
    df = df.copy()

    # Convert all columns to string for consistent comparison
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()
        # Normalize NULL representations
        df[col] = df[col].replace(['None', 'nan', 'NaN', 'null', 'NULL', ''], 'NULL')

    # Normalize column names (lowercase, strip)
    df.columns = [str(col).lower().strip() for col in df.columns]

    return df


def compare_results(
    user_df: pd.DataFrame,
    expected_df: pd.DataFrame,
    order_matters: bool = False,
    check_column_names: bool = False
) -> Tuple[bool, str]:
    """
    Compare user query results with expected results.

    Args:
        user_df: DataFrame from user's query
        expected_df: DataFrame from expected query
        order_matters: If True, row order must match
        check_column_names: If True, column names must match exactly

    Returns:
        Tuple of (is_correct: bool, feedback: str)
    """
    # Handle empty results
    if user_df is None and expected_df is None:
        return True, "Σωστό! Και τα δύο ερωτήματα επέστρεψαν κενά αποτελέσματα."

    if user_df is None:
        return False, "Το ερώτημά σας δεν εκτελέστηκε σωστά."

    if expected_df is None:
        return False, "Σφάλμα στην αναμενόμενη απάντηση."

    user_normalized = normalize_dataframe(user_df)
    expected_normalized = normalize_dataframe(expected_df)

    # Check row count
    if len(user_normalized) != len(expected_normalized):
        return False, (
            f"Λάθος αριθμός γραμμών. "
            f"Αναμένονταν {len(expected_normalized)} γραμμές, "
            f"επιστράφηκαν {len(user_normalized)}."
        )

    # Check column count
    if len(user_normalized.columns) != len(expected_normalized.columns):
        return False, (
            f"Λάθος αριθμός στηλών. "
            f"Αναμένονταν {len(expected_normalized.columns)} στήλες, "
            f"επιστράφηκαν {len(user_normalized.columns)}."
        )

    # Optional: Check column names
    if check_column_names:
        user_cols = list(user_normalized.columns)
        expected_cols = list(expected_normalized.columns)
        if user_cols != expected_cols:
            return False, (
                f"Λάθος ονόματα στηλών.\n"
                f"Αναμένονταν: {expected_cols}\n"
                f"Επιστράφηκαν: {user_cols}"
            )

    # Handle empty DataFrames (both with 0 rows)
    if len(user_normalized) == 0 and len(expected_normalized) == 0:
        return True, "Σωστό! Κενό αποτέλεσμα (όπως αναμενόταν)."

    # Sort both DataFrames if order doesn't matter
    if not order_matters:
        # Sort by all columns for consistent comparison
        user_normalized = user_normalized.sort_values(
            by=list(user_normalized.columns)
        ).reset_index(drop=True)
        expected_normalized = expected_normalized.sort_values(
            by=list(expected_normalized.columns)
        ).reset_index(drop=True)

    # Compare values column by column
    try:
        # Reset column names to match for comparison
        user_values = user_normalized.values
        expected_values = expected_normalized.values

        # Compare each cell
        mismatches = []
        for i in range(len(user_values)):
            for j in range(len(user_values[i])):
                if str(user_values[i][j]) != str(expected_values[i][j]):
                    mismatches.append((i, j, user_values[i][j], expected_values[i][j]))

        if mismatches:
            # Report first few mismatches
            mismatch_msg = "Διαφορές στα δεδομένα:\n"
            for idx, (row, col, user_val, exp_val) in enumerate(mismatches[:3]):
                mismatch_msg += f"  Γραμμή {row+1}, Στήλη {col+1}: "
                mismatch_msg += f"'{user_val}' αντί για '{exp_val}'\n"
            if len(mismatches) > 3:
                mismatch_msg += f"  ... και {len(mismatches) - 3} ακόμη διαφορές."
            return False, mismatch_msg

    except Exception as e:
        return False, f"Σφάλμα κατά τη σύγκριση: {str(e)}"

    return True, "Σωστό! Το ερώτημά σας επέστρεψε τα αναμενόμενα αποτελέσματα."


def get_diff_summary(user_df: pd.DataFrame, expected_df: pd.DataFrame) -> str:
    """
    Generate a summary of differences between user and expected results.
    Useful for debugging when a submission is wrong.
    """
    if user_df is None:
        return "Δεν υπάρχουν αποτελέσματα από το ερώτημά σας."

    if expected_df is None:
        return "Σφάλμα: Δεν βρέθηκε αναμενόμενη απάντηση."

    summary = []

    # Row count
    user_rows = len(user_df)
    expected_rows = len(expected_df)
    if user_rows != expected_rows:
        summary.append(f"• Γραμμές: {user_rows} (αναμένονταν {expected_rows})")

    # Column count
    user_cols = len(user_df.columns)
    expected_cols = len(expected_df.columns)
    if user_cols != expected_cols:
        summary.append(f"• Στήλες: {user_cols} (αναμένονταν {expected_cols})")

    if not summary:
        summary.append("• Οι διαστάσεις είναι σωστές, αλλά τα δεδομένα διαφέρουν.")

    return "\n".join(summary)
