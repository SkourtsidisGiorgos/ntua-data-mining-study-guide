# Exam Simulation 2 - Data Mining NTUA

## Οδηγίες
- Χρόνος: 2.5 ώρες
- 65 multiple choice (1 βαθμός έκαστη)
- 5 ανοιχτές ερωτήσεις (7 βαθμοί έκαστη)
- Σύνολο: 100 βαθμοί

**Σημείωσε τις απαντήσεις σου εδώ:**

| 1-10 | 11-20 | 21-30 | 31-40 | 41-50 | 51-60 | 61-65 |
|------|-------|-------|-------|-------|-------|-------|
| 1: _ | 11: _ | 21: _ | 31: _ | 41: _ | 51: _ | 61: _ |
| 2: _ | 12: _ | 22: _ | 32: _ | 42: _ | 52: _ | 62: _ |
| 3: _ | 13: _ | 23: _ | 33: _ | 43: _ | 53: _ | 63: _ |
| 4: _ | 14: _ | 24: _ | 34: _ | 44: _ | 54: _ | 64: _ |
| 5: _ | 15: _ | 25: _ | 35: _ | 45: _ | 55: _ | 65: _ |
| 6: _ | 16: _ | 26: _ | 36: _ | 46: _ | 56: _ |       |
| 7: _ | 17: _ | 27: _ | 37: _ | 47: _ | 57: _ |       |
| 8: _ | 18: _ | 28: _ | 38: _ | 48: _ | 58: _ |       |
| 9: _ | 19: _ | 29: _ | 39: _ | 49: _ | 59: _ |       |
| 10: _ | 20: _ | 30: _ | 40: _ | 50: _ | 60: _ |       |

---

# ΜΕΡΟΣ Α: Multiple Choice (65 ερωτήσεις)

## Section 1: OLAP & Data Warehousing (Q1-10)

### Q1
Ένα data cube με 5 dimensions (χωρίς ιεραρχίες) έχει πόσα cuboids;
- A) 5
- B) 10
- C) 25
- D) 32

### Q2
Dimensions: Product (3 levels), Time (4 levels), Location (2 levels). Πόσα cuboids;
- A) 9
- B) 12
- C) 24
- D) 64

### Q3
Ποια OLAP operation μετατρέπει "Sales by Day" σε "Sales by Month";
- A) Slice
- B) Drill-down
- C) Roll-up
- D) Pivot

### Q4
Slice operation φιλτράρει σε:
- A) Μία dimension
- B) Δύο dimensions
- C) Όλες τις dimensions
- D) Καμία dimension

### Q5
Star schema vs Snowflake: Ποιο έχει πιο γρήγορα queries;
- A) Snowflake
- B) Star
- C) Ίδια ταχύτητα
- D) Εξαρτάται από τα indexes

### Q6
C(p5, *, t3) σε data cube notation σημαίνει:
- A) Aggregation σε time
- B) Aggregation σε product
- C) Aggregation σε customer
- D) Καμία aggregation

### Q7
Base cuboid με 20 products, 10 stores, 365 days έχει πόσα cells;
- A) 395
- B) 7,300
- C) 73,000
- D) 730,000

### Q8
Γιατί δεν τρέχουμε OLAP queries σε OLTP systems;
- A) Δεν υποστηρίζεται η SQL
- B) Θα επιβραδύνουν τα transactions
- C) Απαιτούν NoSQL
- D) Δεν υπάρχει αρκετή μνήμη

### Q9
Fact table περιέχει:
- A) Descriptive attributes
- B) Measures/metrics
- C) Primary keys μόνο
- D) Foreign keys μόνο

### Q10
Drill-down operation:
- A) Αυξάνει το επίπεδο λεπτομέρειας
- B) Μειώνει το επίπεδο λεπτομέρειας
- C) Φιλτράρει δεδομένα
- D) Περιστρέφει άξονες

---

## Section 2: Decision Trees (Q11-20)

### Q11
Dataset: 8 Yes, 2 No. Entropy = ?
- A) 0
- B) 0.469
- C) 0.722
- D) 1.0

### Q12
Information Gain μετράει:
- A) Το συνολικό entropy
- B) Τη μείωση του entropy μετά το split
- C) Τον αριθμό των nodes
- D) Το βάθος του tree

### Q13
ID3 χρησιμοποιεί ποιο criterion;
- A) Gini Index
- B) Gain Ratio
- C) Information Gain
- D) Chi-squared

### Q14
C4.5 διαφέρει από ID3 γιατί χρησιμοποιεί:
- A) Gini Index
- B) Gain Ratio
- C) MSE
- D) MAE

### Q15
Gini Index = 0 σημαίνει:
- A) Maximum impurity
- B) Pure node (μία κλάση)
- C) 50-50 split
- D) Error

### Q16
Entropy = 1 (για 2 κλάσεις) σημαίνει:
- A) Pure node
- B) Maximum uncertainty
- C) Empty node
- D) Root node

### Q17
Pruning σκοπός:
- A) Αύξηση accuracy στο training set
- B) Μείωση overfitting
- C) Αύξηση depth
- D) Faster training

### Q18
CART χρησιμοποιεί:
- A) Multi-way splits
- B) Binary splits μόνο
- C) Ternary splits
- D) Random splits

### Q19
Αν attribute A έχει 100 unique values, ID3:
- A) Θα το αγνοήσει
- B) Θα το ευνοήσει λόγω υψηλού IG
- C) Θα κάνει error
- D) Θα το χρησιμοποιήσει μόνο στο root

### Q20
Post-pruning:
- A) Σταματάει νωρίς το growing
- B) Χτίζει πρώτα το πλήρες tree, μετά κόβει
- C) Δεν αφαιρεί κόμβους
- D) Αυξάνει το depth

---

## Section 3: Clustering (Q21-30)

### Q21
K-means convergence criterion:
- A) Όταν k=0
- B) Όταν τα centroids δεν αλλάζουν
- C) Μετά από 10 iterations
- D) Όταν όλα τα points είναι σε ένα cluster

### Q22
DBSCAN με ε=2, MinPts=4. Point P έχει 3 neighbors (εκτός εαυτού). P είναι:
- A) Core point
- B) Border point (αν γειτονεύει με core)
- C) Noise point (αν δεν γειτονεύει με core)
- D) B ή C

### Q23
K-means πλεονέκτημα:
- A) Βρίσκει arbitrary shape clusters
- B) Δεν χρειάζεται k
- C) Γρήγορος και scalable
- D) Robust σε outliers

### Q24
DBSCAN πλεονέκτημα:
- A) Πρέπει να ορίσεις k
- B) Μόνο spherical clusters
- C) Βρίσκει arbitrary shapes
- D) Πιο γρήγορος από K-means

### Q25
Core point στο DBSCAN:
- A) |N(p)| > MinPts
- B) |N(p)| ≥ MinPts
- C) |N(p)| < MinPts
- D) |N(p)| = 0

### Q26
K-means++:
- A) Χρησιμοποιεί DBSCAN για initialization
- B) Επιλέγει αρχικά centroids πιο έξυπνα
- C) Είναι πιο αργός από K-means
- D) Δεν χρειάζεται k

### Q27
Noise point στο DBSCAN:
- A) Είναι core point χωρίς neighbors
- B) Δεν είναι ούτε core ούτε border
- C) Έχει ακριβώς MinPts neighbors
- D) Είναι πάντα outlier του dataset

### Q28
K-means centroid update:
- A) Median
- B) Mode
- C) Mean
- D) Max

### Q29
Αν αυξήσουμε το ε στο DBSCAN:
- A) Περισσότερα clusters
- B) Λιγότερα clusters
- C) Περισσότερα noise points
- D) Δεν επηρεάζεται

### Q30
K-means αδυναμία:
- A) Scalability
- B) Ευαισθησία σε initialization
- C) Πολυπλοκότητα
- D) Speed

---

## Section 4: Association Rules (Q31-40)

### Q31
100 transactions, 45 contain {A,B}, 60 contain {A}. Confidence(A→B) = ?
- A) 0.45
- B) 0.60
- C) 0.75
- D) 1.33

### Q32
Support({X}) μετράει:
- A) Confidence
- B) Συχνότητα εμφάνισης του X
- C) Lift
- D) Correlation

### Q33
Lift = 1 σημαίνει:
- A) Τέλεια θετική correlation
- B) Τέλεια αρνητική correlation
- C) Ανεξαρτησία
- D) Error

### Q34
Apriori principle:
- A) Supersets of frequent είναι frequent
- B) Subsets of frequent είναι frequent
- C) Frequent items έχουν υψηλό confidence
- D) Lift > 1 πάντα

### Q35
L₂ = {{A,B}, {A,C}, {A,D}}. Valid 3-candidates:
- A) {A,B,C}, {A,B,D}, {A,C,D}
- B) Κανένα (missing {B,C}, {B,D}, {C,D})
- C) {A,B,C} μόνο
- D) Όλα τα combinations

### Q36
Lift > 1 σημαίνει:
- A) Αρνητική correlation
- B) Θετική correlation
- C) Ανεξαρτησία
- D) Low support

### Q37
Από 4-itemset πόσα rules μπορούν να παραχθούν;
- A) 4
- B) 8
- C) 14
- D) 16

### Q38
FP-Growth vs Apriori:
- A) FP-Growth σαρώνει περισσότερες φορές
- B) Apriori είναι πιο γρήγορος
- C) FP-Growth σαρώνει 2 φορές μόνο
- D) Ίδια performance

### Q39
min_sup = 5%, 1000 transactions. Itemset πρέπει να είναι σε:
- A) ≥5 transactions
- B) ≥50 transactions
- C) ≥500 transactions
- D) =50 transactions ακριβώς

### Q40
Confidence(A→B) ≠ Confidence(B→A) γιατί:
- A) Support(A) ≠ Support(B) συνήθως
- B) Είναι το ίδιο πάντα
- C) Lift διαφέρει
- D) Error στον τύπο

---

## Section 5: DTW & Similarity (Q41-48)

### Q41
Euclidean distance μεταξύ (0,0,0) και (3,4,0):
- A) 5
- B) 7
- C) 12
- D) 25

### Q42
Manhattan distance μεταξύ (1,1) και (4,5):
- A) 5
- B) 7
- C) 12
- D) √41

### Q43
Cosine similarity = 0 σημαίνει:
- A) Identical vectors
- B) Orthogonal vectors
- C) Opposite vectors
- D) Error

### Q44
DTW vs Euclidean:
- A) DTW πιο γρήγορο
- B) DTW handles time warping
- C) Euclidean πιο ακριβές
- D) Ίδια αποτελέσματα

### Q45
DTW base case: DTW(0,0) = ?
- A) ∞
- B) 0
- C) 1
- D) Undefined

### Q46
Jaccard similarity μεταξύ {1,2,3} και {2,3,4,5}:
- A) 0.25
- B) 0.40
- C) 0.50
- D) 0.67

### Q47
DTW(i,j) χρησιμοποιεί:
- A) Μόνο diagonal
- B) Diagonal, horizontal, vertical
- C) Random paths
- D) Shortest path μόνο

### Q48
Cosine similarity range για TF-IDF vectors:
- A) [-1, 1]
- B) [0, 1]
- C) [0, ∞)
- D) (-∞, ∞)

---

## Section 6: Classification Metrics (Q49-55)

### Q49
TP=80, TN=10, FP=5, FN=5. Accuracy = ?
- A) 0.80
- B) 0.85
- C) 0.90
- D) 0.95

### Q50
Precision = TP / (TP + ?):
- A) TN
- B) FP
- C) FN
- D) TP

### Q51
F1 score είναι:
- A) Arithmetic mean of P and R
- B) Geometric mean of P and R
- C) Harmonic mean of P and R
- D) Weighted sum

### Q52
AUC = 0.5 σημαίνει:
- A) Perfect classifier
- B) Random classifier
- C) Worst classifier
- D) Good classifier

### Q53
Recall = ?
- A) TP / (TP + TN)
- B) TP / (TP + FP)
- C) TP / (TP + FN)
- D) TN / (TN + FP)

### Q54
Cancer detection - optimize:
- A) Precision
- B) Recall
- C) Specificity
- D) Accuracy

### Q55
FPR = 1 - ?:
- A) Recall
- B) Precision
- C) Specificity
- D) F1

---

## Section 7: Bayesian & Privacy & TF-IDF (Q56-65)

### Q56
P(A)=0.4, P(B|A)=0.5, P(B|¬A)=0.2. P(A|B) = ?
- A) 0.20
- B) 0.50
- C) 0.63
- D) 0.80

### Q57
Naive Bayes υποθέτει:
- A) Uniform prior
- B) Features conditionally independent given class
- C) No prior
- D) Features always dependent

### Q58
V-structure A→C←B χωρίς evidence. A ⊥ B?
- A) Ναι
- B) Όχι
- C) Εξαρτάται
- D) Πάντα dependent

### Q59
K-anonymity με k=5 απαιτεί:
- A) Ακριβώς 5 records ανά class
- B) ≥5 records ανά equivalence class
- C) ≤5 records
- D) 5 distinct sensitive values

### Q60
L-diversity διορθώνει ποια αδυναμία του k-anonymity;
- A) Re-identification
- B) Homogeneity attack
- C) Slow queries
- D) Large tables

### Q61
Quasi-identifier είναι:
- A) Primary key
- B) Sensitive attribute
- C) Attribute που μαζί με άλλα μπορεί να ταυτοποιήσει
- D) Foreign key

### Q62
TF("data") = 5, IDF("data") = 2. TF-IDF = ?
- A) 2.5
- B) 7
- C) 10
- D) 25

### Q63
IDF υψηλό όταν:
- A) Λέξη πολύ κοινή
- B) Λέξη σπάνια στο corpus
- C) TF υψηλό
- D) Document μεγάλο

### Q64
Λέξη σε όλα τα documents. IDF = ?
- A) 0
- B) 1
- C) N
- D) log(N)

### Q65
Bag of Words αγνοεί:
- A) Word frequency
- B) Word order
- C) Vocabulary
- D) Document ID

---

# ΜΕΡΟΣ Β: Ανοιχτές Ερωτήσεις (5 × 7 = 35 βαθμοί)

## Ερώτηση 1 (7 βαθμοί): SQL & MapReduce

Δίνεται πίνακας `Sales(product_id, store_id, date, amount)`.

**A)** Γράψε SQL query που βρίσκει το συνολικό amount ανά store, μόνο για stores με total > 10000.

**B)** Γράψε MapReduce pseudocode για την ίδια λειτουργία.

---

## Ερώτηση 2 (7 βαθμοί): Decision Tree

Δίνεται dataset:
| Outlook | Humidity | Play |
|---------|----------|------|
| Sunny | High | No |
| Sunny | High | No |
| Sunny | Normal | Yes |
| Rain | High | Yes |
| Rain | Normal | Yes |
| Rain | Normal | No |

**A)** Υπολόγισε το Entropy του συνόλου S.

**B)** Υπολόγισε το Information Gain για το attribute "Outlook".

**C)** Ποιο attribute θα επιλέξει ο ID3 ως root;

---

## Ερώτηση 3 (7 βαθμοί): DBSCAN

Δίνονται σημεία: A(0,0), B(1,0), C(0,1), D(1,1), E(5,5), F(6,5), G(10,10)

ε = 1.5, MinPts = 3

**A)** Υπολόγισε τη γειτονιά N(p) για κάθε σημείο.

**B)** Χαρακτήρισε κάθε σημείο ως Core, Border, ή Noise.

**C)** Προσδιόρισε τα clusters.

---

## Ερώτηση 4 (7 βαθμοί): DTW

Sequences: X = [2, 4, 3], Y = [1, 3]

Distance function: d(xᵢ, yⱼ) = |xᵢ - yⱼ|

**A)** Κατασκεύασε τον πίνακα cost d(xᵢ, yⱼ).

**B)** Υπολόγισε τον πίνακα DTW.

**C)** Βρες το DTW distance και το optimal warping path.

---

## Ερώτηση 5 (7 βαθμοί): Apriori

Transactions:
```
T1: {A, B, C}
T2: {A, C}
T3: {A, B}
T4: {B, C, D}
T5: {A, B, C}
```

min_sup = 40%

**A)** Βρες L₁ (frequent 1-itemsets).

**B)** Βρες L₂ (frequent 2-itemsets).

**C)** Γράψε δύο association rules με confidence > 50%.

---

# Τέλος Εξέτασης

**Έλεγξε τις απαντήσεις σου!**

Χρησιμοποίησε το αρχείο `24_Exam_Simulation_2_Solutions.md` για τις λύσεις.
