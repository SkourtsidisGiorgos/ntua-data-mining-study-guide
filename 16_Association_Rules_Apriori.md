# Association Rules & Apriori - Πλήρης Οδηγός Μελέτης

## 1. Εισαγωγή

**Association Rule Mining** ανακαλύπτει ενδιαφέρουσες σχέσεις μεταξύ items σε μεγάλα datasets. Κλασικό παράδειγμα: **Market Basket Analysis** (ποια προϊόντα αγοράζονται μαζί).

### Παράδειγμα
```
"Πελάτες που αγόρασαν ψωμί ΚΑΙ βούτυρο, αγόρασαν επίσης γάλα"

Rule: {Bread, Butter} → {Milk}
```

---

## 2. Βασικές Έννοιες & Ορισμοί

### 2.1 Itemset

**Itemset**: Σύνολο από items (π.χ. {Bread, Milk, Butter})

**k-itemset**: Itemset με k items
- 1-itemset: {Bread}
- 2-itemset: {Bread, Milk}
- 3-itemset: {Bread, Milk, Butter}

### 2.2 Transaction Database

```
┌─────┬────────────────────────────┐
│ TID │          Items             │
├─────┼────────────────────────────┤
│ T1  │ Bread, Milk                │
│ T2  │ Bread, Butter, Eggs        │
│ T3  │ Milk, Butter, Eggs         │
│ T4  │ Bread, Milk, Butter, Eggs  │
│ T5  │ Bread, Milk, Butter        │
└─────┴────────────────────────────┘
Total Transactions: 5
```

---

## 3. Μέτρα Αξιολόγησης

### 3.1 Support

**Support(X)**: Πόσο συχνά εμφανίζεται το itemset X στις transactions.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              |T που περιέχουν X|                           │
│  Support(X) = ─────────────────────                         │
│                   |T| (total)                               │
│                                                             │
│  "Ποσοστό transactions που περιέχουν το X"                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Support({Bread}) = 4/5 = 0.80 (T1, T2, T4, T5)
Support({Milk}) = 4/5 = 0.80 (T1, T3, T4, T5)
Support({Bread, Milk}) = 3/5 = 0.60 (T1, T4, T5)
Support({Bread, Butter}) = 3/5 = 0.60 (T2, T4, T5)
```

### 3.2 Confidence

**Confidence(X→Y)**: Πόσο συχνά το Y εμφανίζεται όταν υπάρχει το X.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                     Support(X ∪ Y)                          │
│  Confidence(X→Y) = ────────────────                         │
│                       Support(X)                            │
│                                                             │
│  "Αν έχω X, πόσο πιθανό να έχω και Y;"                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Confidence({Bread} → {Milk}):
= Support({Bread, Milk}) / Support({Bread})
= 0.60 / 0.80
= 0.75 = 75%

"75% των transactions με Bread περιέχουν και Milk"
```

### 3.3 Lift

**Lift(X→Y)**: Πόσο πιο πιθανό είναι το Y όταν υπάρχει X, σε σχέση με το baseline.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│               Confidence(X→Y)     Support(X ∪ Y)           │
│  Lift(X→Y) = ─────────────────── = ───────────────────      │
│                Support(Y)         Support(X) × Support(Y)  │
│                                                             │
│  Lift = 1: X και Y ανεξάρτητα                              │
│  Lift > 1: Θετική συσχέτιση                                │
│  Lift < 1: Αρνητική συσχέτιση                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Lift({Bread} → {Milk}):
= Confidence({Bread}→{Milk}) / Support({Milk})
= 0.75 / 0.80
= 0.9375

Lift < 1: Ελαφρώς αρνητική συσχέτιση (τυχαίο)
```

### Σύνοψη Μέτρων

| Μέτρο | Τύπος | Ερμηνεία |
|-------|-------|----------|
| **Support(X)** | \|T with X\| / \|T\| | Συχνότητα εμφάνισης |
| **Confidence(X→Y)** | Sup(X∪Y) / Sup(X) | Conditional probability |
| **Lift(X→Y)** | Conf(X→Y) / Sup(Y) | Correlation measure |

---

## 4. Apriori Algorithm

### 4.1 Βασική Αρχή: Downward Closure (Apriori Principle)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  "Αν ένα itemset είναι INFREQUENT,                         │
│   όλα τα SUPERSETS του είναι επίσης infrequent"            │
│                                                             │
│  Αν Support({A,B}) < min_sup,                              │
│  τότε Support({A,B,C}) ≤ Support({A,B}) < min_sup          │
│                                                             │
│  ΑΝΤΙΣΤΡΟΦΑ:                                                │
│  "Κάθε subset ενός frequent itemset είναι frequent"        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Γιατί είναι χρήσιμο**: Αποκλείουμε candidates χωρίς να μετρήσουμε support!

### 4.2 Αλγόριθμος

```
┌────────────────────────────────────────────────────────────┐
│  APRIORI ALGORITHM                                         │
│  ─────────────────                                         │
│                                                            │
│  INPUT: Transaction database D, minimum support min_sup    │
│  OUTPUT: All frequent itemsets                             │
│                                                            │
│  1. C₁ = all 1-itemsets                                    │
│  2. L₁ = {items in C₁ with support ≥ min_sup}             │
│                                                            │
│  3. FOR k = 2 to max_k:                                    │
│        // Generate candidates                              │
│        Cₖ = generate_candidates(Lₖ₋₁)                      │
│                                                            │
│        // Prune using Apriori principle                    │
│        Cₖ = prune(Cₖ) // remove if any (k-1)-subset ∉ Lₖ₋₁│
│                                                            │
│        // Count support                                    │
│        FOR each transaction t:                             │
│           FOR each candidate c ∈ Cₖ:                       │
│              IF c ⊆ t: count[c]++                          │
│                                                            │
│        // Filter frequent                                  │
│        Lₖ = {c ∈ Cₖ : support(c) ≥ min_sup}               │
│                                                            │
│        IF Lₖ = ∅: BREAK                                    │
│                                                            │
│  4. RETURN L₁ ∪ L₂ ∪ ... ∪ Lₖ                             │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 4.3 Candidate Generation (Join Step)

```
┌────────────────────────────────────────────────────────────┐
│  Για να δημιουργήσουμε Cₖ από Lₖ₋₁:                        │
│                                                            │
│  1. Ταξινομούμε τα items σε κάθε itemset                   │
│  2. JOIN: Ενώνουμε itemsets που έχουν τα πρώτα (k-2)      │
│           items ίδια και διαφορετικό το τελευταίο         │
│                                                            │
│  Παράδειγμα:                                               │
│  L₂ = {{A,B}, {A,C}, {A,D}, {B,C}, {B,D}, {C,D}}          │
│                                                            │
│  {A,B} ∪ {A,C} = {A,B,C}  (join on A)                     │
│  {A,B} ∪ {A,D} = {A,B,D}  (join on A)                     │
│  {A,C} ∪ {A,D} = {A,C,D}  (join on A)                     │
│  {B,C} ∪ {B,D} = {B,C,D}  (join on B)                     │
│                                                            │
│  C₃ = {{A,B,C}, {A,B,D}, {A,C,D}, {B,C,D}}               │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 4.4 Pruning Step

```
┌────────────────────────────────────────────────────────────┐
│  Για κάθε candidate c ∈ Cₖ:                                │
│    Για κάθε (k-1)-subset s του c:                         │
│      IF s ∉ Lₖ₋₁:                                          │
│        Remove c from Cₖ                                    │
│                                                            │
│  Παράδειγμα:                                               │
│  Candidate {A,B,C} - check subsets:                        │
│    {A,B} ∈ L₂? ✓                                          │
│    {A,C} ∈ L₂? ✓                                          │
│    {B,C} ∈ L₂? ✓                                          │
│  → Keep {A,B,C}                                            │
│                                                            │
│  Candidate {A,B,D} - check subsets:                        │
│    {A,B} ∈ L₂? ✓                                          │
│    {A,D} ∈ L₂? ✓                                          │
│    {B,D} ∈ L₂? ✗ (suppose not)                            │
│  → Prune {A,B,D}                                           │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 5. Worked Example (ΤΥΠΙΚΟ ΘΕΜΑ ΕΞΕΤΑΣΕΩΝ!)

### Transaction Database

```
┌─────┬────────────────────┐
│ TID │       Items        │
├─────┼────────────────────┤
│ T1  │ A, C, D            │
│ T2  │ B, C, E            │
│ T3  │ A, B, C, E         │
│ T4  │ B, E               │
│ T5  │ A, B, C, E         │
└─────┴────────────────────┘

min_sup = 2/5 = 0.40 (δηλαδή τουλάχιστον 2 transactions)
```

### Βήμα 1: C₁ → L₁

```
C₁: {A}, {B}, {C}, {D}, {E}

Count support:
  {A}: T1, T3, T5 → count = 3 → sup = 3/5 = 0.60 ≥ 0.40 ✓
  {B}: T2, T3, T4, T5 → count = 4 → sup = 4/5 = 0.80 ≥ 0.40 ✓
  {C}: T1, T2, T3, T5 → count = 4 → sup = 4/5 = 0.80 ≥ 0.40 ✓
  {D}: T1 → count = 1 → sup = 1/5 = 0.20 < 0.40 ✗
  {E}: T2, T3, T4, T5 → count = 4 → sup = 4/5 = 0.80 ≥ 0.40 ✓

L₁ = {{A}, {B}, {C}, {E}}
```

### Βήμα 2: Generate C₂ from L₁

```
C₂ (all 2-combinations of L₁):
  {A,B}, {A,C}, {A,E}, {B,C}, {B,E}, {C,E}

Count support:
  {A,B}: T3, T5 → count = 2 → sup = 0.40 ≥ 0.40 ✓
  {A,C}: T1, T3, T5 → count = 3 → sup = 0.60 ≥ 0.40 ✓
  {A,E}: T3, T5 → count = 2 → sup = 0.40 ≥ 0.40 ✓
  {B,C}: T2, T3, T5 → count = 3 → sup = 0.60 ≥ 0.40 ✓
  {B,E}: T2, T3, T4, T5 → count = 4 → sup = 0.80 ≥ 0.40 ✓
  {C,E}: T2, T3, T5 → count = 3 → sup = 0.60 ≥ 0.40 ✓

L₂ = {{A,B}, {A,C}, {A,E}, {B,C}, {B,E}, {C,E}}
```

### Βήμα 3: Generate C₃ from L₂

```
Join step (itemsets με ίδιο πρώτο item):
  {A,B} ∪ {A,C} = {A,B,C}
  {A,B} ∪ {A,E} = {A,B,E}
  {A,C} ∪ {A,E} = {A,C,E}
  {B,C} ∪ {B,E} = {B,C,E}

C₃ candidates: {A,B,C}, {A,B,E}, {A,C,E}, {B,C,E}

Prune step (check all 2-subsets):
  {A,B,C}: {A,B}✓, {A,C}✓, {B,C}✓ → KEEP
  {A,B,E}: {A,B}✓, {A,E}✓, {B,E}✓ → KEEP
  {A,C,E}: {A,C}✓, {A,E}✓, {C,E}✓ → KEEP
  {B,C,E}: {B,C}✓, {B,E}✓, {C,E}✓ → KEEP

C₃ after pruning: {A,B,C}, {A,B,E}, {A,C,E}, {B,C,E}

Count support:
  {A,B,C}: T3, T5 → count = 2 → sup = 0.40 ≥ 0.40 ✓
  {A,B,E}: T3, T5 → count = 2 → sup = 0.40 ≥ 0.40 ✓
  {A,C,E}: T3, T5 → count = 2 → sup = 0.40 ≥ 0.40 ✓
  {B,C,E}: T2, T3, T5 → count = 3 → sup = 0.60 ≥ 0.40 ✓

L₃ = {{A,B,C}, {A,B,E}, {A,C,E}, {B,C,E}}
```

### Βήμα 4: Generate C₄ from L₃

```
Join step:
  {A,B,C} ∪ {A,B,E} = {A,B,C,E}

C₄ = {{A,B,C,E}}

Prune step (check all 3-subsets):
  {A,B,C} ∈ L₃? ✓
  {A,B,E} ∈ L₃? ✓
  {A,C,E} ∈ L₃? ✓
  {B,C,E} ∈ L₃? ✓
→ KEEP

Count support:
  {A,B,C,E}: T3, T5 → count = 2 → sup = 0.40 ≥ 0.40 ✓

L₄ = {{A,B,C,E}}
```

### Βήμα 5: Generate C₅

```
Χρειάζονται 2+ itemsets σε L₄ για join → STOP

Final Frequent Itemsets:
L₁ ∪ L₂ ∪ L₃ ∪ L₄
```

### Τελικό Αποτέλεσμα

```
┌───────────────────────────────────────────────┐
│  Frequent Itemsets                            │
├───────────────────────────────────────────────┤
│  1-itemsets: {A}, {B}, {C}, {E}              │
│  2-itemsets: {A,B}, {A,C}, {A,E},            │
│              {B,C}, {B,E}, {C,E}             │
│  3-itemsets: {A,B,C}, {A,B,E},               │
│              {A,C,E}, {B,C,E}                │
│  4-itemsets: {A,B,C,E}                       │
└───────────────────────────────────────────────┘
```

---

## 6. Rule Generation

### 6.1 Από Frequent Itemset σε Rules

Για κάθε frequent itemset L, για κάθε non-empty subset S:
- Rule: (L - S) → S
- Confidence = Support(L) / Support(L - S)

### 6.2 Παράδειγμα

```
Frequent itemset: {A, B, C} με support = 0.40

Possible rules:
  {A, B} → {C}: conf = sup({A,B,C}) / sup({A,B}) = 0.40/0.40 = 1.00
  {A, C} → {B}: conf = sup({A,B,C}) / sup({A,C}) = 0.40/0.60 = 0.67
  {B, C} → {A}: conf = sup({A,B,C}) / sup({B,C}) = 0.40/0.60 = 0.67
  {A} → {B, C}: conf = sup({A,B,C}) / sup({A}) = 0.40/0.60 = 0.67
  {B} → {A, C}: conf = sup({A,B,C}) / sup({B}) = 0.40/0.80 = 0.50
  {C} → {A, B}: conf = sup({A,B,C}) / sup({C}) = 0.40/0.80 = 0.50

Αν min_conf = 0.60:
Strong rules: {A,B}→{C}, {A,C}→{B}, {B,C}→{A}, {A}→{B,C}
```

---

## 7. FP-Growth (Overview)

### 7.1 Μειονεκτήματα Apriori

- **Πολλαπλά scans** της βάσης δεδομένων
- **Μεγάλος αριθμός candidates**
- **Πολλοί support counts**

### 7.2 FP-Growth Ιδέα

1. **Compress** τη βάση σε FP-tree (1ο scan)
2. **Mine** directly από το tree (χωρίς candidate generation)

```
┌────────────────────────────────────────────────────────────┐
│  FP-tree: Compact representation of transactions           │
│                                                            │
│  - Κάθε path = μία ή περισσότερες transactions            │
│  - Shared prefixes = κοινά items                          │
│  - Node links = σύνδεση ίδιων items                       │
│                                                            │
│  Πλεονεκτήματα:                                           │
│  - Μόνο 2 database scans                                  │
│  - Δεν χρειάζεται candidate generation                    │
│  - Πιο γρήγορος για μεγάλα datasets                       │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 8. ⚠️ Συχνά Λάθη / Pitfalls

### 8.1 Support Calculation
```
❌ ΛΑΘΟΣ: Support({A,B}) = Support({A}) × Support({B})
✓ ΣΩΣΤΟ: Support({A,B}) = |transactions containing BOTH A and B| / |total|

Το support δεν είναι γινόμενο (εκτός αν είναι ανεξάρτητα)!
```

### 8.2 Confidence Direction
```
❌ ΛΑΘΟΣ: Confidence(A→B) = Confidence(B→A)
✓ ΣΩΣΤΟ: Συνήθως διαφορετικά!

Confidence(A→B) = Sup({A,B}) / Sup({A})
Confidence(B→A) = Sup({A,B}) / Sup({B})

Αν Sup({A}) ≠ Sup({B}), τότε οι confidences διαφέρουν.
```

### 8.3 Apriori Pruning
```
❌ ΛΑΘΟΣ: Αν {A,B} infrequent, μπορεί {A,B,C} να είναι frequent
✓ ΣΩΣΤΟ: ΑΔΥΝΑΤΟ! Downward closure property

{A,B,C} ⊇ {A,B} → Support({A,B,C}) ≤ Support({A,B})
```

### 8.4 Lift Interpretation
```
Lift = 1: Ανεξαρτησία (δεν σημαίνει τίποτα το rule)
Lift > 1: Θετική συσχέτιση
Lift < 1: Αρνητική συσχέτιση

⚠️ Υψηλό confidence ΔΕΝ σημαίνει υψηλό lift!
```

---

## 9. Ερωτήσεις Εξετάσεων

### Ερώτηση 1
Database με 100 transactions:
- 60 περιέχουν {A}
- 75 περιέχουν {B}
- 45 περιέχουν {A, B}

Ποιο είναι το Confidence(A→B);

A) 0.45
B) 0.60
C) 0.75
D) 0.80

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 0.75**

**Υπολογισμός**:
```
Confidence(A→B) = Support({A,B}) / Support({A})
                = (45/100) / (60/100)
                = 45/60
                = 0.75
```
</details>

---

### Ερώτηση 2
Με τα ίδια δεδομένα, ποιο είναι το Lift(A→B);

A) 0.60
B) 0.80
C) 1.00
D) 1.33

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 1.00**

**Υπολογισμός**:
```
Lift(A→B) = Confidence(A→B) / Support({B})
          = 0.75 / 0.75
          = 1.00

Ή εναλλακτικά:
Lift = Support({A,B}) / (Support({A}) × Support({B}))
     = 0.45 / (0.60 × 0.75)
     = 0.45 / 0.45
     = 1.00
```

**Ερμηνεία**: Lift = 1 → A και B είναι ανεξάρτητα.
</details>

---

### Ερώτηση 3
Αν L₂ = {{A,B}, {A,C}, {B,C}, {B,D}}, ποια 3-itemsets θα είναι στο C₃;

A) {A,B,C}, {A,B,D}, {B,C,D}
B) {A,B,C} μόνο
C) {A,B,C}, {B,C,D}
D) Κανένα

<details>
<summary>Απάντηση</summary>

**Σωστό: B) {A,B,C} μόνο**

**Εξήγηση**:
```
Join step:
  {A,B} ∪ {A,C} = {A,B,C}
  {B,C} ∪ {B,D} = {B,C,D}

Prune step:
  {A,B,C}: {A,B}✓, {A,C}✓, {B,C}✓ → KEEP
  {B,C,D}: {B,C}✓, {B,D}✓, {C,D}? → {C,D} ∉ L₂ → PRUNE!
```

Μόνο {A,B,C} περνάει το pruning.
</details>

---

### Ερώτηση 4
Ποια είναι η Apriori property;

A) Frequent itemsets έχουν υψηλό confidence
B) Subsets of infrequent itemsets είναι infrequent
C) Supersets of frequent itemsets είναι frequent
D) Subsets of frequent itemsets είναι frequent

<details>
<summary>Απάντηση</summary>

**Σωστό: D)**

**Εξήγηση**: "Αν ένα itemset είναι frequent, όλα τα subsets του είναι frequent."

Αντιστρόφως: "Αν ένα itemset είναι infrequent, όλα τα supersets του είναι infrequent."
</details>

---

### Ερώτηση 5
5 transactions, min_sup = 40%. {A} εμφανίζεται σε 2 transactions. Είναι frequent;

A) Ναι
B) Όχι
C) Εξαρτάται από το confidence
D) Δεν μπορούμε να ξέρουμε

<details>
<summary>Απάντηση</summary>

**Σωστό: A) Ναι**

**Υπολογισμός**:
```
Support({A}) = 2/5 = 0.40 = 40%
min_sup = 40%

0.40 ≥ 0.40 → Frequent! ✓
```
</details>

---

### Ερώτηση 6
Τι μετράει το Lift;

A) Πόσο συχνά εμφανίζεται ένα item
B) Αν δύο items είναι θετικά/αρνητικά/ανεξάρτητα correlated
C) Τη βεβαιότητα ενός rule
D) Τον αριθμό transactions

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**:
- Lift = 1: Ανεξάρτητα
- Lift > 1: Θετικά correlated
- Lift < 1: Αρνητικά correlated
</details>

---

### Ερώτηση 7
Γιατί ο Apriori σαρώνει τη βάση πολλές φορές;

A) Για να βρει τα frequent 1-itemsets
B) Για να μετρήσει support κάθε k-itemsets ξεχωριστά
C) Για error checking
D) Δεν σαρώνει πολλές φορές

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: Σε κάθε iteration k, ο Apriori σαρώνει τη βάση για να μετρήσει το support των Cₖ candidates. Αν max frequent itemset έχει size m, χρειάζονται m scans.
</details>

---

### Ερώτηση 8
Confidence(A→B) = 0.8, Confidence(B→A) = 0.6. Ποιο support είναι μεγαλύτερο, {A} ή {B};

A) Support({A})
B) Support({B})
C) Ίσα
D) Δεν μπορούμε να ξέρουμε

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Support({B})**

**Εξήγηση**:
```
Conf(A→B) = Sup({A,B}) / Sup({A}) = 0.8
Conf(B→A) = Sup({A,B}) / Sup({B}) = 0.6

Έστω Sup({A,B}) = x

Sup({A}) = x / 0.8 = 1.25x
Sup({B}) = x / 0.6 = 1.67x

Sup({B}) > Sup({A})
```
</details>

---

### Ερώτηση 9
Πόσα rules μπορούν να παραχθούν από ένα frequent 3-itemset {A,B,C};

A) 3
B) 6
C) 8
D) 9

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 6**

**Εξήγηση**:
```
Rules με non-empty antecedent και consequent:

1-item → 2-items:
  {A} → {B,C}
  {B} → {A,C}
  {C} → {A,B}

2-items → 1-item:
  {A,B} → {C}
  {A,C} → {B}
  {B,C} → {A}

Total: 6 rules
```

Γενικά, για n-itemset: 2ⁿ - 2 rules (αφαιρούμε ∅ → all και all → ∅)
Για n=3: 2³ - 2 = 6 ✓
</details>

---

### Ερώτηση 10
FP-Growth έχει πλεονέκτημα έναντι Apriori γιατί:

A) Δεν χρειάζεται minimum support
B) Σαρώνει τη βάση μόνο 2 φορές
C) Υπολογίζει confidence αυτόματα
D) Βρίσκει περισσότερα frequent itemsets

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: FP-Growth:
1. 1ο scan: Build FP-tree
2. 2ο scan: Mine patterns

Apriori: k scans για max k-itemset

FP-Growth αποφεύγει candidate generation (πιο efficient).
</details>

---

## 10. Σύνοψη - Key Points

### Τύποι (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Support(X) = |T containing X| / |T|                       │
│                                                             │
│  Confidence(X→Y) = Support(X∪Y) / Support(X)               │
│                                                             │
│  Lift(X→Y) = Confidence(X→Y) / Support(Y)                  │
│            = Support(X∪Y) / (Support(X) × Support(Y))      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Apriori Algorithm

```
1. Find frequent 1-itemsets (L₁)
2. Generate candidates (Cₖ) from Lₖ₋₁
3. Prune candidates (Apriori principle)
4. Count support, keep frequent (Lₖ)
5. Repeat until no more frequent itemsets
```

### Apriori Principle (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

```
"Subsets of frequent itemsets are frequent"
"Supersets of infrequent itemsets are infrequent"

→ Used for pruning candidates
```

### Lift Interpretation

```
Lift = 1  → Independent (no correlation)
Lift > 1  → Positive correlation
Lift < 1  → Negative correlation
```
