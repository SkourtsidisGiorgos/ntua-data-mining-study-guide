# Data Mining Study Guide 📚

**Οδηγός Μελέτης για το μάθημα Εξόρυξη Γνώσης από Δεδομένα (DSML851)**

Σχολή Ηλεκτρολόγων Μηχανικών και Μηχανικών Υπολογιστών - ΕΜΠ

Διδάσκοντες: Δ. Τσουμάκος, Γ. Αλεξανδρίδης

---

## ⚠️ Σημαντική Σημείωση

**Όλο το περιεχόμενο αυτού του repository έχει δημιουργηθεί με τη βοήθεια AI (Claude).**

Παρόλο που έχει γίνει προσπάθεια για ακρίβεια, ενδέχεται να υπάρχουν λάθη ή ανακρίβειες. Χρησιμοποιήστε το υλικό ως συμπληρωματικό εργαλείο μελέτης και όχι ως μοναδική πηγή. Συνιστάται η διασταύρωση με τις επίσημες διαφάνειες και σημειώσεις του μαθήματος.

---

## 🎯 Για την Εξεταστική 2025-2026

**Το αρχείο 'σημειώσεις_εξόρυξη_απο_ΑΙ.pdf' περιείχε όλη την ύλη που χρειαζόταν για να γράψεις 10 στην εξεταστική Ιανουαρίου 2025-2026.**

---

## 📁 Δομή Repository

```
Data_Mining_Study_Guide/
├── markdown/                  # Οδηγός μελέτης σε Markdown format
├── LaTeX/                     # LaTeX source + compiled PDF
├── sql_training/              # Interactive SQL training system
├── παλια_και_νεα_υλη/         # Υλικό παλιάς και νέας ύλης
├── παλια_θέματα/              # Παλιά θέματα εξετάσεων
└── σημειώσεις_εξόρυξη_απο_ΑΙ.pdf
```

---

## 📖 Περιεχόμενα Οδηγού Μελέτης

### Κύρια Θέματα (Νέα Ύλη 2024-25)

| Κεφάλαιο | Θέμα |
|----------|------|
| 01 | E-R Model & Database Design |
| 02 | Relational Model & Relational Algebra |
| 03 | SQL (Basics & Advanced) |
| 04 | Query Processing & Optimization |
| 05 | Data Preprocessing |
| 06 | Data Streams (Bloom Filters, Count-Min Sketch) |
| 07 | Hidden Markov Models & Sequences |
| 08 | OLAP & Data Warehousing |
| 09 | RAG & Large Language Models |
| 10 | Formulas Cheatsheet |
| 11 | Practice Exam |

### Επιπλέον Υλικό (παλια_και_νεα_υλη/)

- Decision Trees & Classification
- Clustering (DBSCAN, K-Means)
- Association Rules (Apriori)
- Bayesian Networks
- Privacy & K-Anonymity
- DTW & Similarity Measures
- Text Mining & TF-IDF
- Query Containment

---

## 🖥️ SQL Training System

Ένα interactive σύστημα εξάσκησης SQL με Streamlit.

### Εγκατάσταση & Εκτέλεση

```bash
cd sql_training
pip install -r requirements.txt
streamlit run app.py
```

### Χαρακτηριστικά

- **23 ερωτήσεις** σε 3 επίπεδα δυσκολίας (Μέτριο, Δύσκολο, Πολύ Δύσκολο)
- Real database με university schema
- Instant feedback για τις απαντήσεις
- Safe query execution (μόνο SELECT queries)

### Database Schema

```
Students(sid, name, major, year, gpa)
Professors(prof_id, pname, department, salary, office_num)
Courses(cid, title, credits, department, prof_id)
Enrolls(sid, cid, grade, semester)
Publications(pub_id, title, venue, year)
Writes(prof_id, pub_id)
```

---

## 📊 Κατανομή Βαρύτητας Θεμάτων (Εκτίμηση)

| Θέμα | Βαρύτητα |
|------|----------|
| OLAP & Data Warehousing | ~25% |
| SQL | ~20% |
| Data Streams | ~15% |
| HMM & Sequences | ~15% |
| Query Processing | ~10% |
| Data Preprocessing | ~10% |
| RAG & LLMs | ~5% |

---

## 🛠️ Technologies

- **Python** (Streamlit, Pandas, SQLite)
- **LaTeX/XeLaTeX** (για το PDF)
- **Markdown** (για γρήγορη αναφορά)
- **SQLite** (για το training database)

---

## 📄 License

Για εκπαιδευτική χρήση.

---

*Καλή επιτυχία στις εξετάσεις! 🍀*
