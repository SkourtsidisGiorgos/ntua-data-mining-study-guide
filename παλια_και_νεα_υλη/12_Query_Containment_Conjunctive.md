# Query Containment & Conjunctive Queries - Πλήρης Οδηγός

## 1. Βασικές Έννοιες

### Query Containment

**Ορισμός**: **Q1 ⊆ Q2** αν για κάθε database D: **Q1(D) ⊆ Q2(D)**

Δηλαδή: "Τα αποτελέσματα του Q1 είναι **πάντα** υποσύνολο των αποτελεσμάτων του Q2"

### Παράδειγμα Containment
```sql
Q1: SELECT name FROM Employees WHERE salary > 50000
Q2: SELECT name FROM Employees WHERE salary > 30000

Q1 ⊆ Q2 ✓
Γιατί: Κάθε employee με salary > 50000 έχει επίσης salary > 30000
       Άρα Q1(D) ⊆ Q2(D) για κάθε D
```

### Query Equivalence

**Ορισμός**: **Q1 ≡ Q2** αν **Q1 ⊆ Q2** και **Q2 ⊆ Q1**

---

## 2. Conjunctive Queries

### Σύνταξη
```
h(X₁, ..., Xₖ) :- r₁(Y₁), r₂(Y₂), ..., rₙ(Yₙ)
```

**Μέρη**:
- **Head**: h(X₁, ..., Xₖ) - τι επιστρέφουμε
- **Body**: r₁, r₂, ..., rₙ - conditions (relations)
- **Distinguished variables**: Εμφανίζονται στο head
- **Non-distinguished variables**: Μόνο στο body (existentially quantified)

### Παράδειγμα
```
q(X, Z) :- Employee(X, Y), Department(Y, Z)

Μετάφραση σε SQL:
SELECT E.X, D.Z
FROM Employee E, Department D
WHERE E.Y = D.Y

- X, Z: distinguished (στο head)
- Y: non-distinguished (μόνο στο body)
```

---

## 3. Containment Mapping

### Θεώρημα
Για conjunctive queries **χωρίς comparisons**:

**Q1 ⊆ Q2** ⟺ υπάρχει **homomorphism** h: vars(Q2) → vars(Q1)

τέτοιος ώστε:
1. Κάθε relation στο body του Q2 να map σε relation στο Q1
2. Οι distinguished variables να διατηρούνται

### Τι είναι Homomorphism
Mapping από τις μεταβλητές του Q2 στις μεταβλητές του Q1 που:
- Διατηρεί τη δομή των relations
- Κάνει το body του Q2 να "ταιριάζει" στο body του Q1

---

## 4. Λυμένο Παράδειγμα 1

### Queries
```
Q1: h(X, Y) :- r(X, Y)
Q2: h(X, Y) :- r(X, Z), r(Z, Y)
```

### Ερώτηση: Q1 ⊆ Q2;

**Βήμα 1**: Ψάχνουμε mapping από vars(Q2) → vars(Q1)
- Q2 έχει: X, Z, Y
- Q1 έχει: X, Y

**Βήμα 2**: Προσπαθούμε mapping
- h(X) = X (distinguished, πρέπει να διατηρηθεί)
- h(Y) = Y (distinguished, πρέπει να διατηρηθεί)
- h(Z) = ???

**Βήμα 3**: Ελέγχουμε αν το body του Q2 γίνεται subset του body του Q1
- Q2 body: r(X, Z), r(Z, Y)
- Q1 body: r(X, Y)
- Αν h(Z) = X: r(X, X), r(X, Y) - το r(X, X) δεν υπάρχει στο Q1
- Αν h(Z) = Y: r(X, Y), r(Y, Y) - το r(Y, Y) δεν υπάρχει στο Q1

**Συμπέρασμα**: ΔΕΝ υπάρχει containment mapping
**Άρα**: Q1 **⊄** Q2

### Ερώτηση: Q2 ⊆ Q1;

**Βήμα 1**: Ψάχνουμε mapping από vars(Q1) → vars(Q2)
- Q1 έχει: X, Y
- Q2 έχει: X, Z, Y

**Βήμα 2**: Mapping
- h(X) = X
- h(Y) = Y

**Βήμα 3**: Body mapping
- Q1 body: r(X, Y)
- Q2 body: r(X, Z), r(Z, Y)
- r(X, Y) αντιστοιχεί σε... τίποτα exact στο Q2

Αλλά περιμένετε! Χρησιμοποιούμε το αντίστροφο:
Για Q2 ⊆ Q1, ψάχνουμε h: vars(Q1) → vars(Q2)

Αν h(Y) = Z (non-distinguished μπορεί να αλλάξει):
- r(X, Y) από Q1 → r(X, Z) στο Q2 ✓

**Συμπέρασμα**: Υπάρχει containment mapping
**Άρα**: Q2 ⊆ Q1 ✓

---

## 5. Λυμένο Παράδειγμα 2 (Από Εξέταση 2022-23)

### Queries
```
Q1: h(X, Y) :- r(X, W), r(Z, Y), g(W, Z), g(Z, W)
Q2: h(U, V) :- r(U, K), g(K, K), r(K, V)
```

### Ερώτηση: Q2 ⊆ Q1;

**Βήμα 1**: Ψάχνουμε mapping h: vars(Q1) → vars(Q2)

Η Q1 έχει body:
- r(X, W)
- r(Z, Y)
- g(W, Z)
- g(Z, W)

Η Q2 έχει body:
- r(U, K)
- g(K, K)
- r(K, V)

**Βήμα 2**: Προσπαθούμε να βρούμε mapping
- h(X) = U (distinguished)
- h(Y) = V (distinguished)
- h(W) = ?
- h(Z) = ?

Αν h(W) = K και h(Z) = K:
- r(X, W) → r(U, K) ✓
- r(Z, Y) → r(K, V) ✓
- g(W, Z) → g(K, K) ✓
- g(Z, W) → g(K, K) ✓

**Συμπέρασμα**: Υπάρχει containment mapping: {X→U, Y→V, W→K, Z→K}
**Άρα**: Q2 ⊆ Q1 ✓

### Ερώτηση: Q1 ⊆ Q2;

**Βήμα 1**: Ψάχνουμε mapping h: vars(Q2) → vars(Q1)

Q2 body: r(U, K), g(K, K), r(K, V)
Q1 body: r(X, W), r(Z, Y), g(W, Z), g(Z, W)

**Βήμα 2**:
- h(U) = X (distinguished)
- h(V) = Y (distinguished)
- h(K) = ?

Για g(K, K) να ταιριάξει σε g(W, Z) ή g(Z, W):
- g(K, K) → g(W, Z) απαιτεί K=W και K=Z, δηλαδή W=Z
- Αλλά στο Q1, g(W, Z), g(Z, W) σημαίνει ότι W και Z είναι συμμετρικά αλλά όχι απαραίτητα ίσα

**Πρόβλημα**: Δεν μπορούμε να βεβαιωθούμε ότι W=Z για κάθε database.

**Συμπέρασμα**: Δεν υπάρχει containment mapping
**Άρα**: Q1 **⊄** Q2

---

## 6. ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23

```
Assume the following conjunctive queries:
Q1: h(X, Y) :- r(X, W), r(Z, Y), g(W, Z), g(Z, W)
Q2: h(U, V) :- r(U, K), g(K, K), r(K, V)

Which of the following are true:

a) Q2 is not contained in Q1 because there is no containment mapping from Q1 to Q2
b) Q1 is not contained in Q2 because there is no containment mapping from Q2 to Q1 ✓
c) Q2 is contained in Q1 because there is containment mapping from Q1 to Q2 ✓
d) Q1 and Q2 are equivalent
e) Q2 is contained in Q1 although there is no containment mapping from Q1 to Q2
f) There is no containment mapping from Q1 to Q2 but there is containment of Q1 in Q2
   and this can be proved with canonical databases
g) Both techniques of containment mapping and canonical databases can prove that
   there is no containment of Q1 in Q2

ΣΩΣΤΕΣ ΑΠΑΝΤΗΣΕΙΣ: B, C

ΕΞΗΓΗΣΗ:
- B: Σωστό - Q1 ⊄ Q2 γιατί δεν υπάρχει mapping από Q2 στο Q1
- C: Σωστό - Q2 ⊆ Q1 με mapping {X→U, Y→V, W→K, Z→K}
```

---

## 7. Canonical Database Method

Όταν ο containment mapping δεν βρίσκει απάντηση, χρησιμοποιούμε **canonical databases**:

### Μέθοδος
1. Δημιούργησε database D από το body του Q1 (κάθε relation γίνεται tuple)
2. Υπολόγισε Q1(D) και Q2(D)
3. Αν Q1(D) ⊄ Q2(D), τότε Q1 ⊄ Q2

### Παράδειγμα
```
Q1: h(X, Y) :- r(X, Y)
Q2: h(X, Y) :- r(X, Z), r(Z, Y)

Canonical DB για Q1:
D = {r(a, b)}

Q1(D) = {(a, b)}
Q2(D) = {} (δεν υπάρχει Z τέτοιο ώστε r(a,Z) και r(Z,b))

Q1(D) ⊄ Q2(D) → Q1 ⊄ Q2 ✓
```

---

## 8. Σύνοψη Containment Rules

### Για να δείξεις Q1 ⊆ Q2:
1. Βρες homomorphism h: vars(Q2) → vars(Q1)
2. Distinguished variables πρέπει να map στις αντίστοιχες
3. Κάθε relation στο body του Q2 πρέπει να map σε relation στο Q1

### Για να δείξεις Q1 ⊄ Q2:
1. Δείξε ότι δεν υπάρχει containment mapping
2. Ή χρησιμοποίησε canonical database

### Key Points για Εξέταση

| Θέλω να δείξω | Μέθοδος |
|---------------|---------|
| Q1 ⊆ Q2 | Mapping από vars(Q2) → vars(Q1) |
| Q1 ⊄ Q2 | Δεν υπάρχει mapping ή canonical DB |
| Q1 ≡ Q2 | Q1 ⊆ Q2 ΚΑΙ Q2 ⊆ Q1 |

---

## 9. Common Patterns

### Pattern 1: Τα ίδια relations με διαφορετικές μεταβλητές
```
Q1: h(X) :- r(X, Y)
Q2: h(X) :- r(X, X)

Q2 ⊆ Q1 (X=X είναι πιο συγκεκριμένο)
Q1 ⊄ Q2 (υπάρχουν X,Y με X≠Y)
```

### Pattern 2: Περισσότερα relations
```
Q1: h(X) :- r(X, Y), s(Y)
Q2: h(X) :- r(X, Y)

Q1 ⊆ Q2 (Q1 είναι πιο περιοριστικό)
Q2 ⊄ Q1 (Q2 δεν απαιτεί s(Y))
```

### Pattern 3: Self-join pattern
```
Q1: h(X) :- r(X, Y), r(Y, X)
Q2: h(X) :- r(X, Y)

Q1 ⊆ Q2 (Q1 απαιτεί και τα δύο directions)
Q2 ⊄ Q1 (Q2 δεν απαιτεί το reverse)
```

---

## Σύνοψη - Key Points για 10/10

### Containment Mapping Direction
```
Για Q1 ⊆ Q2: Ψάχνουμε mapping από vars(Q2) → vars(Q1)
             (από το "μεγαλύτερο" στο "μικρότερο")
```

### Κανόνες Mapping
1. Distinguished variables → map στις αντίστοιχες
2. Non-distinguished → μπορούν να map οπουδήποτε
3. Κάθε relation του Q2 body → πρέπει να υπάρχει στο Q1 body

### GAV/LAV Connection
- GAV: Global ⊇ Local (same as Query Containment direction)
- LAV: Local ⊆ Global (query answering uses rewriting)

### Quick Check
```
Αν Q2 έχει ΠΕΡΙΣΣΟΤΕΡΑ relations στο body:
→ Συνήθως Q2 ⊆ Q1 (πιο περιοριστικό)

Αν Q2 έχει ΛΙΓΟΤΕΡΑ relations:
→ Συνήθως Q1 ⊆ Q2 (λιγότεροι περιορισμοί)
```
