"""
Question bank for SQL Training System.
Contains 23 questions organized by difficulty level.
"""

# Difficulty levels with colors for UI
DIFFICULTY_LEVELS = {
    'moderate': {'label': 'Μέτρια', 'color': '#4CAF50'},      # Green
    'difficult': {'label': 'Δύσκολη', 'color': '#FF9800'},     # Orange
    'very_hard': {'label': 'Πολύ Δύσκολη', 'color': '#F44336'} # Red
}

QUESTIONS = [
    # ============================================================
    # MODERATE QUESTIONS (10)
    # Topics: SELECT, WHERE, simple JOIN, COUNT/SUM/AVG, GROUP BY, ORDER BY
    # ============================================================

    {
        'id': 1,
        'difficulty': 'moderate',
        'title': 'Όλοι οι φοιτητές',
        'description': 'Εμφανίστε όλα τα στοιχεία όλων των φοιτητών.',
        'hint': 'Χρησιμοποιήστε SELECT * για να επιλέξετε όλες τις στήλες.',
        'expected_query': 'SELECT * FROM Students',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 2,
        'difficulty': 'moderate',
        'title': 'Φοιτητές Πληροφορικής',
        'description': 'Βρείτε τα ονόματα των φοιτητών που σπουδάζουν Πληροφορική.',
        'hint': 'Χρησιμοποιήστε WHERE για να φιλτράρετε βάσει του major.',
        'expected_query': "SELECT name FROM Students WHERE major = 'Πληροφορική'",
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 3,
        'difficulty': 'moderate',
        'title': 'Καθηγητές με υψηλό μισθό',
        'description': 'Βρείτε τα ονόματα και τους μισθούς των καθηγητών που κερδίζουν πάνω από 3000€.',
        'hint': 'Χρησιμοποιήστε WHERE με σύγκριση αριθμών.',
        'expected_query': 'SELECT pname, salary FROM Professors WHERE salary > 3000',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 4,
        'difficulty': 'moderate',
        'title': 'Πλήθος φοιτητών',
        'description': 'Μετρήστε τον συνολικό αριθμό φοιτητών στη βάση δεδομένων.',
        'hint': 'Χρησιμοποιήστε τη συνάρτηση COUNT().',
        'expected_query': 'SELECT COUNT(*) FROM Students',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 5,
        'difficulty': 'moderate',
        'title': 'Μέσος όρος GPA ανά τμήμα',
        'description': 'Υπολογίστε τον μέσο όρο GPA για κάθε τμήμα σπουδών.',
        'hint': 'Χρησιμοποιήστε GROUP BY με AVG().',
        'expected_query': 'SELECT major, AVG(gpa) FROM Students GROUP BY major',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 6,
        'difficulty': 'moderate',
        'title': 'Φοιτητές με φθίνουσα σειρά GPA',
        'description': 'Εμφανίστε τα ονόματα και τα GPA όλων των φοιτητών ταξινομημένα κατά φθίνον GPA.',
        'hint': 'Χρησιμοποιήστε ORDER BY με DESC.',
        'expected_query': 'SELECT name, gpa FROM Students ORDER BY gpa DESC',
        'order_matters': True,
        'check_column_names': False
    },

    {
        'id': 7,
        'difficulty': 'moderate',
        'title': 'Μαθήματα Πληροφορικής',
        'description': 'Βρείτε τους τίτλους και τις πιστωτικές μονάδες των μαθημάτων του τμήματος Πληροφορικής.',
        'hint': 'Φιλτράρετε τον πίνακα Courses με WHERE.',
        'expected_query': "SELECT title, credits FROM Courses WHERE department = 'Πληροφορική'",
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 8,
        'difficulty': 'moderate',
        'title': 'Σύνολο πιστωτικών μονάδων',
        'description': 'Υπολογίστε το σύνολο των πιστωτικών μονάδων (ECTS) όλων των μαθημάτων.',
        'hint': 'Χρησιμοποιήστε τη συνάρτηση SUM().',
        'expected_query': 'SELECT SUM(credits) FROM Courses',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 9,
        'difficulty': 'moderate',
        'title': 'Εγγραφές με βαθμό άνω του 8',
        'description': 'Βρείτε τους κωδικούς φοιτητών και μαθημάτων για εγγραφές με βαθμό πάνω από 8.',
        'hint': 'Φιλτράρετε τον πίνακα Enrolls με WHERE.',
        'expected_query': 'SELECT sid, cid FROM Enrolls WHERE grade > 8',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 10,
        'difficulty': 'moderate',
        'title': 'Πλήθος φοιτητών ανά τμήμα',
        'description': 'Μετρήστε πόσοι φοιτητές υπάρχουν σε κάθε τμήμα.',
        'hint': 'Χρησιμοποιήστε GROUP BY με COUNT().',
        'expected_query': 'SELECT major, COUNT(*) FROM Students GROUP BY major',
        'order_matters': False,
        'check_column_names': False
    },

    # ============================================================
    # DIFFICULT QUESTIONS (8)
    # Topics: Multi-table JOINs, HAVING, IN/EXISTS subqueries, correlated subqueries
    # ============================================================

    {
        'id': 11,
        'difficulty': 'difficult',
        'title': 'Φοιτητές και μαθήματά τους',
        'description': 'Εμφανίστε τα ονόματα των φοιτητών μαζί με τους τίτλους των μαθημάτων στα οποία είναι εγγεγραμμένοι.',
        'hint': 'Χρησιμοποιήστε JOIN μεταξύ Students, Enrolls και Courses.',
        'expected_query': '''
            SELECT s.name, c.title
            FROM Students s
            JOIN Enrolls e ON s.sid = e.sid
            JOIN Courses c ON e.cid = c.cid
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 12,
        'difficulty': 'difficult',
        'title': 'Καθηγητές και μαθήματά τους',
        'description': 'Εμφανίστε τα ονόματα των καθηγητών μαζί με τους τίτλους των μαθημάτων που διδάσκουν.',
        'hint': 'Χρησιμοποιήστε JOIN μεταξύ Professors και Courses.',
        'expected_query': '''
            SELECT p.pname, c.title
            FROM Professors p
            JOIN Courses c ON p.prof_id = c.prof_id
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 13,
        'difficulty': 'difficult',
        'title': 'Τμήματα με μέσο GPA > 7.5',
        'description': 'Βρείτε τα τμήματα που έχουν μέσο όρο GPA φοιτητών μεγαλύτερο από 7.5.',
        'hint': 'Χρησιμοποιήστε GROUP BY με HAVING.',
        'expected_query': '''
            SELECT major
            FROM Students
            GROUP BY major
            HAVING AVG(gpa) > 7.5
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 14,
        'difficulty': 'difficult',
        'title': 'Φοιτητές σε μάθημα Βάσεις Δεδομένων',
        'description': 'Βρείτε τα ονόματα των φοιτητών που είναι εγγεγραμμένοι στο μάθημα "Βάσεις Δεδομένων".',
        'hint': 'Χρησιμοποιήστε JOIN ή υποερώτημα με IN.',
        'expected_query': '''
            SELECT s.name
            FROM Students s
            JOIN Enrolls e ON s.sid = e.sid
            JOIN Courses c ON e.cid = c.cid
            WHERE c.title = 'Βάσεις Δεδομένων'
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 15,
        'difficulty': 'difficult',
        'title': 'Καθηγητές με δημοσιεύσεις μετά το 2022',
        'description': 'Βρείτε τα ονόματα των καθηγητών που έχουν δημοσιεύσεις μετά το 2022.',
        'hint': 'Χρησιμοποιήστε JOIN μεταξύ Professors, Writes και Publications.',
        'expected_query': '''
            SELECT DISTINCT p.pname
            FROM Professors p
            JOIN Writes w ON p.prof_id = w.prof_id
            JOIN Publications pub ON w.pub_id = pub.pub_id
            WHERE pub.year > 2022
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 16,
        'difficulty': 'difficult',
        'title': 'Φοιτητές με GPA πάνω από τον μέσο όρο',
        'description': 'Βρείτε τα ονόματα και τα GPA των φοιτητών που έχουν GPA πάνω από τον συνολικό μέσο όρο.',
        'hint': 'Χρησιμοποιήστε υποερώτημα για τον υπολογισμό του μέσου όρου.',
        'expected_query': '''
            SELECT name, gpa
            FROM Students
            WHERE gpa > (SELECT AVG(gpa) FROM Students)
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 17,
        'difficulty': 'difficult',
        'title': 'Πλήθος εγγραφών ανά μάθημα',
        'description': 'Βρείτε τον τίτλο κάθε μαθήματος και τον αριθμό εγγεγραμμένων φοιτητών, μόνο για μαθήματα με τουλάχιστον 3 εγγραφές.',
        'hint': 'Χρησιμοποιήστε JOIN, GROUP BY και HAVING.',
        'expected_query': '''
            SELECT c.title, COUNT(*) as enrollments
            FROM Courses c
            JOIN Enrolls e ON c.cid = e.cid
            GROUP BY c.cid, c.title
            HAVING COUNT(*) >= 3
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 18,
        'difficulty': 'difficult',
        'title': 'Καθηγητές χωρίς γραφείο',
        'description': 'Βρείτε τα ονόματα των καθηγητών που δεν έχουν αριθμό γραφείου καταχωρημένο.',
        'hint': 'Χρησιμοποιήστε IS NULL για να ελέγξετε για κενές τιμές.',
        'expected_query': '''
            SELECT pname
            FROM Professors
            WHERE office_num IS NULL
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    # ============================================================
    # VERY HARD QUESTIONS (5)
    # Topics: SQL Division (double NOT EXISTS), nested aggregations, complex patterns
    # ============================================================

    {
        'id': 19,
        'difficulty': 'very_hard',
        'title': 'Φοιτητές σε όλα τα μαθήματα Πληροφορικής',
        'description': 'Βρείτε τα ονόματα των φοιτητών που έχουν εγγραφεί σε ΟΛΑ τα μαθήματα του τμήματος Πληροφορικής (SQL Division).',
        'hint': 'Χρησιμοποιήστε διπλό NOT EXISTS για SQL Division: "δεν υπάρχει μάθημα που να μην το έχει πάρει".',
        'expected_query': '''
            SELECT s.name
            FROM Students s
            WHERE NOT EXISTS (
                SELECT c.cid
                FROM Courses c
                WHERE c.department = 'Πληροφορική'
                AND NOT EXISTS (
                    SELECT 1
                    FROM Enrolls e
                    WHERE e.sid = s.sid
                    AND e.cid = c.cid
                )
            )
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 20,
        'difficulty': 'very_hard',
        'title': 'Καθηγητής με τις περισσότερες δημοσιεύσεις',
        'description': 'Βρείτε το όνομα του καθηγητή (ή των καθηγητών) με τον μεγαλύτερο αριθμό δημοσιεύσεων.',
        'hint': 'Χρησιμοποιήστε υποερώτημα για να βρείτε το μέγιστο πλήθος δημοσιεύσεων.',
        'expected_query': '''
            SELECT p.pname
            FROM Professors p
            JOIN Writes w ON p.prof_id = w.prof_id
            GROUP BY p.prof_id, p.pname
            HAVING COUNT(*) = (
                SELECT MAX(pub_count)
                FROM (
                    SELECT COUNT(*) as pub_count
                    FROM Writes
                    GROUP BY prof_id
                )
            )
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 21,
        'difficulty': 'very_hard',
        'title': 'Φοιτητές με βαθμό πάνω από τον μέσο όρο κάθε μαθήματος',
        'description': 'Βρείτε τα ονόματα των φοιτητών που σε ΚΑΘΕ μάθημα που πήραν, είχαν βαθμό πάνω από τον μέσο όρο αυτού του μαθήματος.',
        'hint': 'Χρησιμοποιήστε correlated subquery: για κάθε εγγραφή του φοιτητή, σύγκρινε με τον μέσο όρο του συγκεκριμένου μαθήματος.',
        'expected_query': '''
            SELECT DISTINCT s.name
            FROM Students s
            WHERE NOT EXISTS (
                SELECT 1
                FROM Enrolls e1
                WHERE e1.sid = s.sid
                AND e1.grade IS NOT NULL
                AND e1.grade <= (
                    SELECT AVG(e2.grade)
                    FROM Enrolls e2
                    WHERE e2.cid = e1.cid
                    AND e2.grade IS NOT NULL
                )
            )
            AND EXISTS (
                SELECT 1
                FROM Enrolls e3
                WHERE e3.sid = s.sid
                AND e3.grade IS NOT NULL
            )
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 22,
        'difficulty': 'very_hard',
        'title': 'Τμήμα με τον υψηλότερο μέσο όρο μισθών',
        'description': 'Βρείτε το τμήμα με τον υψηλότερο μέσο μισθό καθηγητών.',
        'hint': 'Χρησιμοποιήστε φωλιασμένα GROUP BY με υποερώτημα για το μέγιστο.',
        'expected_query': '''
            SELECT department
            FROM Professors
            GROUP BY department
            HAVING AVG(salary) = (
                SELECT MAX(avg_sal)
                FROM (
                    SELECT AVG(salary) as avg_sal
                    FROM Professors
                    GROUP BY department
                )
            )
        ''',
        'order_matters': False,
        'check_column_names': False
    },

    {
        'id': 23,
        'difficulty': 'very_hard',
        'title': 'Ζεύγη καθηγητών με κοινή δημοσίευση',
        'description': 'Βρείτε όλα τα ζεύγη καθηγητών (ονόματα) που έχουν συν-γράψει τουλάχιστον μία δημοσίευση.',
        'hint': 'Χρησιμοποιήστε self-join στον πίνακα Writes. Χρησιμοποιήστε < για να αποφύγετε διπλότυπα ζεύγη.',
        'expected_query': '''
            SELECT DISTINCT p1.pname, p2.pname
            FROM Writes w1
            JOIN Writes w2 ON w1.pub_id = w2.pub_id AND w1.prof_id < w2.prof_id
            JOIN Professors p1 ON w1.prof_id = p1.prof_id
            JOIN Professors p2 ON w2.prof_id = p2.prof_id
        ''',
        'order_matters': False,
        'check_column_names': False
    },
]


def get_questions_by_difficulty(difficulty: str = None) -> list:
    """
    Get questions filtered by difficulty level.

    Args:
        difficulty: 'moderate', 'difficult', 'very_hard', or None for all.

    Returns:
        List of questions matching the difficulty filter.
    """
    if difficulty is None:
        return QUESTIONS
    return [q for q in QUESTIONS if q['difficulty'] == difficulty]


def get_question_by_id(question_id: int) -> dict:
    """
    Get a specific question by its ID.

    Args:
        question_id: The question ID.

    Returns:
        Question dictionary or None if not found.
    """
    for q in QUESTIONS:
        if q['id'] == question_id:
            return q
    return None


def get_question_count() -> dict:
    """
    Get count of questions by difficulty.

    Returns:
        Dictionary with difficulty levels as keys and counts as values.
    """
    counts = {'moderate': 0, 'difficult': 0, 'very_hard': 0, 'total': 0}
    for q in QUESTIONS:
        counts[q['difficulty']] += 1
        counts['total'] += 1
    return counts
