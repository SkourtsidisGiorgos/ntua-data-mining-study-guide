# Clustering: DBSCAN & K-means - Πλήρης Οδηγός Μελέτης

## 1. Εισαγωγή

**Clustering** είναι unsupervised learning που ομαδοποιεί δεδομένα σε clusters χωρίς προκαθορισμένες κατηγορίες.

### Τύποι Clustering

| Τύπος | Περιγραφή | Παράδειγμα |
|-------|-----------|------------|
| **Partitional** | Διαμερίζει σε k clusters | K-means |
| **Hierarchical** | Δημιουργεί ιεραρχία clusters | Agglomerative |
| **Density-based** | Clusters με βάση πυκνότητα | DBSCAN |

---

## 2. K-means Algorithm

### 2.1 Βασική Ιδέα

Διαμερίζει n σημεία σε **k clusters** ελαχιστοποιώντας το **within-cluster variance**.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Objective: minimize Σ Σ ||x - μₖ||²                       │
│                      k x∈Cₖ                                 │
│                                                             │
│  μₖ = centroid του cluster k                               │
│  Cₖ = σύνολο σημείων στο cluster k                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Αλγόριθμος

```
┌────────────────────────────────────────────────────────────┐
│  K-MEANS ALGORITHM                                         │
│  ─────────────────                                         │
│                                                            │
│  INPUT: Data points X, number of clusters k                │
│  OUTPUT: k clusters C₁, C₂, ..., Cₖ                       │
│                                                            │
│  1. INITIALIZE: Επέλεξε k αρχικά centroids τυχαία          │
│                                                            │
│  2. REPEAT until convergence:                              │
│                                                            │
│     a) ASSIGNMENT STEP:                                    │
│        Για κάθε σημείο x, ανάθεσέ το στο cluster          │
│        με το κοντινότερο centroid:                         │
│        Cᵢ = {x : ||x - μᵢ|| ≤ ||x - μⱼ|| ∀j}             │
│                                                            │
│     b) UPDATE STEP:                                        │
│        Υπολόγισε νέα centroids ως τον μέσο όρο:           │
│        μₖ = (1/|Cₖ|) × Σ x                                 │
│                        x∈Cₖ                                │
│                                                            │
│  3. RETURN clusters C₁, ..., Cₖ                           │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 2.3 Centroid Update Formula

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Νέο Centroid μₖ = (1/nₖ) × Σ xᵢ                           │
│                           i∈Cₖ                              │
│                                                             │
│  nₖ = αριθμός σημείων στο cluster k                        │
│                                                             │
│  Για 2D: μₖ = ((Σxᵢ)/nₖ, (Σyᵢ)/nₖ)                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.4 Worked Example

**Data points**: A(1,1), B(1,2), C(2,1), D(5,4), E(5,5), F(6,5)
**k = 2**

**Iteration 1**:
```
Initial centroids (random): μ₁ = A(1,1), μ₂ = D(5,4)

Assignment:
  A(1,1): dist to μ₁=0, dist to μ₂=5 → C₁
  B(1,2): dist to μ₁=1, dist to μ₂=4.47 → C₁
  C(2,1): dist to μ₁=1, dist to μ₂=4.24 → C₁
  D(5,4): dist to μ₁=5, dist to μ₂=0 → C₂
  E(5,5): dist to μ₁=5.66, dist to μ₂=1 → C₂
  F(6,5): dist to μ₁=6.40, dist to μ₂=1.41 → C₂

Clusters: C₁ = {A, B, C}, C₂ = {D, E, F}

Update centroids:
  μ₁ = ((1+1+2)/3, (1+2+1)/3) = (4/3, 4/3) = (1.33, 1.33)
  μ₂ = ((5+5+6)/3, (4+5+5)/3) = (16/3, 14/3) = (5.33, 4.67)
```

**Iteration 2**:
```
New centroids: μ₁ = (1.33, 1.33), μ₂ = (5.33, 4.67)

Assignment:
  A(1,1): dist to μ₁=0.47, dist to μ₂=5.44 → C₁
  B(1,2): dist to μ₁=0.75, dist to μ₂=5.11 → C₁
  C(2,1): dist to μ₁=0.75, dist to μ₂=4.93 → C₁
  D(5,4): dist to μ₁=4.63, dist to μ₂=0.75 → C₂
  E(5,5): dist to μ₁=5.23, dist to μ₂=0.47 → C₂
  F(6,5): dist to μ₁=5.88, dist to μ₂=0.75 → C₂

Clusters δεν άλλαξαν → CONVERGENCE!

Final: C₁ = {A, B, C}, C₂ = {D, E, F}
```

### 2.5 Visual Representation

```
    y
    6 |
    5 |           E . . F    C₂
    4 |           D
    3 |
    2 |  B
    1 |  A . C              C₁
    0 +-------------------> x
      0  1  2  3  4  5  6
```

### 2.6 Πλεονεκτήματα & Μειονεκτήματα

**Πλεονεκτήματα**:
- ✅ Απλός και κατανοητός
- ✅ Γρήγορος: O(n × k × iterations)
- ✅ Κλιμακώνεται σε μεγάλα datasets

**Μειονεκτήματα**:
- ❌ Πρέπει να ορίσεις k εκ των προτέρων
- ❌ Ευαίσθητος στα initial centroids
- ❌ Μόνο spherical clusters (δεν χειρίζεται arbitrary shapes)
- ❌ Ευαίσθητος σε outliers
- ❌ Convergence to local minimum

---

## 3. DBSCAN (Density-Based Spatial Clustering)

### 3.1 Βασική Ιδέα

Βρίσκει clusters ως **περιοχές υψηλής πυκνότητας** διαχωρισμένες από περιοχές χαμηλής πυκνότητας.

### 3.2 Παράμετροι

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ε (Eps): Ακτίνα γειτονιάς (radius)                        │
│           Ορίζει την "απόσταση" για γείτονες                │
│                                                             │
│  MinPts: Ελάχιστα σημεία για να είναι "πυκνή" περιοχή      │
│          Συνήθως MinPts ≥ D+1 (D = διαστάσεις)             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Ταξινόμηση Σημείων (ΚΡΙΣΙΜΟ για εξετάσεις!)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Ν(p) = {q ∈ D : dist(p,q) ≤ ε}  (ε-neighborhood)          │
│                                                             │
│  CORE POINT:                                                │
│    |Ν(p)| ≥ MinPts                                          │
│    → Έχει τουλάχιστον MinPts σημεία στην ε-γειτονιά        │
│       (συμπεριλαμβανομένου του εαυτού του!)                │
│                                                             │
│  BORDER POINT:                                              │
│    |Ν(p)| < MinPts ΚΑΙ υπάρχει core point q με p ∈ Ν(q)    │
│    → Δεν είναι core αλλά είναι στη γειτονιά ενός core      │
│                                                             │
│  NOISE POINT:                                               │
│    Δεν είναι ούτε Core ούτε Border                          │
│    → Outlier / anomaly                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.4 Connectivity Definitions

```
Directly Density-Reachable:
  p → q αν:
  1. p είναι core point
  2. q ∈ Ν(p)

Density-Reachable:
  Υπάρχει chain p₁ → p₂ → ... → pₙ
  όπου κάθε βήμα είναι directly density-reachable

Density-Connected:
  p, q είναι density-connected αν υπάρχει σημείο o
  τέτοιο ώστε p ← o → q (και τα δύο density-reachable από o)
```

### 3.5 Αλγόριθμος

```
┌────────────────────────────────────────────────────────────┐
│  DBSCAN ALGORITHM                                          │
│  ────────────────                                          │
│                                                            │
│  INPUT: Dataset D, ε, MinPts                               │
│  OUTPUT: Clusters + Noise points                           │
│                                                            │
│  1. Mark all points as UNVISITED                           │
│                                                            │
│  2. FOR each point p in D:                                 │
│        IF p is VISITED: continue                           │
│        Mark p as VISITED                                   │
│        N = Ν(p)  // ε-neighborhood of p                    │
│                                                            │
│        IF |N| < MinPts:                                    │
│           Mark p as NOISE (may change later!)              │
│        ELSE:                                               │
│           Create new cluster C                             │
│           ExpandCluster(p, N, C, ε, MinPts)               │
│                                                            │
│  ExpandCluster(p, N, C, ε, MinPts):                       │
│     Add p to C                                             │
│     FOR each q in N:                                       │
│        IF q is UNVISITED:                                  │
│           Mark q as VISITED                                │
│           N' = Ν(q)                                        │
│           IF |N'| ≥ MinPts:                                │
│              N = N ∪ N'   // expand neighborhood           │
│        IF q not in any cluster:                            │
│           Add q to C                                       │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 3.6 Worked Example (ΤΥΠΙΚΟ ΘΕΜΑ ΕΞΕΤΑΣΕΩΝ!)

**Data points** (2D):
```
A(1,2), B(2,1), C(2,2), D(3,2), E(8,8), F(8,9), G(9,8), H(25,25)

Parameters: ε = 2, MinPts = 3
```

**Βήμα 1: Υπολόγισε γειτονιές**
```
Ν(A) = {A, B, C}        |Ν(A)| = 3 ≥ 3 → CORE ✓
Ν(B) = {A, B, C}        |Ν(B)| = 3 ≥ 3 → CORE ✓
Ν(C) = {A, B, C, D}     |Ν(C)| = 4 ≥ 3 → CORE ✓
Ν(D) = {C, D}           |Ν(D)| = 2 < 3, αλλά C∈Ν(D) και C is core → BORDER
Ν(E) = {E, F, G}        |Ν(E)| = 3 ≥ 3 → CORE ✓
Ν(F) = {E, F, G}        |Ν(F)| = 3 ≥ 3 → CORE ✓
Ν(G) = {E, F, G}        |Ν(G)| = 3 ≥ 3 → CORE ✓
Ν(H) = {H}              |Ν(H)| = 1 < 3, no core nearby → NOISE ✗
```

**Distance calculations (Euclidean)**:
```
dist(A,B) = √((2-1)² + (1-2)²) = √2 ≈ 1.41 ≤ 2 ✓
dist(A,C) = √((2-1)² + (2-2)²) = 1 ≤ 2 ✓
dist(C,D) = √((3-2)² + (2-2)²) = 1 ≤ 2 ✓
dist(E,F) = √((8-8)² + (9-8)²) = 1 ≤ 2 ✓
dist(E,H) = √((25-8)² + (25-8)²) = 24 > 2 ✗
```

**Βήμα 2: Σχηματισμός Clusters**
```
Cluster 1: A, B, C, D  (connected via core points A, B, C)
Cluster 2: E, F, G     (connected via core points E, F, G)
Noise: H               (isolated point)
```

**Visual**:
```
    y
   25|                              H (noise)
    9|              F
    8|              E  G            Cluster 2
    .
    2|  A  C  D
    1|     B                        Cluster 1
    0+-------------------------> x
      1  2  3     8  9      25
```

**Summary**:
```
┌─────────────────────────────────────┐
│  Point │ |N(p)| │  Type   │ Cluster │
├─────────────────────────────────────┤
│   A    │   3    │  CORE   │    1    │
│   B    │   3    │  CORE   │    1    │
│   C    │   4    │  CORE   │    1    │
│   D    │   2    │  BORDER │    1    │
│   E    │   3    │  CORE   │    2    │
│   F    │   3    │  CORE   │    2    │
│   G    │   3    │  CORE   │    2    │
│   H    │   1    │  NOISE  │   N/A   │
└─────────────────────────────────────┘
```

### 3.7 Πλεονεκτήματα & Μειονεκτήματα

**Πλεονεκτήματα**:
- ✅ Δεν χρειάζεται να ορίσεις k
- ✅ Βρίσκει clusters arbitrary shape
- ✅ Robust σε outliers (τα βρίσκει ως noise)
- ✅ Deterministic (δεν εξαρτάται από initialization)

**Μειονεκτήματα**:
- ❌ Δύσκολο να βρεις ε και MinPts
- ❌ Αδυναμία με varying densities
- ❌ Πιο αργός: O(n²) naive, O(n log n) με spatial index

---

## 4. Σύγκριση K-means vs DBSCAN

| Χαρακτηριστικό | K-means | DBSCAN |
|----------------|---------|--------|
| **Παράμετροι** | k (αριθμός clusters) | ε, MinPts |
| **Σχήμα clusters** | Spherical | Arbitrary |
| **Outliers** | Τους αγνοεί | Τους ανιχνεύει |
| **Αριθμός clusters** | Fixed (k) | Αυτόματος |
| **Initialization** | Sensitive | Not needed |
| **Density** | Uniform | Can vary |
| **Complexity** | O(n×k×iter) | O(n²) or O(n log n) |

### Πότε να χρησιμοποιήσεις τι:

```
K-means:
  → Ξέρεις τον αριθμό clusters
  → Τα clusters είναι σφαιρικά
  → Δεν έχεις πολλά outliers
  → Θέλεις γρήγορο αλγόριθμο

DBSCAN:
  → Δεν ξέρεις τον αριθμό clusters
  → Τα clusters έχουν περίεργα σχήματα
  → Υπάρχουν outliers
  → Η πυκνότητα είναι σχετικά ομοιόμορφη
```

---

## 5. ⚠️ Συχνά Λάθη / Pitfalls

### 5.1 K-means
```
❌ ΛΑΘΟΣ: Το k-means εγγυάται το global optimum
✓ ΣΩΣΤΟ: Μπορεί να converge σε local minimum

❌ ΛΑΘΟΣ: Centroid = geometric median
✓ ΣΩΣΤΟ: Centroid = arithmetic mean
```

### 5.2 DBSCAN
```
❌ ΛΑΘΟΣ: Border point δεν μετράει τον εαυτό του στο |Ν(p)|
✓ ΣΩΣΤΟ: Κάθε σημείο ΜΕΤΡΑΕΙ τον εαυτό του στη γειτονιά!

❌ ΛΑΘΟΣ: Core αν |Ν(p)| > MinPts
✓ ΣΩΣΤΟ: Core αν |Ν(p)| ≥ MinPts (greater than OR EQUAL!)

❌ ΛΑΘΟΣ: Noise points μπορούν να γίνουν core later
✓ ΣΩΣΤΟ: Noise μπορεί να γίνει BORDER (αν core βρεθεί κοντά)
```

### 5.3 Υπολογισμός Αποστάσεων
```
Euclidean: d = √(Σ(xᵢ - yᵢ)²)
Manhattan: d = Σ|xᵢ - yᵢ|

DBSCAN συνήθως χρησιμοποιεί Euclidean by default.
```

---

## 6. Ερωτήσεις Εξετάσεων

### Ερώτηση 1
Σε DBSCAN με ε=1.5 και MinPts=3, ένα σημείο P έχει 2 σημεία στην ε-γειτονιά του (εκτός του εαυτού του). Τι τύπος είναι το P;

A) Core
B) Border
C) Noise
D) Εξαρτάται

<details>
<summary>Απάντηση</summary>

**Σωστό: D) Εξαρτάται**

**Εξήγηση**:
- |Ν(P)| = 2 + 1 (εαυτός) = 3 ≥ MinPts=3 → **CORE**!

**Προσοχή**: Το σημείο μετράει και τον εαυτό του!

Αν η ερώτηση λέει "2 σημεία **συμπεριλαμβανομένου** του εαυτού του":
- |Ν(P)| = 2 < 3 → NOT Core
- Αν υπάρχει γειτονικό core → Border
- Αλλιώς → Noise
</details>

---

### Ερώτηση 2
Ποια δήλωση είναι ΛΑΘΟΣ για το DBSCAN;

A) Μπορεί να βρει clusters arbitrary shape
B) Πρέπει να ορίσεις τον αριθμό clusters εκ των προτέρων
C) Ανιχνεύει outliers ως noise
D) Δεν επηρεάζεται από το order των σημείων

<details>
<summary>Απάντηση</summary>

**Σωστό: B) ΛΑΘΟΣ**

**Εξήγηση**: Το DBSCAN ΔΕΝ χρειάζεται τον αριθμό clusters. Τους βρίσκει αυτόματα!
Αυτό είναι ένα από τα κύρια πλεονεκτήματά του.

**Σημείωση για D**: Strictly speaking, DBSCAN μπορεί να δώσει διαφορετικά labels σε border points αν αλλάξει η σειρά, αλλά η γενική δομή είναι ίδια.
</details>

---

### Ερώτηση 3
Στο K-means, τι γίνεται αν ένα cluster αδειάσει (δεν έχει assigned points);

A) Ο αλγόριθμος σταματάει
B) Το centroid μένει στη θέση του
C) Το centroid επανατοποθετείται randomly
D) Εξαρτάται από την υλοποίηση

<details>
<summary>Απάντηση</summary>

**Σωστό: D) Εξαρτάται από την υλοποίηση**

**Εξήγηση**: Διαφορετικές υλοποιήσεις χειρίζονται διαφορετικά αυτή την περίπτωση:
- Random reinitialization
- Keep the centroid
- Assign to farthest point from other centroids
</details>

---

### Ερώτηση 4
K-means: Points A(0,0), B(2,0), C(10,0). Initial centroids: μ₁=(0,0), μ₂=(1,0). Μετά το πρώτο iteration, ποια είναι τα νέα centroids;

A) μ₁=(0,0), μ₂=(6,0)
B) μ₁=(1,0), μ₂=(10,0)
C) μ₁=(0,0), μ₂=(10,0)
D) μ₁=(1,0), μ₂=(6,0)

<details>
<summary>Απάντηση</summary>

**Σωστό: B) μ₁=(1,0), μ₂=(10,0)**

**Υπολογισμός**:
```
Assignment:
  A(0,0): dist to μ₁=0, dist to μ₂=1 → C₁
  B(2,0): dist to μ₁=2, dist to μ₂=1 → C₂
  C(10,0): dist to μ₁=10, dist to μ₂=9 → C₂

C₁ = {A}, C₂ = {B, C}

Update:
  μ₁ = (0/1, 0/1) = (0,0)?

Περίμενε! Ξαναελέγχουμε:
  A(0,0): dist to μ₁(0,0)=0, dist to μ₂(1,0)=1 → C₁ (closer to μ₁)
  B(2,0): dist to μ₁(0,0)=2, dist to μ₂(1,0)=1 → C₂ (closer to μ₂)
  C(10,0): dist to μ₁(0,0)=10, dist to μ₂(1,0)=9 → C₂

C₁ = {A}, C₂ = {B, C}

Update centroids:
  μ₁ = A = (0,0)
  μ₂ = ((2+10)/2, (0+0)/2) = (6,0)
```

Hmm, αυτό δίνει (0,0) και (6,0)... ας ξαναελέγξω τις επιλογές.

Αν η απάντηση είναι B) μ₁=(1,0), μ₂=(10,0):
Αυτό θα ίσχυε αν:
- C₁ = {A, B} → μ₁ = (1, 0)
- C₂ = {C} → μ₂ = (10, 0)

Assignment ξανά:
  A(0,0): dist to μ₁(0,0)=0, dist to μ₂(1,0)=1 → μ₁
  B(2,0): dist to μ₁(0,0)=2, dist to μ₂(1,0)=1 → μ₂
  C(10,0): dist to μ₁(0,0)=10, dist to μ₂(1,0)=9 → μ₂

So C₁={A}, C₂={B,C}

**Correct answer**: A) μ₁=(0,0), μ₂=(6,0)
</details>

---

### Ερώτηση 5
DBSCAN: Points P1(0,0), P2(1,0), P3(0,1), P4(10,10) με ε=1.5, MinPts=3. Πόσα clusters θα βρει;

A) 1
B) 2
C) 3
D) 4

<details>
<summary>Απάντηση</summary>

**Σωστό: A) 1**

**Υπολογισμός**:
```
Ν(P1) = {P1, P2, P3}    |Ν| = 3 ≥ 3 → CORE
Ν(P2) = {P1, P2, P3}    |Ν| = 3 ≥ 3 → CORE
Ν(P3) = {P1, P2, P3}    |Ν| = 3 ≥ 3 → CORE
Ν(P4) = {P4}            |Ν| = 1 < 3 → NOISE

Cluster 1: {P1, P2, P3}
Noise: {P4}
```

Άρα 1 cluster (+ 1 noise point).
</details>

---

### Ερώτηση 6
Ποιο είναι το βασικό πρόβλημα του K-means με outliers;

A) Δεν μπορεί να τρέξει
B) Οι outliers επηρεάζουν τα centroids
C) Δημιουργεί περισσότερα clusters
D) Ο αλγόριθμος δεν converge

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: Το centroid υπολογίζεται ως μέσος όρος. Οι outliers "τραβούν" το centroid προς τα έξω, αλλοιώνοντας τη θέση του.

Παράδειγμα:
- Points: (1,1), (2,1), (1,2), (100,100)
- Mean = (26, 26) - πολύ μακριά από τα περισσότερα points!
</details>

---

### Ερώτηση 7
Στο DBSCAN, αν αυξήσουμε το ε (ε-neighborhood radius), τι θα συμβεί συνήθως;

A) Περισσότερα clusters
B) Λιγότερα clusters, περισσότερα noise points
C) Λιγότερα clusters, λιγότερα noise points
D) Δεν επηρεάζεται

<details>
<summary>Απάντηση</summary>

**Σωστό: C) Λιγότερα clusters, λιγότερα noise points**

**Εξήγηση**: Μεγαλύτερο ε → μεγαλύτερη γειτονιά → περισσότερα σημεία στη γειτονιά → περισσότερα core points → τα clusters ενώνονται → λιγότερα clusters.

Επίσης, σημεία που ήταν noise μπορεί τώρα να μπουν σε γειτονιά core point → γίνονται border.
</details>

---

### Ερώτηση 8
Πόσες επαναλήψεις χρειάζεται το K-means;

A) Πάντα n (αριθμός σημείων)
B) Πάντα k (αριθμός clusters)
C) Μέχρι να μην αλλάζουν τα centroids (ή max iterations)
D) Μία μόνο

<details>
<summary>Απάντηση</summary>

**Σωστό: C)**

**Εξήγηση**: K-means σταματάει όταν τα centroids σταθεροποιηθούν ή όταν φτάσει max iterations. Τυπικά converge σε λίγες επαναλήψεις.
</details>

---

### Ερώτηση 9
Ποιο σημείο ΔΕΕΝ μπορεί να είναι border point σε DBSCAN;

A) Σημείο με |Ν(p)| = 1
B) Σημείο με |Ν(p)| = MinPts
C) Σημείο που είναι στη γειτονιά ενός core
D) Σημείο με |Ν(p)| = MinPts - 1

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: Αν |Ν(p)| ≥ MinPts, τότε το σημείο είναι CORE, όχι border.

Border = NOT core (|Ν(p)| < MinPts) + είναι στη γειτονιά ενός core.
</details>

---

### Ερώτηση 10
K-means++είναι βελτίωση του K-means που:

A) Χρησιμοποιεί Gini για να διαλέξει splits
B) Επιλέγει αρχικά centroids πιο έξυπνα
C) Χρησιμοποιεί DBSCAN για initialization
D) Κάνει automatic k selection

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: K-means++ επιλέγει τα αρχικά centroids με πιθανότητα ανάλογη της απόστασης από ήδη επιλεγμένα centroids. Αυτό βελτιώνει τη σύγκλιση και αποφεύγει κακές αρχικοποιήσεις.
</details>

---

## 7. Σύνοψη - Key Points

### K-means

```
┌────────────────────────────────────────────────────────────┐
│  1. Initialize k centroids                                 │
│  2. REPEAT:                                                │
│     - Assign points to nearest centroid                    │
│     - Update centroids = mean of assigned points           │
│  3. Until convergence                                      │
│                                                            │
│  Centroid: μₖ = (1/nₖ) × Σ xᵢ                             │
│                         i∈Cₖ                               │
└────────────────────────────────────────────────────────────┘
```

### DBSCAN Point Classification (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

```
┌────────────────────────────────────────────────────────────┐
│  CORE:   |Ν(p)| ≥ MinPts                                   │
│  BORDER: |Ν(p)| < MinPts BUT in neighborhood of core       │
│  NOISE:  Neither core nor border                           │
│                                                            │
│  ⚠️ Ν(p) INCLUDES p itself!                                │
└────────────────────────────────────────────────────────────┘
```

### Σύγκριση (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

```
┌───────────────┬────────────────┬────────────────┐
│               │    K-means     │    DBSCAN      │
├───────────────┼────────────────┼────────────────┤
│ # clusters    │ Must specify k │ Automatic      │
│ Shape         │ Spherical      │ Arbitrary      │
│ Outliers      │ Problematic    │ Detected       │
│ Parameters    │ k              │ ε, MinPts      │
│ Deterministic │ No             │ Yes (mostly)   │
└───────────────┴────────────────┴────────────────┘
```
