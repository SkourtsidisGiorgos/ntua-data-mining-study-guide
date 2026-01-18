# Classification Metrics - Πλήρης Οδηγός Μελέτης

## 1. Εισαγωγή

Τα **classification metrics** αξιολογούν την απόδοση ενός classification model. Η επιλογή του σωστού metric εξαρτάται από το πρόβλημα (π.χ. imbalanced classes, κόστος λαθών).

---

## 2. Confusion Matrix (Πίνακας Σύγχυσης)

### 2.1 Βασική Δομή (Binary Classification)

```
                    PREDICTED
                 Positive  Negative
              ┌──────────┬──────────┐
    Positive  │    TP    │    FN    │
ACTUAL        ├──────────┼──────────┤
    Negative  │    FP    │    TN    │
              └──────────┴──────────┘
```

### 2.2 Ορισμοί

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  TP (True Positive):  Πρόβλεψη + , Πραγματικό +            │
│                       → Σωστά εντοπίσαμε positive           │
│                                                             │
│  TN (True Negative):  Πρόβλεψη - , Πραγματικό -            │
│                       → Σωστά εντοπίσαμε negative           │
│                                                             │
│  FP (False Positive): Πρόβλεψη + , Πραγματικό -            │
│                       → Type I Error (False Alarm)          │
│                                                             │
│  FN (False Negative): Πρόβλεψη - , Πραγματικό +            │
│                       → Type II Error (Miss)                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Παράδειγμα

**Spam Detection**: Προβλέπουμε αν email είναι spam (+) ή όχι (-)

| | Predicted Spam | Predicted Not Spam |
|---|---|---|
| **Actually Spam** | TP = 85 | FN = 15 |
| **Actually Not Spam** | FP = 10 | TN = 890 |

Total: 1000 emails (100 spam, 900 not spam)

---

## 3. Βασικά Metrics

### 3.1 Accuracy (Ακρίβεια)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              TP + TN                                        │
│  Accuracy = ─────────────────                               │
│             TP + TN + FP + FN                               │
│                                                             │
│  = (Σωστές προβλέψεις) / (Όλες οι προβλέψεις)              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Accuracy = (85 + 890) / 1000 = 975/1000 = 0.975 = 97.5%
```

**⚠️ Πρόβλημα με Imbalanced Data**:
```
Αν έχουμε 990 not spam και 10 spam:
- Model που προβλέπει πάντα "not spam"
- Accuracy = 990/1000 = 99%... αλλά ΟΛΟΙ οι spammers περνούν!
```

### 3.2 Precision (Ακρίβεια Θετικών Προβλέψεων)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│               TP                                            │
│  Precision = ────────                                       │
│              TP + FP                                        │
│                                                             │
│  = (Σωστά positive) / (Προβλέψεις ως positive)             │
│                                                             │
│  "Από αυτά που είπα positive, πόσα ήταν όντως positive?"   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Precision = 85 / (85 + 10) = 85/95 = 0.895 = 89.5%
```

**Σημαντικό όταν**: Το FP είναι costly (π.χ. μη-spam email πάει στα spam)

### 3.3 Recall / Sensitivity / True Positive Rate (TPR)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│            TP                                               │
│  Recall = ────────                                          │
│           TP + FN                                           │
│                                                             │
│  = (Σωστά positive) / (Πραγματικά positive)                │
│                                                             │
│  "Από τα όντως positive, πόσα βρήκα;"                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Recall = 85 / (85 + 15) = 85/100 = 0.85 = 85%
```

**Σημαντικό όταν**: Το FN είναι costly (π.χ. χάνουμε cancer diagnosis)

### 3.4 Specificity / True Negative Rate (TNR)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                TN                                           │
│  Specificity = ────────                                     │
│                TN + FP                                      │
│                                                             │
│  = (Σωστά negative) / (Πραγματικά negative)                │
│                                                             │
│  "Από τα όντως negative, πόσα αναγνώρισα ως negative;"     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
Specificity = 890 / (890 + 10) = 890/900 = 0.989 = 98.9%
```

### 3.5 F1 Score

Harmonic mean του Precision και Recall - **balances both metrics**.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│            2 × Precision × Recall                           │
│  F1 Score = ─────────────────────────                       │
│              Precision + Recall                             │
│                                                             │
│          2 × TP                                             │
│        = ────────────────                                   │
│          2×TP + FP + FN                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
F1 = 2 × 0.895 × 0.85 / (0.895 + 0.85)
   = 1.5215 / 1.745
   = 0.872 = 87.2%

Εναλλακτικά:
F1 = 2×85 / (2×85 + 10 + 15) = 170 / 195 = 0.872
```

**Ιδιότητα**: F1 είναι χαμηλό αν ένα από Precision/Recall είναι χαμηλό!
```
Precision = 0.9, Recall = 0.9 → F1 = 0.9
Precision = 0.9, Recall = 0.1 → F1 = 0.18 (χαμηλό!)
```

### 3.6 False Positive Rate (FPR)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│         FP                                                  │
│  FPR = ────────── = 1 - Specificity                        │
│        FP + TN                                              │
│                                                             │
│  "Ποσοστό negative που λάθος τα είπα positive"             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Παράδειγμα**:
```
FPR = 10 / (10 + 890) = 10/900 = 0.011 = 1.1%
```

---

## 4. Σύνοψη Τύπων (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Accuracy    = (TP + TN) / (TP + TN + FP + FN)               │
│                                                               │
│  Precision   = TP / (TP + FP)       [όσα είπα +]             │
│                                                               │
│  Recall      = TP / (TP + FN)       [όσα ήταν +]             │
│                                                               │
│  Specificity = TN / (TN + FP)       [όσα ήταν -]             │
│                                                               │
│  F1          = 2×Precision×Recall / (Precision + Recall)     │
│             = 2×TP / (2×TP + FP + FN)                        │
│                                                               │
│  FPR         = FP / (FP + TN) = 1 - Specificity              │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Mnemonics (Μνημονικοί Κανόνες)

```
Precision: P = TP / (TP + FP)   → Παρονομαστής: Predictions as Positive
Recall:    R = TP / (TP + FN)   → Παρονομαστής: Reality was Positive

         Predicted
         +      -
       ┌─────┬─────┐
    +  │ TP  │ FN  │ ← TP + FN = Actual Positives (Recall denominator)
Real   ├─────┼─────┤
    -  │ FP  │ TN  │ ← TN + FP = Actual Negatives (Specificity denominator)
       └─────┴─────┘
         ↑
         TP + FP = Predicted Positives (Precision denominator)
```

---

## 5. ROC Curve & AUC

### 5.1 ROC Curve

**ROC** = Receiver Operating Characteristic

Γράφημα: **TPR (Recall)** vs **FPR** για διάφορα thresholds.

```
  TPR
  1.0 ┼────────────┐
      │      ●──●──●  ← Good classifier
      │    ●
      │  ●
  0.5 ┼─────●───────── Random classifier
      │   ●          (diagonal)
      │ ●
      │●
  0.0 ┼────┼────┼────┼──→ FPR
      0   0.25 0.5 0.75 1.0
```

**Ερμηνεία**:
- **Πάνω-αριστερά** = Perfect (TPR=1, FPR=0)
- **Διαγώνιος** = Random guess
- **Κάτω-δεξιά** = Worse than random

### 5.2 AUC (Area Under ROC Curve)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  AUC = 1.0  → Perfect classifier                           │
│  AUC = 0.5  → Random classifier                            │
│  AUC < 0.5  → Worse than random (flip predictions!)        │
│                                                             │
│  AUC = P(score(random +) > score(random -))                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Κατηγοριοποίηση AUC**:
```
0.9 - 1.0: Excellent
0.8 - 0.9: Good
0.7 - 0.8: Fair
0.6 - 0.7: Poor
0.5 - 0.6: Fail
```

---

## 6. Multi-Class Metrics

### 6.1 Confusion Matrix (Multi-class)

```
                     PREDICTED
             Class A   Class B   Class C
          ┌─────────┬─────────┬─────────┐
 Class A  │   50    │    5    │    5    │  = 60 actual A
ACTUAL    ├─────────┼─────────┼─────────┤
 Class B  │    3    │   40    │    7    │  = 50 actual B
          ├─────────┼─────────┼─────────┤
 Class C  │    2    │    8    │   80    │  = 90 actual C
          └─────────┴─────────┴─────────┘
            = 55      = 53      = 92       Total: 200
```

### 6.2 Micro-Averaging vs Macro-Averaging

**Micro-Average**: Aggregate contributions, then compute metric
```
Micro-Precision = Σ TPᵢ / Σ (TPᵢ + FPᵢ)

Σ TP = 50 + 40 + 80 = 170
Σ FP = (3+2) + (5+8) + (5+7) = 5 + 13 + 12 = 30

Micro-Precision = 170 / (170 + 30) = 170/200 = 0.85
```

**Macro-Average**: Compute per-class, then average
```
Precision_A = 50/55 = 0.909
Precision_B = 40/53 = 0.755
Precision_C = 80/92 = 0.870

Macro-Precision = (0.909 + 0.755 + 0.870) / 3 = 0.845
```

**Πότε τι**:
- **Micro**: Κάθε sample έχει ίσο βάρος (imbalanced classes OK)
- **Macro**: Κάθε class έχει ίσο βάρος (μικρές classes μετράνε ίσα)

---

## 7. ⚠️ Συχνά Λάθη / Pitfalls

### 7.1 Accuracy Paradox
```
❌ ΛΑΘΟΣ: Υψηλό accuracy = καλό model
✓ ΣΩΣΤΟ: Σε imbalanced data, accuracy μπορεί να είναι misleading

Dataset: 990 negative, 10 positive
Model που λέει πάντα "negative": Accuracy = 99%... αλλά άχρηστο!
```

### 7.2 Σύγχυση Precision/Recall
```
❌ ΛΑΘΟΣ: Precision = TP / (TP + FN)
✓ ΣΩΣΤΟ: Precision = TP / (TP + FP)   [predicted positives]
         Recall    = TP / (TP + FN)   [actual positives]

Precision: "Πόσα από τα predicted + είναι σωστά"
Recall:    "Πόσα από τα actual + τα βρήκα"
```

### 7.3 F1 vs Accuracy
```
❌ ΛΑΘΟΣ: F1 > Accuracy πάντα
✓ ΣΩΣΤΟ: Εξαρτάται από τα δεδομένα

F1 = harmonic mean, πιο αυστηρό
Accuracy μπορεί να είναι υψηλό με imbalanced classes
```

### 7.4 Specificity vs Recall
```
Specificity = TN / (TN + FP) → για τα NEGATIVE
Recall      = TP / (TP + FN) → για τα POSITIVE

Είναι "αντίστροφα" για τις δύο κλάσεις!
```

---

## 8. Trade-offs

### 8.1 Precision-Recall Trade-off

```
Threshold ↑ (more strict):
  - Precision ↑ (fewer FP)
  - Recall ↓ (more FN)

Threshold ↓ (more lenient):
  - Precision ↓ (more FP)
  - Recall ↑ (fewer FN)

Δεν μπορείς να έχεις και τα δύο υψηλά ταυτόχρονα!
```

### 8.2 Πότε προτιμούμε τι

| Scenario | Optimize for | Why |
|----------|--------------|-----|
| Medical diagnosis | **Recall** | Miss = death |
| Spam filter | **Precision** | FP = lost important email |
| Fraud detection | **Recall** | Miss = money loss |
| Product recommendation | **Precision** | FP = annoy user |
| General balance | **F1** | Balance both |

---

## 9. Ερωτήσεις Εξετάσεων

### Ερώτηση 1
Confusion matrix:
```
         Pred +  Pred -
Actual +   40      10
Actual -   20      30
```
Ποιο είναι το Precision;

A) 0.40
B) 0.67
C) 0.80
D) 0.50

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 0.67**

**Υπολογισμός**:
```
TP = 40, FP = 20, FN = 10, TN = 30

Precision = TP / (TP + FP) = 40 / (40 + 20) = 40/60 = 0.667
```
</details>

---

### Ερώτηση 2
Με το ίδιο confusion matrix, ποιο είναι το Recall;

A) 0.40
B) 0.67
C) 0.80
D) 0.50

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 0.80**

**Υπολογισμός**:
```
Recall = TP / (TP + FN) = 40 / (40 + 10) = 40/50 = 0.80
```
</details>

---

### Ερώτηση 3
Αν Precision = 0.8 και Recall = 0.6, ποιο είναι το F1 Score;

A) 0.685
B) 0.700
C) 0.657
D) 0.720

<details>
<summary>Απάντηση</summary>

**Σωστό: A) 0.685** (ή περίπου 0.686)

**Υπολογισμός**:
```
F1 = 2 × P × R / (P + R)
   = 2 × 0.8 × 0.6 / (0.8 + 0.6)
   = 0.96 / 1.4
   = 0.686
```
</details>

---

### Ερώτηση 4
Τι σημαίνει AUC = 0.5;

A) Perfect classifier
B) Random classifier
C) Classifier που κάνει πάντα λάθος
D) Classifier με υψηλό recall

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Random classifier**

**Εξήγηση**: AUC = 0.5 σημαίνει ότι η ROC curve είναι η διαγώνιος, δηλαδή ο classifier δεν είναι καλύτερος από random guessing.
</details>

---

### Ερώτηση 5
Σε ποιο σενάριο είναι πιο σημαντικό το Recall από το Precision;

A) Spam filtering
B) Cancer detection
C) Product recommendations
D) Movie rating predictions

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Cancer detection**

**Εξήγηση**: Στην ανίχνευση καρκίνου:
- FN (miss cancer) = πολύ κακό (θάνατος)
- FP (false alarm) = λιγότερο κακό (επιπλέον tests)

Άρα θέλουμε υψηλό Recall για να μη χάσουμε κανέναν ασθενή.
</details>

---

### Ερώτηση 6
Confusion matrix:
```
         Pred +  Pred -
Actual +   95       5
Actual -    5     895
```
Ποιο είναι το Accuracy;

A) 95%
B) 99%
C) 98%
D) 95.5%

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 99%**

**Υπολογισμός**:
```
Accuracy = (TP + TN) / Total = (95 + 895) / 1000 = 990/1000 = 0.99 = 99%
```
</details>

---

### Ερώτηση 7
Ποια είναι η σχέση FPR και Specificity;

A) FPR = Specificity
B) FPR = 1 - Specificity
C) FPR = 1 / Specificity
D) Δεν υπάρχει σχέση

<details>
<summary>Απάντηση</summary>

**Σωστό: B) FPR = 1 - Specificity**

**Εξήγηση**:
```
Specificity = TN / (TN + FP)
FPR = FP / (FP + TN) = 1 - TN/(TN+FP) = 1 - Specificity
```
</details>

---

### Ερώτηση 8
Γιατί είναι προβληματικό να χρησιμοποιούμε μόνο accuracy σε imbalanced datasets;

A) Accuracy είναι πάντα 0
B) Accuracy δεν υπολογίζεται
C) Ένα naive model που προβλέπει πάντα την πλειοψηφία μπορεί να έχει υψηλό accuracy
D) Accuracy δεν λαμβάνει υπόψη τα TN

<details>
<summary>Απάντηση</summary>

**Σωστό: C)**

**Εξήγηση**: Αν έχουμε 99% class A, 1% class B, ένα model που λέει πάντα "A" θα έχει 99% accuracy χωρίς να κάνει τίποτα χρήσιμο για class B.
</details>

---

### Ερώτηση 9
Σε multi-class classification με 3 κλάσεις, macro-average precision:

A) Υπολογίζει precision για κάθε sample και κάνει average
B) Υπολογίζει precision για κάθε class και κάνει average
C) Υπολογίζει global TP/(TP+FP)
D) Χρησιμοποιεί weighted average

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**:
- Macro: υπολογίζει metric για κάθε class, μετά κάνει απλό average
- Micro: aggregate TP, FP, FN across all classes, μετά υπολογίζει

```
Macro = (P_A + P_B + P_C) / 3
```
</details>

---

### Ερώτηση 10
Ποιο metric δίνει περισσότερο βάρος στις minority classes;

A) Micro-average
B) Macro-average
C) Accuracy
D) Weighted F1

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Macro-average**

**Εξήγηση**: Macro-average δίνει ίσο βάρος σε κάθε class, ανεξάρτητα από το μέγεθός της. Έτσι μικρές classes μετράνε το ίδιο με τις μεγάλες.
</details>

---

### Ερώτηση 11 (Υπολογιστική)
TP=80, TN=900, FP=20, FN=20. Υπολόγισε F1.

A) 0.80
B) 0.85
C) 0.89
D) 0.91

<details>
<summary>Απάντηση</summary>

**Σωστό: A) 0.80**

**Υπολογισμός**:
```
Method 1:
Precision = 80/(80+20) = 0.80
Recall = 80/(80+20) = 0.80
F1 = 2×0.80×0.80/(0.80+0.80) = 1.28/1.60 = 0.80

Method 2:
F1 = 2×TP / (2×TP + FP + FN)
   = 2×80 / (160 + 20 + 20)
   = 160/200 = 0.80
```
</details>

---

## 10. Σύνοψη - Key Points

### Confusion Matrix

```
         Pred +  Pred -
Actual +   TP      FN     ← Actual Positives
Actual -   FP      TN     ← Actual Negatives
           ↑       ↑
   Pred Positives  Pred Negatives
```

### Τύποι (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

| Metric | Formula | Ερώτηση που απαντάει |
|--------|---------|----------------------|
| **Accuracy** | (TP+TN)/(TP+TN+FP+FN) | "Πόσα σωστά συνολικά;" |
| **Precision** | TP/(TP+FP) | "Από τα predicted +, πόσα σωστά;" |
| **Recall** | TP/(TP+FN) | "Από τα actual +, πόσα βρήκα;" |
| **Specificity** | TN/(TN+FP) | "Από τα actual -, πόσα βρήκα;" |
| **F1** | 2PR/(P+R) | "Balance Precision & Recall" |
| **FPR** | FP/(FP+TN) | "False alarm rate" |

### ROC/AUC

```
ROC: Plot TPR vs FPR για διάφορα thresholds
AUC = 1.0: Perfect
AUC = 0.5: Random
AUC < 0.5: Worse than random
```

### Trade-offs

```
↑ Threshold → ↑ Precision, ↓ Recall
↓ Threshold → ↓ Precision, ↑ Recall

Cancer detection → Optimize Recall (don't miss!)
Spam filter → Optimize Precision (don't lose emails!)
Balanced → Optimize F1
```
