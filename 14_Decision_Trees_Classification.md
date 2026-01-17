# Decision Trees & Classification - Πλήρης Οδηγός Μελέτης

## 1. Εισαγωγή

Τα **Decision Trees** είναι supervised learning models που χρησιμοποιούνται για classification και regression. Χτίζουν ένα δέντρο αποφάσεων βασισμένο στα features των δεδομένων.

### Βασική Δομή
```
                    [Root Node]
                    /         \
            [Internal]      [Internal]
            /      \            |
        [Leaf]  [Leaf]      [Leaf]
        Class A  Class B    Class A
```

**Όροι**:
- **Root Node**: Αρχικός κόμβος (feature με μεγαλύτερη διαχωριστική ικανότητα)
- **Internal Node**: Ενδιάμεσος κόμβος (test σε κάποιο attribute)
- **Leaf Node**: Τελικός κόμβος (class label/prediction)
- **Branch**: Σύνδεση μεταξύ κόμβων (outcome του test)

---

## 2. Βασικές Έννοιες & Τύποι

### 2.1 Entropy (Εντροπία)

Μετράει την **αβεβαιότητα** ή **impurity** ενός συνόλου δεδομένων.

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  H(S) = -Σ pᵢ × log₂(pᵢ)                       │
│         i                                       │
│                                                 │
│  pᵢ = πιθανότητα της κλάσης i στο σύνολο S     │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Ιδιότητες**:
- H(S) = 0 → **Τέλεια καθαρότητα** (όλα της ίδιας κλάσης)
- H(S) = 1 → **Μέγιστη αβεβαιότητα** (για 2 κλάσεις: 50-50 split)
- H(S) ∈ [0, log₂(n)] όπου n = αριθμός κλάσεων

**Παράδειγμα 1** (Εξετάσεις):
```
Dataset S: 9 "Yes" (Play Tennis), 5 "No"
Total: 14 samples

p(Yes) = 9/14
p(No) = 5/14

H(S) = -(9/14)×log₂(9/14) - (5/14)×log₂(5/14)
     = -(9/14)×(-0.637) - (5/14)×(-1.485)
     = 0.410 + 0.530
     = 0.940 bits
```

**Παράδειγμα 2** (Ακραίες περιπτώσεις):
```
Όλα "Yes" (10/10):
H(S) = -(10/10)×log₂(1) = -1×0 = 0 ✓ (pure)

Μισά-μισά (5 Yes, 5 No):
H(S) = -(5/10)×log₂(0.5) - (5/10)×log₂(0.5)
     = -0.5×(-1) - 0.5×(-1)
     = 0.5 + 0.5 = 1.0 ✓ (max uncertainty)
```

### 2.2 Information Gain

Μετράει τη **μείωση της αβεβαιότητας** όταν διαχωρίζουμε με βάση ένα attribute.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  IG(S, A) = H(S) - Σ (|Sᵥ|/|S|) × H(Sᵥ)                   │
│                    v∈Values(A)                              │
│                                                             │
│  H(S) = entropy πριν το split                               │
│  Sᵥ = subset όπου attribute A = v                          │
│  |Sᵥ|/|S| = weighted proportion                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Κανόνας**: Διαλέγουμε το attribute με το **ΜΕΓΑΛΥΤΕΡΟ Information Gain**!

**Παράδειγμα Υπολογισμού** (Τυπικό θέμα εξετάσεων):
```
Dataset S: 14 samples (9 Yes, 5 No)
H(S) = 0.940 (υπολογίστηκε παραπάνω)

Attribute: Outlook (values: Sunny, Overcast, Rain)

Split results:
  Sunny: 5 samples (2 Yes, 3 No)
    H(Sunny) = -(2/5)log₂(2/5) - (3/5)log₂(3/5)
             = 0.971

  Overcast: 4 samples (4 Yes, 0 No)
    H(Overcast) = 0 (pure!)

  Rain: 5 samples (3 Yes, 2 No)
    H(Rain) = -(3/5)log₂(3/5) - (2/5)log₂(2/5)
            = 0.971

Weighted average entropy after split:
H(S|Outlook) = (5/14)×0.971 + (4/14)×0 + (5/14)×0.971
             = 0.347 + 0 + 0.347
             = 0.694

Information Gain:
IG(S, Outlook) = H(S) - H(S|Outlook)
               = 0.940 - 0.694
               = 0.246 bits
```

### 2.3 Gain Ratio (C4.5)

Το Information Gain **ευνοεί attributes με πολλές τιμές**. Το Gain Ratio το διορθώνει.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  GainRatio(S, A) = IG(S, A) / SplitInfo(S, A)              │
│                                                             │
│  SplitInfo(S, A) = -Σ (|Sᵥ|/|S|) × log₂(|Sᵥ|/|S|)        │
│                     v∈Values(A)                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Attribute: Outlook με splits 5, 4, 5

SplitInfo(S, Outlook) = -(5/14)×log₂(5/14) - (4/14)×log₂(4/14) - (5/14)×log₂(5/14)
                      = 0.530 + 0.516 + 0.530
                      = 1.577

GainRatio(S, Outlook) = 0.246 / 1.577 = 0.156
```

### 2.4 Gini Index

Εναλλακτικό μέτρο impurity (χρησιμοποιείται στο CART).

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Gini(S) = 1 - Σ pᵢ²                                       │
│                i                                            │
│                                                             │
│  Gini = 0 → pure (μία κλάση)                               │
│  Gini = 0.5 → max impurity (2 κλάσεις 50-50)               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Dataset: 9 Yes, 5 No (14 total)

p(Yes) = 9/14 = 0.643
p(No) = 5/14 = 0.357

Gini(S) = 1 - (0.643)² - (0.357)²
        = 1 - 0.413 - 0.127
        = 0.459
```

**Gini Gain** (για επιλογή split):
```
GiniGain(S, A) = Gini(S) - Σ (|Sᵥ|/|S|) × Gini(Sᵥ)
```

---

## 3. Αλγόριθμοι

### 3.1 ID3 (Iterative Dichotomiser 3)

```
┌────────────────────────────────────────────────────────────┐
│  ID3(S, Attributes)                                        │
│  ─────────────────                                         │
│  1. IF all samples belong to same class C                  │
│        RETURN Leaf(C)                                      │
│                                                            │
│  2. IF Attributes is empty                                 │
│        RETURN Leaf(majority class)                         │
│                                                            │
│  3. A_best = argmax IG(S, A) for A in Attributes           │
│                                                            │
│  4. Create Node for A_best                                 │
│                                                            │
│  5. FOR EACH value v of A_best:                            │
│        Sᵥ = samples where A_best = v                       │
│        IF Sᵥ is empty:                                     │
│           Add Leaf(majority class of S)                    │
│        ELSE:                                               │
│           Add ID3(Sᵥ, Attributes - {A_best})               │
│                                                            │
│  6. RETURN Node                                            │
└────────────────────────────────────────────────────────────┘
```

**Χαρακτηριστικά ID3**:
- Χρησιμοποιεί **Information Gain**
- Μόνο **categorical attributes**
- Τείνει να δημιουργεί **bushy trees** (πολλά branches)
- **Ευνοεί attributes με πολλές τιμές**

### 3.2 C4.5 (Successor of ID3)

Βελτιώσεις σε σχέση με ID3:
- Χρησιμοποιεί **Gain Ratio** αντί για Information Gain
- Υποστηρίζει **continuous attributes** (βρίσκει optimal threshold)
- Χειρίζεται **missing values**
- Ενσωματώνει **pruning**

### 3.3 CART (Classification and Regression Trees)

- Χρησιμοποιεί **Gini Index**
- Πάντα **binary splits**
- Υποστηρίζει και **regression** (με MSE)

---

## 4. Worked Examples (Πλήρης Κατασκευή Δέντρου)

### Παράδειγμα: Play Tennis Dataset

**Dataset**:
| Outlook | Temperature | Humidity | Wind | Play? |
|---------|-------------|----------|------|-------|
| Sunny | Hot | High | Weak | No |
| Sunny | Hot | High | Strong | No |
| Overcast | Hot | High | Weak | Yes |
| Rain | Mild | High | Weak | Yes |
| Rain | Cool | Normal | Weak | Yes |
| Rain | Cool | Normal | Strong | No |
| Overcast | Cool | Normal | Strong | Yes |
| Sunny | Mild | High | Weak | No |
| Sunny | Cool | Normal | Weak | Yes |
| Rain | Mild | Normal | Weak | Yes |
| Sunny | Mild | Normal | Strong | Yes |
| Overcast | Mild | High | Strong | Yes |
| Overcast | Hot | Normal | Weak | Yes |
| Rain | Mild | High | Strong | No |

**Βήμα 1: Υπολογισμός H(S)**
```
Total: 14 samples (9 Yes, 5 No)

H(S) = -(9/14)×log₂(9/14) - (5/14)×log₂(5/14)
     = 0.940 bits
```

**Βήμα 2: Υπολογισμός IG για κάθε attribute**

**Outlook**:
```
Sunny:    5 samples → 2 Yes, 3 No → H = 0.971
Overcast: 4 samples → 4 Yes, 0 No → H = 0.000
Rain:     5 samples → 3 Yes, 2 No → H = 0.971

H(S|Outlook) = (5/14)×0.971 + (4/14)×0 + (5/14)×0.971 = 0.694

IG(S, Outlook) = 0.940 - 0.694 = 0.246 ✓
```

**Temperature**:
```
Hot:  4 samples → 2 Yes, 2 No → H = 1.0
Mild: 6 samples → 4 Yes, 2 No → H = 0.918
Cool: 4 samples → 3 Yes, 1 No → H = 0.811

H(S|Temp) = (4/14)×1.0 + (6/14)×0.918 + (4/14)×0.811 = 0.911

IG(S, Temp) = 0.940 - 0.911 = 0.029
```

**Humidity**:
```
High:   7 samples → 3 Yes, 4 No → H = 0.985
Normal: 7 samples → 6 Yes, 1 No → H = 0.592

H(S|Humidity) = (7/14)×0.985 + (7/14)×0.592 = 0.789

IG(S, Humidity) = 0.940 - 0.789 = 0.151
```

**Wind**:
```
Weak:   8 samples → 6 Yes, 2 No → H = 0.811
Strong: 6 samples → 3 Yes, 3 No → H = 1.0

H(S|Wind) = (8/14)×0.811 + (6/14)×1.0 = 0.892

IG(S, Wind) = 0.940 - 0.892 = 0.048
```

**Βήμα 3: Επιλογή Root**
```
┌────────────────────────────────────┐
│  Attribute    │  Information Gain │
├────────────────────────────────────┤
│  Outlook      │  0.246 ← ΜΕΓΙΣΤΟ  │
│  Humidity     │  0.151            │
│  Wind         │  0.048            │
│  Temperature  │  0.029            │
└────────────────────────────────────┘

Root = Outlook
```

**Βήμα 4: Κατασκευή Δέντρου**
```
                      [Outlook]
                    /     |     \
              Sunny  Overcast   Rain
                /        |         \
          [Humidity]   Yes      [Wind]
          /      \               /     \
       High    Normal       Weak    Strong
         |        |           |         |
        No       Yes        Yes        No
```

**Εξήγηση**:
- Overcast → 4/4 Yes → Pure node, STOP
- Sunny → 2 Yes, 3 No → Needs splitting
  - Humidity: High (0Y, 3N), Normal (2Y, 0N) → IG = 0.971 (max!)
- Rain → 3 Yes, 2 No → Needs splitting
  - Wind: Weak (3Y, 0N), Strong (0Y, 2N) → Perfect split!

---

## 5. ⚠️ Συχνά Λάθη / Pitfalls

### 5.1 Λάθος Υπολογισμός Entropy
```
❌ ΛΑΘΟΣ: H = p × log₂(p) (ξεχνάς το minus!)
✓ ΣΩΣΤΟ: H = -p × log₂(p)

❌ ΛΑΘΟΣ: log₂(0) = 0
✓ ΣΩΣΤΟ: Αν p=0, ο όρος p×log₂(p) = 0 (by convention)
```

### 5.2 Weighted Average
```
❌ ΛΑΘΟΣ: H(S|A) = (H(S₁) + H(S₂)) / 2
✓ ΣΩΣΤΟ: H(S|A) = (|S₁|/|S|)×H(S₁) + (|S₂|/|S|)×H(S₂)

Το βάρος είναι το μέγεθος κάθε subset!
```

### 5.3 Σύγχυση Gain vs Gain Ratio
```
ID3:  Χρησιμοποιεί Information Gain
C4.5: Χρησιμοποιεί Gain Ratio

Gain Ratio = IG / SplitInfo
```

### 5.4 Gini vs Entropy
```
Entropy: H(S) = -Σ pᵢ × log₂(pᵢ)  → range [0, log₂(n)]
Gini:    G(S) = 1 - Σ pᵢ²        → range [0, 0.5] for 2 classes

Για 50-50 split:
  Entropy = 1.0
  Gini = 0.5
```

---

## 6. Pruning (Κλάδεμα)

### 6.1 Pre-Pruning (Early Stopping)
Σταματάμε το splitting **πριν** το δέντρο γίνει πολύ βαθύ.

Κριτήρια:
- Maximum depth
- Minimum samples per leaf
- Minimum information gain threshold
- Maximum number of leaves

### 6.2 Post-Pruning
Χτίζουμε το πλήρες δέντρο και μετά **αφαιρούμε** branches.

**Reduced Error Pruning**:
1. Για κάθε internal node, αξιολόγησε: "Τι αν το αντικαταστήσω με leaf;"
2. Αν το accuracy στο validation set δεν χειροτερεύει, κάνε prune

**Cost Complexity Pruning (CART)**:
```
Cost = Error + α × |Leaves|

Μεγάλο α → Πιο μικρό δέντρο (aggressive pruning)
Μικρό α → Πιο μεγάλο δέντρο
```

---

## 7. Ερωτήσεις Εξετάσεων

### Ερώτηση 1
Δίνεται dataset με 10 "Yes" και 6 "No". Ποια είναι η entropy;

A) 0.0
B) 0.5
C) 0.863
D) 0.954

<details>
<summary>Απάντηση</summary>

**Σωστό: D) 0.954**

**Υπολογισμός**:
```
p(Yes) = 10/16 = 0.625
p(No) = 6/16 = 0.375

H(S) = -(0.625)×log₂(0.625) - (0.375)×log₂(0.375)
     = -(0.625)×(-0.678) - (0.375)×(-1.415)
     = 0.424 + 0.530
     = 0.954
```

**Γιατί οι άλλες είναι λάθος**:
- A) 0.0 θα ήταν αν όλα ήταν μίας κλάσης
- B) 0.5 είναι max Gini, όχι entropy
- C) 0.863 θα ήταν αν ήταν 8 Yes, 8 No
</details>

---

### Ερώτηση 2
Ποιο attribute θα διαλέξει ο ID3 ως root;

| Attribute | Information Gain |
|-----------|------------------|
| A | 0.25 |
| B | 0.15 |
| C | 0.30 |
| D | 0.20 |

A) A
B) B
C) C
D) D

<details>
<summary>Απάντηση</summary>

**Σωστό: C) C**

**Εξήγηση**: ID3 διαλέγει το attribute με το **ΜΕΓΑΛΥΤΕΡΟ Information Gain**.
IG(C) = 0.30 είναι το μέγιστο.
</details>

---

### Ερώτηση 3
Ένα dataset έχει 20 samples: 10 Class A, 10 Class B. Ποιο είναι το Gini Index;

A) 0.0
B) 0.25
C) 0.5
D) 1.0

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 0.5**

**Υπολογισμός**:
```
p(A) = p(B) = 0.5

Gini = 1 - (0.5)² - (0.5)²
     = 1 - 0.25 - 0.25
     = 0.5
```

**Σημείωση**: 0.5 είναι το μέγιστο Gini για 2 κλάσεις (max impurity).
</details>

---

### Ερώτηση 4
Τι σημαίνει entropy = 0;

A) Maximum uncertainty
B) Uniform distribution
C) Τέλεια καθαρότητα (pure node)
D) 50-50 split

<details>
<summary>Απάντηση</summary>

**Σωστό: C) Τέλεια καθαρότητα**

**Εξήγηση**: Entropy = 0 σημαίνει ότι όλα τα samples ανήκουν στην ίδια κλάση → δεν χρειάζεται περαιτέρω splitting.
</details>

---

### Ερώτηση 5
Ποια είναι η βασική διαφορά μεταξύ ID3 και C4.5;

A) ID3 χρησιμοποιεί Gini, C4.5 χρησιμοποιεί Entropy
B) ID3 χρησιμοποιεί Information Gain, C4.5 χρησιμοποιεί Gain Ratio
C) C4.5 δεν μπορεί να χειριστεί categorical attributes
D) ID3 κάνει post-pruning, C4.5 δεν κάνει

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**:
- **ID3**: Information Gain (ευνοεί attributes με πολλές τιμές)
- **C4.5**: Gain Ratio (διορθώνει το bias του ID3)

Επιπλέον, C4.5 υποστηρίζει continuous attributes και missing values.
</details>

---

### Ερώτηση 6
Dataset: 8 samples με attribute A που έχει 2 τιμές (V1: 5 samples, V2: 3 samples).
Αν V1 έχει H=0.72 και V2 έχει H=0.92, ποιο είναι το H(S|A);

A) 0.72
B) 0.795
C) 0.82
D) 0.92

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 0.795**

**Υπολογισμός**:
```
H(S|A) = (5/8)×0.72 + (3/8)×0.92
       = 0.625×0.72 + 0.375×0.92
       = 0.45 + 0.345
       = 0.795
```
</details>

---

### Ερώτηση 7
Αν H(S) = 1.0 και H(S|A) = 0.6, ποιο είναι το Information Gain του A;

A) 0.4
B) 0.6
C) 1.0
D) 1.6

<details>
<summary>Απάντηση</summary>

**Σωστό: A) 0.4**

**Υπολογισμός**:
```
IG(S, A) = H(S) - H(S|A) = 1.0 - 0.6 = 0.4
```
</details>

---

### Ερώτηση 8
Γιατί το Information Gain ευνοεί attributes με πολλές τιμές;

A) Γιατί υπολογίζει λάθος το entropy
B) Γιατί πολλές τιμές δίνουν μικρότερα, πιο καθαρά subsets
C) Γιατί το Gini είναι πιο ακριβές
D) Δεν ισχύει αυτό

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: Ένα attribute με πολλές τιμές (π.χ. ID με unique values) δημιουργεί πολλά μικρά subsets, καθένα με χαμηλό entropy → υψηλό IG.

Παράδειγμα: Attribute "CustomerID" με unique values → κάθε subset έχει 1 sample → H=0 για όλα → IG = H(S) - 0 = μέγιστο!

Αυτό είναι πρόβλημα γιατί το CustomerID δεν γενικεύει!
</details>

---

### Ερώτηση 9
Ποιος αλγόριθμος χρησιμοποιεί ΜΟΝΟ binary splits;

A) ID3
B) C4.5
C) CART
D) Κανένας

<details>
<summary>Απάντηση</summary>

**Σωστό: C) CART**

**Εξήγηση**:
- ID3/C4.5: Multi-way splits (ένα branch για κάθε τιμή του attribute)
- CART: Πάντα binary splits (π.χ. age ≤ 30 vs age > 30)
</details>

---

### Ερώτηση 10
Ποια τεχνική pruning χτίζει πρώτα το πλήρες δέντρο;

A) Pre-pruning
B) Post-pruning
C) Και οι δύο
D) Καμία

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Post-pruning**

**Εξήγηση**:
- **Pre-pruning**: Σταματάει νωρίς (δεν χτίζει πλήρες δέντρο)
- **Post-pruning**: Χτίζει πλήρες δέντρο, μετά αφαιρεί branches
</details>

---

### Ερώτηση 11 (Υπολογιστική)
Υπολόγισε το SplitInfo για attribute A με τρεις τιμές: V1 (6 samples), V2 (4 samples), V3 (2 samples) από σύνολο 12.

A) 1.46
B) 1.33
C) 1.58
D) 1.79

<details>
<summary>Απάντηση</summary>

**Σωστό: A) 1.46**

**Υπολογισμός**:
```
SplitInfo = -(6/12)×log₂(6/12) - (4/12)×log₂(4/12) - (2/12)×log₂(2/12)
          = -(0.5)×log₂(0.5) - (0.333)×log₂(0.333) - (0.167)×log₂(0.167)
          = -(0.5)×(-1) - (0.333)×(-1.585) - (0.167)×(-2.585)
          = 0.5 + 0.528 + 0.431
          = 1.459 ≈ 1.46
```
</details>

---

## 8. Σύνοψη - Key Points

### Τύποι (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

| Μέτρο | Τύπος | Range |
|-------|-------|-------|
| **Entropy** | H(S) = -Σ pᵢ × log₂(pᵢ) | [0, log₂(n)] |
| **Information Gain** | IG = H(S) - H(S\|A) | [0, H(S)] |
| **Gain Ratio** | GR = IG / SplitInfo | - |
| **Gini** | G(S) = 1 - Σ pᵢ² | [0, 0.5] for 2 classes |

### Αλγόριθμοι (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

| Algorithm | Criterion | Splits | Special |
|-----------|-----------|--------|---------|
| **ID3** | Information Gain | Multi-way | Categorical only |
| **C4.5** | Gain Ratio | Multi-way | Handles continuous, missing |
| **CART** | Gini Index | Binary only | Regression support |

### Ιδιότητες Entropy

```
H = 0   → Pure node (μία κλάση)
H = 1   → Max uncertainty (2 κλάσεις 50-50)

Όσο μεγαλύτερο το IG, τόσο καλύτερο το split!
```

### Pruning

```
Pre-pruning:  Stop early (max depth, min samples)
Post-pruning: Build full, then cut (reduced error, cost complexity)
```
