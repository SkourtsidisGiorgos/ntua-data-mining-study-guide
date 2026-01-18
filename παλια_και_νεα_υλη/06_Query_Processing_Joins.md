# Query Processing & Join Algorithms - Πλήρης Οδηγός Μελέτης

## 1. Query Evaluation Strategies

### 1.1 Materialization
- **Τι κάνει**: Υπολογίζει κάθε operation, **αποθηκεύει** ενδιάμεσα αποτελέσματα
- **Πού αποθηκεύει**: Στο disk ή στη memory
- **Πλεονέκτημα**: Απλό, predictable
- **Μειονέκτημα**: Μεγάλο I/O cost, απαιτεί χώρο

```
Query: σ_A>10(R ⋈ S)

Materialization:
1. Υπολόγισε R ⋈ S → αποθήκευσε σε temp_table
2. Υπολόγισε σ_A>10(temp_table) → αποτέλεσμα
```

### 1.2 Pipelined Evaluation
- **Τι κάνει**: Επεξεργάζεται **tuple-by-tuple** χωρίς αποθήκευση
- **Πλεονέκτημα**: Λιγότερο I/O, λιγότερη memory
- **Μειονέκτημα**: Δεν λειτουργεί πάντα (blocking operations)

```
Query: σ_A>10(R ⋈ S)

Pipelined:
1. Πάρε tuple από R ⋈ S
2. Αν A>10, προώθησε στο output
3. Επανέλαβε (χωρίς να αποθηκεύσεις το join result)
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25 - ΚΡΙΣΙΜΟ!

```
Q: In relational database query processing and optimization, which
   correctly describes the difference between pipelined evaluation
   and materialization?

a) Pipelined stores intermediate results, while materialization
   passes results directly between operators without storing them.
b) Pipelined execution processes one tuple at a time and passes it
   to the next operator, whereas materialization stores intermediate
   results in memory or disk before passing them to subsequent operators. ✓
c) Pipelined is only for join operations, materialization only for aggregation.
d) They are interchangeable in relational query processing.

ΑΠΑΝΤΗΣΗ: B

ΕΞΗΓΗΣΗ:
- Pipelining = tuple-by-tuple, NO storage
- Materialization = computes & STORES intermediate results
```

### Σύγκριση

| Χαρακτηριστικό | Materialization | Pipelining |
|----------------|-----------------|------------|
| Ενδιάμεσα αποτελέσματα | **Αποθηκεύονται** | **ΟΧΙ** αποθήκευση |
| Memory | Υψηλή | Χαμηλή |
| I/O | Υψηλό | Χαμηλό |
| Blocking ops | Υποστηρίζει | Περιορισμένο |
| Processing style | Operator-at-a-time | Tuple-at-a-time |

---

## 2. Join Algorithms

### 2.1 Nested Loop Join

**Αλγόριθμος**:
```python
for each tuple r in R:
    for each tuple s in S:
        if r.key == s.key:  # ή άλλη συνθήκη
            output(r, s)
```

**Χαρακτηριστικά**:
- **Complexity**: O(n × m)
- **Υποστηρίζει**: **ΟΛΟΥΣ** τους τύπους joins (=, <, >, ≤, ≥, ≠)
- **Memory**: Χαμηλή (μόνο current tuples)
- **Πότε χρησιμοποιείται**: Μικρά tables, non-equi joins

### 2.2 Block Nested Loop Join

**Βελτίωση**: Διαβάζει blocks αντί για single tuples
```python
for each block B_R in R:
    for each block B_S in S:
        for each tuple r in B_R:
            for each tuple s in B_S:
                if condition(r, s):
                    output(r, s)
```

**Πλεονέκτημα**: Λιγότερο I/O (διαβάζει κάθε block μία φορά per outer block)

### 2.3 Hash Join

**Αλγόριθμος**:
```
Build Phase:
1. Φτιάξε hash table από το μικρότερο table (build input)
   hash(join_key) → bucket

Probe Phase:
2. Για κάθε tuple του μεγαλύτερου table (probe input):
   - Υπολόγισε hash(join_key)
   - Ψάξε στο αντίστοιχο bucket για matches
```

**Χαρακτηριστικά**:
- **Complexity**: O(n + m) average case
- **Υποστηρίζει**: **ΜΟΝΟ equi-joins** (=)
- **Memory**: Πρέπει να χωράει το hash table
- **Πότε χρησιμοποιείται**: Μεγάλα tables, equi-joins

### ⚠️ ΚΡΙΣΙΜΟ ΓΙΑ ΕΞΕΤΑΣΕΙΣ
```
Hash Join ΔΕΝ υποστηρίζει inequality joins (<, >, ≤, ≥)!
```

### 2.4 Sort-Merge Join

**Αλγόριθμος**:
```
Sort Phase:
1. Ταξινόμησε R με βάση το join key
2. Ταξινόμησε S με βάση το join key

Merge Phase:
3. Merge τα sorted relations (όπως merge sort)
   - Για κάθε matching key, output όλους τους συνδυασμούς
```

**Χαρακτηριστικά**:
- **Complexity**: O(n log n + m log m) για sort + O(n + m) για merge
- **Υποστηρίζει**: **ΜΟΝΟ equi-joins** (=)
- **Memory**: Για sorting (external sort αν δεν χωράει)
- **Πότε χρησιμοποιείται**: Ήδη sorted data, large tables

---

## 3. Σύγκριση Join Algorithms

| Algorithm | Equi-Join | Non-Equi Join | Complexity | Best For |
|-----------|-----------|---------------|------------|----------|
| **Nested Loop** | ✓ | ✓ | O(n×m) | Small tables, any condition |
| **Block NL** | ✓ | ✓ | O(n×m) | Limited memory |
| **Hash Join** | ✓ | ✗ | O(n+m) | Large tables, equi-join |
| **Sort-Merge** | ✓ | ✗ | O(n log n) | Pre-sorted data |

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25

```
Q: Which of the following join algorithms is NOT suitable to compute
   inequality joins (a type of non-equijoin that uses inequalities)?

a) Hash Join ✓
b) (Sort) Merge Join ✓
c) Nested Loop Join
d) All of the above

ΑΠΑΝΤΗΣΗ: A (και B - αλλά ρωτάει συνήθως για Hash Join)

ΕΞΗΓΗΣΗ:
- Hash Join: ΜΟΝΟ equi-joins (hash function works only with =)
- Sort-Merge: ΜΟΝΟ equi-joins
- Nested Loop: ΟΛΑ τα joins (μπορεί να ελέγξει οποιαδήποτε συνθήκη)
```

### Πότε χρησιμοποιούμε τι

| Σενάριο | Προτεινόμενος Algorithm |
|---------|------------------------|
| Μικρά tables | Nested Loop |
| R.a = S.b (equi-join, μεγάλα tables) | **Hash Join** |
| R.a < S.b (inequality) | **Nested Loop** (μόνη επιλογή!) |
| R.a > S.b (inequality) | **Nested Loop** |
| Sorted data | Sort-Merge |
| Limited memory | Block Nested Loop |

---

## 4. Index-Based Joins

### Index Nested Loop Join
```python
for each tuple r in R:
    # Χρησιμοποίησε index στο S
    matches = S.index.lookup(r.key)
    for s in matches:
        output(r, s)
```

**Πλεονέκτημα**: Πολύ γρήγορο αν υπάρχει index
**Complexity**: O(n × log m) αν υπάρχει B-tree index

---

## 5. Query Optimization Basics

### Heuristic Optimization
1. **Push selections down**: Κάνε selections νωρίς (μειώνει rows)
2. **Push projections down**: Κράτα μόνο τα απαραίτητα columns (μειώνει width)
3. **Reorder joins**: Ξεκίνα από τα μικρότερα tables

### Παράδειγμα
```sql
-- Original
SELECT name FROM Employee E, Department D
WHERE E.dept_id = D.id AND D.location = 'Athens'

-- Optimized (conceptually)
1. σ_location='Athens'(Department)  -- Filter first (reduces D significantly)
2. Join με Employee
3. π_name                           -- Project last
```

### Query Plan Tree
```
      π_name
         |
         ⋈
        / \
       E   σ_location='Athens'(D)
```

---

## 6. Semi-Join

### Ορισμός
**R ⋉ S** = Tuples του R που έχουν match στο S

```sql
R ⋉ S = π_R(R ⋈ S)
```

**Χρήση**: Distributed databases - μειώνει data transfer
**Ιδέα**: Στείλε μόνο τα join keys για να βρεις ποια rows χρειάζονται

---

## 7. Blocking vs Non-Blocking Operations

### Blocking Operations
Πρέπει να διαβάσουν **ΟΛΟ** το input πριν δώσουν output:
- **Sort**
- **Aggregation** (SUM, AVG, etc.)
- **Hash Join** (build phase)
- **Distinct** (χρειάζεται να δει όλα τα values)

### Non-Blocking Operations
Μπορούν να δώσουν output **αμέσως**:
- **Selection (σ)** - φιλτράρισμα
- **Projection (π)** - επιλογή columns
- **Nested Loop Join** - μπορεί να emit μόλις βρει match

**Για Pipelining**: Πρέπει οι operators να είναι non-blocking ή να υπάρχει hybrid approach.

---

## 8. Ερωτήσεις Εξετάσεων - Πλήρης Συλλογή

### Ερώτηση 1: Pipelining Definition
```
Q: Pipelining processes intermediate results without storing them.

A) True ✓
B) False

ΑΠΑΝΤΗΣΗ: A (TRUE)
```

### Ερώτηση 2: Hash Join Limitation
```
Q: Hash Join can be used for:

A) All types of joins
B) Only equi-joins ✓
C) Only inequality joins
D) Only cross joins

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 3: Non-Equi Join Algorithm
```
Q: Which algorithm can perform R.a < S.b join?

A) Hash Join
B) Sort-Merge Join
C) Nested Loop Join ✓
D) Both A and B

ΑΠΑΝΤΗΣΗ: C (Only Nested Loop)
```

### Ερώτηση 4: Materialization vs Pipelining
```
Q: Which approach stores intermediate results?

A) Pipelining
B) Materialization ✓
C) Both
D) Neither

ΑΠΑΝΤΗΣΗ: B
```

### Ερώτηση 5: Best Algorithm Selection
```
Q: For joining two very large tables on equality:

A) Nested Loop Join
B) Hash Join ✓
C) Cross Join
D) Self Join

ΑΠΑΝΤΗΣΗ: B (Hash Join has O(n+m) complexity)
```

### Ερώτηση 6: Algorithm Complexity
```
Q: Which join algorithm has O(n × m) worst case?

A) Hash Join
B) Sort-Merge Join
C) Nested Loop Join ✓
D) Index Join

ΑΠΑΝΤΗΣΗ: C
```

---

## Σύνοψη - Key Points για 10/10

### Evaluation Strategies (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)
```
Pipelining:    Tuple-at-a-time, NO storage
Materialization: Operator-at-a-time, STORES intermediate results
```

### Join Algorithm Support (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

| Condition | Algorithms |
|-----------|------------|
| R.a **=** S.b | Hash, Sort-Merge, Nested Loop |
| R.a **<** S.b | **ΜΟΝΟ Nested Loop** |
| R.a **>** S.b | **ΜΟΝΟ Nested Loop** |
| R.a **≤** S.b | **ΜΟΝΟ Nested Loop** |
| R.a **≠** S.b | **ΜΟΝΟ Nested Loop** |

### Quick Reference

| Question | Answer |
|----------|--------|
| Inequality join algorithm | Nested Loop |
| Fastest for large equi-join | Hash Join |
| Stores intermediate results | Materialization |
| Processes tuple-by-tuple | Pipelining |
| O(n × m) complexity | Nested Loop |
| O(n + m) complexity | Hash Join |
| Needs pre-sorted data | Sort-Merge Join |

### Blocking Operations (για pipelining)
- Sort
- Aggregation
- Hash Join (build phase)
- Distinct

### Non-Blocking Operations
- Selection (σ)
- Projection (π)
- Nested Loop Join
