# Practice Questions with Answers - Data Mining NTUA

## Οδηγίες Χρήσης
- Διάβασε την ερώτηση
- Προσπάθησε να απαντήσεις ΠΡΙΝ δεις τη λύση
- Έλεγξε την απάντηση και την εξήγηση
- Σημείωσε τις ερωτήσεις που έκανες λάθος για επανάληψη

---

# ΕΝΟΤΗΤΑ 1: OLAP & Data Warehousing (8 ερωτήσεις)

## Q1.1
Ένα data cube έχει 4 dimensions χωρίς ιεραρχίες. Πόσα cuboids έχει;

A) 4
B) 8
C) 16
D) 32

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 16**

**Εξήγηση**: Χωρίς ιεραρχίες, cuboids = 2^n = 2^4 = 16

**Γιατί οι άλλες είναι λάθος**:
- A) 4 = μόνο οι dimensions
- B) 8 = 2^3
- D) 32 = 2^5
</details>

---

## Q1.2
Ένα data cube έχει 3 dimensions με L₁=3, L₂=4, L₃=2 επίπεδα ιεραρχίας. Πόσα cuboids υπάρχουν;

A) 9
B) 14
C) 24
D) 64

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 24**

**Εξήγηση**: Με ιεραρχίες, cuboids = L₁ × L₂ × L₃ = 3 × 4 × 2 = 24

**Γιατί οι άλλες είναι λάθος**:
- A) 9 = L₁ + L₂ + L₃ (λάθος πράξη)
- B) 14 = ???
- D) 64 = 4³ ή 2^6
</details>

---

## Q1.3
Ποια OLAP operation φιλτράρει σε ΜΙΑ μόνο dimension;

A) Dice
B) Slice
C) Roll-up
D) Pivot

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Slice**

**Εξήγηση**:
- Slice = φιλτράρισμα σε 1 dimension
- Dice = φιλτράρισμα σε 2+ dimensions

**Γιατί οι άλλες είναι λάθος**:
- A) Dice = 2+ dimensions
- C) Roll-up = aggregation, όχι filtering
- D) Pivot = περιστροφή αξόνων
</details>

---

## Q1.4
Τι κάνει η Roll-up operation;

A) Αυξάνει το επίπεδο λεπτομέρειας
B) Μειώνει το επίπεδο λεπτομέρειας (aggregation)
C) Φιλτράρει δεδομένα
D) Περιστρέφει τους άξονες

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Μειώνει το επίπεδο λεπτομέρειας**

**Εξήγηση**: Roll-up = aggregation, πηγαίνει σε υψηλότερο επίπεδο ιεραρχίας (π.χ. day → month)

**Γιατί οι άλλες είναι λάθος**:
- A) Αυτό είναι Drill-down
- C) Αυτό είναι Slice/Dice
- D) Αυτό είναι Pivot
</details>

---

## Q1.5
Σε ποιο schema οι dimension tables είναι denormalized;

A) Snowflake Schema
B) Star Schema
C) 3NF Schema
D) BCNF Schema

<details>
<summary>Απάντηση</summary>

**Σωστό: B) Star Schema**

**Εξήγηση**:
- Star Schema: Denormalized dimensions = λιγότερα JOINs = πιο γρήγορα queries
- Snowflake Schema: Normalized dimensions

**Γιατί οι άλλες είναι λάθος**:
- A) Snowflake = normalized
- C, D) OLTP schemas, όχι data warehouse
</details>

---

## Q1.6
Base cuboid με 10 products, 5 stores, 12 months. Πόσα cells έχει;

A) 27
B) 60
C) 600
D) 6000

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 600**

**Εξήγηση**: Cells = p₁ × p₂ × p₃ = 10 × 5 × 12 = 600
</details>

---

## Q1.7
Τι σημαίνει C(*, c5, t3) σε data cube notation;

A) Aggregation μόνο στο time
B) Aggregation στα products και cities
C) Aggregation μόνο στα products
D) Καμία aggregation

<details>
<summary>Απάντηση</summary>

**Σωστό: C) Aggregation μόνο στα products**

**Εξήγηση**:
- * = aggregation σε αυτή τη dimension
- c5 = συγκεκριμένη city (5)
- t3 = συγκεκριμένος time (3)

Άρα μόνο το product (*) έχει aggregation.
</details>

---

## Q1.8
Γιατί δεν τρέχουμε OLAP queries σε OLTP systems;

A) OLTP δεν υποστηρίζει SQL
B) OLAP queries είναι resource-intensive και θα επιβραδύνουν τα transactions
C) OLAP απαιτεί NoSQL
D) OLTP δεν έχει αρκετά data

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: OLAP queries κάνουν full table scans, complex aggregations, και θα επηρεάσουν τα day-to-day transactions.
</details>

---

# ΕΝΟΤΗΤΑ 2: SQL & Relational Databases (8 ερωτήσεις)

## Q2.1
Ποια είναι η διαφορά μεταξύ Primary Key και Unique Key;

A) Καμία διαφορά
B) Primary Key επιτρέπει NULL, Unique όχι
C) Primary Key δεν επιτρέπει NULL, Unique επιτρέπει
D) Unique Key δεν μπορεί να χρησιμοποιηθεί σε JOIN

<details>
<summary>Απάντηση</summary>

**Σωστό: C)**

**Εξήγηση**: Primary Key = Unique + NOT NULL
</details>

---

## Q2.2
```sql
SELECT * FROM Products
WHERE price > 100 AND category = 'A' OR category = 'B';
```
Τι επιστρέφει αυτό το query;

A) Products με price > 100 που είναι A ή B
B) Products με (price > 100 AND A) OR (οποιοδήποτε B)
C) Όλα τα products
D) Syntax error

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: AND έχει προτεραιότητα από OR!
Διαβάζεται ως: `(price > 100 AND category = 'A') OR (category = 'B')`

Για το A χρειάζεται: `WHERE price > 100 AND (category = 'A' OR category = 'B')`
</details>

---

## Q2.3
Ποιο είναι σωστό για HAVING;

A) Φιλτράρει rows πριν το GROUP BY
B) Φιλτράρει groups μετά το GROUP BY
C) Είναι ίδιο με WHERE
D) Χρησιμοποιείται χωρίς GROUP BY

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**:
- WHERE: Φιλτράρει rows ΠΡΙΝ το GROUP BY
- HAVING: Φιλτράρει groups ΜΕΤΑ το GROUP BY
</details>

---

## Q2.4
```sql
SELECT category, SUM(sales)
FROM Products
WHERE price > 10
GROUP BY category
HAVING SUM(sales) > 1000;
```
Σε ποια σειρά εκτελούνται;

A) WHERE → GROUP BY → HAVING
B) GROUP BY → WHERE → HAVING
C) HAVING → GROUP BY → WHERE
D) WHERE → HAVING → GROUP BY

<details>
<summary>Απάντηση</summary>

**Σωστό: A)**

**Εξήγηση**: Σειρά εκτέλεσης:
1. FROM
2. WHERE (φιλτράρει rows)
3. GROUP BY (ομαδοποίηση)
4. HAVING (φιλτράρει groups)
5. SELECT
6. ORDER BY
</details>

---

## Q2.5
Ποιο query βρίσκει books με total quantity > 100;

A) `SELECT BookID FROM Sales WHERE SUM(quantity) > 100`
B) `SELECT BookID, SUM(quantity) FROM Sales GROUP BY BookID HAVING SUM(quantity) > 100`
C) `SELECT BookID FROM Sales HAVING SUM(quantity) > 100`
D) `SELECT BookID FROM Sales WHERE quantity > 100`

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**: Χρειάζεται GROUP BY για aggregation και HAVING για το condition στο aggregate.

**Γιατί οι άλλες είναι λάθος**:
- A) SUM δεν επιτρέπεται στο WHERE
- C) HAVING χωρίς GROUP BY δεν λειτουργεί σωστά
- D) Βρίσκει individual rows με quantity > 100, όχι totals
</details>

---

## Q2.6
Τι κάνει ο σ (sigma) operator στη Relational Algebra;

A) Επιλέγει columns (Projection)
B) Επιλέγει rows (Selection)
C) Ενώνει tables
D) Αφαιρεί duplicates

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**:
- σ (sigma) = Selection = WHERE (επιλέγει ROWS)
- π (pi) = Projection = SELECT columns
</details>

---

## Q2.7
```sql
UPDATE Students SET marks = marks * 1.20 WHERE grade = 'A';
```
Αν marks = 80, ποια η νέα τιμή;

A) 80
B) 96
C) 100
D) 120

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 96**

**Εξήγηση**: 80 × 1.20 = 96 (αύξηση 20%, ΟΧΙ 120!)
</details>

---

## Q2.8
Ποιο είναι σωστό για NULL comparisons;

A) `WHERE price = NULL` βρίσκει NULL values
B) `WHERE price IS NULL` βρίσκει NULL values
C) NULL = NULL επιστρέφει TRUE
D) COUNT(*) αγνοεί NULLs

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**:
- `price = NULL` επιστρέφει UNKNOWN (όχι αποτελέσματα!)
- Πρέπει: `price IS NULL`
- NULL = NULL → UNKNOWN (όχι TRUE)
- COUNT(*) μετράει ΟΛΕΣ τις rows, COUNT(column) αγνοεί NULLs
</details>

---

# ΕΝΟΤΗΤΑ 3: MapReduce (5 ερωτήσεις)

## Q3.1
Ποια είναι η σωστή σειρά του MapReduce data flow;

A) Mapper → Reducer → Combiner → Partitioner
B) Mapper → Combiner → Reducer → Partitioner
C) Mapper → Combiner → Partitioner → Reducer
D) Mapper → Partitioner → Combiner → Reducer

<details>
<summary>Απάντηση</summary>

**Σωστό: C)**

**Εξήγηση**: Σειρά: 1→2→4→3
1. Mapper
2. Combiner (local aggregation)
4. Partitioner (διαμοιρασμός σε reducers)
3. Reducer (final aggregation)
</details>

---

## Q3.2
Ποιος κάνει schedule τα MapReduce jobs στο Hadoop;

A) NameNode
B) DataNode
C) JobTracker
D) TaskTracker

<details>
<summary>Απάντηση</summary>

**Σωστό: C) JobTracker**

**Εξήγηση**:
- JobTracker: Schedules jobs
- TaskTracker: Executes tasks
- NameNode: HDFS metadata
- DataNode: HDFS data
</details>

---

## Q3.3
Για DISTINCT operation στο MapReduce, τι κάνει ο Reducer;

A) emit(key, sum(values))
B) emit(key, count(values))
C) emit(key)
D) emit(key, max(values))

<details>
<summary>Απάντηση</summary>

**Σωστό: C) emit(key)**

**Εξήγηση**:
```python
Map(id, x): emit(x, null)
Reduce(x, values): emit(x)  # Απλά emit το key
```
Κάθε unique key εμφανίζεται μία φορά.
</details>

---

## Q3.4
Ο NameNode αποθηκεύει:

A) Τα actual data blocks
B) Metadata (file names, locations)
C) MapReduce results
D) Τα intermediate data

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**:
- NameNode = HDFS metadata (ποια blocks, σε ποια nodes)
- DataNode = actual data blocks
</details>

---

## Q3.5
Για ποια operation ΔΕΝ μπορούμε να χρησιμοποιήσουμε Combiner απευθείας;

A) Sum
B) Count
C) Average
D) Max

<details>
<summary>Απάντηση</summary>

**Σωστό: C) Average**

**Εξήγηση**:
- Sum, Count, Max, Min: Associative & Commutative → OK
- Average: Δεν είναι associative!
  - Πρέπει να κρατήσουμε (sum, count) και να κάνουμε sum/count στο τέλος
</details>

---

# ΕΝΟΤΗΤΑ 4: Data Preprocessing (4 ερωτήσεις)

## Q4.1
Min-Max normalization: Data = {200, 400, 600}. Ποια είναι η normalized τιμή του 400 στο range [0,1];

A) 0.25
B) 0.5
C) 0.75
D) 1.0

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 0.5**

**Εξήγηση**:
min = 200, max = 600
400 → (400-200)/(600-200) = 200/400 = 0.5
</details>

---

## Q4.2
Decimal Scaling: Data = {-85, 7, 120}. Ποια τιμή έχει το j;

A) 1
B) 2
C) 3
D) 4

<details>
<summary>Απάντηση</summary>

**Σωστό: C) 3**

**Εξήγηση**:
max(|v|) = 120
120 < 1000 = 10³ → j = 3

(Σημείωση: Με j=2, 120/100 = 1.2 ≥ 1, άρα δεν αρκεί)
</details>

---

## Q4.3
Equal Width Binning: Data range [10, 70], k=3 bins. Ποιο είναι το width;

A) 10
B) 20
C) 30
D) 60

<details>
<summary>Απάντηση</summary>

**Σωστό: B) 20**

**Εξήγηση**:
width = (max - min) / k = (70 - 10) / 3 = 60 / 3 = 20
</details>

---

## Q4.4
Ποια μέθοδος normalization εγγυάται ότι όλες οι τιμές είναι στο (-1, 1);

A) Min-Max [0, 1]
B) Z-Score
C) Decimal Scaling
D) Equal Width Binning

<details>
<summary>Απάντηση</summary>

**Σωστό: C) Decimal Scaling**

**Εξήγηση**:
- Min-Max [0, 1]: [0, 1]
- Z-Score: Καμία εγγύηση (μπορεί να είναι οτιδήποτε)
- Decimal Scaling: Πάντα |v'| < 1, άρα (-1, 1)
</details>

---

# ΕΝΟΤΗΤΑ 5: Data Integration (3 ερωτήσεις)

## Q5.1
Στο GAV (Global-as-View):

A) Local schemas ορίζονται ως views του global
B) Global schema ορίζεται ως view των local
C) Query processing είναι δύσκολο
D) Εύκολο να προσθέσεις νέες πηγές

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

**Εξήγηση**:
- GAV: **G**lobal **A**s **V**iew (of local)
- Query: Easy (unfold)
- Add source: Hard
</details>

---

## Q5.2
Το σύμβολο Local ⊆ Global αντιστοιχεί σε:

A) GAV
B) LAV
C) Open-World Assumption
D) Closed-World Assumption

<details>
<summary>Απάντηση</summary>

**Σωστό: B) LAV**

**Εξήγηση**:
- GAV: Global ⊇ Local (global superset)
- LAV: Local ⊆ Global (local subset)
</details>

---

## Q5.3
Σε ποια προσέγγιση είναι εύκολο να προσθέσεις νέες data sources;

A) GAV
B) LAV
C) Και στις δύο
D) Σε καμία

<details>
<summary>Απάντηση</summary>

**Σωστό: B) LAV**

**Εξήγηση**:
- LAV: Κάθε νέα source ορίζεται ως view του (σταθερού) global → Easy!
- GAV: Πρέπει να ξαναγράψεις το global view → Hard
</details>

---

# ΕΝΟΤΗΤΑ 6: Query Processing & General Concepts (2 ερωτήσεις)

## Q6.1
Ποιος join algorithm υποστηρίζει inequality joins (π.χ. R.a < S.b);

A) Hash Join
B) Sort-Merge Join
C) Nested Loop Join
D) Κανένας

<details>
<summary>Απάντηση</summary>

**Σωστό: C) Nested Loop Join**

**Εξήγηση**:
- Hash Join: ΜΟΝΟ equi-join (=)
- Sort-Merge: ΜΟΝΟ equi-join (=)
- Nested Loop: ΟΛΟΙ οι τύποι (=, <, >, ≠, κτλ.)
</details>

---

## Q6.2
Η κλίμακα Kelvin είναι:

A) Nominal
B) Ordinal
C) Interval
D) Ratio

<details>
<summary>Απάντηση</summary>

**Σωστό: D) Ratio**

**Εξήγηση**:
- Kelvin έχει absolute zero (0K = no molecular motion)
- Celsius/Fahrenheit = Interval (0° δεν είναι "καθόλου")
</details>

---

# BONUS QUESTIONS

## B1: Pipelining
Pipelining processes intermediate results without storing them. True or False?

<details>
<summary>Απάντηση</summary>

**TRUE**

Pipelining = tuple-by-tuple processing, χωρίς αποθήκευση ενδιάμεσων.
</details>

---

## B2: Viterbi Algorithm
Ο Viterbi algorithm χρησιμοποιείται για:

A) Training HMM parameters
B) Finding most likely state sequence
C) Counting states
D) Generating random sequences

<details>
<summary>Απάντηση</summary>

**Σωστό: B)**

- Baum-Welch: Training
- Viterbi: Decoding (best path)
</details>

---

## B3: Ordered Data
Ποιο είναι ordered data;

A) Shopping basket items
B) Social network friends
C) DNA sequence
D) Set of hashtags

<details>
<summary>Απάντηση</summary>

**Σωστό: C) DNA sequence**

DNA = ordered sequence (ATCG...)
</details>

---

# Σύνοψη Σκορ

| Ενότητα | Ερωτήσεις | Σκορ μου |
|---------|-----------|----------|
| OLAP | 8 | __/8 |
| SQL | 8 | __/8 |
| MapReduce | 5 | __/5 |
| Preprocessing | 4 | __/4 |
| Data Integration | 3 | __/3 |
| Query/Concepts | 2 | __/2 |
| Bonus | 3 | __/3 |
| **ΣΥΝΟΛΟ** | **33** | **__/33** |

**Στόχος**: 30+/33 για 10/10 στις εξετάσεις!
