# General Concepts - HMMs, Data Types & More - Οδηγός Μελέτης

## 1. Τύποι Δεδομένων (Attribute Types)

### 1.1 Nominal (Categorical)
- **Ορισμός**: Κατηγορίες **χωρίς σειρά**
- **Operations**: = , ≠ (μόνο equality)
- **Παραδείγματα**: Χρώμα (red, blue), Φύλο (M, F), ID, Zip code

```
Nominal: {red, blue, green}
         Δεν μπορούμε να πούμε red < blue
```

### 1.2 Ordinal
- **Ορισμός**: Κατηγορίες **ΜΕ σειρά** αλλά χωρίς σταθερή απόσταση
- **Operations**: = , ≠ , < , >
- **Παραδείγματα**: Μέγεθος (S < M < L), Βαθμολογία (poor < fair < good)

```
Ordinal: small < medium < large
         Αλλά medium - small ≠ large - medium (μη σταθερή απόσταση)
```

### 1.3 Interval
- **Ορισμός**: Αριθμητικά με **σταθερή απόσταση** αλλά **ΧΩΡΙΣ true zero**
- **Operations**: = , ≠ , < , > , + , - (όχι ×, ÷ με νόημα)
- **Παραδείγματα**: Θερμοκρασία Celsius/Fahrenheit, Ημερομηνία

```
Interval: Celsius temperature
          10°C - 5°C = 5°C (διαφορά έχει νόημα)
          20°C δεν είναι "διπλάσια" από 10°C
          0°C δεν είναι "καθόλου θερμοκρασία"
```

### 1.4 Ratio
- **Ορισμός**: Αριθμητικά με **true zero** (absolute zero point)
- **Operations**: Όλες (= , ≠ , < , > , + , - , × , ÷)
- **Παραδείγματα**: Kelvin, Βάρος, Ύψος, Χρήματα, Ηλικία

```
Ratio: Kelvin temperature, Weight, Height
       0 Kelvin = absolute zero (no molecular motion)
       20kg είναι διπλάσια από 10kg
       0kg = καθόλου βάρος
```

### ⚠️ ΚΡΙΣΙΜΟ ΓΙΑ ΕΞΕΤΑΣΕΙΣ
```
Θερμοκρασία Celsius = Interval (0°C δεν είναι "καθόλου")
Θερμοκρασία Kelvin = Ratio (0K = absolute zero)
```

### Πίνακας Σύνοψης

| Type | Order | Distance | True Zero | Operations |
|------|-------|----------|-----------|------------|
| Nominal | ✗ | ✗ | ✗ | =, ≠ |
| Ordinal | ✓ | ✗ | ✗ | =, ≠, <, > |
| Interval | ✓ | ✓ | ✗ | =, ≠, <, >, +, - |
| Ratio | ✓ | ✓ | ✓ | =, ≠, <, >, +, -, ×, ÷ |

---

## 2. Ordered vs Unordered Data

### Ordered Data
Η **σειρά** των στοιχείων **έχει σημασία**.

**Παραδείγματα**:
- Video frames (η σειρά αλλάζει την ιστορία)
- Time series (stock prices over time)
- DNA sequences (ATCG sequence)
- Text (λέξεις σε πρόταση)
- Audio signals

### Unordered Data
Η **σειρά** των στοιχείων **δεν έχει σημασία**.

**Παραδείγματα**:
- Social network connections (friends)
- Shopping baskets (items purchased)
- Set of keywords
- Bag of words (NLP)

### Παράδειγμα Εξέτασης
```
Ερώτηση: Which of the following is ordered data?

A) Social network friends
B) Items in a shopping cart
C) Video frames ✓
D) Set of hashtags

ΑΠΑΝΤΗΣΗ: C
```

---

## 3. ER Diagrams - Cardinality

### Ορισμός
**Cardinality**: Πόσα instances μιας entity μπορούν να συνδεθούν με μια άλλη.

### Τύποι

**1:1 (One-to-One)**:
```
Person ──── Passport
Κάθε person έχει ακριβώς 1 passport
Κάθε passport ανήκει σε 1 person
```

**1:N (One-to-Many)**:
```
Department ───< Employee
Κάθε department έχει πολλούς employees
Κάθε employee ανήκει σε 1 department
```

**M:N (Many-to-Many)**:
```
Student >───< Course
Κάθε student παίρνει πολλά courses
Κάθε course έχει πολλούς students
```

### Notation
```
─────   1
───<    N (many) στην πλευρά με το <
>───<   M:N
```

---

## 4. Hidden Markov Models (HMMs)

### Τι είναι το HMM
- **Probabilistic model** για sequences
- Έχει **hidden states** (δεν τα βλέπουμε άμεσα)
- Βλέπουμε μόνο τα **observations** (emissions)

### Δομή HMM

```
Hidden States:  S1 ──→ S2 ──→ S3 ──→ ...
                 ↓      ↓      ↓
Observations:   O1     O2     O3
```

### Trainable Parameters

1. **Initial State Probabilities (π)**:
   - P(start in state Si)
   - Vector: π = [π₁, π₂, ..., πₙ]

2. **Transition Probabilities (A)**:
   - P(go from Si to Sj)
   - Matrix: A[i][j] = P(Sj | Si)

3. **Emission Probabilities (B)**:
   - P(observe Ok when in state Si)
   - Matrix: B[i][k] = P(Ok | Si)

### ⚠️ ΓΙΑ ΕΞΕΤΑΣΕΙΣ
```
HMM Trainable Parameters = Initial probabilities + Transition probabilities
                         = π + A
(Emission probabilities συχνά θεωρούνται fixed ή ξεχωριστά)
```

### Αλγόριθμοι HMM

| Algorithm | Σκοπός |
|-----------|--------|
| **Baum-Welch** | Training (EM algorithm) - μαθαίνει parameters |
| **Viterbi** | Decoding - βρίσκει most likely sequence of states |
| **Forward** | Evaluation - P(observations given model) |

### Baum-Welch Algorithm
- Είναι **Expectation-Maximization (EM)** algorithm
- **E-step**: Υπολογισμός expected state occupancies
- **M-step**: Update parameters

### Viterbi Algorithm
- **Dynamic programming** approach
- Βρίσκει το **most likely path** of hidden states
- Χρήση: Speech recognition, POS tagging

---

## 5. Sequences & Subsequences

### Sequence
- **Ordered list** of elements
- Π.χ.: <a, b, c, d, e>

### Subsequence
- **Διατηρεί τη σειρά** αλλά **όχι απαραίτητα συνεχόμενα**

```
Sequence: <a, b, c, d, e>
Subsequences:
  <a, c, e>      ✓ (διατηρεί σειρά)
  <b, d>         ✓
  <a, e>         ✓
  <c, a>         ✗ (αλλάζει σειρά)
```

### Substring vs Subsequence
- **Substring**: Συνεχόμενα στοιχεία
- **Subsequence**: Διατηρεί σειρά, όχι απαραίτητα συνεχόμενα

```
String: "abcde"
Substrings: "abc", "bcd", "de", "abcde"
Subsequences: "ace", "bd", "ae", "abcde"
```

---

## 6. Sequence Mining Concepts

### Support of a Sequence
```
Support(S) = (# sequences containing S) / (total # sequences)
```

### Frequent Sequence
Sequence με support ≥ min_support

### Maximal Frequent Sequence
Frequent sequence που δεν είναι subsequence κανενός άλλου frequent

---

## 7. Similarity Measures

### Jaccard Similarity (for sets)
```
J(A, B) = |A ∩ B| / |A ∪ B|
```

### Cosine Similarity (for vectors)
```
cos(A, B) = (A · B) / (||A|| × ||B||)
```

### Edit Distance (Levenshtein)
Minimum edits (insert, delete, substitute) για μετατροπή string A → B

---

## 8. Ερωτήσεις Εξετάσεων

### Ερώτηση 1: Kelvin Scale
```
Η κλίμακα Kelvin είναι:

A) Nominal
B) Ordinal
C) Interval
D) Ratio ✓

ΑΠΑΝΤΗΣΗ: D
ΕΞΗΓΗΣΗ: 0 Kelvin = absolute zero (true zero point)
```

### Ερώτηση 2: Celsius Scale
```
Η κλίμακα Celsius είναι:

A) Nominal
B) Ordinal
C) Interval ✓
D) Ratio

ΑΠΑΝΤΗΣΗ: C
ΕΞΗΓΗΣΗ: 0°C δεν είναι "καθόλου θερμοκρασία"
```

### Ερώτηση 3: Ordered Data
```
Which represents ordered data?

A) Set of user IDs
B) DNA sequence ✓
C) Bag of words
D) Social network friends

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 4: HMM Training
```
Τι μαθαίνει ο Baum-Welch algorithm;

A) Transition probabilities ✓
B) Observation sequence
C) Hidden state sequence
D) Number of states

ΑΠΑΝΤΗΣΗ: A
ΕΞΗΓΗΣΗ: Baum-Welch trains the HMM parameters (π, A, B)
```

### Ερώτηση 5: Viterbi Purpose
```
Ο Viterbi algorithm χρησιμοποιείται για:

A) Training the HMM
B) Finding most likely state sequence ✓
C) Generating observations
D) Counting states

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 6: Ordinal vs Interval
```
Ποια είναι η διαφορά ordinal από interval;

A) Ordinal έχει order
B) Interval έχει equal spacing ✓
C) Ordinal έχει true zero
D) Καμία διαφορά

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Ordinal: S < M < L (αλλά M-S ≠ L-M)
         Interval: 10°C - 5°C = 15°C - 10°C = 5°C
```

### Ερώτηση 7: Subsequence
```
Ποια είναι subsequence του <A, B, C, D>;

A) <B, A>
B) <C, D, A>
C) <A, C> ✓
D) <D, B>

ΑΠΑΝΤΗΣΗ: C
ΕΞΗΓΗΣΗ: Διατηρεί τη σειρά A→C
```

---

## Σύνοψη - Key Points

### Data Types Hierarchy
```
Nominal < Ordinal < Interval < Ratio
(λιγότερες) ─────────────────→ (περισσότερες) operations
```

### Quick Reference

| Question | Answer |
|----------|--------|
| Celsius | Interval |
| Kelvin | **Ratio** |
| Fahrenheit | Interval |
| Age | Ratio |
| ZIP code | Nominal |
| Grade (A,B,C) | Ordinal |
| Weight | Ratio |
| Temperature difference | Interval |

### HMM Algorithms

| Algorithm | Purpose |
|-----------|---------|
| Baum-Welch | Training (learns parameters) |
| Viterbi | Decoding (finds best path) |
| Forward/Backward | Evaluation (computes probability) |

### Ordered vs Unordered

| Ordered | Unordered |
|---------|-----------|
| Video | Shopping basket |
| Time series | Social connections |
| DNA sequence | Set of keywords |
| Text | Bag of words |
