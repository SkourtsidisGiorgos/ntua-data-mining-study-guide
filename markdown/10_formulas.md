# Συγκεντρωτικός Τύπων & Γρήγορη Αναφορά

## Relational Algebra

| Τελεστής | Σύμβολο | SQL Αντίστοιχο | Περιγραφή |
|----------|---------|----------------|-----------|
| Selection | σ_cond(R) | WHERE | Φιλτράρισμα γραμμών |
| Projection | π_cols(R) | SELECT cols | Επιλογή στηλών (+ DISTINCT) |
| Union | R ∪ S | UNION | Ένωση συνόλων |
| Intersection | R ∩ S | INTERSECT | Τομή συνόλων |
| Difference | R − S | EXCEPT | Διαφορά συνόλων |
| Natural Join | R ⋈ S | NATURAL JOIN | Join σε κοινές στήλες |
| Theta Join | R ⋈_θ S | JOIN ON | Join με συνθήκη |
| Division | R ÷ S | NOT EXISTS×2 | "Για όλα" queries |

---

## SQL

### Σειρά Εκτέλεσης
```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

### WHERE vs HAVING
| WHERE | HAVING |
|-------|--------|
| ΠΡΙΝ grouping | ΜΕΤΑ grouping |
| ΟΧΙ aggregates | ΝΑΙ aggregates |

### Division Pattern
```sql
SELECT ... WHERE NOT EXISTS (
    SELECT ... WHERE NOT EXISTS (...)
)
```

---

## Join Algorithms

| Αλγόριθμος | Κόστος | Equi-Join | Inequality |
|------------|--------|-----------|------------|
| Nested Loop | O(n×m) | ✓ | ✓ |
| Hash Join | O(n+m) | ✓ | ❌ |
| Sort-Merge | O(n log n) | ✓ | ❌ |

### Pipelined vs Blocking
- **Pipelined:** σ, π, Nested Loop outer
- **Blocking:** Sort, Hash build, Aggregation, Distinct

---

## Τύποι Χαρακτηριστικών (NOIR)

| Τύπος | Πράξεις | Παράδειγμα |
|-------|---------|------------|
| Nominal | =, ≠ | Χρώμα, ID |
| Ordinal | <, > | Rating 1-5 |
| Interval | +, − | °C, Έτος |
| Ratio | ×, ÷ | Ύψος, Kelvin |

**Τεστ Interval vs Ratio:** "Μπορώ να πω διπλάσιο;"
- ΝΑΙ → Ratio
- ΟΧΙ → Interval

---

## Discretization & Normalization

### Equal-Width Binning
```
Width = (max - min) / k
Bin i: [min + (i-1)×width, min + i×width)
```

### Equal-Frequency Binning
```
Records per bin = n / k
```

### Min-Max Normalization
```
x' = (x - min) / (max - min)
```
Αποτέλεσμα: [0, 1]

### Z-Score Standardization
```
z = (x - μ) / σ
```
Αποτέλεσμα: mean=0, std=1

---

## Μέτρα Απόστασης

### Euclidean (L2)
```
d = √(Σ(xᵢ - yᵢ)²)
```

### Manhattan (L1)
```
d = Σ|xᵢ - yᵢ|
```

### Cosine Similarity
```
cos(θ) = (x · y) / (||x|| × ||y||)
```
**Σημείωση:** Μόνο κατεύθυνση, αγνοεί μέγεθος

---

## Bloom Filter

### False Positive Rate
```
p ≈ (1 - e^(-kn/m))^k
```
- m = bits
- n = elements inserted
- k = hash functions

### Optimal k
```
k = (m/n) × ln(2) ≈ 0.693 × (m/n)
```

### ΚΡΙΣΙΜΟ
- **False Positives:** ΝΑΙ (maybe yes)
- **False Negatives:** ΠΟΤΕ (no = definitely no)

---

## Count-Min Sketch

### Update
```
count[i][hᵢ(x)] += 1   για κάθε hash function
```

### Query
```
estimate(x) = min(count[i][hᵢ(x)])   για όλα τα i
```

### ΚΡΙΣΙΜΟ
- **Overestimate:** ΠΑΝΤΑ (estimate ≥ actual)
- **Underestimate:** ΠΟΤΕ

---

## Hidden Markov Models

### Forward Algorithm (Πιθανότητα Ακολουθίας)

**Αρχικοποίηση (t=1):**
```
α₁(i) = πᵢ × bᵢ(o₁)
```

**Επαγωγή (t > 1):**
```
αₜ(j) = [Σᵢ αₜ₋₁(i) × aᵢⱼ] × bⱼ(oₜ)
```

**Τερματισμός:**
```
P(O|λ) = Σᵢ αₜ(i)
```

### Viterbi Algorithm (Καλύτερο Path)

**Αρχικοποίηση:**
```
δ₁(i) = πᵢ × bᵢ(o₁)
```

**Επαγωγή:**
```
δₜ(j) = max_i[δₜ₋₁(i) × aᵢⱼ] × bⱼ(oₜ)
```

### ΣΗΜΑΝΤΙΚΟ
- Forward: **ΑΘΡΟΙΣΗ (Σ)**
- Viterbi: **ΜΕΓΙΣΤΟ (max)**
- **ΜΗΝ ΞΕΧΝΑΣ** το bⱼ(oₜ) στο τέλος!

---

## OLAP Operations

| Λειτουργία | Περιγραφή | Παράδειγμα |
|------------|-----------|------------|
| Roll-up | Λιγότερη λεπτομέρεια | day→month→year |
| Drill-down | Περισσότερη λεπτομέρεια | year→month→day |
| Slice | Μία διάσταση, μία τιμή | Time=2024 |
| Dice | Πολλές διαστάσεις/τιμές | Time=2024 ∧ Product='A' |
| Pivot | Περιστροφή αξόνων | Rows↔Columns |

### Cube Calculations
```
Cuboids: 2ⁿ (n = αριθμός διαστάσεων)
Cells: (|d₁|+1) × (|d₂|+1) × ... × (|dₙ|+1)
```

---

## E-R → Relational Μετατροπή

| Στοιχείο | Κανόνας |
|----------|---------|
| Strong Entity | Πίνακας με attributes |
| Weak Entity | (owner_PK + partial_key) = PK |
| 1:1 | FK σε οποιαδήποτε πλευρά |
| 1:N | FK στην N-πλευρά |
| M:N | Νέος πίνακας με 2 FKs |
| Multivalued | Ξεχωριστός πίνακας |

---

## Query Processing

| Concept | Περιγραφή |
|---------|-----------|
| Pipelining | Tuple-by-tuple, χαμηλή μνήμη |
| Materialization | Αποθήκευση ενδιάμεσων, blocking |
| Push Selection | Φίλτρα νωρίτερα = λιγότερα data |
| Push Projection | Λιγότερες στήλες νωρίτερα |

---

## RAG (Retrieval-Augmented Generation)

### Pipeline
```
Index docs → Query → Retrieve → Augment prompt → Generate
```

### Πλεονεκτήματα
- Grounded responses (λιγότερα hallucinations)
- Up-to-date (χωρίς re-training)
- Attribution (πηγές)

### Chunking Trade-off
- Μικρά chunks: Ακριβές retrieval, λιγότερο context
- Μεγάλα chunks: Περισσότερο context, λιγότερο ακριβές

---

## Γρήγορος Πίνακας Αναφοράς

| Θέμα | Κλειδί-Τύπος/Έννοια |
|------|---------------------|
| Selection | σ = WHERE (γραμμές) |
| Projection | π = SELECT (στήλες, DISTINCT) |
| Division | NOT EXISTS × 2 |
| Hash Join | ΜΟΝΟ equi-join (=) |
| NOIR | Nominal→Ordinal→Interval→Ratio |
| Ratio vs Interval | "Διπλάσιο;" ΝΑΙ=Ratio |
| Bloom Filter | No false negatives! |
| Count-Min | Always overestimates |
| Forward vs Viterbi | Σ vs max |
| Roll-up | Less detail (↑ hierarchy) |
| Drill-down | More detail (↓ hierarchy) |
| Slice vs Dice | 1 dim vs πολλές |
| Pipelining | Tuple-by-tuple |
| Materialization | Store intermediate |

---

## Τι να ΑΠΟΜΝΗΜΟΝΕΥΣΕΤΕ

1. **SQL execution order:** FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY
2. **NOIR:** Nominal < Ordinal < Interval < Ratio
3. **Hash Join:** ΜΟΝΟ για = (όχι >, <)
4. **Bloom Filter:** No false negatives
5. **Count-Min Sketch:** Always overestimates
6. **Forward:** Σ (sum), Viterbi: max
7. **ΜΗΝ ΞΕΧΝΑΣ:** bⱼ(oₜ) στο HMM!
8. **Roll-up:** Less detail, Drill-down: More detail
9. **Slice:** 1 dimension, Dice: πολλές
10. **Pivot:** Rotate axes
