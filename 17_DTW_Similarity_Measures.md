# DTW & Similarity Measures - Πλήρης Οδηγός Μελέτης

## 1. Εισαγωγή

**Similarity/Distance Measures** αξιολογούν πόσο "κοντά" ή "μακριά" είναι δύο αντικείμενα. Η επιλογή του κατάλληλου μέτρου εξαρτάται από τον τύπο δεδομένων.

---

## 2. Μέτρα Απόστασης (Distance Metrics)

### 2.1 Euclidean Distance

Η "ευθεία γραμμή" απόσταση στον n-διάστατο χώρο.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  d(x, y) = √(Σ (xᵢ - yᵢ)²)                                 │
│             i=1 to n                                        │
│                                                             │
│  2D: d = √((x₁-y₁)² + (x₂-y₂)²)                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
x = (1, 2, 3)
y = (4, 6, 3)

d = √((1-4)² + (2-6)² + (3-3)²)
  = √(9 + 16 + 0)
  = √25
  = 5
```

### 2.2 Manhattan Distance (City Block / L1)

Η "ταξί" απόσταση - κίνηση μόνο οριζόντια/κάθετα.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  d(x, y) = Σ |xᵢ - yᵢ|                                     │
│            i=1 to n                                         │
│                                                             │
│  2D: d = |x₁-y₁| + |x₂-y₂|                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
x = (1, 2)
y = (4, 6)

d = |1-4| + |2-6|
  = 3 + 4
  = 7
```

### 2.3 Minkowski Distance (Generalized)

Γενίκευση Euclidean και Manhattan.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  d(x, y) = (Σ |xᵢ - yᵢ|^p)^(1/p)                          │
│             i=1 to n                                        │
│                                                             │
│  p = 1: Manhattan Distance                                 │
│  p = 2: Euclidean Distance                                 │
│  p → ∞: Chebyshev Distance (max|xᵢ - yᵢ|)                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.4 Cosine Similarity

Μετράει τη γωνία μεταξύ δύο vectors (χρήσιμο για text/sparse data).

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    x · y                                    │
│  cos(θ) = ─────────────────────                            │
│            ||x|| × ||y||                                    │
│                                                             │
│           Σ xᵢ × yᵢ                                        │
│         = ─────────────────────                            │
│           √(Σ xᵢ²) × √(Σ yᵢ²)                             │
│                                                             │
│  Similarity: 1 = identical direction                        │
│              0 = orthogonal                                 │
│             -1 = opposite direction                         │
│                                                             │
│  Distance: 1 - cos(θ)                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
x = (1, 2, 3)
y = (2, 4, 6)

cos(θ) = (1×2 + 2×4 + 3×6) / (√(1+4+9) × √(4+16+36))
       = (2 + 8 + 18) / (√14 × √56)
       = 28 / (3.74 × 7.48)
       = 28 / 28
       = 1.0

Vectors έχουν ίδια κατεύθυνση (y = 2x)
```

### 2.5 Jaccard Similarity

Για sets - μετράει overlap.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              |A ∩ B|                                        │
│  J(A, B) = ───────────                                      │
│              |A ∪ B|                                        │
│                                                             │
│  Range: [0, 1]                                              │
│  1 = identical sets                                         │
│  0 = no common elements                                     │
│                                                             │
│  Distance: 1 - J(A, B)                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
A = {apple, banana, orange}
B = {banana, orange, grape}

A ∩ B = {banana, orange} → |A ∩ B| = 2
A ∪ B = {apple, banana, orange, grape} → |A ∪ B| = 4

J(A, B) = 2/4 = 0.5
```

### Σύγκριση Μέτρων

| Metric | Best For | Property |
|--------|----------|----------|
| **Euclidean** | Continuous, dense | Sensitive to magnitude |
| **Manhattan** | Grid-like, sparse | More robust to outliers |
| **Cosine** | Text, high-dim | Only considers direction |
| **Jaccard** | Sets, binary | Ignores frequency |

---

## 3. Dynamic Time Warping (DTW)

### 3.1 Το Πρόβλημα

**Euclidean**: Συγκρίνει point-to-point (i με i)
- Πρόβλημα: Αν οι ακολουθίες είναι **shifted ή stretched**, μεγάλη απόσταση!

```
Euclidean fails:
Series 1: [1, 2, 3, 4, 5]
Series 2: [1, 1, 2, 3, 4, 5]  (shifted by 1)

ED compares: 1-1, 2-1, 3-2, 4-3, 5-4... BIG distance!
```

**DTW**: Επιτρέπει **non-linear alignment** (warping)
- Βρίσκει optimal matching ακόμα κι αν οι ακολουθίες έχουν διαφορετική ταχύτητα

### 3.2 DTW Recurrence Relation

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  DTW(i, j) = d(xᵢ, yⱼ) + min { DTW(i-1, j)                │
│                               { DTW(i, j-1)                │
│                               { DTW(i-1, j-1)              │
│                                                             │
│  d(xᵢ, yⱼ) = |xᵢ - yⱼ| ή (xᵢ - yⱼ)²                      │
│                                                             │
│  Base cases:                                                │
│  DTW(0, 0) = 0                                              │
│  DTW(i, 0) = ∞  για i > 0                                  │
│  DTW(0, j) = ∞  για j > 0                                  │
│                                                             │
│  Final answer: DTW(n, m)                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Επεξήγηση Transitions

```
Από (i-1, j-1) → (i, j): Diagonal (κανονικό matching)
Από (i-1, j) → (i, j):   Vertical (repeat y element)
Από (i, j-1) → (i, j):   Horizontal (repeat x element)

       j-1   j
      ┌─────┬─────┐
  i-1 │  ↘  │  ↓  │
      ├─────┼─────┤
  i   │  →  │ (i,j)│
      └─────┴─────┘
```

### 3.4 Worked Example (ΤΥΠΙΚΟ ΘΕΜΑ ΕΞΕΤΑΣΕΩΝ!)

**Sequences**:
```
X = [1, 3, 4, 2]  (n=4)
Y = [2, 4, 3]     (m=3)

Distance: |xᵢ - yⱼ| (absolute difference)
```

**Βήμα 1: Cost Matrix (d(xᵢ, yⱼ))**

```
        Y:  2    4    3
           ┌────┬────┬────┐
  X: 1     │ 1  │ 3  │ 2  │
           ├────┼────┼────┤
     3     │ 1  │ 1  │ 0  │
           ├────┼────┼────┤
     4     │ 2  │ 0  │ 1  │
           ├────┼────┼────┤
     2     │ 0  │ 2  │ 1  │
           └────┴────┴────┘

d(1,2)=|1-2|=1, d(1,4)=3, d(1,3)=2
d(3,2)=1, d(3,4)=1, d(3,3)=0
d(4,2)=2, d(4,4)=0, d(4,3)=1
d(2,2)=0, d(2,4)=2, d(2,3)=1
```

**Βήμα 2: DTW Matrix (Cumulative Cost)**

```
Initialize: DTW(0,0) = 0, borders = ∞

        Y:  -    2    4    3
           ┌────┬────┬────┬────┐
  X: -     │ 0  │ ∞  │ ∞  │ ∞  │
           ├────┼────┼────┼────┤
     1     │ ∞  │ ?  │ ?  │ ?  │
           ├────┼────┼────┼────┤
     3     │ ∞  │ ?  │ ?  │ ?  │
           ├────┼────┼────┼────┤
     4     │ ∞  │ ?  │ ?  │ ?  │
           ├────┼────┼────┼────┤
     2     │ ∞  │ ?  │ ?  │ ?  │
           └────┴────┴────┴────┘
```

**Fill DTW matrix:**

```
DTW(1,1) = d(1,2) + min(DTW(0,0), DTW(0,1), DTW(1,0))
         = 1 + min(0, ∞, ∞) = 1 + 0 = 1

DTW(1,2) = d(1,4) + min(DTW(0,1), DTW(0,2), DTW(1,1))
         = 3 + min(∞, ∞, 1) = 3 + 1 = 4

DTW(1,3) = d(1,3) + min(DTW(0,2), DTW(0,3), DTW(1,2))
         = 2 + min(∞, ∞, 4) = 2 + 4 = 6

DTW(2,1) = d(3,2) + min(DTW(1,0), DTW(1,1), DTW(2,0))
         = 1 + min(∞, 1, ∞) = 1 + 1 = 2

DTW(2,2) = d(3,4) + min(DTW(1,1), DTW(1,2), DTW(2,1))
         = 1 + min(1, 4, 2) = 1 + 1 = 2

DTW(2,3) = d(3,3) + min(DTW(1,2), DTW(1,3), DTW(2,2))
         = 0 + min(4, 6, 2) = 0 + 2 = 2

DTW(3,1) = d(4,2) + min(DTW(2,0), DTW(2,1), DTW(3,0))
         = 2 + min(∞, 2, ∞) = 2 + 2 = 4

DTW(3,2) = d(4,4) + min(DTW(2,1), DTW(2,2), DTW(3,1))
         = 0 + min(2, 2, 4) = 0 + 2 = 2

DTW(3,3) = d(4,3) + min(DTW(2,2), DTW(2,3), DTW(3,2))
         = 1 + min(2, 2, 2) = 1 + 2 = 3

DTW(4,1) = d(2,2) + min(DTW(3,0), DTW(3,1), DTW(4,0))
         = 0 + min(∞, 4, ∞) = 0 + 4 = 4

DTW(4,2) = d(2,4) + min(DTW(3,1), DTW(3,2), DTW(4,1))
         = 2 + min(4, 2, 4) = 2 + 2 = 4

DTW(4,3) = d(2,3) + min(DTW(3,2), DTW(3,3), DTW(4,2))
         = 1 + min(2, 3, 4) = 1 + 2 = 3
```

**Final DTW Matrix:**

```
        Y:  -    2    4    3
           ┌────┬────┬────┬────┐
  X: -     │ 0  │ ∞  │ ∞  │ ∞  │
           ├────┼────┼────┼────┤
     1     │ ∞  │ 1  │ 4  │ 6  │
           ├────┼────┼────┼────┤
     3     │ ∞  │ 2  │ 2  │ 2  │
           ├────┼────┼────┼────┤
     4     │ ∞  │ 4  │ 2  │ 3  │
           ├────┼────┼────┼────┤
     2     │ ∞  │ 4  │ 4  │[3] │
           └────┴────┴────┴────┘

DTW Distance = 3
```

**Βήμα 3: Optimal Warping Path (Backtracking)**

```
Start: (4,3) → 3
       (3,2) → 2 (diagonal, min of 2,3,4)
       (2,2) → 2 (diagonal, min of 1,4,2)
       (1,1) → 1 (diagonal)
       (0,0) → 0

Path: (0,0)→(1,1)→(2,2)→(3,2)→(4,3)

Alignment:
X[1]=1 ↔ Y[1]=2
X[2]=3 ↔ Y[2]=4
X[3]=4 ↔ Y[2]=4  (Y[2] reused!)
X[4]=2 ↔ Y[3]=3
```

**Visual Warping Path:**

```
        Y:  2    4    3
           ┌────┬────┬────┐
  X: 1     │ ●  │    │    │
           ├──↘─┼────┼────┤
     3     │    │ ●  │    │
           ├────┼──↓─┼────┤
     4     │    │ ●  │    │
           ├────┼────┼──↘─┤
     2     │    │    │ ●  │
           └────┴────┴────┘
```

### 3.5 DTW vs Euclidean

| Property | Euclidean | DTW |
|----------|-----------|-----|
| **Alignment** | 1-to-1 | Many-to-many |
| **Speed** | O(n) | O(n×m) |
| **Stretch/Shift** | Sensitive | Robust |
| **Triangle Inequality** | Yes | No |

---

## 4. ⚠️ Συχνά Λάθη / Pitfalls

### 4.1 DTW Base Cases
```
❌ ΛΑΘΟΣ: DTW(0,j) = 0 ή DTW(i,0) = 0
✓ ΣΩΣΤΟ: DTW(0,j) = ∞, DTW(i,0) = ∞ (για i,j > 0)
         DTW(0,0) = 0 μόνο!

Αυτό εξασφαλίζει ότι δεν μπορούμε να "παραλείψουμε" στοιχεία.
```

### 4.2 Cost vs Distance
```
❌ ΛΑΘΟΣ: d(x,y) = x - y
✓ ΣΩΣΤΟ: d(x,y) = |x - y| ή (x - y)²

Η απόσταση πρέπει να είναι μη-αρνητική!
```

### 4.3 Cosine Similarity
```
❌ ΛΑΘΟΣ: Cosine similarity μετράει απόσταση
✓ ΣΩΣΤΟ: Cosine similarity μετράει ΟΜΟΙΟΤΗΤΑ (1 = ίδια)

Cosine Distance = 1 - Cosine Similarity
```

### 4.4 Jaccard Denominator
```
❌ ΛΑΘΟΣ: Jaccard = |A ∩ B| / max(|A|, |B|)
✓ ΣΩΣΤΟ: Jaccard = |A ∩ B| / |A ∪ B|

|A ∪ B| = |A| + |B| - |A ∩ B|
```

---

## 5. Ερωτήσεις Εξετάσεων

### Ερώτηση 1
Euclidean distance μεταξύ (1, 2, 3) και (4, 6, 3);

A) 5
B) 7
C) 25
D) √34

<details>
<summary>Απάντηση</summary>

**Σωστό: A) 5**

**Υπολογισμός**:
```
d = √((1-4)² + (2-6)² + (3-3)²)
  = √(9 + 16 + 0)
  = √25
  = 5
```
</details>

---

### Ερώτηση 2
Manhattan distance μεταξύ (0, 0) και (3, 4);

A) 5
B) 7
C) 12
D) 25

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 7**

**Υπολογισμός**:
```
d = |0-3| + |0-4| = 3 + 4 = 7
```

(Σημείωση: Euclidean θα ήταν √(9+16) = 5)
</details>

---

### Ερώτηση 3
Cosine similarity μεταξύ (1, 0) και (0, 1);

A) 0
B) 0.5
C) 1
D) -1

<details>
<summary>Απάντηση</summary>

**Σωστό: A) 0**

**Υπολογισμός**:
```
cos(θ) = (1×0 + 0×1) / (√1 × √1)
       = 0 / 1
       = 0
```

Τα vectors είναι orthogonal (κάθετα).
</details>

---

### Ερώτηση 4
Jaccard similarity μεταξύ {1, 2, 3} και {2, 3, 4};

A) 0.25
B) 0.50
C) 0.67
D) 0.75

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 0.50**

**Υπολογισμός**:
```
A ∩ B = {2, 3} → |A ∩ B| = 2
A ∪ B = {1, 2, 3, 4} → |A ∪ B| = 4

J = 2/4 = 0.50
```
</details>

---

### Ερώτηση 5
Στο DTW, τι σημαίνει η diagonal transition (i-1, j-1) → (i, j);

A) Skip element in X
B) Skip element in Y
C) Match xᵢ with yⱼ
D) Repeat previous match

<details>
<summary>Απάντηση</summary>

**Σωστό: C) Match xᵢ with yⱼ**

**Εξήγηση**:
- Diagonal: κανονικό 1-1 matching
- Vertical (i-1,j)→(i,j): repeat Y element
- Horizontal (i,j-1)→(i,j): repeat X element
</details>

---

### Ερώτηση 6
Γιατί το DTW είναι καλύτερο από Euclidean για time series με time shift;

A) Είναι πιο γρήγορο
B) Επιτρέπει non-linear alignment
C) Χρησιμοποιεί cosine distance
D) Αγνοεί outliers

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: DTW επιτρέπει "warping" - μπορεί να ταιριάξει σημεία που δεν είναι στην ίδια θέση, αντιμετωπίζοντας shifts και stretches.
</details>

---

### Ερώτηση 7
DTW(i, j) = d(xᵢ, yⱼ) + min(...). Τι είναι το d(xᵢ, yⱼ);

A) Το συνολικό DTW distance
B) Η τοπική απόσταση μεταξύ xᵢ και yⱼ
C) Η Euclidean distance ολόκληρων των sequences
D) Η μέση απόσταση

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: d(xᵢ, yⱼ) είναι η τοπική (local) cost για το matching του xᵢ με το yⱼ, συνήθως |xᵢ - yⱼ| ή (xᵢ - yⱼ)².
</details>

---

### Ερώτηση 8
Sequences X=[1, 2], Y=[1, 2, 3]. Πόσο είναι το DTW matrix size;

A) 2×2
B) 2×3
C) 3×4
D) 3×3

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 3×4** (με τη row/column για base case)

**Εξήγηση**:
- X έχει 2 elements + 1 base = 3 rows
- Y έχει 3 elements + 1 base = 4 columns

Αν δεν μετράμε base: 2×3 (option B)
</details>

---

### Ερώτηση 9
Ποιο μέτρο αγνοεί το magnitude και εστιάζει στη direction;

A) Euclidean
B) Manhattan
C) Cosine
D) Jaccard

<details>
<summary>Απάντηση</summary>

**Σωστό: C) Cosine**

**Εξήγηση**: Cosine similarity μετράει τη γωνία μεταξύ vectors. Vectors (1,2,3) και (2,4,6) έχουν cosine=1 (ίδια κατεύθυνση) παρόλο που έχουν διαφορετικό magnitude.
</details>

---

### Ερώτηση 10
Αν X = [2, 4], Y = [3] και d = |xᵢ - yⱼ|, ποιο είναι το DTW distance;

A) 1
B) 2
C) 3
D) 5

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 2**

**Υπολογισμός**:
```
Cost matrix:
     Y: 3
X: 2  |2-3|=1
   4  |4-3|=1

DTW matrix:
       -    3
   -   0    ∞
   2   ∞    1  (0 + 1)
   4   ∞    2  (1 + 1)

DTW = 2
```

Path: (0,0)→(1,1)→(2,1): both X elements match to single Y element
</details>

---

## 6. Σύνοψη - Key Points

### Distance Metrics (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  Euclidean:   d = √(Σ(xᵢ - yᵢ)²)                          │
│                                                            │
│  Manhattan:   d = Σ|xᵢ - yᵢ|                              │
│                                                            │
│  Cosine sim:  cos(θ) = (x·y) / (||x|| × ||y||)            │
│               distance = 1 - cos(θ)                        │
│                                                            │
│  Jaccard:     J = |A ∩ B| / |A ∪ B|                       │
│               distance = 1 - J                             │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### DTW Recurrence (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  DTW(i, j) = d(xᵢ, yⱼ) + min { DTW(i-1, j-1)  [diagonal] │
│                               { DTW(i-1, j)    [vertical] │
│                               { DTW(i, j-1)    [horizontal]│
│                                                            │
│  Base: DTW(0,0) = 0                                        │
│        DTW(i,0) = DTW(0,j) = ∞ (for i,j > 0)              │
│                                                            │
│  Answer: DTW(n, m)                                         │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Σύγκριση

| Metric | Best For | Note |
|--------|----------|------|
| Euclidean | Dense, continuous | Sensitive to scale |
| Manhattan | Sparse, grid | Robust to outliers |
| Cosine | Text, high-dim | Direction only |
| Jaccard | Sets | Binary |
| DTW | Time series | Handles warping |
