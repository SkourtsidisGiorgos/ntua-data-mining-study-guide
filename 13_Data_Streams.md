# Mining Data Streams - Πλήρης Οδηγός Μελέτης

## 1. Τι είναι τα Data Streams

### Ορισμός
**Data Stream**: Συνεχής συσσώρευση δεδομένων στο χρόνο
- Συνήθως με **μεγάλους ρυθμούς** άφιξης
- **Αδύνατο** ή **μη πρακτικό** να αποθηκεύσουμε όλα τα δεδομένα
- Περιορισμοί πόρων (memory, storage, processing)

### Παραδείγματα Data Streams

| Τύπος | Παράδειγμα |
|-------|------------|
| **Transactions** | Credit cards, Online purchases |
| **Clickstreams** | User activity σε website |
| **Social Streams** | Trending topics στο Twitter/X |
| **Network Streams** | Network traffic, intrusion detection |
| **Sensor Data** | IoT devices, weather stations |

---

## 2. Προκλήσεις στο Mining Data Streams

### 2.1 One-Pass Constraint
```
Κάθε data sample μπορεί να επεξεργαστεί ΜΟΝΟ ΜΙΑ ΦΟΡΑ

Πρόβλημα: Οι περισσότεροι data mining αλγόριθμοι είναι iterative
         και απαιτούν πολλαπλά passes πάνω στα δεδομένα
```

### 2.2 Concept Drift
```
Εξέλιξη των δεδομένων στο χρόνο:
- Αλλαγή στατιστικών ιδιοτήτων
- Αλλαγή correlations μεταξύ attributes
- Τα παλιά patterns μπορεί να μην ισχύουν πλέον
```

### 2.3 Resource Constraints
```
- Δεν ελέγχουμε τη διαδικασία δημιουργίας δεδομένων
- Τα δεδομένα μπορεί να φτάνουν με ρυθμό που δεν μπορούμε να επεξεργαστούμε
- Load shedding: Απορρίπτουμε samples που δεν προλαβαίνουμε
```

### 2.4 Massive-Domain Constraints
```
- Μεγάλος αριθμός distinct values
- Παράδειγμα: IP addresses σε network stream analysis
- Δυσκολία ακόμα και σε απλές στατιστικές (distinct count)
```

---

## 3. Synopsis Data Structures

### Γιατί χρειαζόμαστε Synopsis
Λόγω του μεγάλου όγκου, **όλες** οι streaming μέθοδοι δημιουργούν **online synopsis** των δεδομένων.

### Τύποι Synopsis

| Τύπος | Περιγραφή | Χρήση |
|-------|-----------|-------|
| **Generic** | Random sampling (reservoir) | General purpose |
| **Specific** | Για συγκεκριμένες εργασίες | Distinct/Frequent counting |

---

## 4. Reservoir Sampling

### Ορισμός
Μέθοδος για διατήρηση **uniform random sample** μεγέθους k από data stream.

### Πρόβλημα
```
- Δεν μπορούμε να αποθηκεύσουμε όλα τα δεδομένα και μετά να κάνουμε sample
- Πρέπει να διατηρούμε δυναμικά ένα sample μεγέθους k
- Static case: probability = k/n
- Στα streams το n συνεχώς αυξάνεται!
```

### Αλγόριθμος Reservoir Sampling

```python
# Reservoir Sampling Algorithm
def reservoir_sampling(stream, k):
    reservoir = []

    for n, item in enumerate(stream, 1):
        if n <= k:
            # Πρώτα k στοιχεία: βάλε τα κατευθείαν
            reservoir.append(item)
        else:
            # n-th στοιχείο: βάλε με πιθανότητα k/n
            j = random.randint(1, n)
            if j <= k:
                # Αντικατέστησε τυχαίο στοιχείο
                reservoir[j-1] = item

    return reservoir
```

### Βήματα
1. **Insert** το n-th data point με πιθανότητα **k/n**
2. Αν γίνει insertion, **eject** ένα από τα παλιά k points με πιθανότητα **1/k**

### Ιδιότητα
Μετά από n stream points, η πιθανότητα κάθε point να είναι στο reservoir = **k/n**

---

## 5. Sampling with Decay (για Concept Drift)

### Πρόβλημα με Reservoir Sampling
```
Reservoir sampling ΔΕΝ χειρίζεται concept drift:
- Data points επιλέγονται uniformly χωρίς decay
- Σε πολλές εφαρμογές, τα πιο πρόσφατα δεδομένα είναι πιο σημαντικά
```

### Λύση: Bias Function
Εισαγωγή **decay framework** με bias function f(r, n):
- p(r, n): πιθανότητα το r-th data point να είναι στο reservoir όταν φτάνει το n-th
- p(r, n) ∝ f(r, n)

### Exponential Bias Function
```
f(r, n) = e^(-λ(n-r))

- λ: bias rate, συνήθως λ ∈ [0,1]
- λ = 0: unbiased case (standard reservoir)
- Memoryless function
```

### Maximum Reservoir Size
```
k < 1/λ
```

---

## 6. Bloom Filters

### Τι κάνουν
Απαντούν αν ένα στοιχείο **υπάρχει** σε ένα set (set-membership query).

### Χαρακτηριστικά

| Χαρακτηριστικό | Τιμή |
|----------------|------|
| **False Positives** | Πιθανά |
| **False Negatives** | **ΑΔΥΝΑΤΑ** |

```
ΚΡΙΣΙΜΟ: Αν το Bloom Filter λέει ότι ένα στοιχείο ΔΕΝ υπάρχει,
         τότε ΣΙΓΟΥΡΑ δεν υπάρχει!
```

### Δομή Bloom Filter
1. **Binary bit array** μήκους m
2. **w independent hash functions** h₁(x), h₂(x), ..., hᵥ(x)
   - Κάθε hash function maps element → integer σε [0, m-1]

### Λειτουργία

**Initialization:**
```
Όλα τα m bits αρχικοποιούνται σε 0
```

**Insert element x:**
```python
for i in range(w):
    index = h_i(x)
    bloom_filter[index] = 1  # Set bit to 1
# Bits που είναι ήδη 1 δεν γυρίζουν πίσω σε 0 (collision)
```

**Check if y exists:**
```python
for i in range(w):
    index = h_i(y)
    if bloom_filter[index] == 0:
        return False  # ΣΙΓΟΥΡΑ δεν υπάρχει
return True  # Πιθανώς υπάρχει (may be false positive)
```

### Διάγραμμα Bloom Filter

```
Element x hashes to positions: h₁(x)=1, h₂(x)=4, h₃(x)=7, h₄(x)=11

Bloom Filter (m=12):
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 0 │ 1 │ 0 │ 0 │ 1 │ 0 │ 0 │ 1 │ 0 │ 0 │ 0 │ 1 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
  0   1   2   3   4   5   6   7   8   9  10  11

Check y: if ALL h_i(y) positions are 1 → "probably yes"
         if ANY h_i(y) position is 0 → "definitely no"
```

### False Positive Probability

```
F = (1 - e^(-nw/m))^w

Minimized when: w = (m/n) × ln(2)
Then: F = 2^(-m×ln(2)/n)
```

### Bloom Filter Size

```
Για fixed false positive rate F:
m = (ln(1/F) - ln(2) - 1) × n

Όπου n = αριθμός distinct elements
```

### Ιδιότητες Bloom Filters
1. **Cascade**: Μπορούν να χρησιμοποιηθούν σε cascade (logical AND)
2. **Approximate distinct count**: N ≈ (m × ln(m/m₀)) / w
3. **Union/Intersection**: Logical OR για union πολλαπλών streams
4. **Speed**: Πολύ γρήγορα - bit-level operations

---

## 7. Count-Min Sketches

### Τι είναι
**Επέκταση** των Bloom Filters που υποστηρίζει **count-based summaries**.

### Δομή
- w **numeric arrays**, κάθε ένα μήκους m
- Κάθε array αντιστοιχεί σε hash function hᵢ(·)

```
Count-Min Sketch (w=4, m=8):

h₁(·) → │ 0 │ 3 │ 1 │ 5 │ 2 │ 0 │ 1 │ 0 │
h₂(·) → │ 1 │ 0 │ 4 │ 2 │ 0 │ 3 │ 1 │ 2 │
h₃(·) → │ 0 │ 2 │ 0 │ 1 │ 3 │ 0 │ 2 │ 1 │
h₄(·) → │ 2 │ 1 │ 3 │ 0 │ 1 │ 2 │ 0 │ 4 │
```

### Λειτουργία

**Initialization:**
```
Όλα τα m×w cells αρχικοποιούνται σε 0
```

**Insert element x:**
```python
for i in range(w):
    index = h_i(x)
    count_min[i][index] += 1  # Increment counter
```

**Query frequency of y:**
```python
def estimate_frequency(y):
    values = [count_min[i][h_i(y)] for i in range(w)]
    return min(values)  # Return MINIMUM value
```

### Γιατί Minimum;
- Κάθε Vᵢ(y) μπορεί να **overestimate** τη συχνότητα λόγω collisions
- Το **minimum** είναι η καλύτερη εκτίμηση

### Estimation Quality

**Για streams με θετικές συχνότητες:**
```
Με πιθανότητα 1 - e^(-w):
E(y) ≤ G(y) + (n_f × e) / m

Όπου:
- E(y): estimated frequency
- G(y): actual frequency
- n_f: total frequencies so far
```

---

## 8. Flajolet-Martin Algorithm

### Χρήση
**Distinct element counting** σε streams με πολλά infrequent items.

### Ιδέα
```
1. Hash function h(·) → binary representation (L bits, usually 64)
2. R = αριθμός least significant bits που είναι 0
3. R_max = maximum R recorded so far
4. Distinct elements ≈ 2^R_max
```

### Γιατί δουλεύει
```
- Πιθανότητα hash να τελειώνει σε 0: 1/2
- Πιθανότητα hash να τελειώνει σε 00: 1/4
- Πιθανότητα hash να τελειώνει σε 000: 1/8
- ...
- Πιθανότητα για R trailing zeros: 1/2^R

Άρα αν είδαμε R_max trailing zeros, περίπου 2^R_max distinct elements
```

---

## 9. Σύγκριση Data Structures

| Structure | Χρήση | False Positives | False Negatives |
|-----------|-------|-----------------|-----------------|
| **Bloom Filter** | Set membership | Ναι | Όχι |
| **Count-Min Sketch** | Frequency counting | Overestimates | - |
| **Flajolet-Martin** | Distinct counting | - | - |
| **AMS Sketch** | Second moments (variance) | - | - |

---

## 10. Clustering σε Data Streams

### STREAM Algorithm
Προσαρμογή k-means για data streams.

**Βήματα:**
1. Διαίρεσε stream σε segments μεγέθους m (χωράει στη memory)
2. Εφάρμοσε k-means σε κάθε segment
3. Κράτα τα k centers με weights (αριθμός assigned points)
4. Όταν kr > m, πέρασε σε 2nd clustering level

### CluStream Algorithm
Χειρίζεται **concept drift** (σε αντίθεση με STREAM).

**Two-stage methodology:**
1. **Microclustering** (online): Εξαγωγή λεπτομερών στατιστικών για clusters
2. **Macroclustering** (offline): Aggregation των clusters

---

## 11. Frequent Pattern Mining σε Streams

### Lossy Counting Algorithm

**Ιδέα:**
1. Χώρισε το stream σε segments μεγέθους w = ⌊1/ε⌋
2. Μέτρα συχνότητες κατά τη διάρκεια κάθε segment
3. Στο boundary: απόρριψε infrequent items
4. Repeat

```
ε = desired accuracy (hyperparameter)
```

---

## 12. Outlier Detection σε Streams

### Τύποι Outliers

| Τύπος | Περιγραφή | Παράδειγμα |
|-------|-----------|------------|
| **Individual records** | Novelty detection | First article about an event |
| **Aggregate trends** | Change detection | Spike in network traffic |

### Μέθοδοι
1. **Proximity-based** σε windows: k-nearest neighbors
2. **Clustering-based**: Δημιουργία νέου cluster = potential outlier
3. **Velocity density estimation**: Detect concept drift

---

## 13. Classification σε Streams

### Offline Mode
1. Δημιούργησε representative sample (reservoir sampling)
2. Εφάρμοσε standard classification algorithm

### Online Mode - Very Fast Decision Trees (VFDT)
- Βασίζεται σε **Hoeffding Trees**
- Δημιουργεί tree με sampling
- **Hoeffding bound** εγγυάται ποιότητα
- **Υπόθεση**: Δεν υπάρχει concept drift

---

## 14. Ερωτήσεις Εξετάσεων

### Ερώτηση 1: Bloom Filter Properties
```
Q: Which of the following is TRUE about Bloom Filters?

a) False negatives are possible but false positives are not
b) False positives are possible but false negatives are not ✓
c) Both false positives and false negatives are possible
d) Neither false positives nor false negatives are possible

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Bloom Filters μπορούν να πουν "probably yes" (false positive)
         αλλά αν πουν "no" είναι ΣΙΓΟΥΡΑ σωστό (no false negatives)
```

### Ερώτηση 2: Reservoir Sampling
```
Q: In reservoir sampling with reservoir size k, what is the probability
   of including the n-th element in the reservoir?

a) k/n ✓
b) n/k
c) 1/k
d) 1/n

ΑΠΑΝΤΗΣΗ: A
```

### Ερώτηση 3: Challenges in Stream Mining
```
Q: Which is NOT a challenge in mining data streams?

a) One-pass constraint
b) Concept drift
c) Resource constraints
d) Multiple passes over data ✓

ΑΠΑΝΤΗΣΗ: D
ΕΞΗΓΗΣΗ: Multiple passes είναι αυτό που ΔΕΝ μπορούμε να κάνουμε σε streams
```

### Ερώτηση 4: Count-Min Sketch
```
Q: In Count-Min Sketch, why do we take the MINIMUM value from all
   hash function counters?

a) To maximize accuracy
b) Because collisions can only increase counts, never decrease ✓
c) For faster computation
d) To save memory

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Collisions προκαλούν overestimation, άρα το minimum
         είναι η πιο ακριβής εκτίμηση
```

### Ερώτηση 5: Concept Drift
```
Q: Which sampling method can handle concept drift?

a) Standard reservoir sampling
b) Sampling with exponential decay ✓
c) Simple random sampling
d) Stratified sampling

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 6: Flajolet-Martin
```
Q: The Flajolet-Martin algorithm is used for:

a) Set membership queries
b) Frequency counting
c) Distinct element counting ✓
d) Pattern mining

ΑΠΑΝΤΗΣΗ: C
```

---

## 15. Σύνοψη - Key Points για Εξετάσεις

### Data Stream Challenges (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)
```
1. One-pass constraint: Κάθε δεδομένο επεξεργάζεται ΜΟΝΟ ΜΙΑ ΦΟΡΑ
2. Concept Drift: Τα δεδομένα αλλάζουν στατιστικές ιδιότητες με το χρόνο
3. Resource Constraints: Limited memory/storage/processing
4. Massive-Domain: Πολλές distinct τιμές (π.χ. IP addresses)
```

### Bloom Filter (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)
```
- Set membership query: "Has element x appeared?"
- FALSE POSITIVES: Πιθανά (collisions)
- FALSE NEGATIVES: ΑΔΥΝΑΤΑ
- Αν λέει "ΟΧΙ" → ΣΙΓΟΥΡΑ δεν υπάρχει
```

### Count-Min Sketch vs Bloom Filter
```
Bloom Filter: Binary (exists/not exists)
Count-Min:    Counts (how many times)
```

### Reservoir Sampling Formula
```
Probability of n-th element being in reservoir = k/n
```

### Algorithms Summary

| Algorithm | Purpose | Handles Drift? |
|-----------|---------|----------------|
| Reservoir Sampling | Random sample | No |
| Sampling with Decay | Biased sample | Yes |
| Bloom Filter | Set membership | - |
| Count-Min Sketch | Frequency count | - |
| Flajolet-Martin | Distinct count | - |
| STREAM | Clustering | No |
| CluStream | Clustering | Yes |
| VFDT | Classification | No |

### Quick Reference

| Θέλω να κάνω | Χρησιμοποιώ |
|--------------|-------------|
| Random sample από stream | Reservoir Sampling |
| Sample με recency bias | Sampling with Decay |
| Check αν είδα element x | Bloom Filter |
| Μέτρα πόσες φορές είδα x | Count-Min Sketch |
| Μέτρα distinct elements | Flajolet-Martin |
| Clustering | STREAM/CluStream |
| Classification | VFDT |

