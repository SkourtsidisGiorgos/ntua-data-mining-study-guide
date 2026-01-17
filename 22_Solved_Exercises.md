# Solved Exercises - Λυμένες Ασκήσεις Data Mining

## Οδηγίες Χρήσης
Για κάθε άσκηση:
1. Διάβασε την εκφώνηση
2. Προσπάθησε να τη λύσεις ΠΡΏΤΑ
3. Μετά έλεγξε τη λύση
4. Σημείωσε τις ασκήσεις που δυσκολεύτηκες

---

# ΕΝΟΤΗΤΑ 1: Decision Trees & Entropy (5 ασκήσεις)

## Άσκηση 1.1: Υπολογισμός Entropy

**Εκφώνηση**: Dataset με 10 samples: 6 "Yes", 4 "No". Υπολόγισε την entropy.

<details>
<summary>Λύση</summary>

**Βήμα 1**: Υπολογισμός πιθανοτήτων
```
p(Yes) = 6/10 = 0.6
p(No) = 4/10 = 0.4
```

**Βήμα 2**: Εφαρμογή τύπου
```
H(S) = -Σ pᵢ × log₂(pᵢ)
     = -(0.6 × log₂(0.6)) - (0.4 × log₂(0.4))
     = -(0.6 × (-0.737)) - (0.4 × (-1.322))
     = 0.442 + 0.529
     = 0.971 bits
```

**Απάντηση**: H(S) = **0.971 bits**
</details>

---

## Άσκηση 1.2: Information Gain

**Εκφώνηση**: Dataset με H(S) = 1.0. Attribute A διαχωρίζει σε:
- Subset 1: 4 samples (3 Yes, 1 No)
- Subset 2: 4 samples (1 Yes, 3 No)

Υπολόγισε IG(S, A).

<details>
<summary>Λύση</summary>

**Βήμα 1**: Entropy κάθε subset
```
H(S1) = -(3/4)log₂(3/4) - (1/4)log₂(1/4)
      = -(0.75)(-0.415) - (0.25)(-2)
      = 0.311 + 0.5
      = 0.811

H(S2) = -(1/4)log₂(1/4) - (3/4)log₂(3/4)
      = 0.5 + 0.311
      = 0.811
```

**Βήμα 2**: Weighted average
```
H(S|A) = (4/8) × 0.811 + (4/8) × 0.811
       = 0.5 × 0.811 + 0.5 × 0.811
       = 0.811
```

**Βήμα 3**: Information Gain
```
IG(S, A) = H(S) - H(S|A)
         = 1.0 - 0.811
         = 0.189 bits
```

**Απάντηση**: IG = **0.189 bits**
</details>

---

## Άσκηση 1.3: Gini Index

**Εκφώνηση**: Dataset με 20 samples: 12 Class A, 8 Class B. Υπολόγισε το Gini Index.

<details>
<summary>Λύση</summary>

**Υπολογισμός**:
```
p(A) = 12/20 = 0.6
p(B) = 8/20 = 0.4

Gini = 1 - Σpᵢ²
     = 1 - (0.6)² - (0.4)²
     = 1 - 0.36 - 0.16
     = 0.48
```

**Απάντηση**: Gini = **0.48**
</details>

---

## Άσκηση 1.4: Επιλογή Root Node

**Εκφώνηση**:
| Attribute | Information Gain |
|-----------|------------------|
| Age | 0.15 |
| Income | 0.22 |
| Student | 0.08 |
| Credit | 0.19 |

Ποιο attribute θα επιλέξει ο ID3 ως root;

<details>
<summary>Λύση</summary>

Ο ID3 επιλέγει το attribute με το **ΜΕΓΑΛΥΤΕΡΟ Information Gain**.

**Απάντηση**: **Income** (IG = 0.22)
</details>

---

## Άσκηση 1.5: Gain Ratio

**Εκφώνηση**: IG(S, A) = 0.3, SplitInfo(S, A) = 1.5. Υπολόγισε το Gain Ratio.

<details>
<summary>Λύση</summary>

```
GainRatio = IG / SplitInfo
          = 0.3 / 1.5
          = 0.2
```

**Απάντηση**: GainRatio = **0.2**
</details>

---

# ΕΝΟΤΗΤΑ 2: Clustering (5 ασκήσεις)

## Άσκηση 2.1: K-means Centroid Update

**Εκφώνηση**: Cluster C₁ περιέχει points: (1,2), (3,4), (2,3). Υπολόγισε το νέο centroid.

<details>
<summary>Λύση</summary>

```
μ = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)
  = ((1+3+2)/3, (2+4+3)/3)
  = (6/3, 9/3)
  = (2, 3)
```

**Απάντηση**: Νέο centroid = **(2, 3)**
</details>

---

## Άσκηση 2.2: DBSCAN Point Classification

**Εκφώνηση**: ε=2, MinPts=3.
- Point P έχει 4 σημεία στην ε-γειτονιά του (συμπεριλαμβανομένου του εαυτού του)
- Point Q έχει 2 σημεία στην ε-γειτονιά του
- Point R έχει 1 σημείο (μόνο τον εαυτό του)

Χαρακτήρισε κάθε σημείο.

<details>
<summary>Λύση</summary>

```
P: |N(P)| = 4 ≥ MinPts=3 → CORE POINT
Q: |N(Q)| = 2 < 3 → NOT CORE
   Αν Q είναι στη γειτονιά κάποιου core → BORDER
   Αλλιώς → NOISE
R: |N(R)| = 1 < 3 και μόνος του → NOISE POINT
```

**Απάντηση**: P = Core, Q = Border ή Noise, R = Noise
</details>

---

## Άσκηση 2.3: K-means Assignment

**Εκφώνηση**: Centroids: μ₁=(0,0), μ₂=(5,5). Point P=(2,1). Σε ποιο cluster ανήκει;

<details>
<summary>Λύση</summary>

```
d(P, μ₁) = √((2-0)² + (1-0)²) = √(4+1) = √5 ≈ 2.24
d(P, μ₂) = √((2-5)² + (1-5)²) = √(9+16) = √25 = 5

d(P, μ₁) < d(P, μ₂)
```

**Απάντηση**: P ανήκει στο **Cluster 1** (πιο κοντά στο μ₁)
</details>

---

## Άσκηση 2.4: DBSCAN Clusters

**Εκφώνηση**: Points: A(0,0), B(1,0), C(0,1), D(10,10), E(11,10). ε=2, MinPts=2.
Πόσα clusters και noise points;

<details>
<summary>Λύση</summary>

```
Γειτονιές (ε=2):
N(A) = {A, B, C}  |N|=3 ≥ 2 → CORE
N(B) = {A, B, C}  |N|=3 ≥ 2 → CORE
N(C) = {A, B, C}  |N|=3 ≥ 2 → CORE
N(D) = {D, E}     |N|=2 ≥ 2 → CORE
N(E) = {D, E}     |N|=2 ≥ 2 → CORE

Clusters:
- Cluster 1: {A, B, C} (συνδεδεμένα)
- Cluster 2: {D, E} (συνδεδεμένα)
- Noise: κανένα
```

**Απάντηση**: **2 clusters**, **0 noise**
</details>

---

## Άσκηση 2.5: K-means Convergence

**Εκφώνηση**: Μετά το update, τα centroids δεν άλλαξαν. Τι σημαίνει αυτό;

<details>
<summary>Λύση</summary>

Αν τα centroids δεν αλλάζουν, ο αλγόριθμος έχει **converge**. Οι assignments των points δεν θα αλλάξουν στο επόμενο iteration.

**Απάντηση**: Ο αλγόριθμος **σταματάει** - έχει φτάσει σε stable solution.
</details>

---

# ΕΝΟΤΗΤΑ 3: Association Rules (5 ασκήσεις)

## Άσκηση 3.1: Support Calculation

**Εκφώνηση**: 100 transactions, 40 περιέχουν {A}, 30 περιέχουν {B}, 20 περιέχουν {A,B}. Υπολόγισε Support({A}), Support({B}), Support({A,B}).

<details>
<summary>Λύση</summary>

```
Support({A}) = 40/100 = 0.40 = 40%
Support({B}) = 30/100 = 0.30 = 30%
Support({A,B}) = 20/100 = 0.20 = 20%
```

**Απάντηση**: Sup(A)=0.40, Sup(B)=0.30, Sup(A,B)=0.20
</details>

---

## Άσκηση 3.2: Confidence

**Εκφώνηση**: Με τα ίδια δεδομένα, υπολόγισε Confidence(A→B).

<details>
<summary>Λύση</summary>

```
Confidence(A→B) = Support({A,B}) / Support({A})
                = 0.20 / 0.40
                = 0.50 = 50%
```

**Απάντηση**: Conf(A→B) = **0.50**
</details>

---

## Άσκηση 3.3: Lift

**Εκφώνηση**: Με τα ίδια δεδομένα, υπολόγισε Lift(A→B). Τι σημαίνει;

<details>
<summary>Λύση</summary>

```
Lift(A→B) = Confidence(A→B) / Support({B})
          = 0.50 / 0.30
          = 1.67

Εναλλακτικά:
Lift = Sup({A,B}) / (Sup({A}) × Sup({B}))
     = 0.20 / (0.40 × 0.30)
     = 0.20 / 0.12
     = 1.67
```

**Ερμηνεία**: Lift > 1 → Θετική συσχέτιση. Όταν αγοράζεις A, είναι 1.67x πιο πιθανό να αγοράσεις και B.

**Απάντηση**: Lift = **1.67** (θετική συσχέτιση)
</details>

---

## Άσκηση 3.4: Apriori Pruning

**Εκφώνηση**: L₂ = {{A,B}, {A,C}, {B,C}}. Είναι το {A,B,C} valid candidate για C₃;

<details>
<summary>Λύση</summary>

Για να είναι valid, ΟΛΟΙ οι 2-subsets του {A,B,C} πρέπει να είναι στο L₂:
```
{A,B} ∈ L₂? ✓
{A,C} ∈ L₂? ✓
{B,C} ∈ L₂? ✓
```

**Απάντηση**: **Ναι**, {A,B,C} είναι valid candidate.
</details>

---

## Άσκηση 3.5: Rules Generation

**Εκφώνηση**: Frequent itemset {A,B,C} με sup=0.15. sup(A)=0.30, sup(B)=0.40, sup({A,B})=0.25.
Υπολόγισε confidence για {A,B}→{C}.

<details>
<summary>Λύση</summary>

```
Confidence({A,B}→{C}) = Support({A,B,C}) / Support({A,B})
                      = 0.15 / 0.25
                      = 0.60 = 60%
```

**Απάντηση**: Conf({A,B}→{C}) = **0.60**
</details>

---

# ΕΝΟΤΗΤΑ 4: DTW & Similarity (5 ασκήσεις)

## Άσκηση 4.1: Euclidean Distance

**Εκφώνηση**: Υπολόγισε Euclidean distance μεταξύ (2, 3, 1) και (5, 7, 1).

<details>
<summary>Λύση</summary>

```
d = √((2-5)² + (3-7)² + (1-1)²)
  = √(9 + 16 + 0)
  = √25
  = 5
```

**Απάντηση**: d = **5**
</details>

---

## Άσκηση 4.2: Manhattan Distance

**Εκφώνηση**: Υπολόγισε Manhattan distance μεταξύ (1, 5) και (4, 1).

<details>
<summary>Λύση</summary>

```
d = |1-4| + |5-1|
  = 3 + 4
  = 7
```

**Απάντηση**: d = **7**
</details>

---

## Άσκηση 4.3: Cosine Similarity

**Εκφώνηση**: Vectors A=(1, 2), B=(2, 4). Υπολόγισε cosine similarity.

<details>
<summary>Λύση</summary>

```
A · B = 1×2 + 2×4 = 2 + 8 = 10
||A|| = √(1² + 2²) = √5
||B|| = √(2² + 4²) = √20

cos(θ) = 10 / (√5 × √20)
       = 10 / √100
       = 10 / 10
       = 1.0
```

**Απάντηση**: cos(θ) = **1.0** (ίδια κατεύθυνση, B = 2A)
</details>

---

## Άσκηση 4.4: Jaccard Similarity

**Εκφώνηση**: Set A = {1, 2, 3, 4}, Set B = {3, 4, 5, 6}. Υπολόγισε Jaccard similarity.

<details>
<summary>Λύση</summary>

```
A ∩ B = {3, 4} → |A ∩ B| = 2
A ∪ B = {1, 2, 3, 4, 5, 6} → |A ∪ B| = 6

J(A, B) = 2/6 = 0.333
```

**Απάντηση**: J = **0.333**
</details>

---

## Άσκηση 4.5: DTW Simple

**Εκφώνηση**: X = [1, 3], Y = [2, 4], d = |xᵢ - yⱼ|. Υπολόγισε DTW distance.

<details>
<summary>Λύση</summary>

**Cost matrix**:
```
      Y: 2   4
X: 1    1   3
   3    1   1
```

**DTW matrix**:
```
        -    2    4
   -    0    ∞    ∞
   1    ∞    1    4
   3    ∞    2    2
```

**Υπολογισμός**:
```
DTW(1,1) = |1-2| + min(0,∞,∞) = 1 + 0 = 1
DTW(1,2) = |1-4| + min(∞,∞,1) = 3 + 1 = 4
DTW(2,1) = |3-2| + min(∞,1,∞) = 1 + 1 = 2
DTW(2,2) = |3-4| + min(1,4,2) = 1 + 1 = 2
```

**Απάντηση**: DTW = **2**
</details>

---

# ΕΝΟΤΗΤΑ 5: Classification Metrics (5 ασκήσεις)

## Άσκηση 5.1: Confusion Matrix Basics

**Εκφώνηση**: TP=50, TN=40, FP=10, FN=20. Υπολόγισε Accuracy.

<details>
<summary>Λύση</summary>

```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
         = (50 + 40) / (50 + 40 + 10 + 20)
         = 90 / 120
         = 0.75 = 75%
```

**Απάντηση**: Accuracy = **75%**
</details>

---

## Άσκηση 5.2: Precision & Recall

**Εκφώνηση**: Με τα ίδια δεδομένα, υπολόγισε Precision και Recall.

<details>
<summary>Λύση</summary>

```
Precision = TP / (TP + FP) = 50 / (50 + 10) = 50/60 = 0.833

Recall = TP / (TP + FN) = 50 / (50 + 20) = 50/70 = 0.714
```

**Απάντηση**: Precision = **0.833**, Recall = **0.714**
</details>

---

## Άσκηση 5.3: F1 Score

**Εκφώνηση**: Precision=0.8, Recall=0.6. Υπολόγισε F1.

<details>
<summary>Λύση</summary>

```
F1 = 2 × P × R / (P + R)
   = 2 × 0.8 × 0.6 / (0.8 + 0.6)
   = 0.96 / 1.4
   = 0.686
```

**Απάντηση**: F1 = **0.686**
</details>

---

## Άσκηση 5.4: Specificity

**Εκφώνηση**: TN=180, FP=20. Υπολόγισε Specificity.

<details>
<summary>Λύση</summary>

```
Specificity = TN / (TN + FP)
            = 180 / (180 + 20)
            = 180 / 200
            = 0.90
```

**Απάντηση**: Specificity = **0.90**
</details>

---

## Άσκηση 5.5: FPR

**Εκφώνηση**: Με Specificity=0.90, ποιο είναι το FPR;

<details>
<summary>Λύση</summary>

```
FPR = 1 - Specificity
    = 1 - 0.90
    = 0.10
```

**Απάντηση**: FPR = **0.10**
</details>

---

# ΕΝΟΤΗΤΑ 6: Bayesian (5 ασκήσεις)

## Άσκηση 6.1: Bayes' Theorem

**Εκφώνηση**: P(Rain)=0.3, P(Cloudy|Rain)=0.9, P(Cloudy|¬Rain)=0.2. Αν είναι cloudy, τι πιθανότητα βροχής;

<details>
<summary>Λύση</summary>

```
P(Cloudy) = P(C|R)×P(R) + P(C|¬R)×P(¬R)
          = 0.9×0.3 + 0.2×0.7
          = 0.27 + 0.14
          = 0.41

P(Rain|Cloudy) = P(C|R)×P(R) / P(C)
               = 0.27 / 0.41
               = 0.659
```

**Απάντηση**: P(Rain|Cloudy) = **0.659** ≈ 66%
</details>

---

## Άσκηση 6.2: Naive Bayes

**Εκφώνηση**: P(Spam)=0.4, P("free"|Spam)=0.7, P("free"|Ham)=0.1. Email με "free". Είναι spam;

<details>
<summary>Λύση</summary>

```
P(Spam|free) ∝ P(free|Spam) × P(Spam) = 0.7 × 0.4 = 0.28
P(Ham|free)  ∝ P(free|Ham) × P(Ham)   = 0.1 × 0.6 = 0.06

Normalize:
P(Spam|free) = 0.28 / (0.28 + 0.06) = 0.28/0.34 = 0.824
```

**Απάντηση**: **Spam** (P = 82.4%)
</details>

---

## Άσκηση 6.3: CPT Size

**Εκφώνηση**: Node X με 3 binary parents. Πόσες rows στο CPT;

<details>
<summary>Λύση</summary>

```
Rows = |Parent₁| × |Parent₂| × |Parent₃|
     = 2 × 2 × 2
     = 8
```

**Απάντηση**: **8 rows**
</details>

---

## Άσκηση 6.4: D-Separation

**Εκφώνηση**: Network A → B → C. Είναι A ⊥ C | B;

<details>
<summary>Λύση</summary>

Serial structure: B "μπλοκάρει" την πληροφορία όταν είναι γνωστό.

**Απάντηση**: **Ναι**, A ⊥ C | B
</details>

---

## Άσκηση 6.5: V-Structure

**Εκφώνηση**: Network A → C ← B. Είναι A ⊥ B; Είναι A ⊥ B | C;

<details>
<summary>Λύση</summary>

V-structure:
- Χωρίς evidence σε C: A ⊥ B ✓
- Με evidence σε C: A ⫫̸ B | C ✗ (explaining away)

**Απάντηση**: A ⊥ B (Ναι), A ⊥ B | C (Όχι)
</details>

---

# ΕΝΟΤΗΤΑ 7: Privacy & TF-IDF (5 ασκήσεις)

## Άσκηση 7.1: K-Anonymity Check

**Εκφώνηση**: Dataset με QI=(Age, Zipcode):
| Age | Zipcode | Disease |
|-----|---------|---------|
| 20-30 | 123** | HIV |
| 20-30 | 123** | Cancer |
| 40-50 | 456** | Flu |

Είναι 2-anonymous;

<details>
<summary>Λύση</summary>

Equivalence classes:
- (20-30, 123**): 2 records ✓
- (40-50, 456**): 1 record ✗

**Απάντηση**: **Όχι**, δεν είναι 2-anonymous (η 2η class έχει μόνο 1 record)
</details>

---

## Άσκηση 7.2: L-Diversity Check

**Εκφώνηση**: Equivalence class με 4 records: HIV, HIV, HIV, Cancer. Είναι 2-diverse;

<details>
<summary>Λύση</summary>

Distinct sensitive values: {HIV, Cancer} = 2 values

**Απάντηση**: **Ναι**, είναι 2-diverse (2 distinct values ≥ L=2)
</details>

---

## Άσκηση 7.3: TF Calculation

**Εκφώνηση**: Document: "the cat sat on the mat the cat". TF("cat") = ?

<details>
<summary>Λύση</summary>

Count "cat": 2 εμφανίσεις

**Απάντηση**: TF("cat") = **2**
</details>

---

## Άσκηση 7.4: IDF Calculation

**Εκφώνηση**: N=1000 documents, "algorithm" εμφανίζεται σε 100. IDF("algorithm") = ?

<details>
<summary>Λύση</summary>

```
IDF = log(N/df) = log(1000/100) = log(10) = 1 (base 10)
                                          ≈ 2.3 (natural log)
```

**Απάντηση**: IDF = **log(10)** ≈ 1 (base 10) ή 2.3 (ln)
</details>

---

## Άσκηση 7.5: TF-IDF

**Εκφώνηση**: TF("data")=3, IDF("data")=2. TF-IDF("data") = ?

<details>
<summary>Λύση</summary>

```
TF-IDF = TF × IDF = 3 × 2 = 6
```

**Απάντηση**: TF-IDF = **6**
</details>

---

# ΕΝΟΤΗΤΑ 8: OLAP & Normalization (5 ασκήσεις)

## Άσκηση 8.1: Cuboids με Ιεραρχίες

**Εκφώνηση**: 3 dimensions με L₁=4, L₂=3, L₃=2 levels. Πόσα cuboids;

<details>
<summary>Λύση</summary>

```
Cuboids = L₁ × L₂ × L₃ = 4 × 3 × 2 = 24
```

**Απάντηση**: **24 cuboids**
</details>

---

## Άσκηση 8.2: Min-Max Normalization

**Εκφώνηση**: Data = {10, 20, 30, 40}. Normalize 25 στο [0, 1].

<details>
<summary>Λύση</summary>

```
min = 10, max = 40

v' = (v - min) / (max - min)
   = (25 - 10) / (40 - 10)
   = 15 / 30
   = 0.5
```

**Απάντηση**: 25 → **0.5**
</details>

---

## Άσκηση 8.3: Decimal Scaling

**Εκφώνηση**: Data = {-450, 23, 199}. Βρες το j και normalize 199.

<details>
<summary>Λύση</summary>

```
max(|v|) = max(450, 23, 199) = 450
450 < 1000 = 10³ → j = 3

199 / 10³ = 199 / 1000 = 0.199
```

**Απάντηση**: j = **3**, 199 → **0.199**
</details>

---

## Άσκηση 8.4: OLAP Operation

**Εκφώνηση**: "Sales per day" → "Sales per month". Ποια OLAP operation;

<details>
<summary>Λύση</summary>

Πηγαίνουμε από λεπτομερές (day) σε aggregate (month).

**Απάντηση**: **Roll-up**
</details>

---

## Άσκηση 8.5: Slice vs Dice

**Εκφώνηση**: Επιλογή: "Product = TV AND Location IN (Athens, Patras)". Slice ή Dice;

<details>
<summary>Λύση</summary>

Φιλτράρουμε σε 2 dimensions: Product ΚΑΙ Location.

**Απάντηση**: **Dice** (2+ dimensions)
</details>

---

# Σύνοψη Τύπων

| Topic | Formula |
|-------|---------|
| Entropy | H = -Σ pᵢ log₂(pᵢ) |
| Information Gain | IG = H(S) - H(S\|A) |
| Gini | G = 1 - Σ pᵢ² |
| K-means centroid | μ = (1/n) Σ xᵢ |
| DBSCAN Core | \|N(p)\| ≥ MinPts |
| Support | Sup(X) = \|T with X\| / \|T\| |
| Confidence | Conf(X→Y) = Sup(X∪Y) / Sup(X) |
| Lift | Lift = Conf(X→Y) / Sup(Y) |
| Euclidean | d = √(Σ(xᵢ-yᵢ)²) |
| Cosine | cos(θ) = (x·y) / (\|\|x\|\| × \|\|y\|\|) |
| DTW | DTW(i,j) = d(i,j) + min(DTW(i-1,j-1), DTW(i-1,j), DTW(i,j-1)) |
| Precision | P = TP / (TP + FP) |
| Recall | R = TP / (TP + FN) |
| F1 | F1 = 2PR / (P + R) |
| Bayes | P(A\|B) = P(B\|A)P(A) / P(B) |
| TF-IDF | TF(t,d) × log(N/df(t)) |
| Cuboids | 2ⁿ ή L₁×L₂×...×Lₙ |
| Min-Max | (v-min)/(max-min) |
