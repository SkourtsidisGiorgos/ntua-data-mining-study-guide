# Επεξεργασία & Βελτιστοποίηση Ερωτημάτων (Query Processing)

## Βασικές Έννοιες - ΑΠΟΜΝΗΜΟΝΕΥΣΗ!

### Pipelining vs Materialization

| Χαρακτηριστικό | Pipelining | Materialization |
|----------------|------------|-----------------|
| Αποθήκευση | ΟΧΙ ενδιάμεσα | ΝΑΙ ενδιάμεσα στο δίσκο/μνήμη |
| Επεξεργασία | Tuple-by-tuple | Batch processing |
| Μνήμη | Χαμηλή | Υψηλή |
| Latency | Χαμηλή (άμεση έξοδος) | Υψηλή (περιμένει όλα) |

---

## Ερώτηση Εξέτασης 2025 (Q5)

**Ερώτηση:** Ποια πρόταση περιγράφει σωστά τη διαφορά μεταξύ pipelined evaluation και materialization;

**Σωστή απάντηση: (b)**
> "Η pipelined εκτέλεση επεξεργάζεται ένα tuple τη φορά και το περνάει στον επόμενο τελεστή, ενώ η materialization αποθηκεύει τα ενδιάμεσα αποτελέσματα σε μνήμη ή δίσκο πριν τα περάσει στους επόμενους τελεστές."

**Γιατί οι άλλες είναι λάθος:**
- (a) Αντιστρέφει τους ορισμούς
- (c) Pipelining δεν είναι μόνο για joins
- (d) Δεν είναι το ίδιο πράγμα

---

## Τελεστές: Pipelined vs Blocking

### Pipelined Operators (Μπορούν να παράγουν output άμεσα)

| Τελεστής | Εξήγηση |
|----------|---------|
| Selection (σ) | Φιλτράρει tuple-by-tuple |
| Projection (π) | Επιλέγει στήλες tuple-by-tuple |
| Nested Loop Join (outer) | Ο εξωτερικός βρόχος μπορεί να streamάρει |

### Blocking Operators (Χρειάζονται ΟΛΑ τα δεδομένα πρώτα)

| Τελεστής | Εξήγηση |
|----------|---------|
| Sort | Πρέπει να δει ΟΛΑ για να ταξινομήσει |
| Hash Join (build phase) | Πρέπει να χτίσει το hash table πρώτα |
| Aggregation (GROUP BY) | Πρέπει να δει όλες τις ομάδες |
| Duplicate elimination | Πρέπει να δει όλα για να βρει duplicates |

---

## Αλγόριθμοι Join

### 1. Nested Loop Join

**Ψευδοκώδικας:**
```
for each tuple r in R:
    for each tuple s in S:
        if θ(r, s):
            output (r, s)
```

**Κόστος:** O(n × m) - n tuples στο R, m tuples στο S

**Κατάλληλο για:**
- Μικρούς πίνακες
- Όταν υπάρχει index στον inner relation
- Inequality joins (< , >, ≠)

---

### 2. Hash Join

**Δύο φάσεις:**
1. **Build Phase:** Χτίσε hash table στο μικρότερο relation (blocking)
2. **Probe Phase:** Σαρώνει το μεγαλύτερο relation και κάνει lookup

**Κόστος:** O(n + m) - γραμμικό!

**Κατάλληλο για:**
- **ΜΟΝΟ equi-joins** (=)
- Όταν το μικρότερο relation χωράει στη μνήμη

**ΠΡΟΣΟΧΗ - Εξέταση Q7:** Hash Join **ΔΕΝ** είναι κατάλληλο για inequality joins!

---

### 3. Sort-Merge Join

**Τρεις φάσεις:**
1. **Sort R:** Ταξινόμηση του R στο join attribute
2. **Sort S:** Ταξινόμηση του S στο join attribute
3. **Merge:** Linear scan και των δύο (σαν merge sort)

**Κόστος:** O(n log n + m log m) για sorting + O(n + m) για merge

**Κατάλληλο για:**
- Equi-joins
- Ήδη ταξινομημένα δεδομένα
- Μεγάλα datasets που δεν χωράνε στη μνήμη

---

### Σύγκριση Αλγορίθμων Join

| Αλγόριθμος | Κόστος | Equi-Join | Inequality Join | Χρειάζεται Μνήμη |
|------------|--------|-----------|-----------------|------------------|
| Nested Loop | O(n×m) | ✓ | ✓ | Χαμηλή |
| Hash Join | O(n+m) | ✓ | ❌ | Build phase |
| Sort-Merge | O(n log n + m log m) | ✓ | ❌ | Sort buffers |

---

## Ερώτηση Εξέτασης 2025 (Q7)

**Ερώτηση:** Ποιος αλγόριθμος join ΔΕΝ είναι κατάλληλος για inequality joins;

**Απάντηση: (a) Hash Join**

**Εξήγηση:** Το Hash Join βασίζεται στην ισότητα τιμών για να λειτουργήσει το hashing. Ανισότητες (>, <, ≤, ≥) δεν μπορούν να εκμεταλλευτούν hash tables.

---

## Query Optimization Strategies

### 1. Σπρώξε τα Selections Νωρίτερα (Push Selection Down)

**Πριν:**
```
π_name(σ_dept='CS'(Employee ⋈ Department))
```

**Μετά (βελτιστοποιημένο):**
```
π_name(σ_dept='CS'(Employee) ⋈ Department)
```

**Γιατί:** Μειώνει τον αριθμό των tuples ΠΡΙΝ το join

---

### 2. Σπρώξε τα Projections Νωρίτερα (Push Projection Down)

Κράτα μόνο τις στήλες που χρειάζονται για τους επόμενους τελεστές.

---

### 3. Επιλογή Join Order

Για πολλαπλά joins, η σειρά επηρεάζει το κόστος:
- Αρχίζε με μικρά αποτελέσματα
- Χρησιμοποίησε indexes όπου υπάρχουν

---

## Cost-Based Optimization

### Παράγοντες Κόστους

1. **I/O Cost:** Πόσα blocks διαβάζονται/γράφονται
2. **CPU Cost:** Υπολογισμοί
3. **Memory Usage:** Buffer requirements
4. **Network Cost:** Για κατανεμημένες βάσεις

### Selectivity (Επιλεκτικότητα)

```
Selectivity = |σ_condition(R)| / |R|
```

- Selectivity ≈ 0: Πολύ λίγα tuples περνάνε
- Selectivity ≈ 1: Σχεδόν όλα τα tuples περνάνε

---

## Indexing για Query Performance

### Τύποι Index

| Τύπος | Καλό για | Κακό για |
|-------|----------|----------|
| B+ Tree | Range queries, ordering | Equality μόνο |
| Hash Index | Equality lookups | Range queries |
| Bitmap | Low cardinality, analytics | High cardinality, OLTP |

### Πότε χρησιμοποιείται Index

- Selectivity < 15% (εμπειρικός κανόνας)
- Συχνά queries στη στήλη
- Δεν αλλάζει συχνά (writes expensive)

---

## Παράδειγμα: Query Plan Analysis

**Query:**
```sql
SELECT E.name, D.dname
FROM Employee E, Department D
WHERE E.dept_id = D.id AND E.salary > 50000;
```

**Query Plan (μη βελτιστοποιημένο):**
```
π_name,dname
    |
σ_E.dept_id=D.id ∧ salary>50000
    |
    ×
   / \
  E   D
```

**Query Plan (βελτιστοποιημένο):**
```
π_name,dname
    |
   ⋈_{dept_id=id}
   / \
σ_salary>50000  D
  |
  E
```

**Βελτιώσεις:**
1. Push selection (salary > 50000) πριν το join
2. Αντικατέστησε Cartesian product + selection με join

---

## Συχνά Λάθη στις Εξετάσεις

### 1. Pipelining vs Blocking σύγχυση
- ❌ Sort είναι pipelined
- ✓ Sort είναι BLOCKING (χρειάζεται όλα τα δεδομένα)

### 2. Hash Join για inequality
- ❌ Hash Join δουλεύει για >
- ✓ Hash Join δουλεύει ΜΟΝΟ για =

### 3. Materialization = κακό
- ❌ Materialization πάντα αποφεύγεται
- ✓ Μερικές φορές είναι απαραίτητο (blocking operators)

---

## Γρήγορη Αναφορά

```
╔══════════════════════════════════════════════════════════════════╗
║              QUERY PROCESSING CHEAT SHEET                        ║
╠══════════════════════════════════════════════════════════════════╣
║ PIPELINING: Tuple-by-tuple, χαμηλή μνήμη, άμεση έξοδος           ║
║ MATERIALIZATION: Αποθήκευση ενδιάμεσων, blocking                 ║
╠══════════════════════════════════════════════════════════════════╣
║ PIPELINED:  σ, π, Nested Loop (outer)                            ║
║ BLOCKING:   Sort, Hash build, Aggregation, Distinct              ║
╠══════════════════════════════════════════════════════════════════╣
║ JOIN ALGORITHMS:                                                 ║
║   Nested Loop: O(n×m), works for all conditions                  ║
║   Hash Join:   O(n+m), ONLY equi-join (=)                        ║
║   Sort-Merge:  O(n log n), needs sorted data                     ║
╠══════════════════════════════════════════════════════════════════╣
║ INEQUALITY JOINS (>, <, ≤, ≥):                                   ║
║   ✓ Nested Loop Join                                             ║
║   ❌ Hash Join                                                    ║
║   ❌ Sort-Merge Join (standard version)                           ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Ασκήσεις Εξάσκησης

### Άσκηση 1
Δίνεται το query:
```sql
SELECT *
FROM A, B, C
WHERE A.x = B.x AND B.y = C.y AND A.z > 100;
```

1. Σχεδιάστε ένα μη-βελτιστοποιημένο query plan
2. Σχεδιάστε ένα βελτιστοποιημένο query plan
3. Εξηγήστε τις βελτιώσεις

### Άσκηση 2
Για κάθε τελεστή, αναφέρετε αν είναι pipelined ή blocking:
1. Selection με condition salary > 50000
2. Sort by name
3. Hash join build phase
4. Projection π_name,dept
5. GROUP BY department

### Άσκηση 3
Ποιος αλγόριθμος join είναι καλύτερος για τα εξής σενάρια;
1. Μικρός πίνακας join με μεγάλο, equality condition
2. Join με condition `A.date > B.date`
3. Και οι δύο πίνακες ήδη ταξινομημένοι στο join attribute
