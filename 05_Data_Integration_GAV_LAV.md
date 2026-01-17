# Data Integration - GAV & LAV - Πλήρης Οδηγός Μελέτης

## 1. Εισαγωγή στο Data Integration

### Το Πρόβλημα
- Πολλαπλές **heterogeneous** πηγές δεδομένων
- Διαφορετικά schemas, formats, semantics
- Θέλουμε **ενιαία πρόσβαση** (unified view)

### Η Λύση: Mediated Schema

```
                    ┌─────────────────┐
                    │  Global Schema  │
                    │   (Mediator)    │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
      ┌─────▼─────┐    ┌─────▼─────┐    ┌─────▼─────┐
      │  Source 1 │    │  Source 2 │    │  Source 3 │
      │  (Local)  │    │  (Local)  │    │  (Local)  │
      └───────────┘    └───────────┘    └───────────┘
```

### Δύο Προσεγγίσεις
1. **GAV** (Global-as-View): Το global ορίζεται με βάση τα local
2. **LAV** (Local-as-View): Τα local ορίζονται με βάση το global

---

## 2. GAV (Global-as-View)

### Ορισμός
Το **Global schema** ορίζεται ως **view** πάνω στα local schemas.

### Χαρακτηριστικά

| Πλεονέκτημα | Μειονέκτημα |
|-------------|-------------|
| **Εύκολο query processing** | Δύσκολο να προσθέσεις sources |
| Simple unfolding | Πρέπει να ξαναγραφεί το global view |
| Deterministic answers | Λιγότερη ευελιξία |

### Query Processing
**Απλό "unfold"**: Αντικατέστησε το global view με τον ορισμό του.

### Σύμβολο

```
Global ⊇ Local

"Το global περιέχει τουλάχιστον ό,τι παρέχουν τα local"
```

### Παράδειγμα GAV

**Local Schemas**:
```sql
Loan_Accounts(account_number, holder_name, account_type)
Loan_Payments(account_number, payment_amount, payment_date)
```

**Global Schema (GAV)**:
```sql
Bank_Recent_Payments(account_number, holder_name, payment_amount, account_type) AS
SELECT la.account_number, la.holder_name, lp.payment_amount, la.account_type
FROM Loan_Accounts la
JOIN Loan_Payments lp ON la.account_number = lp.account_number
WHERE lp.payment_date > '2024-01-01'
```

**Query on Global**:
```sql
SELECT * FROM Bank_Recent_Payments WHERE account_type = 'Personal'
```

**Unfolded Query** (εκτελείται στα local):
```sql
SELECT la.account_number, la.holder_name, lp.payment_amount, la.account_type
FROM Loan_Accounts la
JOIN Loan_Payments lp ON la.account_number = lp.account_number
WHERE lp.payment_date > '2024-01-01'
  AND la.account_type = 'Personal'
```

---

## 3. LAV (Local-as-View)

### Ορισμός
Τα **Local schemas** ορίζονται ως **views** πάνω στο global schema.

### Χαρακτηριστικά

| Πλεονέκτημα | Μειονέκτημα |
|-------------|-------------|
| **Εύκολο να προσθέσεις sources** | Δύσκολο query processing |
| Ευέλικτο | Query rewriting problem |
| Extensible | Μπορεί να μην υπάρχει exact answer |

### Query Processing
**Query Rewriting**: Πρέπει να βρεθεί ισοδύναμο query στα local.

### Σύμβολο

```
Local ⊆ Global

"Το local περιέχεται στο global"
```

### Παράδειγμα LAV

**Global Schema**:
```sql
Bank_Recent_Payments(account_number, holder_name, payment_amount, account_type)
```

**Local Schemas (LAV)**:
```sql
-- Local View 1: Περιέχει μόνο Personal accounts
Loan_Accounts(account_number, holder_name, account_type) AS
    π_{account_number, holder_name, account_type}(
        σ_{account_type='Personal'}(Bank_Recent_Payments)
    )

-- Local View 2: Περιέχει μόνο payments > 1000
Loan_Payments(account_number, payment_amount) AS
    π_{account_number, payment_amount}(
        σ_{payment_amount > 1000}(Bank_Recent_Payments)
    )
```

**Query on Global**:
```sql
SELECT account_number FROM Bank_Recent_Payments WHERE payment_amount > 500
```

**Πρόβλημα**: Πώς απαντάμε αυτό από τα local views;
- Loan_Payments έχει μόνο payments > 1000
- Δεν μπορούμε να πάρουμε payments μεταξύ 500-1000!

---

## 4. Σύγκριση GAV vs LAV

| Χαρακτηριστικό | GAV | LAV |
|----------------|-----|-----|
| **Ορισμός** | Global = View(Local) | Local = View(Global) |
| **Query Processing** | Εύκολο (unfold) | Δύσκολο (rewriting) |
| **Προσθήκη Source** | Δύσκολη | **Εύκολη** |
| **Σύμβολο** | Global ⊇ Local | Local ⊆ Global |
| **Χρήση** | Σταθερές πηγές | Δυναμικές πηγές |

### Κανόνας Μνημονικής

```
GAV: Global As View → Global defined using local
     G ⊇ L → "Global superset of Local"

LAV: Local As View → Local defined using global
     L ⊆ G → "Local subset of Global"
```

---

## 5. Open-World vs Closed-World Assumption

### Closed-World Assumption (CWA)
- Αυτό που **ΔΕΝ** υπάρχει στη βάση είναι **ΨΕΥΔΕΣ**
- SQL databases χρησιμοποιούν CWA
- Π.χ.: Αν δεν υπάρχει record για "John", τότε "John" δεν υπάρχει

### Open-World Assumption (OWA)
- Αυτό που **ΔΕΝ** υπάρχει στη βάση **ΜΠΟΡΕΙ** να είναι αληθές
- Χρησιμοποιείται σε LAV
- Π.χ.: Αν δεν υπάρχει record για "John", δεν ξέρουμε αν υπάρχει ή όχι

### Certain Answers
Στο LAV με OWA, ψάχνουμε **certain answers**:
- Απαντήσεις που είναι σίγουρα σωστές
- Ανεξάρτητα από τα άγνωστα δεδομένα

---

## 6. Query Containment

### Ορισμός
**Q1 ⊆ Q2** αν για κάθε database D: **Q1(D) ⊆ Q2(D)**

"Τα αποτελέσματα του Q1 είναι πάντα υποσύνολο των αποτελεσμάτων του Q2"

### Παράδειγμα
```sql
Q1: SELECT name FROM Employees WHERE salary > 50000
Q2: SELECT name FROM Employees WHERE salary > 30000

Q1 ⊆ Q2 (κάθε αποτέλεσμα του Q1 είναι και στο Q2)
```

### Query Equivalence
**Q1 ≡ Q2** αν **Q1 ⊆ Q2** και **Q2 ⊆ Q1**

---

## 7. Containment Mapping

### Μέθοδος
Για conjunctive queries χωρίς comparisons:

**Q1 ⊆ Q2** αν υπάρχει **homomorphism** h: vars(Q2) → vars(Q1)

### Παράδειγμα

```
Q1: q(X) :- r(X,Y), r(Y,X)
Q2: q(X) :- r(X,Y)

Ερώτηση: Q1 ⊆ Q2;

Mapping: h(X) = X, h(Y) = Y
r(X,Y) στο Q2 → r(X,Y) στο Q1 ✓

Άρα Q1 ⊆ Q2 ✓
```

---

## 8. Conjunctive Queries

### Σύνταξη
```
h(X₁, ..., Xₖ) :- r₁(Y₁), r₂(Y₂), ..., rₙ(Yₙ)
```

- **Head**: h(X₁, ..., Xₖ) - τι επιστρέφουμε
- **Body**: r₁, r₂, ..., rₙ - conditions (join)
- **Distinguished variables**: Εμφανίζονται στο head
- **Non-distinguished**: Μόνο στο body (existentially quantified)

### Παράδειγμα

```
q(X,Z) :- Employee(X,Y), Department(Y,Z)

Equivalent SQL:
SELECT E.X, D.Z
FROM Employee E, Department D
WHERE E.Y = D.Y
```

---

## 9. Λυμένο Παράδειγμα Εξέτασης

### Σενάριο
**Global Schema**:
```
Bank_Recent_Payments(account_number, holder_name, payment_amount, account_type)
```

**Local Sources**:
```
S1: Loan_Accounts(account_number, holder_name, account_type)
S2: Loan_Payments(account_number, payment_amount)
```

### Ερώτηση: Ποιο είναι το σωστό GAV mapping;

**Επιλογή A**:
```sql
Bank_Recent_Payments(a, h, p, t) :-
    Loan_Accounts(a, h, t), Loan_Payments(a, p)
```

**Επιλογή B**:
```sql
Bank_Recent_Payments(a, h, p, t) :-
    Loan_Accounts(a, h, t)
```

**Επιλογή C**:
```sql
Bank_Recent_Payments(a, h, p, t) :-
    Loan_Payments(a, p)
```

### Ανάλυση

**A είναι ΣΩΣΤΟ** γιατί:
- Χρησιμοποιεί και τα δύο local sources
- Συνδέει τα μέσω account_number
- Παρέχει όλα τα attributes του global

**B είναι ΛΑΘΟΣ** γιατί:
- Δεν παρέχει payment_amount (p)

**C είναι ΛΑΘΟΣ** γιατί:
- Δεν παρέχει holder_name (h) και account_type (t)

---

## 10. Ερωτήσεις Εξετάσεων

### Ερώτηση 1: GAV vs LAV Definition
```
Ποιο είναι σωστό για GAV;

A) Local schemas ορίζονται ως views του global
B) Global schema ορίζεται ως view των local ✓
C) Query processing είναι δύσκολο
D) Εύκολο να προσθέσεις νέες πηγές

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 2: Symbol Recognition
```
Το σύμβολο Local ⊆ Global αντιστοιχεί σε:

A) GAV
B) LAV ✓
C) Query containment
D) Schema equivalence

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 3: Query Processing
```
Σε ποια προσέγγιση το query processing είναι απλό unfold;

A) LAV
B) GAV ✓
C) Both
D) Neither

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 4: Adding Sources
```
Ποια προσέγγιση επιτρέπει εύκολη προσθήκη νέων πηγών;

A) GAV
B) LAV ✓
C) Both equally
D) Depends on the sources

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 5: Open-World Assumption
```
Στο Open-World Assumption:

A) Ό,τι δεν υπάρχει στη βάση είναι ψευδές
B) Ό,τι δεν υπάρχει μπορεί να είναι αληθές ✓
C) Η βάση περιέχει όλη την αλήθεια
D) Δεν επιτρέπονται NULL values

ΑΠΑΝΤΗΣΗ: B
```

---

## Σύνοψη - Key Points

### GAV
- Global = View(Local)
- Symbol: **Global ⊇ Local**
- Query: **Easy (unfold)**
- Add source: **Hard**

### LAV
- Local = View(Global)
- Symbol: **Local ⊆ Global**
- Query: **Hard (rewriting)**
- Add source: **Easy**

### Μνημονικό
```
GAV = "G defined As View of L" → G ⊇ L → Easy queries
LAV = "L defined As View of G" → L ⊆ G → Easy extensions
```

### Σύμβολα
- **⊇** = superset (GAV: Global contains Local data)
- **⊆** = subset (LAV: Local is subset of Global)
