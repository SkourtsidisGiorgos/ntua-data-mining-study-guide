"""
Database schema creation for the University SQL Training database.
"""
import sqlite3
from pathlib import Path


def create_database(db_path: str = None) -> str:
    """
    Create the university database with all tables.

    Args:
        db_path: Path to the database file. If None, creates in the database folder.

    Returns:
        Path to the created database.
    """
    if db_path is None:
        db_path = Path(__file__).parent / "university.db"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop existing tables if they exist (for clean recreation)
    tables = ['Writes', 'Enrolls', 'Publications', 'Courses', 'Professors', 'Students']
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")

    # Create Students table
    cursor.execute("""
        CREATE TABLE Students (
            sid INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            major TEXT NOT NULL,
            year INTEGER NOT NULL CHECK (year BETWEEN 1 AND 6),
            gpa REAL NOT NULL CHECK (gpa >= 0 AND gpa <= 10)
        )
    """)

    # Create Professors table
    cursor.execute("""
        CREATE TABLE Professors (
            prof_id INTEGER PRIMARY KEY,
            pname TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL CHECK (salary > 0),
            office_num TEXT
        )
    """)

    # Create Courses table (references Professors)
    cursor.execute("""
        CREATE TABLE Courses (
            cid TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            credits INTEGER NOT NULL CHECK (credits > 0),
            department TEXT NOT NULL,
            prof_id INTEGER,
            FOREIGN KEY (prof_id) REFERENCES Professors(prof_id)
        )
    """)

    # Create Enrolls table (M:N between Students and Courses)
    cursor.execute("""
        CREATE TABLE Enrolls (
            sid INTEGER,
            cid TEXT,
            grade REAL CHECK (grade IS NULL OR (grade >= 0 AND grade <= 10)),
            semester TEXT NOT NULL,
            PRIMARY KEY (sid, cid, semester),
            FOREIGN KEY (sid) REFERENCES Students(sid),
            FOREIGN KEY (cid) REFERENCES Courses(cid)
        )
    """)

    # Create Publications table
    cursor.execute("""
        CREATE TABLE Publications (
            pub_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            venue TEXT NOT NULL,
            year INTEGER NOT NULL CHECK (year > 1900)
        )
    """)

    # Create Writes table (M:N between Professors and Publications)
    cursor.execute("""
        CREATE TABLE Writes (
            prof_id INTEGER,
            pub_id INTEGER,
            PRIMARY KEY (prof_id, pub_id),
            FOREIGN KEY (prof_id) REFERENCES Professors(prof_id),
            FOREIGN KEY (pub_id) REFERENCES Publications(pub_id)
        )
    """)

    conn.commit()
    conn.close()

    return str(db_path)


def get_schema_description() -> str:
    """
    Returns a human-readable description of the database schema in Greek.
    """
    return """
📊 **Σχήμα Βάσης Δεδομένων Πανεπιστημίου**

**Students** (Φοιτητές)
- `sid` - Κωδικός φοιτητή (PRIMARY KEY)
- `name` - Όνομα φοιτητή
- `major` - Τμήμα σπουδών
- `year` - Έτος σπουδών (1-6)
- `gpa` - Μέσος όρος βαθμολογίας (0-10)

**Professors** (Καθηγητές)
- `prof_id` - Κωδικός καθηγητή (PRIMARY KEY)
- `pname` - Όνομα καθηγητή
- `department` - Τμήμα
- `salary` - Μισθός
- `office_num` - Αριθμός γραφείου

**Courses** (Μαθήματα)
- `cid` - Κωδικός μαθήματος (PRIMARY KEY)
- `title` - Τίτλος μαθήματος
- `credits` - Πιστωτικές μονάδες (ECTS)
- `department` - Τμήμα
- `prof_id` - Κωδικός διδάσκοντα (FOREIGN KEY → Professors)

**Enrolls** (Εγγραφές)
- `sid` - Κωδικός φοιτητή (FOREIGN KEY → Students)
- `cid` - Κωδικός μαθήματος (FOREIGN KEY → Courses)
- `grade` - Βαθμός (0-10, μπορεί να είναι NULL)
- `semester` - Εξάμηνο (π.χ. 'Fall2024')
- PRIMARY KEY: (sid, cid, semester)

**Publications** (Δημοσιεύσεις)
- `pub_id` - Κωδικός δημοσίευσης (PRIMARY KEY)
- `title` - Τίτλος δημοσίευσης
- `venue` - Συνέδριο/Περιοδικό
- `year` - Έτος δημοσίευσης

**Writes** (Συγγραφή)
- `prof_id` - Κωδικός καθηγητή (FOREIGN KEY → Professors)
- `pub_id` - Κωδικός δημοσίευσης (FOREIGN KEY → Publications)
- PRIMARY KEY: (prof_id, pub_id)

---
**Σχέσεις:**
- Ένας Καθηγητής διδάσκει πολλά Μαθήματα (1:N)
- Πολλοί Φοιτητές εγγράφονται σε πολλά Μαθήματα (M:N μέσω Enrolls)
- Πολλοί Καθηγητές γράφουν πολλές Δημοσιεύσεις (M:N μέσω Writes)
"""


if __name__ == "__main__":
    db_path = create_database()
    print(f"Database created at: {db_path}")
