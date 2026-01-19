# SQL Training System - Σύστημα Εκπαίδευσης SQL

Διαδραστικό εργαλείο εκπαίδευσης SQL με πραγματική βάση δεδομένων.

## Εγκατάσταση

```bash
# Μετάβαση στον φάκελο
cd sql_training

# Εγκατάσταση εξαρτήσεων
pip install -r requirements.txt
```

## Εκτέλεση

```bash
streamlit run app.py
```

Η εφαρμογή θα ανοίξει αυτόματα στο http://localhost:8501

## Χαρακτηριστικά

- **23 ερωτήσεις** σε 3 επίπεδα δυσκολίας
- **Πραγματική SQLite βάση δεδομένων** με δεδομένα πανεπιστημίου
- **Ασφαλής εκτέλεση** - μόνο SELECT ερωτήματα επιτρέπονται
- **Άμεση ανατροφοδότηση** - εκτελέστε ερωτήματα χωρίς βαθμολόγηση
- **Παρακολούθηση προόδου** - δείτε πόσες ερωτήσεις έχετε ολοκληρώσει

## Δομή Βάσης Δεδομένων

```
Students(sid, name, major, year, gpa)
Professors(prof_id, pname, department, salary, office_num)
Courses(cid, title, credits, department, prof_id)
Enrolls(sid, cid, grade, semester)
Publications(pub_id, title, venue, year)
Writes(prof_id, pub_id)
```

## Επίπεδα Δυσκολίας

| Επίπεδο | Αριθμός | Θέματα |
|---------|---------|--------|
| Μέτρια | 10 | SELECT, WHERE, απλά JOINs, COUNT/SUM/AVG, GROUP BY |
| Δύσκολη | 8 | Πολλαπλά JOINs, HAVING, υποερωτήματα |
| Πολύ Δύσκολη | 5 | SQL Division, φωλιασμένες συναθροίσεις |

## Δομή Φακέλων

```
sql_training/
├── app.py                    # Κύρια εφαρμογή Streamlit
├── requirements.txt          # Εξαρτήσεις Python
├── README.md                 # Οδηγίες
├── database/
│   ├── schema.py             # Δημιουργία σχήματος
│   ├── seed_data.py          # Δεδομένα δοκιμών
│   └── university.db         # Βάση SQLite (δημιουργείται αυτόματα)
├── questions/
│   ├── question_bank.py      # Τράπεζα ερωτήσεων
│   └── grading.py            # Λογική βαθμολόγησης
└── utils/
    └── query_executor.py     # Ασφαλής εκτέλεση SQL
```
