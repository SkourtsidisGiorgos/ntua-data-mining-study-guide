# MapReduce - Πλήρης Οδηγός Μελέτης

## 1. Τι είναι το MapReduce

### Ορισμός
- **Distributed computing model** για επεξεργασία μεγάλων datasets
- Λειτουργεί με **<key, value> pairs**
- Αυτόματος διαμοιρασμός σε πολλαπλά nodes

### Βασική Ιδέα
```
Input Data → Split → Map → Shuffle & Sort → Reduce → Output
```

- **Parallelism**: Πολλοί Mappers τρέχουν ταυτόχρονα
- **Fault tolerance**: Αν αποτύχει ένα node, το task ξανατρέχει αλλού

---

## 2. Components

### 2.1 Mapper
- **Input**: <key, value> pair (π.χ. <line_number, text>)
- **Output**: Λίστα από <key, value> pairs
- **Λειτουργία**: Εξάγει/μετασχηματίζει δεδομένα

```
Map(key, value) → list(<key', value'>)
```

### 2.2 Combiner (Optional)
- **Mini-reducer** που τρέχει τοπικά στον ίδιο node με τον Mapper
- **Σκοπός**: Μείωση δεδομένων που μεταφέρονται στο δίκτυο
- **ΠΡΟΣΟΧΗ**: Δεν αλλάζει το αποτέλεσμα (πρέπει να είναι associative & commutative)

```
Combiner(key, list(values)) → <key, partial_aggregate>
```

### 2.3 Partitioner
- **Λειτουργία**: Αποφασίζει ποιος Reducer θα λάβει κάθε key
- **Default**: Hash partitioning: `hash(key) mod num_reducers`
- Εξασφαλίζει ότι **ίδια keys πηγαίνουν στον ίδιο Reducer**

### 2.4 Reducer
- **Input**: <key, list(values)> - όλες οι τιμές για ένα key
- **Output**: <key, final_value>
- **Λειτουργία**: Aggregation/συνδυασμός τιμών

```
Reduce(key, list(values)) → list(<key', value'>)
```

---

## 3. Data Flow Sequence

### ⚠️ ΚΡΙΣΙΜΟ ΓΙΑ ΕΞΕΤΑΣΕΙΣ

**Σωστή Σειρά: 1 → 2 → 4 → 3**

| Βήμα | Component | Περιγραφή |
|------|-----------|-----------|
| 1 | **Mapper** | Επεξεργασία input, emit <k,v> |
| 2 | **Combiner** | Local aggregation (optional) |
| 4 | **Partitioner** | Διαμοιρασμός σε Reducers |
| 3 | **Reducer** | Final aggregation |

### Αναλυτικό Διάγραμμα

```
┌─────────────────────────────────────────────────────────────────┐
│                         INPUT DATA                               │
│              (split σε chunks για κάθε Mapper)                   │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌─────────┐     ┌─────────┐     ┌─────────┐
        │ MAPPER 1│     │ MAPPER 2│     │ MAPPER 3│
        │  (1)    │     │  (1)    │     │  (1)    │
        └────┬────┘     └────┬────┘     └────┬────┘
             │               │               │
        ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
        │COMBINER │     │COMBINER │     │COMBINER │
        │  (2)    │     │  (2)    │     │  (2)    │
        └────┬────┘     └────┬────┘     └────┬────┘
             │               │               │
             └───────────────┼───────────────┘
                             │
                    ┌────────▼────────┐
                    │   PARTITIONER   │
                    │      (4)        │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ REDUCER 1│  │ REDUCER 2│  │ REDUCER 3│
        │   (3)    │  │   (3)    │  │   (3)    │
        └────┬─────┘  └────┬─────┘  └────┬─────┘
             │              │              │
             ▼              ▼              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        OUTPUT DATA                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Hadoop Components

### HDFS (Hadoop Distributed File System)

| Component | Ρόλος |
|-----------|-------|
| **NameNode** | Αποθηκεύει **metadata** (file names, locations, permissions) |
| **DataNode** | Αποθηκεύει τα **actual data blocks** |

- **NameNode** = Single point of failure (συνήθως έχει Secondary NameNode)
- **DataNode** = Πολλαπλά, για redundancy

### MapReduce Framework

| Component | Ρόλος |
|-----------|-------|
| **JobTracker** | **Schedules** τα MapReduce jobs ⚠️ ΣΗΜΑΝΤΙΚΟ |
| **TaskTracker** | **Executes** τα tasks (Mapper/Reducer) |

**ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ**: "Ποιος κάνει schedule τα MapReduce jobs;"
**ΑΠΑΝΤΗΣΗ**: JobTracker

---

## 5. Pseudocode Examples

### 5.1 DISTINCT(X) - Αφαίρεση Duplicates

```python
def Map(id, x):
    emit(x, null)

def Reduce(x, values):
    emit(x)
```

**Εξήγηση**:
- Mapper: Emit κάθε value ως key
- Reducer: Λαμβάνει κάθε unique key μία φορά, emit μόνο το key

**Παράδειγμα**:
```
Input: [A, B, A, C, B, A]

Map output:
  (A, null), (B, null), (A, null), (C, null), (B, null), (A, null)

After Shuffle & Sort:
  A → [null, null, null]
  B → [null, null]
  C → [null]

Reduce output:
  A, B, C
```

### 5.2 WordCount

```python
def Map(doc_id, text):
    for word in text.split():
        emit(word, 1)

def Reduce(word, counts):
    emit(word, sum(counts))
```

**Με Combiner** (optimization):
```python
def Combine(word, counts):
    emit(word, sum(counts))  # Ίδια με Reduce
```

**Παράδειγμα**:
```
Input: "hello world hello"

Map output:
  (hello, 1), (world, 1), (hello, 1)

After Shuffle & Sort:
  hello → [1, 1]
  world → [1]

Reduce output:
  (hello, 2), (world, 1)
```

### 5.3 Sum by Key

```python
def Map(id, record):
    # record = (key, value)
    emit(record.key, record.value)

def Reduce(key, values):
    emit(key, sum(values))
```

### 5.4 Average by Key

```python
def Map(id, record):
    emit(record.key, (record.value, 1))  # (sum, count)

def Reduce(key, values):
    total_sum = sum(v[0] for v in values)
    total_count = sum(v[1] for v in values)
    emit(key, total_sum / total_count)
```

**ΠΡΟΣΟΧΗ**: Δεν μπορούμε να χρησιμοποιήσουμε Combiner απευθείας για average!

### 5.5 Max/Min by Key

```python
def Map(id, record):
    emit(record.key, record.value)

def Reduce(key, values):
    emit(key, max(values))  # ή min(values)
```

### 5.6 Inverted Index

```python
def Map(doc_id, text):
    for word in set(text.split()):  # unique words only
        emit(word, doc_id)

def Reduce(word, doc_ids):
    emit(word, list(doc_ids))
```

**Παράδειγμα**:
```
Doc1: "data mining"
Doc2: "data science"
Doc3: "mining gold"

Output:
  data → [Doc1, Doc2]
  mining → [Doc1, Doc3]
  science → [Doc2]
  gold → [Doc3]
```

### 5.7 Join (Reduce-side)

```python
# Table R(A, B) and S(B, C)
def Map(table_name, record):
    if table_name == 'R':
        emit(record.B, ('R', record.A))
    else:  # S
        emit(record.B, ('S', record.C))

def Reduce(B, values):
    R_values = [v[1] for v in values if v[0] == 'R']
    S_values = [v[1] for v in values if v[0] == 'S']
    for a in R_values:
        for c in S_values:
            emit((a, B, c))
```

### 5.8 Top-K Elements

```python
# Βρες τα K πιο συχνά elements (π.χ. words)

def Map(doc_id, text):
    for word in text.split():
        emit(word, 1)

def Combiner(word, counts):
    emit(word, sum(counts))

def Reduce(word, counts):
    emit(word, sum(counts))

# ΔΕΥΤΕΡΟ MapReduce Job για Top-K
def Map2(word, count):
    # Emit με reverse key για sorting
    emit(count, word)  # Key = count για sorting

def Reduce2(count, words):
    # Reducer λαμβάνει sorted by count (descending)
    for word in words:
        if global_count < K:
            emit(word, count)
            global_count += 1
```

**Παράδειγμα**:
```
Top-3 words από: "the cat sat on the mat the"

Word counts: the=3, cat=1, sat=1, on=1, mat=1
Top-3: the(3), cat(1), sat(1)
```

### 5.9 Matrix Multiplication (A × B)

```python
# Matrix A: m×n, Matrix B: n×p
# Element A[i,k] συνεισφέρει σε όλα τα C[i,j]
# Element B[k,j] συνεισφέρει σε όλα τα C[i,j]

def Map(matrix_name, element):
    if matrix_name == 'A':
        # A[i,k] → emit για κάθε j (στήλη του result)
        i, k, value = element
        for j in range(p):  # p = columns of B
            emit((i, j), ('A', k, value))
    else:  # B
        # B[k,j] → emit για κάθε i (γραμμή του result)
        k, j, value = element
        for i in range(m):  # m = rows of A
            emit((i, j), ('B', k, value))

def Reduce(ij, values):
    i, j = ij
    A_values = {}  # k → value
    B_values = {}  # k → value

    for v in values:
        if v[0] == 'A':
            A_values[v[1]] = v[2]
        else:
            B_values[v[1]] = v[2]

    result = sum(A_values[k] * B_values[k]
                 for k in A_values if k in B_values)
    emit((i, j), result)
```

**Παράδειγμα**:
```
A = [[1, 2],    B = [[5, 6],
     [3, 4]]         [7, 8]]

C[0,0] = A[0,0]*B[0,0] + A[0,1]*B[1,0] = 1*5 + 2*7 = 19
C[0,1] = A[0,0]*B[0,1] + A[0,1]*B[1,1] = 1*6 + 2*8 = 22
...
```

### 5.10 Co-occurrence Matrix (Pairs Approach)

```python
# Μέτρα πόσες φορές δύο words εμφανίζονται μαζί σε window

def Map(doc_id, text):
    words = text.split()
    for i, word_i in enumerate(words):
        # Window size = 2 (neighbors)
        for j in range(max(0, i-2), min(len(words), i+3)):
            if i != j:
                emit((word_i, words[j]), 1)

def Combiner(pair, counts):
    emit(pair, sum(counts))

def Reduce(pair, counts):
    emit(pair, sum(counts))
```

**Παράδειγμα**:
```
Input: "the quick brown fox"
Window = 1 (immediate neighbors)

Pairs emitted:
(the, quick), (quick, the), (quick, brown),
(brown, quick), (brown, fox), (fox, brown)
```

### 5.11 Co-occurrence Matrix (Stripes Approach)

```python
# Πιο αποδοτικό - ομαδοποίηση ανά word

def Map(doc_id, text):
    words = text.split()
    for i, word_i in enumerate(words):
        stripe = {}  # neighbor → count
        for j in range(max(0, i-2), min(len(words), i+3)):
            if i != j:
                neighbor = words[j]
                stripe[neighbor] = stripe.get(neighbor, 0) + 1
        emit(word_i, stripe)

def Reduce(word, stripes):
    merged = {}
    for stripe in stripes:
        for neighbor, count in stripe.items():
            merged[neighbor] = merged.get(neighbor, 0) + count
    emit(word, merged)
```

**Πλεονέκτημα Stripes**: Λιγότερα intermediate key-value pairs

### 5.12 PageRank Iteration

```python
# Ένα iteration του PageRank algorithm
# Graph: node → list of outgoing links

def Map(node, data):
    page_rank, outlinks = data
    n = len(outlinks)

    # Distribute PageRank to neighbors
    for neighbor in outlinks:
        emit(neighbor, page_rank / n)

    # Emit graph structure για να διατηρηθεί
    emit(node, outlinks)

def Reduce(node, values):
    outlinks = None
    sum_pr = 0

    for v in values:
        if isinstance(v, list):  # Graph structure
            outlinks = v
        else:  # PageRank contribution
            sum_pr += v

    # PageRank formula: PR = (1-d)/N + d * sum(contributions)
    d = 0.85  # damping factor
    N = total_nodes
    new_pr = (1 - d) / N + d * sum_pr

    emit(node, (new_pr, outlinks))
```

**Παράδειγμα**:
```
Graph:
A → [B, C]
B → [A]
C → [A, B]

Initial PR: A=1/3, B=1/3, C=1/3

After Map:
B receives: PR(A)/2 = 1/6
A receives: PR(B)/1 + PR(C)/2 = 1/3 + 1/6 = 1/2
...
```

### 5.13 K-Means Clustering Iteration

```python
# Ένα iteration του K-Means algorithm
# Centroids broadcast σε όλους τους mappers

def Map(point_id, point):
    # Βρες το πιο κοντινό centroid
    min_dist = infinity
    closest = None

    for centroid_id, centroid in centroids.items():
        dist = euclidean_distance(point, centroid)
        if dist < min_dist:
            min_dist = dist
            closest = centroid_id

    # Emit (centroid_id, point) για partial sum
    emit(closest, (point, 1))

def Combiner(centroid_id, points_counts):
    total_point = [0] * dimensions
    total_count = 0

    for point, count in points_counts:
        total_point = vector_add(total_point,
                                 vector_multiply(point, count))
        total_count += count

    emit(centroid_id, (total_point, total_count))

def Reduce(centroid_id, partial_sums):
    total_point = [0] * dimensions
    total_count = 0

    for partial_point, count in partial_sums:
        total_point = vector_add(total_point, partial_point)
        total_count += count

    # New centroid = average of assigned points
    new_centroid = vector_divide(total_point, total_count)
    emit(centroid_id, new_centroid)
```

### 5.14 Relational Selection (σ)

```python
# σ_condition(R)

def Map(id, record):
    if evaluate_condition(record):
        emit(record, None)

def Reduce(record, values):
    emit(record)
```

### 5.15 Relational Projection (π)

```python
# π_attributes(R)

def Map(id, record):
    projected = extract_attributes(record, attributes)
    emit(projected, None)

def Reduce(projected, values):
    emit(projected)  # Αυτόματο distinct
```

### 5.16 Group By με Aggregation

```python
# SELECT group_key, AGG(value) FROM R GROUP BY group_key

def Map(id, record):
    emit(record.group_key, record.value)

def Reduce(group_key, values):
    result = aggregate_function(values)  # SUM, AVG, COUNT, etc.
    emit(group_key, result)
```

**Παράδειγμα SQL σε MapReduce**:
```sql
SELECT department, AVG(salary)
FROM Employees
GROUP BY department
```

```python
def Map(emp_id, employee):
    emit(employee.department, (employee.salary, 1))

def Reduce(department, salary_counts):
    total_salary = sum(sc[0] for sc in salary_counts)
    total_count = sum(sc[1] for sc in salary_counts)
    emit(department, total_salary / total_count)
```

---

## 6. Ερωτήσεις Εξετάσεων

### Ερώτηση 1: Data Flow Sequence
```
Ποια είναι η σωστή σειρά επεξεργασίας;

A) Mapper → Reducer → Combiner → Partitioner
B) Mapper → Partitioner → Combiner → Reducer
C) Mapper → Combiner → Reducer → Partitioner
D) Mapper → Combiner → Partitioner → Reducer ✓

ΑΠΑΝΤΗΣΗ: D (1 → 2 → 4 → 3)
```

### Ερώτηση 2: JobTracker Role
```
Ποιος κάνει schedule τα MapReduce jobs;

A) NameNode
B) DataNode
C) JobTracker ✓
D) TaskTracker

ΑΠΑΝΤΗΣΗ: C - JobTracker
```

### Ερώτηση 3: Combiner Usage
```
Πότε μπορούμε να χρησιμοποιήσουμε Combiner;

Μπορούμε:
✓ Sum
✓ Count
✓ Max/Min

Δεν μπορούμε (απευθείας):
✗ Average (πρέπει να κρατήσουμε sum και count)
✗ Median
✗ Distinct count (αν δεν είναι exact)
```

### Ερώτηση 4: Pseudocode για Count Distinct
```python
def Map(id, x):
    emit(x, 1)

def Reduce(x, values):
    emit(x, 1)  # Κάθε unique x μετράει 1

# Για να πάρουμε το συνολικό count:
# Χρειάζεται δεύτερο MapReduce job
def Map2(x, count):
    emit("total", 1)

def Reduce2(key, counts):
    emit(key, sum(counts))
```

### Ερώτηση 5: NameNode vs DataNode
```
Ο NameNode αποθηκεύει:

A) Τα actual δεδομένα
B) Metadata (file locations, permissions) ✓
C) Τα MapReduce results
D) Τα intermediate data

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 6: Partitioner Function
```
Ποιος ο ρόλος του Partitioner;

Διασφαλίζει ότι:
- Records με το ΙΔΙΟ key πηγαίνουν στον ΙΔΙΟ Reducer
- Ισοκατανομή φορτίου μεταξύ Reducers

Default: hash(key) % num_reducers
```

---

## 7. Συχνά Λάθη

1. **Λάθος σειρά**: Ο Partitioner είναι **ΠΡΙΝ** τον Reducer, όχι μετά
2. **Combiner = Reducer**: Ο Combiner πρέπει να έχει την **ίδια λογική** με τον Reducer
3. **Average με Combiner**: Πρέπει να κρατήσεις (sum, count), όχι μόνο average
4. **NameNode**: Δεν αποθηκεύει **data**, μόνο **metadata**

---

## Σύνοψη - Key Points

1. **Data Flow**: Mapper → Combiner → Partitioner → Reducer (1→2→4→3)
2. **JobTracker**: Schedules MapReduce jobs
3. **TaskTracker**: Executes tasks
4. **NameNode**: HDFS metadata
5. **DataNode**: HDFS actual data
6. **Combiner**: Optional local aggregation (same logic as Reducer)
7. **Partitioner**: hash(key) % num_reducers

### Pseudocode Patterns - Basic

| Operation | Map emit | Reduce |
|-----------|----------|--------|
| DISTINCT | (x, null) | emit(key) |
| COUNT | (key, 1) | emit(key, sum) |
| SUM | (key, value) | emit(key, sum) |
| AVG | (key, (value, 1)) | emit(key, sum/count) |
| MAX/MIN | (key, value) | emit(key, max/min) |
| INVERTED INDEX | (word, doc_id) | emit(word, list) |

### Pseudocode Patterns - Advanced

| Operation | Key Idea |
|-----------|----------|
| **JOIN** | Tag με table name, group by join key |
| **TOP-K** | 2 jobs: count + sort by count |
| **MATRIX MULT** | Key=(i,j), tag με matrix name |
| **CO-OCCURRENCE** | Pairs: emit (word1,word2) / Stripes: emit word→{neighbors} |
| **PAGERANK** | Distribute PR/outdegree, sum στο reduce |
| **K-MEANS** | Assign to closest, average στο reduce |
| **σ (SELECT)** | Filter στο Map, emit στο Reduce |
| **π (PROJECT)** | Extract columns, emit για distinct |
| **GROUP BY** | Key=group column, aggregate values |

### Combiner Compatibility

| Operation | Combiner OK? | Reason |
|-----------|--------------|--------|
| SUM | Ναι | Associative + Commutative |
| COUNT | Ναι | Associative + Commutative |
| MAX/MIN | Ναι | Associative + Commutative |
| AVERAGE | Όχι απευθείας | Πρέπει (sum, count) |
| MEDIAN | Όχι | Non-associative |
| DISTINCT | Ναι | Set union |
