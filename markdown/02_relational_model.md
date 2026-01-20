# Σχεσιακό Μοντέλο & Σχεσιακή Άλγεβρα

## Βασικοί Τελεστές - ΑΠΟΜΝΗΜΟΝΕΥΣΗ!

| Σύμβολο | Όνομα | Περιγραφή | SQL Αντίστοιχο |
|---------|-------|-----------|----------------|
| σ | Selection | Επιλογή γραμμών (filter) | WHERE |
| π | Projection | Επιλογή στηλών | SELECT columns |
| ∪ | Union | Ένωση συνόλων | UNION |
| ∩ | Intersection | Τομή συνόλων | INTERSECT |
| − | Difference | Διαφορά συνόλων | EXCEPT |
| × | Cartesian Product | Καρτεσιανό γινόμενο | FROM A, B |
| ⋈ | Natural Join | Ένωση με κοινές στήλες | NATURAL JOIN |
| ⋈θ | Theta Join | Ένωση με συνθήκη | JOIN ON |
| ρ | Rename | Μετονομασία | AS |
| ÷ | Division | "Για όλα" queries | (σύνθετο) |

---

## Selection (σ) - Επιλογή Γραμμών

### Σύνταξη
```
σ_condition(R)
```

### Συνθήκες (Conditions)
- Σύγκριση: `=`, `≠`, `<`, `>`, `≤`, `≥`
- Λογικοί τελεστές: `AND (∧)`, `OR (∨)`, `NOT (¬)`

### Παράδειγμα

**Πίνακας Employee:**
| name | dept | salary |
|------|------|--------|
| Alice | CS | 50000 |
| Bob | Math | 45000 |
| Carol | CS | 60000 |

**Query:** `σ_dept='CS'(Employee)`

**Αποτέλεσμα:**
| name | dept | salary |
|------|------|--------|
| Alice | CS | 50000 |
| Carol | CS | 60000 |

**Query με σύνθετη συνθήκη:** `σ_salary>48000 ∧ dept='CS'(Employee)`

**Αποτέλεσμα:**
| name | dept | salary |
|------|------|--------|
| Alice | CS | 50000 |
| Carol | CS | 60000 |

---

## Projection (π) - Επιλογή Στηλών

### Σύνταξη
```
π_attr1, attr2, ...(R)
```

### ΣΗΜΑΝΤΙΚΟ: Αφαιρεί τα διπλότυπα!

### Παράδειγμα

**Query:** `π_name, dept(Employee)`

**Αποτέλεσμα:**
| name | dept |
|------|------|
| Alice | CS |
| Bob | Math |
| Carol | CS |

**Query:** `π_dept(Employee)`

**Αποτέλεσμα:** `{CS, Math}` ← Τα duplicates αφαιρούνται!

---

## Πράξεις Συνόλων (∪, ∩, −)

### ΠΡΟΣΟΧΗ: Απαιτούν συμβατά schemas!

Για να εφαρμοστούν `∪`, `∩`, `−`, οι πίνακες ΠΡΕΠΕΙ να έχουν:
- Ίδιο αριθμό στηλών
- Συμβατούς τύπους δεδομένων

### Παράδειγμα

**R:** {1, 2, 3}
**S:** {2, 3, 4}

| Πράξη | Αποτέλεσμα |
|-------|------------|
| R ∪ S | {1, 2, 3, 4} |
| R ∩ S | {2, 3} |
| R − S | {1} |

---

## Natural Join (⋈)

### Λειτουργία
Ενώνει πίνακες στις **κοινές στήλες** (ίδιο όνομα ΚΑΙ τιμή).

### Παράδειγμα

**Student:**
| sid | name |
|-----|------|
| 1 | Alice |
| 2 | Bob |

**Enrolls:**
| sid | course |
|-----|--------|
| 1 | CS101 |
| 1 | CS102 |
| 3 | CS101 |

**Query:** `Student ⋈ Enrolls`

**Αποτέλεσμα:**
| sid | name | course |
|-----|------|--------|
| 1 | Alice | CS101 |
| 1 | Alice | CS102 |

*Σημείωση: sid=2 (Bob) δεν εμφανίζεται (δεν υπάρχει στο Enrolls), sid=3 δεν εμφανίζεται (δεν υπάρχει στο Student)*

---

## Theta Join (⋈θ)

### Σύνταξη
```
R ⋈_θ S = σ_θ(R × S)
```

Join με arbitrary condition (όχι μόνο ισότητα).

---

## Outer Joins

| Τύπος | Σύμβολο | Περιγραφή |
|-------|---------|-----------|
| Left Outer | ⟕ | Κρατάει ΟΛΕΣ τις γραμμές του R (NULL για unmatched) |
| Right Outer | ⟖ | Κρατάει ΟΛΕΣ τις γραμμές του S (NULL για unmatched) |
| Full Outer | ⟗ | Κρατάει ΟΛΕΣ τις γραμμές και των δύο |

---

## Division (÷) - "Για Όλα" Queries

### Χρήση
Όταν θέλουμε να βρούμε τα tuples που σχετίζονται με **ΟΛΑ** τα elements ενός συνόλου.

### Τύπος
```
R(A, B) ÷ S(B) = {a | για ΚΑΘΕ b ∈ S, (a, b) ∈ R}
```

### Παράδειγμα
**Ερώτηση:** Βρες τους φοιτητές που είναι εγγεγραμμένοι σε ΟΛΑ τα μαθήματα.

```
π_sid,cid(Enrolls) ÷ π_cid(Course)
```

---

## Λυμένα Παραδείγματα

### Παράδειγμα 1: SQL → Relational Algebra (Στυλ Εξέτασης)

**Πίνακες:**
- `Student(sid, name, dept)`
- `Course(cid, title, credits)`
- `Enrolls(sid, cid, grade)`

**Query:** Βρες τα ονόματα των CS φοιτητών που είναι εγγεγραμμένοι σε μαθήματα με ≥4 credits.

**SQL:**
```sql
SELECT DISTINCT S.name
FROM Student S, Enrolls E, Course C
WHERE S.sid = E.sid
  AND E.cid = C.cid
  AND S.dept = 'CS'
  AND C.credits >= 4;
```

**Relational Algebra - Βήμα προς Βήμα:**

**Βήμα 1:** Φίλτραρε φοιτητές από CS
```
R₁ = σ_dept='CS'(Student)
```

**Βήμα 2:** Φίλτραρε μαθήματα με ≥4 credits
```
R₂ = σ_credits≥4(Course)
```

**Βήμα 3:** Join με Enrolls
```
R₃ = R₁ ⋈ Enrolls ⋈ R₂
```

**Βήμα 4:** Project name
```
Result = π_name(R₃)
```

**Τελική Απάντηση (μία έκφραση):**
```
π_name(σ_dept='CS'(Student) ⋈ Enrolls ⋈ σ_credits≥4(Course))
```

---

### Παράδειγμα 2: Ερώτηση Εξέτασης 2025 (Q6)

**Δίνεται:** Σχέση R(A, B, C) και η πράξη:
```
π_A,C(σ_B='X'(R)) ∩ π_A,C(σ_B='Y'(R))
```

**Τι αναπαριστά το αποτέλεσμα;**

**Απάντηση: (a) Όλα τα ζεύγη (A, C) που εμφανίζονται στο R ΤΟΣΟ για B='X' ΟΣΟ ΚΑΙ για B='Y'**

**Εξήγηση:**
1. `π_A,C(σ_B='X'(R))` → ζεύγη (A,C) όπου B='X'
2. `π_A,C(σ_B='Y'(R))` → ζεύγη (A,C) όπου B='Y'
3. `∩` → κοινά ζεύγη = εμφανίζονται ΚΑΙ για B='X' ΚΑΙ για B='Y'

---

### Παράδειγμα 3: HW1 2025 - Relational Algebra Queries

**Πίνακες:**
- `Professor(prof_id, pname, department, office_num)`
- `Publication(pub_id, title, venue, year)`
- `Writes(prof_id, pub_id)`

**Query 1:** Βρες το ID και όνομα των καθηγητών στο 'CS' department ή με office_num μεταξύ 400-499.
```
π_prof_id,pname(σ_department='CS' ∨ (office_num≥400 ∧ office_num≤499)(Professor))
```

**Query 2:** Βρες τα ονόματα των καθηγητών που έχουν δημοσιεύσει στο 'VLDB'.
```
π_pname(Professor ⋈ Writes ⋈ σ_venue='VLDB'(Publication))
```

**Query 3:** Βρες τους καθηγητές που έχουν δημοσιεύσει σε ΟΛΑ τα venues όπου δημοσιεύτηκε paper το 2025.
```
π_prof_id,venue(Professor ⋈ Writes ⋈ Publication) ÷ π_venue(σ_year=2025(Publication))
```
Και μετά join με Professor για να πάρουμε τα ονόματα:
```
π_pname(Professor ⋈ (π_prof_id,venue(Professor ⋈ Writes ⋈ Publication) ÷ π_venue(σ_year=2025(Publication))))
```

**Query 4:** Βρες τους καθηγητές που ΔΕΝ έχουν δημοσιεύσει ποτέ.
```
π_prof_id,pname(Professor) − π_prof_id,pname(Professor ⋈ Writes)
```

---

## Προτεραιότητα Τελεστών

Από υψηλότερη σε χαμηλότερη:
1. σ, π, ρ (Unary operators)
2. ×, ⋈ (Products and Joins)
3. ∩ (Intersection)
4. ∪, − (Union and Difference)

---

## Συχνά Λάθη στις Εξετάσεις

### 1. Projection αφαιρεί duplicates
- `π_dept(Employee)` επιστρέφει DISTINCT τιμές!

### 2. Natural Join matches σε ΟΛΕΣ τις κοινές στήλες
- ❌ Λάθος: `R ⋈ S` μόνο σε μία στήλη
- ✓ Σωστό: Matches σε ΟΛΕΣ τις στήλες με ίδιο όνομα

### 3. Selection vs Projection σύγχυση
- σ = γραμμές (horizontal slice)
- π = στήλες (vertical slice)

### 4. Set operations χρειάζονται συμβατά schemas
- Δεν γίνεται `π_name(R) ∪ π_dept(S)` αν διαφορετικοί τύποι

---

## Γρήγορη Αναφορά

```
╔══════════════════════════════════════════════════════════════╗
║              RELATIONAL ALGEBRA CHEAT SHEET                  ║
╠══════════════════════════════════════════════════════════════╣
║ Selection:   σ_condition(R)     — Φιλτράρισμα γραμμών        ║
║ Projection:  π_cols(R)          — Επιλογή στηλών (+ DISTINCT)║
║ Natural Join: R ⋈ S             — Join σε κοινές στήλες      ║
║ Theta Join:  R ⋈_θ S            — Join με συνθήκη            ║
║ Division:    R ÷ S              — "Για όλα" queries          ║
║ Rename:      ρ_newname(R)       — Μετονομασία                ║
╠══════════════════════════════════════════════════════════════╣
║                    SQL → RA Mapping                          ║
╠══════════════════════════════════════════════════════════════╣
║ WHERE       = σ                                              ║
║ SELECT cols = π                                              ║
║ JOIN ON     = ⋈_θ                                            ║
║ UNION       = ∪                                              ║
║ INTERSECT   = ∩                                              ║
║ EXCEPT      = −                                              ║
╠══════════════════════════════════════════════════════════════╣
║               Συνηθισμένο Pattern                            ║
╠══════════════════════════════════════════════════════════════╣
║              π_cols(σ_cond(R ⋈ S))                           ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Ασκήσεις Εξάσκησης

### Άσκηση 1
Δίνονται οι πίνακες:
- `Supplier(sid, sname, city)`
- `Part(pid, pname, color)`
- `Supplies(sid, pid, quantity)`

Γράψτε σε Relational Algebra:
1. Ονόματα προμηθευτών από 'Athens'
2. Ονόματα κομματιών που προμηθεύει κάποιος από 'Athens'
3. Προμηθευτές που προμηθεύουν ΟΛΑ τα κόκκινα κομμάτια

### Άσκηση 2
Μετατρέψτε σε Relational Algebra:
```sql
SELECT DISTINCT E.name
FROM Employee E, Department D
WHERE E.dept_id = D.id AND D.budget > 1000000;
```
