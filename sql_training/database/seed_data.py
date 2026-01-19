"""
Seed data for the University SQL Training database.
"""
import sqlite3
from pathlib import Path


def seed_database(db_path: str = None) -> None:
    """
    Insert sample data into the university database.

    Args:
        db_path: Path to the database file. If None, uses the default location.
    """
    if db_path is None:
        db_path = Path(__file__).parent / "university.db"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # ==================== STUDENTS ====================
    students = [
        (1, 'Γιάννης Παπαδόπουλος', 'Πληροφορική', 3, 7.5),
        (2, 'Μαρία Κωνσταντίνου', 'Πληροφορική', 4, 8.2),
        (3, 'Νίκος Αντωνίου', 'Μαθηματικά', 2, 6.8),
        (4, 'Ελένη Γεωργίου', 'Πληροφορική', 3, 9.1),
        (5, 'Δημήτρης Νικολάου', 'Φυσική', 1, 7.0),
        (6, 'Αθηνά Παπαγεωργίου', 'Μαθηματικά', 4, 8.5),
        (7, 'Κώστας Δημητρίου', 'Πληροφορική', 2, 5.9),
        (8, 'Σοφία Ιωάννου', 'Φυσική', 3, 7.8),
        (9, 'Πέτρος Αλεξίου', 'Πληροφορική', 5, 8.0),
        (10, 'Άννα Μιχαήλ', 'Μαθηματικά', 1, 9.3),
        (11, 'Χρήστος Βασιλείου', 'Πληροφορική', 4, 6.5),
        (12, 'Κατερίνα Σταύρου', 'Φυσική', 2, 7.2),
        (13, 'Αλέξανδρος Παύλου', 'Πληροφορική', 3, 8.8),
        (14, 'Εύα Θεοδώρου', 'Μαθηματικά', 3, 7.1),
        (15, 'Μιχάλης Κυριάκου', 'Φυσική', 4, 6.0),
    ]
    cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", students)

    # ==================== PROFESSORS ====================
    professors = [
        (101, 'Δρ. Αναστασία Λεβέντη', 'Πληροφορική', 3200, 'Α101'),
        (102, 'Δρ. Βασίλης Καραγιάννης', 'Πληροφορική', 2800, 'Α102'),
        (103, 'Δρ. Γεωργία Μαυρίδου', 'Μαθηματικά', 3000, 'Β201'),
        (104, 'Δρ. Δημήτρης Σωτηρίου', 'Φυσική', 2900, 'Γ301'),
        (105, 'Δρ. Ειρήνη Χατζή', 'Πληροφορική', 3500, 'Α103'),
        (106, 'Δρ. Ζαχαρίας Παπά', 'Μαθηματικά', 2700, 'Β202'),
        (107, 'Δρ. Ηλίας Κόκκινος', 'Φυσική', 3100, None),
    ]
    cursor.executemany("INSERT INTO Professors VALUES (?, ?, ?, ?, ?)", professors)

    # ==================== COURSES ====================
    courses = [
        ('CS101', 'Εισαγωγή στον Προγραμματισμό', 6, 'Πληροφορική', 101),
        ('CS201', 'Δομές Δεδομένων', 6, 'Πληροφορική', 101),
        ('CS301', 'Βάσεις Δεδομένων', 6, 'Πληροφορική', 102),
        ('CS401', 'Μηχανική Μάθηση', 6, 'Πληροφορική', 105),
        ('CS402', 'Τεχνητή Νοημοσύνη', 6, 'Πληροφορική', 105),
        ('MA101', 'Γραμμική Άλγεβρα', 5, 'Μαθηματικά', 103),
        ('MA201', 'Απειροστικός Λογισμός', 5, 'Μαθηματικά', 103),
        ('MA301', 'Πιθανότητες & Στατιστική', 5, 'Μαθηματικά', 106),
        ('PH101', 'Γενική Φυσική I', 6, 'Φυσική', 104),
        ('PH201', 'Γενική Φυσική II', 6, 'Φυσική', 104),
        ('PH301', 'Κβαντική Φυσική', 6, 'Φυσική', 107),
    ]
    cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?, ?)", courses)

    # ==================== ENROLLS ====================
    enrolls = [
        # Γιάννης - CS major, 3rd year
        (1, 'CS101', 8.0, 'Fall2022'),
        (1, 'CS201', 7.5, 'Spring2023'),
        (1, 'CS301', 7.0, 'Fall2023'),
        (1, 'MA101', 6.5, 'Fall2022'),
        (1, 'CS401', None, 'Spring2024'),  # Currently taking

        # Μαρία - CS major, 4th year (excellent student)
        (2, 'CS101', 9.0, 'Fall2021'),
        (2, 'CS201', 8.5, 'Spring2022'),
        (2, 'CS301', 9.0, 'Fall2022'),
        (2, 'CS401', 8.0, 'Spring2023'),
        (2, 'CS402', 8.5, 'Fall2023'),
        (2, 'MA101', 8.0, 'Fall2021'),
        (2, 'MA201', 7.5, 'Spring2022'),

        # Νίκος - Math major, 2nd year
        (3, 'MA101', 7.0, 'Fall2023'),
        (3, 'MA201', 6.5, 'Spring2024'),
        (3, 'CS101', 6.0, 'Fall2023'),

        # Ελένη - CS major, 3rd year (top student)
        (4, 'CS101', 10.0, 'Fall2022'),
        (4, 'CS201', 9.5, 'Spring2023'),
        (4, 'CS301', 9.0, 'Fall2023'),
        (4, 'MA101', 9.0, 'Fall2022'),
        (4, 'MA201', 9.5, 'Spring2023'),
        (4, 'CS401', 9.0, 'Spring2024'),
        (4, 'CS402', None, 'Spring2024'),  # Currently taking

        # Δημήτρης - Physics major, 1st year
        (5, 'PH101', 7.5, 'Fall2024'),
        (5, 'MA101', 7.0, 'Fall2024'),

        # Αθηνά - Math major, 4th year
        (6, 'MA101', 9.0, 'Fall2021'),
        (6, 'MA201', 8.5, 'Spring2022'),
        (6, 'MA301', 8.0, 'Fall2022'),
        (6, 'CS101', 7.5, 'Fall2021'),
        (6, 'CS201', 8.0, 'Spring2022'),

        # Κώστας - CS major, 2nd year (struggling)
        (7, 'CS101', 5.5, 'Fall2023'),
        (7, 'MA101', 4.5, 'Fall2023'),
        (7, 'CS201', None, 'Spring2024'),  # Currently taking

        # Σοφία - Physics major, 3rd year
        (8, 'PH101', 8.0, 'Fall2022'),
        (8, 'PH201', 7.5, 'Spring2023'),
        (8, 'PH301', 8.0, 'Fall2023'),
        (8, 'MA101', 7.0, 'Fall2022'),
        (8, 'MA201', 7.5, 'Spring2023'),

        # Πέτρος - CS major, 5th year (all CS courses)
        (9, 'CS101', 8.0, 'Fall2020'),
        (9, 'CS201', 7.5, 'Spring2021'),
        (9, 'CS301', 8.0, 'Fall2021'),
        (9, 'CS401', 8.5, 'Spring2022'),
        (9, 'CS402', 8.0, 'Fall2022'),

        # Άννα - Math major, 1st year (excellent)
        (10, 'MA101', 10.0, 'Fall2024'),
        (10, 'CS101', 9.5, 'Fall2024'),

        # Χρήστος - CS major, 4th year
        (11, 'CS101', 6.5, 'Fall2021'),
        (11, 'CS201', 6.0, 'Spring2022'),
        (11, 'CS301', 7.0, 'Fall2022'),
        (11, 'MA101', 5.5, 'Fall2021'),

        # Κατερίνα - Physics major, 2nd year
        (12, 'PH101', 7.5, 'Fall2023'),
        (12, 'PH201', 7.0, 'Spring2024'),
        (12, 'MA101', 7.0, 'Fall2023'),

        # Αλέξανδρος - CS major, 3rd year
        (13, 'CS101', 9.0, 'Fall2022'),
        (13, 'CS201', 9.0, 'Spring2023'),
        (13, 'CS301', 8.5, 'Fall2023'),
        (13, 'CS401', 9.0, 'Spring2024'),
        (13, 'MA101', 8.0, 'Fall2022'),
        (13, 'MA301', 8.5, 'Spring2023'),

        # Εύα - Math major, 3rd year
        (14, 'MA101', 7.0, 'Fall2022'),
        (14, 'MA201', 7.5, 'Spring2023'),
        (14, 'MA301', 6.5, 'Fall2023'),
        (14, 'CS101', 6.5, 'Fall2022'),

        # Μιχάλης - Physics major, 4th year
        (15, 'PH101', 6.0, 'Fall2021'),
        (15, 'PH201', 5.5, 'Spring2022'),
        (15, 'PH301', 6.0, 'Fall2022'),
        (15, 'MA101', 5.0, 'Fall2021'),
    ]
    cursor.executemany("INSERT INTO Enrolls VALUES (?, ?, ?, ?)", enrolls)

    # ==================== PUBLICATIONS ====================
    publications = [
        (1, 'Deep Learning for Natural Language Processing', 'EMNLP', 2022),
        (2, 'Efficient Algorithms for Graph Processing', 'SIGMOD', 2021),
        (3, 'Neural Networks in Computer Vision', 'CVPR', 2023),
        (4, 'Database Query Optimization Techniques', 'VLDB', 2022),
        (5, 'Machine Learning at Scale', 'NeurIPS', 2023),
        (6, 'Quantum Computing Basics', 'Nature Physics', 2021),
        (7, 'Advanced Statistical Methods', 'JASA', 2022),
        (8, 'AI Ethics and Society', 'AI Magazine', 2023),
        (9, 'Big Data Analytics', 'IEEE BigData', 2022),
        (10, 'Reinforcement Learning Applications', 'ICML', 2023),
    ]
    cursor.executemany("INSERT INTO Publications VALUES (?, ?, ?, ?)", publications)

    # ==================== WRITES ====================
    writes = [
        # Δρ. Λεβέντη - 3 publications
        (101, 1),
        (101, 2),
        (101, 5),

        # Δρ. Καραγιάννης - 2 publications
        (102, 2),
        (102, 4),

        # Δρ. Μαυρίδου - 2 publications
        (103, 7),
        (103, 9),

        # Δρ. Σωτηρίου - 1 publication
        (104, 6),

        # Δρ. Χατζή - 4 publications (most prolific)
        (105, 1),
        (105, 3),
        (105, 5),
        (105, 8),
        (105, 10),

        # Δρ. Παπά - 1 publication
        (106, 7),

        # Δρ. Κόκκινος - 2 publications
        (107, 6),
        (107, 9),

        # Co-authored publications (some already listed above)
        # Pub 1: Λεβέντη + Χατζή
        # Pub 2: Λεβέντη + Καραγιάννης
        # Pub 5: Λεβέντη + Χατζή
        # Pub 6: Σωτηρίου + Κόκκινος
        # Pub 7: Μαυρίδου + Παπά
        # Pub 9: Μαυρίδου + Κόκκινος
    ]
    cursor.executemany("INSERT INTO Writes VALUES (?, ?)", writes)

    conn.commit()
    conn.close()


def get_sample_data_preview(db_path: str = None) -> dict:
    """
    Get a preview of sample data from each table.

    Returns:
        Dictionary with table names as keys and sample rows as values.
    """
    if db_path is None:
        db_path = Path(__file__).parent / "university.db"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    preview = {}
    tables = ['Students', 'Professors', 'Courses', 'Enrolls', 'Publications', 'Writes']

    for table in tables:
        cursor.execute(f"SELECT * FROM {table} LIMIT 3")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        preview[table] = {'columns': columns, 'rows': rows}

    conn.close()
    return preview


if __name__ == "__main__":
    from schema import create_database

    db_path = create_database()
    seed_database(db_path)
    print(f"Database seeded successfully at: {db_path}")

    # Show preview
    preview = get_sample_data_preview(db_path)
    for table, data in preview.items():
        print(f"\n{table}:")
        print(f"  Columns: {data['columns']}")
        for row in data['rows']:
            print(f"  {row}")
