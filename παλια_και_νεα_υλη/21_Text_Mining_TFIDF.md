# Text Mining & TF-IDF - Πλήρης Οδηγός Μελέτης

## 1. Εισαγωγή

**Text Mining** αναλύει και εξάγει πληροφορίες από κείμενα. **TF-IDF** είναι μέθοδος για να μετρήσουμε τη σημασία λέξεων σε documents.

---

## 2. Βασικές Έννοιες

### 2.1 Document Representation

```
┌─────────────────────────────────────────────────────────────┐
│  BAG OF WORDS (BoW):                                        │
│  - Αγνοεί τη σειρά των λέξεων                              │
│  - Μετράει μόνο frequencies                                 │
│  - Document = vector of word counts                         │
│                                                             │
│  Παράδειγμα:                                                │
│  "the cat sat on the mat" → {the:2, cat:1, sat:1, on:1, mat:1}│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Preprocessing Steps

1. **Tokenization**: Split σε words
2. **Lowercasing**: Convert σε πεζά
3. **Stopword removal**: Αφαίρεση common words (the, is, at)
4. **Stemming**: Reduce σε root (running → run)
5. **Lemmatization**: Reduce σε dictionary form (better → good)

---

## 3. Term Frequency (TF)

### 3.1 Ορισμός

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  TF(t, d) = (αριθμός εμφανίσεων του t στο d)               │
│                                                             │
│  Variants:                                                  │
│                                                             │
│  Raw count:      tf(t,d) = f(t,d)                          │
│                                                             │
│  Boolean:        tf(t,d) = 1 if t∈d, else 0                │
│                                                             │
│  Log normalized: tf(t,d) = 1 + log(f(t,d)) if f>0          │
│                                                             │
│  Augmented:      tf(t,d) = 0.5 + 0.5 × f(t,d)/max{f(w,d)}  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Παράδειγμα

```
Document: "the cat sat on the mat the cat"

TF("the") = 3
TF("cat") = 2
TF("sat") = 1
TF("on") = 1
TF("mat") = 1
```

---

## 4. Inverse Document Frequency (IDF)

### 4.1 Ορισμός

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              N                                              │
│  IDF(t) = log(────)                                        │
│              df(t)                                          │
│                                                             │
│  N = total number of documents                              │
│  df(t) = number of documents containing term t              │
│                                                             │
│  Variants (smooth):                                         │
│                                                             │
│  IDF(t) = log(N / (df(t) + 1)) + 1                         │
│                                                             │
│  IDF(t) = log((N + 1) / (df(t) + 1))                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Ερμηνεία

```
Λέξη σε ΠΟΛΛΑ documents → χαμηλό IDF (λιγότερο σημαντική)
Λέξη σε ΛΙΓΑ documents → υψηλό IDF (πιο διακριτική)

Παράδειγμα (N=1000):
  "the" εμφανίζεται σε 950 docs: IDF = log(1000/950) ≈ 0.02
  "algorithm" σε 50 docs:        IDF = log(1000/50) = 3.00
  "DBSCAN" σε 5 docs:            IDF = log(1000/5) = 5.30
```

---

## 5. TF-IDF

### 5.1 Ορισμός

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  TF-IDF(t, d) = TF(t, d) × IDF(t)                          │
│                                                             │
│  Υψηλό TF-IDF σημαίνει:                                    │
│  - Λέξη εμφανίζεται συχνά στο ΣΥΓΚΕΚΡΙΜΕΝΟ document        │
│  - Λέξη είναι ΣΠΑΝΙΑ στα υπόλοιπα documents                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Worked Example

**Corpus (3 documents)**:
```
D1: "the cat sat on the mat"
D2: "the dog sat on the log"
D3: "the cat and the dog"
```

**Βήμα 1: Calculate TF**
```
       | D1  | D2  | D3  |
-------|-----|-----|-----|
the    |  2  |  2  |  2  |
cat    |  1  |  0  |  1  |
sat    |  1  |  1  |  0  |
on     |  1  |  1  |  0  |
mat    |  1  |  0  |  0  |
dog    |  0  |  1  |  1  |
log    |  0  |  1  |  0  |
and    |  0  |  0  |  1  |
```

**Βήμα 2: Calculate DF and IDF (N=3)**
```
       | df  | IDF = log(N/df)     |
-------|-----|---------------------|
the    |  3  | log(3/3) = 0        |
cat    |  2  | log(3/2) = 0.405    |
sat    |  2  | log(3/2) = 0.405    |
on     |  2  | log(3/2) = 0.405    |
mat    |  1  | log(3/1) = 1.099    |
dog    |  2  | log(3/2) = 0.405    |
log    |  1  | log(3/1) = 1.099    |
and    |  1  | log(3/1) = 1.099    |
```

**Βήμα 3: Calculate TF-IDF**
```
       | D1              | D2              | D3              |
-------|-----------------|-----------------|-----------------|
the    | 2 × 0 = 0       | 2 × 0 = 0       | 2 × 0 = 0       |
cat    | 1 × 0.405 = 0.41| 0 × 0.405 = 0   | 1 × 0.405 = 0.41|
sat    | 1 × 0.405 = 0.41| 1 × 0.405 = 0.41| 0 × 0.405 = 0   |
on     | 1 × 0.405 = 0.41| 1 × 0.405 = 0.41| 0 × 0.405 = 0   |
mat    | 1 × 1.099 = 1.10| 0 × 1.099 = 0   | 0 × 1.099 = 0   |
dog    | 0 × 0.405 = 0   | 1 × 0.405 = 0.41| 1 × 0.405 = 0.41|
log    | 0 × 1.099 = 0   | 1 × 1.099 = 1.10| 0 × 1.099 = 0   |
and    | 0 × 1.099 = 0   | 0 × 1.099 = 0   | 1 × 1.099 = 1.10|
```

**Παρατηρήσεις**:
- "the" έχει TF-IDF = 0 παντού (πολύ κοινή)
- "mat", "log", "and" έχουν υψηλό TF-IDF (unique στα docs τους)
- Αυτές οι λέξεις "χαρακτηρίζουν" κάθε document

---

## 6. Document Similarity

### 6.1 Vector Space Model

```
Κάθε document = vector στο term space

D1 = [0, 0.41, 0.41, 0.41, 1.10, 0, 0, 0]
D2 = [0, 0, 0.41, 0.41, 0, 0.41, 1.10, 0]
D3 = [0, 0.41, 0, 0, 0, 0.41, 0, 1.10]
```

### 6.2 Cosine Similarity

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                  d₁ · d₂                                   │
│  sim(d₁, d₂) = ──────────────                              │
│                 ||d₁|| × ||d₂||                            │
│                                                             │
│  = Σ(tfidf₁[i] × tfidf₂[i]) / (√Σtfidf₁²[i] × √Σtfidf₂²[i])│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα: sim(D1, D2)**:
```
D1 · D2 = 0 + 0 + 0.41×0.41 + 0.41×0.41 + 0 + 0 + 0 + 0
        = 0.168 + 0.168
        = 0.336

||D1|| = √(0.41² + 0.41² + 0.41² + 1.10²)
       = √(0.168 + 0.168 + 0.168 + 1.21) = √1.714 = 1.31

||D2|| = √(0.41² + 0.41² + 0.41² + 1.10²)
       = √1.714 = 1.31

sim(D1, D2) = 0.336 / (1.31 × 1.31) = 0.336 / 1.716 = 0.20
```

---

## 7. ⚠️ Συχνά Λάθη / Pitfalls

### 7.1 Log Base
```
❌ ΛΑΘΟΣ: Υποθέτουμε ln χωρίς να το ξεκαθαρίσουμε
✓ ΣΩΣΤΟ: Δεν έχει σημασία η βάση (σταθερός συντελεστής)

Συνήθως: log₁₀ ή ln (natural log)
```

### 7.2 df = 0
```
❌ ΛΑΘΟΣ: IDF = log(N/0) → undefined!
✓ ΣΩΣΤΟ: Χρήση smoothing: log(N/(df+1)) ή log((N+1)/(df+1))
```

### 7.3 TF-IDF για Query
```
Για search: υπολόγισε TF-IDF για το query document
και βρες similarity με τα corpus documents.
```

---

## 8. Ερωτήσεις Εξετάσεων

### Ερώτηση 1
N=100 documents, λέξη "algorithm" εμφανίζεται σε 10. IDF(algorithm) = ?

A) 1
B) 10
C) log(10)
D) log(100)

<details>
<summary>Απάντηση</summary>

**Σωστό: C) log(10)**

**Υπολογισμός**:
```
IDF = log(N/df) = log(100/10) = log(10) ≈ 1 (αν base 10)
                                       ≈ 2.3 (αν ln)
```
</details>

---

### Ερώτηση 2
Λέξη εμφανίζεται σε ΟΛΑ τα documents. IDF = ?

A) 0
B) 1
C) log(N)
D) N

<details>
<summary>Απάντηση</summary>

**Σωστό: A) 0**

**Υπολογισμός**:
```
df = N (εμφανίζεται σε όλα)
IDF = log(N/N) = log(1) = 0
```

Αυτό σημαίνει ότι η λέξη δεν είναι διακριτική!
</details>

---

### Ερώτηση 3
Document D: "cat cat dog". TF("cat") = ?

A) 1
B) 2
C) 2/3
D) 3

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 2**

**Εξήγηση**: TF = raw count = 2 (η λέξη "cat" εμφανίζεται 2 φορές).

Αν η ερώτηση ζητούσε normalized TF, θα ήταν 2/3.
</details>

---

### Ερώτηση 4
Γιατί χρησιμοποιούμε IDF;

A) Για να μετρήσουμε τη συχνότητα
B) Για να μειώσουμε τη σημασία common words
C) Για encryption
D) Για compression

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: IDF μειώνει το βάρος λέξεων που εμφανίζονται παντού (π.χ. "the", "is") και αυξάνει το βάρος σπάνιων, πιο διακριτικών λέξεων.
</details>

---

### Ερώτηση 5
TF-IDF υψηλό σημαίνει:

A) Λέξη πολύ κοινή
B) Λέξη σπάνια σε όλο το corpus
C) Λέξη συχνή στο doc ΚΑΙ σπάνια αλλού
D) Λέξη με πολλά γράμματα

<details>
<summary>Απάντηση</summary>

**Σωστό: C)**

**Εξήγηση**: TF-IDF = TF × IDF
- Υψηλό TF: συχνή στο document
- Υψηλό IDF: σπάνια στο corpus
- Υψηλό TF-IDF: συνδυασμός των δύο
</details>

---

### Ερώτηση 6
Ποια λέξη έχει υψηλότερο IDF;

A) "the" (εμφανίζεται σε 90% docs)
B) "algorithm" (εμφανίζεται σε 10% docs)
C) "DBSCAN" (εμφανίζεται σε 1% docs)
D) Ίδιο IDF για όλες

<details>
<summary>Απάντηση</summary>

**Σωστό: C) "DBSCAN"**

**Εξήγηση**:
```
IDF = log(N/df)

Smaller df → Higher IDF

DBSCAN: df = 0.01×N → IDF = log(100) = highest
algorithm: df = 0.10×N → IDF = log(10)
the: df = 0.90×N → IDF = log(1.11) ≈ 0
```
</details>

---

### Ερώτηση 7
Cosine similarity range είναι:

A) [0, 1]
B) [-1, 1]
C) [0, ∞)
D) (-∞, ∞)

<details>
<summary>Απάντηση</summary>

**Σωστό: A) [0, 1]** για TF-IDF vectors

**Εξήγηση**: Επειδή TF-IDF values είναι non-negative, τα vectors είναι στο θετικό orthant, οπότε cosine similarity ∈ [0, 1].

(Για general vectors: [-1, 1])
</details>

---

### Ερώτηση 8
Bag of Words αγνοεί:

A) Word frequency
B) Word order
C) Document length
D) Vocabulary

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Word order**

**Εξήγηση**: "the cat sat on the mat" και "the mat sat on the cat" έχουν ΙΔΙΟ BoW representation!
</details>

---

## 9. Σύνοψη - Key Points

### Τύποι (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  TF(t, d) = count of t in d                                │
│                                                             │
│  IDF(t) = log(N / df(t))                                   │
│                                                             │
│  TF-IDF(t, d) = TF(t, d) × IDF(t)                         │
│                                                             │
│  N = total documents                                        │
│  df(t) = documents containing t                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Interpretation

```
High TF:     Word common IN THIS document
High IDF:    Word RARE across corpus
High TF-IDF: Word is characteristic of this document

Low IDF (≈0): Word in almost all docs → not discriminative
```

### Document Similarity

```
Cosine Similarity = (d₁ · d₂) / (||d₁|| × ||d₂||)

Range for TF-IDF: [0, 1]
1 = identical documents
0 = completely different
```
