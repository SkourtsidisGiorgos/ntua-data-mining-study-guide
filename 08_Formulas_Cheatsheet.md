# Formulas Cheatsheet - Data Mining NTUA

## Διάβασε αυτό 5 λεπτά πριν την εξέταση!

---

## 1. OLAP - Cuboid Calculations

### Χωρίς Ιεραρχίες
```
┌──────────────────────────────┐
│  Cuboids = 2^n               │
│                              │
│  n = αριθμός dimensions      │
└──────────────────────────────┘

Παράδειγμα: 3 dimensions → 2³ = 8 cuboids
```

### Με Ιεραρχίες
```
┌──────────────────────────────────────┐
│  Cuboids = L₁ × L₂ × ... × Lₙ       │
│                                      │
│  Lᵢ = επίπεδα στη dimension i       │
│       (συμπεριλαμβάνεται το "all")  │
└──────────────────────────────────────┘

Παράδειγμα: L₁=3, L₂=4, L₃=2 → 3×4×2 = 24 cuboids
```

### Base Cuboid Cells
```
┌──────────────────────────────────────┐
│  Cells = p₁ × p₂ × ... × pₙ         │
│                                      │
│  pᵢ = distinct τιμές στη dimension i │
└──────────────────────────────────────┘

Παράδειγμα: 10 products × 5 stores × 12 months = 600 cells
```

---

## 2. Normalization

### Min-Max [0, 1]
```
┌──────────────────────────────┐
│       v - min                │
│  v' = ─────────              │
│       max - min              │
└──────────────────────────────┘

min → 0
max → 1
```

### Min-Max [new_min, new_max]
```
┌─────────────────────────────────────────────────────┐
│       v - min                                       │
│  v' = ───────── × (new_max - new_min) + new_min    │
│       max - min                                     │
└─────────────────────────────────────────────────────┘
```

### Decimal Scaling
```
┌──────────────────────────────┐
│  v' = v / 10^j               │
│                              │
│  j = ψηφία του max(|v|)      │
└──────────────────────────────┘

max(|v|) < 10   → j = 1
max(|v|) < 100  → j = 2
max(|v|) < 1000 → j = 3
```

### Z-Score
```
┌──────────────────────────────┐
│       v - μ                  │
│  v' = ─────                  │
│         σ                    │
│                              │
│  μ = mean                    │
│  σ = standard deviation      │
└──────────────────────────────┘
```

### Equal Width Binning
```
┌──────────────────────────────┐
│        max - min             │
│  width = ─────────           │
│            k                 │
│                              │
│  k = αριθμός bins            │
└──────────────────────────────┘
```

---

## 3. MapReduce Sequence

```
┌───────────────────────────────────────────┐
│  ΣΕΙΡΑ: 1 → 2 → 4 → 3                     │
│                                           │
│  1. Mapper                                │
│  2. Combiner (optional)                   │
│  4. Partitioner                           │
│  3. Reducer                               │
└───────────────────────────────────────────┘
```

### Pseudocode Patterns
```
DISTINCT:     Map: emit(x, null)      Reduce: emit(x)
COUNT:        Map: emit(key, 1)       Reduce: emit(key, sum)
SUM:          Map: emit(key, value)   Reduce: emit(key, sum)
AVG:          Map: emit(key, (v,1))   Reduce: emit(key, sum/count)
```

---

## 4. GAV vs LAV

```
┌────────────────────────────────────────┐
│  GAV: Global ⊇ Local                   │
│       Query: EASY (unfold)             │
│       Add source: HARD                 │
│                                        │
│  LAV: Local ⊆ Global                   │
│       Query: HARD (rewriting)          │
│       Add source: EASY                 │
└────────────────────────────────────────┘
```

---

## 5. Join Algorithms

```
┌────────────────────────────────────────┐
│  Nested Loop:  ALL joins (=, <, >)     │
│  Hash Join:    ONLY equi-join (=)      │
│  Sort-Merge:   ONLY equi-join (=)      │
└────────────────────────────────────────┘

Inequality join (< , >) → ΜΟΝΟ Nested Loop!
```

---

## 6. Data Types

```
┌────────────────────────────────────────┐
│  Nominal:  =, ≠                        │
│  Ordinal:  =, ≠, <, >                  │
│  Interval: =, ≠, <, >, +, -            │
│  Ratio:    =, ≠, <, >, +, -, ×, ÷      │
└────────────────────────────────────────┘

ΘΥΜΗΣΟΥ:
Celsius → Interval
Kelvin  → Ratio (absolute zero!)
```

---

## 7. SQL Quick Reference

```sql
-- Aggregation
GROUP BY + HAVING (για aggregate conditions)
WHERE (για row conditions)

-- Operator Precedence
AND πριν από OR

-- NULL
IS NULL  (όχι = NULL)

-- Increase 20%
SET price = price * 1.20
```

### Relational Algebra
```
σ (sigma) = Selection (WHERE)  → rows
π (pi)    = Projection (SELECT) → columns
```

---

## 8. OLAP Operations

```
┌────────────────────────────────────────┐
│  Slice:      1 dimension filter        │
│  Dice:       2+ dimensions filter      │
│  Roll-up:    Aggregation (↑ level)     │
│  Drill-down: Disaggregation (↓ level)  │
│  Pivot:      Rotate axes               │
└────────────────────────────────────────┘
```

---

## 9. Hadoop Components

```
┌────────────────────────────────────────┐
│  JobTracker:  SCHEDULES jobs           │
│  TaskTracker: EXECUTES tasks           │
│  NameNode:    HDFS METADATA            │
│  DataNode:    HDFS DATA                │
└────────────────────────────────────────┘
```

---

## 10. HMM Algorithms

```
┌────────────────────────────────────────┐
│  Baum-Welch: TRAINS parameters         │
│  Viterbi:    FINDS best state path     │
└────────────────────────────────────────┘
```

---

## Quick Calculation Examples

### Min-Max: 200, 300, 400 → [0,1]
```
min=200, max=400
200 → 0
300 → (300-200)/(400-200) = 100/200 = 0.5
400 → 1
```

### Decimal Scaling: -997, 3, 83
```
max(|v|) = 997 < 1000 → j=3
-997/1000 = -0.997
3/1000 = 0.003
83/1000 = 0.083
```

### Cuboids: 3 dims με L₁=2, L₂=3, L₃=4
```
Cuboids = 2 × 3 × 4 = 24
```

---

## 11. Query Containment

```
┌────────────────────────────────────────────────┐
│  Για Q1 ⊆ Q2:                                  │
│  Ψάχνουμε mapping: vars(Q2) → vars(Q1)         │
│                                                │
│  Distinguished vars: πρέπει να map αντίστοιχα  │
│  Non-distinguished: μπορούν να map οπουδήποτε  │
│  Κάθε relation Q2 body: πρέπει να map σε Q1    │
└────────────────────────────────────────────────┘

Canonical Database: Όταν δεν βρίσκεις mapping,
                    δημιούργησε DB από body του Q1
```

---

## 12. ER Diagrams - Cardinality

```
┌────────────────────────────────────────────────┐
│  Cardinality = πόσα instances μιας entity      │
│                συνδέονται με κάθε instance     │
│                μιας άλλης entity               │
└────────────────────────────────────────────────┘

FK Placement:
┌─────────────────────────────────────┐
│  1:1   → Either side               │
│  1:N   → N side (many side)        │
│  M:N   → New junction table        │
└─────────────────────────────────────┘
```

---

## 13. Query Processing

```
┌────────────────────────────────────────────────┐
│  Pipelining:     Tuple-by-tuple, NO storage    │
│  Materialization: Stores intermediate results  │
└────────────────────────────────────────────────┘

Blocking Operations (για pipelining):
- Sort
- Aggregation
- Hash Join (build phase)
- Distinct
```

---

## 14. Data Streams

### Challenges
```
1. One-pass constraint (μία φορά κάθε δεδομένο)
2. Concept Drift (αλλαγή στατιστικών)
3. Resource constraints
4. Massive-domain constraints
```

### Reservoir Sampling
```
┌────────────────────────────────────────────────┐
│  Πιθανότητα n-th element στο reservoir = k/n  │
│                                                │
│  k = μέγεθος reservoir                         │
│  n = τρέχων αριθμός elements                   │
└────────────────────────────────────────────────┘
```

### Bloom Filter
```
┌────────────────────────────────────────────────┐
│  FALSE POSITIVES:  Πιθανά (collisions)         │
│  FALSE NEGATIVES:  ΑΔΥΝΑΤΑ                     │
│                                                │
│  Αν λέει "ΟΧΙ" → ΣΙΓΟΥΡΑ δεν υπάρχει!         │
└────────────────────────────────────────────────┘

False positive probability:
F = (1 - e^(-nw/m))^w

Optimal: w = (m/n) × ln(2)
```

### Count-Min Sketch
```
┌────────────────────────────────────────────────┐
│  Frequency estimate = min(all hash counters)   │
│                                                │
│  Γιατί MIN? Collisions → overestimation        │
│  MIN είναι η πιο ακριβής εκτίμηση              │
└────────────────────────────────────────────────┘
```

### Flajolet-Martin (Distinct Count)
```
┌────────────────────────────────────────────────┐
│  Distinct elements ≈ 2^R_max                   │
│                                                │
│  R_max = max trailing zeros in hash output     │
└────────────────────────────────────────────────┘
```

### Algorithms Summary
```
┌────────────────────────────────────────────────┐
│  Reservoir Sampling → Random sample            │
│  Bloom Filter       → Set membership           │
│  Count-Min Sketch   → Frequency count          │
│  Flajolet-Martin    → Distinct count           │
│  STREAM             → Clustering (no drift)    │
│  CluStream          → Clustering (with drift)  │
│  VFDT               → Classification           │
└────────────────────────────────────────────────┘
```

---

---

## 15. Decision Trees

### Entropy
```
┌──────────────────────────────────────┐
│  H(S) = -Σ pᵢ × log₂(pᵢ)            │
│                                      │
│  H = 0: Pure (μία κλάση)            │
│  H = 1: Max uncertainty (50-50)     │
└──────────────────────────────────────┘
```

### Information Gain
```
┌──────────────────────────────────────┐
│  IG(S, A) = H(S) - Σ (|Sᵥ|/|S|)×H(Sᵥ)│
│                                      │
│  Επιλέγουμε attribute με MAX IG!    │
└──────────────────────────────────────┘
```

### Gain Ratio (C4.5)
```
GainRatio = IG / SplitInfo
SplitInfo = -Σ (|Sᵥ|/|S|) × log₂(|Sᵥ|/|S|)
```

### Gini Index (CART)
```
┌──────────────────────────────────────┐
│  Gini(S) = 1 - Σ pᵢ²                │
│                                      │
│  Gini = 0: Pure                     │
│  Gini = 0.5: Max impurity (50-50)   │
└──────────────────────────────────────┘
```

---

## 16. Clustering

### K-means Centroid Update
```
┌──────────────────────────────────────┐
│  μₖ = (1/nₖ) × Σ xᵢ                 │
│               i∈Cₖ                   │
│                                      │
│  Centroid = Mean of cluster points  │
└──────────────────────────────────────┘
```

### DBSCAN Point Classification
```
┌──────────────────────────────────────┐
│  CORE:   |N(p)| ≥ MinPts            │
│  BORDER: |N(p)| < MinPts, near core │
│  NOISE:  Neither core nor border    │
│                                      │
│  ⚠️ N(p) INCLUDES p itself!         │
└──────────────────────────────────────┘
```

---

## 17. Association Rules

### Support, Confidence, Lift
```
┌──────────────────────────────────────────┐
│  Support(X) = |T with X| / |T|          │
│                                          │
│  Confidence(X→Y) = Sup(X∪Y) / Sup(X)    │
│                                          │
│  Lift(X→Y) = Conf(X→Y) / Sup(Y)         │
│            = Sup(X∪Y) / (Sup(X)×Sup(Y)) │
│                                          │
│  Lift = 1: Independent                   │
│  Lift > 1: Positive correlation          │
│  Lift < 1: Negative correlation          │
└──────────────────────────────────────────┘
```

---

## 18. DTW & Distance Metrics

### Distance Formulas
```
┌──────────────────────────────────────────┐
│  Euclidean:  d = √(Σ(xᵢ - yᵢ)²)         │
│  Manhattan:  d = Σ|xᵢ - yᵢ|             │
│  Cosine:     sim = (x·y)/(||x||×||y||)  │
│  Jaccard:    J = |A∩B| / |A∪B|          │
└──────────────────────────────────────────┘
```

### DTW Recurrence
```
┌──────────────────────────────────────────┐
│  DTW(i,j) = d(xᵢ,yⱼ) + min {            │
│                             DTW(i-1,j-1) │
│                             DTW(i-1,j)   │
│                             DTW(i,j-1)   │
│                            }             │
│                                          │
│  Base: DTW(0,0)=0, DTW(i,0)=DTW(0,j)=∞  │
└──────────────────────────────────────────┘
```

---

## 19. Classification Metrics

```
┌──────────────────────────────────────────┐
│  Accuracy    = (TP+TN) / (TP+TN+FP+FN)  │
│  Precision   = TP / (TP+FP)             │
│  Recall      = TP / (TP+FN)             │
│  Specificity = TN / (TN+FP)             │
│  F1          = 2×P×R / (P+R)            │
│  FPR         = FP / (FP+TN) = 1 - Spec  │
└──────────────────────────────────────────┘
```

---

## 20. Bayesian

### Bayes' Theorem
```
┌──────────────────────────────────────────┐
│              P(B|A) × P(A)               │
│  P(A|B) = ─────────────────              │
│                 P(B)                     │
│                                          │
│  P(B) = P(B|A)×P(A) + P(B|¬A)×P(¬A)     │
└──────────────────────────────────────────┘
```

### Naive Bayes
```
P(C|X₁,...,Xₙ) ∝ P(C) × Π P(Xᵢ|C)
```

---

## 21. TF-IDF

```
┌──────────────────────────────────────────┐
│  TF(t, d) = count of t in d             │
│                                          │
│  IDF(t) = log(N / df(t))                │
│                                          │
│  TF-IDF(t, d) = TF(t, d) × IDF(t)       │
│                                          │
│  High TF-IDF = important for this doc   │
└──────────────────────────────────────────┘
```

---

## 22. Privacy

```
┌──────────────────────────────────────────┐
│  K-ANONYMITY:                            │
│    ≥ k records per equivalence class    │
│                                          │
│  L-DIVERSITY:                            │
│    ≥ L distinct sensitive values/class  │
│                                          │
│  T-CLOSENESS:                            │
│    Distribution in class ≈ overall       │
└──────────────────────────────────────────┘
```

---

## Τελευταίος Έλεγχος ✓

**OLAP & Warehouse:**
- [ ] Cuboids: 2^n ή L₁×L₂×...×Lₙ
- [ ] Cells: p₁×p₂×...×pₙ
- [ ] Slice=1 dim, Dice=2+ dims
- [ ] Roll-up=aggregate, Drill-down=detail

**MapReduce:**
- [ ] Σειρά: 1→2→4→3 (Map→Combine→Partition→Reduce)
- [ ] JobTracker schedules, TaskTracker executes

**Data Integration:**
- [ ] GAV: ⊇, easy query, hard add source
- [ ] LAV: ⊆, hard query, easy add source

**Decision Trees:**
- [ ] Entropy=0 → pure, Entropy=1 → max uncertainty
- [ ] ID3: Information Gain
- [ ] C4.5: Gain Ratio
- [ ] CART: Gini Index, binary splits

**Clustering:**
- [ ] K-means: centroid = mean
- [ ] DBSCAN: Core if |N(p)| ≥ MinPts
- [ ] DBSCAN counts point itself!

**Association Rules:**
- [ ] Conf = Sup(X∪Y)/Sup(X)
- [ ] Lift=1 → independent

**Metrics:**
- [ ] Precision = TP/(TP+FP)
- [ ] Recall = TP/(TP+FN)
- [ ] F1 = harmonic mean

**Other:**
- [ ] Kelvin = Ratio scale
- [ ] Hash Join = ONLY equi-join
- [ ] Bloom Filter: NO false negatives
- [ ] Reservoir: probability k/n
- [ ] Pipelining: NO storage
- [ ] IDF: log(N/df), high for rare words
