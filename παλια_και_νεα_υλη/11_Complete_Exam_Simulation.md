# Complete Exam Simulation - Data Mining NTUA
## 60+ Questions from Past Exams (2022-2025)

---

# Instructions
- Χρόνος: 75 λεπτά
- Διάβασε κάθε ερώτηση προσεκτικά
- Απάντησε ΠΡΙΝ κοιτάξεις τη λύση
- Σημείωσε τα λάθη σου για επανάληψη
- Στόχος: 55+/60 για 10/10

---

# ΜΕΡΟΣ A: OLAP & Data Warehousing (12 ερωτήσεις)

## Q1 [Εξέταση 2024-25]
Which OLAP operation allows users to view data from different perspectives by rotating axes of the data cube?

a) Slice and Dice
b) Roll-up
c) Pivot
d) Drill-down

<details>
<summary>Απάντηση</summary>

**C) Pivot**

Pivot = Περιστροφή αξόνων για διαφορετική οπτική γωνία
</details>

---

## Q2 [Εξέταση 2024-25]
Which is a major disadvantage of running OLAP queries on an OLTP system?

a) It reduces the effectiveness of dimensional modeling
b) It increases transactional throughput but slows down ETL processing
c) It introduces high query latency and can negatively impact real-time transactional performance
d) It prevents the use of star and snowflake schemas

<details>
<summary>Απάντηση</summary>

**C)**

OLAP queries είναι resource-intensive και επιβραδύνουν τα OLTP transactions.
</details>

---

## Q3 [Εξέταση 2024-25]
What is a dimension hierarchy in OLAP?

a) A method of indexing data for faster retrieval
b) A structure that organizes data at different levels of granularity
c) A process of normalizing fact tables in a data warehouse
d) A relationship between primary keys and foreign keys

<details>
<summary>Απάντηση</summary>

**B)**

Dimension hierarchy = δομή με διαφορετικά επίπεδα λεπτομέρειας (π.χ. Day→Month→Year)
</details>

---

## Q4 [Εξέταση 2022-23]
Let a data warehouse cube consist of 4 dimensions, each of which has 5 hierarchy levels (including all). How many cuboids exist?

a) 4^5
b) 5^4
c) 2^4
d) 20

<details>
<summary>Απάντηση</summary>

**B) 5^4 = 625**

Με ιεραρχίες: Cuboids = L₁ × L₂ × L₃ × L₄ = 5 × 5 × 5 × 5 = 5^4
</details>

---

## Q5 [Εξέταση 2022-23]
How is the snowflake schema different from the star schema?

a) Snowflake does not contain a fact table
b) Dimension tables are split into further tables in the snowflake schema
c) Star schema has dimension tables, snowflake does not
d) The fact table in snowflake is smaller than in star

<details>
<summary>Απάντηση</summary>

**B)**

Snowflake = normalized dimensions (split into sub-tables)
</details>

---

## Q6 [Εξέταση 2022-23]
A data cube has n dimensions, and each dimension has exactly p distinct values. What is the maximum number of cells in the base cuboid?

a) p^n
b) p
c) pn
d) 2^n

<details>
<summary>Απάντηση</summary>

**A) p^n**

Cells = p₁ × p₂ × ... × pₙ = p × p × ... × p = p^n
</details>

---

## Q7 [Εξέταση 2022-23]
Let data cube C consist of 3 dimensions: product, customer, time. What is the correct query to find the total sales for product p7 by customer c7 for all time?

a) C(*, *, *)
b) C(p7, *, *)
c) C(p7, c7, *)
d) C(*, c7, *)

<details>
<summary>Απάντηση</summary>

**C) C(p7, c7, *)**

p7 = specific product, c7 = specific customer, * = all times (aggregation)
</details>

---

## Q8 [Εξέταση 2022-23]
For query "find the total sales for all products and customers per day", which cuboid would answer this fastest?

a) (product, customer)
b) (time)
c) (product, customer, time)
d) ()

<details>
<summary>Απάντηση</summary>

**B) (time)**

"Per day" = χρειάζεται time dimension
"All products and customers" = aggregation σε αυτά
(time) cuboid έχει ήδη aggregated τα products και customers
</details>

---

## Q9
Ποια OLAP operation μειώνει το επίπεδο λεπτομέρειας μέσω aggregation;

a) Slice
b) Dice
c) Roll-up
d) Drill-down

<details>
<summary>Απάντηση</summary>

**C) Roll-up**

Roll-up = aggregation (π.χ. Day → Month → Year)
Drill-down = αντίθετο (περισσότερη λεπτομέρεια)
</details>

---

## Q10
Ένα cube έχει 3 dimensions χωρίς ιεραρχίες. Πόσα cuboids υπάρχουν;

a) 3
b) 6
c) 8
d) 9

<details>
<summary>Απάντηση</summary>

**C) 8**

Χωρίς ιεραρχίες: Cuboids = 2^n = 2^3 = 8
</details>

---

## Q11
Ποια είναι Slice operation;

a) Product='TV' AND Location='Athens'
b) Time='Q1'
c) Product IN ('TV','Radio')
d) Sales > 1000

<details>
<summary>Απάντηση</summary>

**B) Time='Q1'**

Slice = φιλτράρισμα σε ΜΙΑ μόνο dimension
</details>

---

## Q12
Base cuboid με 10 products, 5 stores, 12 months. Πόσα cells;

a) 27
b) 60
c) 600
d) 6000

<details>
<summary>Απάντηση</summary>

**C) 600**

Cells = 10 × 5 × 12 = 600
</details>

---

# ΜΕΡΟΣ B: SQL & Relational Databases (15 ερωτήσεις)

## Q13 [Εξέταση 2022-23]
What is a relation in RDBMS?

a) Table
b) Key
c) Data Types
d) Row

<details>
<summary>Απάντηση</summary>

**A) Table**
</details>

---

## Q14 [Εξέταση 2022-23]
The primary key must be?

a) Unique
b) Not Null
c) Both A and B
d) None of the above

<details>
<summary>Απάντηση</summary>

**C) Both A and B**

Primary Key = Unique + NOT NULL
</details>

---

## Q15 [Εξέταση 2022-23]
What is the difference between PRIMARY KEY and UNIQUE KEY?

a) Primary key can store null, unique cannot
b) We can have only one primary key but multiple unique keys
c) Primary key cannot be a date variable
d) None of these

<details>
<summary>Απάντηση</summary>

**B)**

- Only ONE primary key per table
- Multiple unique keys allowed
- Primary key cannot be NULL, unique can have ONE null
</details>

---

## Q16 [Εξέταση 2024-25]
Which best describes a "foreign key"?

a) A key used to access data from an external database
b) A key that uniquely identifies a record in a table
c) A key that establishes a relationship between two tables by referencing a primary key
d) A key used for indexing data

<details>
<summary>Απάντηση</summary>

**C)**
</details>

---

## Q17 [Εξέταση 2022-23]
What does: UPDATE student SET marks = marks * 1.20;

a) Increases marks by 120%
b) Decreases marks by 20%
c) Increases marks by 20%
d) None of the above

<details>
<summary>Απάντηση</summary>

**C) Increases marks by 20%**

80 × 1.20 = 96 (αύξηση κατά 16 = 20% του 80)
</details>

---

## Q18 [Εξέταση 2022-23]
The Select command is a part of what type of statement?

a) DML
b) DDL
c) View
d) None of the above

<details>
<summary>Απάντηση</summary>

**A) DML**

DML = SELECT, INSERT, UPDATE, DELETE
DDL = CREATE, ALTER, DROP
</details>

---

## Q19 [Εξέταση 2022-23]
Which SQL keyword is used to retrieve only unique values?

A) DISTINCTIVE
B) UNIQUE
C) DISTINCT
D) DIFFERENT

<details>
<summary>Απάντηση</summary>

**C) DISTINCT**
</details>

---

## Q20 [Εξέταση 2022-23]
Which type of JOIN returns rows that do NOT have matching values?

a) Natural JOIN
b) Outer JOIN
c) EQUI JOIN
d) All of the above

<details>
<summary>Απάντηση</summary>

**B) Outer JOIN**
</details>

---

## Q21 [Εξέταση 2022-23]
A CASE SQL statement is?

a) A way to establish a loop in SQL
b) A way to establish an IF-THEN-ELSE in SQL
c) A way to establish a data definition in SQL
d) All of the above

<details>
<summary>Απάντηση</summary>

**B)**
</details>

---

## Q22 [Εξέταση 2022-23]
Get all data from student table whose name starts with p?

a) SELECT * FROM student WHERE name LIKE '%p%';
b) SELECT * FROM student WHERE name LIKE 'p%';
c) SELECT * FROM student WHERE name LIKE '_p%';
d) SELECT * FROM student WHERE name LIKE '%p';

<details>
<summary>Απάντηση</summary>

**B) 'p%'**

'p%' = starts with p
</details>

---

## Q23 [Εξέταση 2022-23]
Display all cities whose humidity is in range 60 to 75?

a) SELECT * FROM weather WHERE humidity IN (60 to 75)
b) SELECT * FROM weather WHERE humidity BETWEEN 60 AND 75
c) SELECT * FROM weather WHERE humidity NOT IN (60 AND 75)
d) SELECT * FROM weather WHERE humidity NOT BETWEEN 60 AND 75

<details>
<summary>Απάντηση</summary>

**B) BETWEEN 60 AND 75**
</details>

---

## Q24 [Εξέταση 2022-23]
Which SQL statement is correct?

a) SELECT Username AND Password FROM Users
b) SELECT Username, Password FROM Users
c) SELECT Username, Password WHERE Username = 'user1'
d) None of these

<details>
<summary>Απάντηση</summary>

**B)**

Columns χωρίζονται με κόμμα, όχι AND
</details>

---

## Q25 [Εξέταση 2022-23]
Which are valid logical operators in SQL?

A) SOME
B) ALL
C) AND
D) All of the above

<details>
<summary>Απάντηση</summary>

**D) All of the above**
</details>

---

## Q26 [Εξέταση 2024-25]
```
π_{A,C}(σ_{B='X'}(R)) ∩ π_{A,C}(σ_{B='Y'}(R))
```
What does the result represent?

a) All (A, C) pairs that appear for both B='X' and B='Y'
b) All (A, C) pairs that appear for either B='X' or B='Y'
c) All (A, C) pairs that appear only when B='X' but not when B='Y'
d) All tuples that satisfy both B='X' and B='Y' simultaneously

<details>
<summary>Απάντηση</summary>

**A)**

INTERSECT = κοινά στοιχεία και στις δύο πλευρές
</details>

---

## Q27 [Εξέταση 2022-23]
How can you change "Thomas" into "Michel" in the "LastName" column?

a) UPDATE User SET LastName = 'Thomas' INTO LastName = 'Michel'
b) MODIFY Users SET LastName = 'Michel' WHERE LastName = 'Thomas'
c) MODIFY Users SET LastName = 'Thomas' INTO LastName = 'Michel'
d) UPDATE Users SET LastName = 'Michel' WHERE LastName = 'Thomas'

<details>
<summary>Απάντηση</summary>

**D)**

UPDATE table SET column = new_value WHERE condition
</details>

---

# ΜΕΡΟΣ C: MapReduce & Hadoop (8 ερωτήσεις)

## Q28 [Εξέταση 2022-23]
Relative to MapReduce, which is correct?

a) A MapReduce job splits input data into independent chunks processed by map tasks in parallel
b) The MapReduce framework operates on <key, value> pairs
c) Applications implement Mapper and Reducer functions
d) All of the above

<details>
<summary>Απάντηση</summary>

**D) All of the above**
</details>

---

## Q29 [Εξέταση 2022-23]
What is the process that schedules MapReduce jobs?

a) Namenode daemon
b) Jobtracker
c) Tasktracker
d) Datanode daemon

<details>
<summary>Απάντηση</summary>

**B) Jobtracker**

JobTracker = schedules jobs
TaskTracker = executes tasks
</details>

---

## Q30 [Εξέταση 2022-23]
What is the correct sequence of data flow? (1=Mapper, 2=Combiner, 3=Reducer, 4=Partitioner)

a) 1, 2, 3, 4
b) 1, 2, 4, 3
c) 1, 3, 2, 4
d) 1, 4, 2, 3

<details>
<summary>Απάντηση</summary>

**B) 1, 2, 4, 3**

Mapper → Combiner → Partitioner → Reducer
</details>

---

## Q31
Ο NameNode αποθηκεύει:

a) Τα actual data blocks
b) Metadata (file names, locations)
c) MapReduce results
d) Intermediate data

<details>
<summary>Απάντηση</summary>

**B) Metadata**

NameNode = metadata
DataNode = actual data
</details>

---

## Q32
Για ποια operation ΔΕΝ μπορούμε να χρησιμοποιήσουμε Combiner απευθείας;

a) Sum
b) Count
c) Average
d) Max

<details>
<summary>Απάντηση</summary>

**C) Average**

Average δεν είναι associative - πρέπει να κρατήσουμε (sum, count)
</details>

---

## Q33
Για DISTINCT operation στο MapReduce, τι κάνει ο Reducer;

a) emit(key, sum(values))
b) emit(key, count(values))
c) emit(key)
d) emit(key, max(values))

<details>
<summary>Απάντηση</summary>

**C) emit(key)**

DISTINCT: Map: emit(x, null), Reduce: emit(x)
</details>

---

## Q34
Ο Partitioner διασφαλίζει ότι:

a) Κάθε key πηγαίνει σε τυχαίο Reducer
b) Records με ίδιο key πηγαίνουν στον ίδιο Reducer
c) Τα data είναι sorted
d) Ο Combiner τρέχει σωστά

<details>
<summary>Απάντηση</summary>

**B)**

Default: hash(key) % num_reducers → ίδια keys στον ίδιο reducer
</details>

---

## Q35
Ποιος εκτελεί τα tasks (Mapper/Reducer);

a) NameNode
b) DataNode
c) JobTracker
d) TaskTracker

<details>
<summary>Απάντηση</summary>

**D) TaskTracker**

JobTracker = schedules
TaskTracker = executes
</details>

---

# ΜΕΡΟΣ D: Data Preprocessing (6 ερωτήσεις)

## Q36 [Εξέταση 2022-23]
Using min-max normalization to [0, 1] for data: 200, 300, 400, 600, 1000, what are the new values?

a) 0, 0.2, 0.3, 0.5, 1
b) 0, 0.2, 0.25, 0.4, 1
c) 0, 0.125, 0.25, 0.5, 1
d) 0.2, 0.3, 0.4, 0.6, 1

<details>
<summary>Απάντηση</summary>

**C) 0, 0.125, 0.25, 0.5, 1**

min=200, max=1000
300 → (300-200)/(1000-200) = 100/800 = 0.125
400 → 200/800 = 0.25
600 → 400/800 = 0.5
</details>

---

## Q37 [Εξέταση 2022-23]
Using decimal scaling for data: -997, 3, 83, what are the new values?

a) -1, 0, 0.1
b) -9.97, 0.03, 0.83
c) -0.997, 0.003, 0.083
d) -99.7, 0.3, 8.3

<details>
<summary>Απάντηση</summary>

**C) -0.997, 0.003, 0.083**

max(|v|) = 997 < 1000 → j = 3
Divide by 10^3 = 1000
</details>

---

## Q38
Min-Max normalization: Data = {200, 400, 600}. Ποια η normalized τιμή του 400 στο [0,1];

a) 0.25
b) 0.5
c) 0.75
d) 1.0

<details>
<summary>Απάντηση</summary>

**B) 0.5**

min=200, max=600
400 → (400-200)/(600-200) = 200/400 = 0.5
</details>

---

## Q39
Decimal Scaling: Data = {-85, 7, 120}. Ποια η τιμή του j;

a) 1
b) 2
c) 3
d) 4

<details>
<summary>Απάντηση</summary>

**C) 3**

max(|v|) = 120
120 < 1000 = 10^3 → j = 3
</details>

---

## Q40
Equal Width Binning: Data range [10, 70], k=3 bins. Ποιο το width;

a) 10
b) 20
c) 30
d) 60

<details>
<summary>Απάντηση</summary>

**B) 20**

width = (max - min) / k = (70 - 10) / 3 = 60 / 3 = 20
</details>

---

## Q41
Ποια μέθοδος normalization εγγυάται ότι όλες οι τιμές είναι στο (-1, 1);

a) Min-Max [0, 1]
b) Z-Score
c) Decimal Scaling
d) Equal Width Binning

<details>
<summary>Απάντηση</summary>

**C) Decimal Scaling**

Decimal scaling: |v'| < 1, άρα (-1, 1)
</details>

---

# ΜΕΡΟΣ E: Data Integration GAV/LAV (5 ερωτήσεις)

## Q42
Στο GAV (Global-as-View):

a) Local schemas ορίζονται ως views του global
b) Global schema ορίζεται ως view των local
c) Query processing είναι δύσκολο
d) Εύκολο να προσθέσεις νέες πηγές

<details>
<summary>Απάντηση</summary>

**B)**

GAV: Global As View (of local sources)
- Query: Easy (unfold)
- Add source: Hard
</details>

---

## Q43
Το σύμβολο Local ⊆ Global αντιστοιχεί σε:

a) GAV
b) LAV
c) Open-World Assumption
d) Closed-World Assumption

<details>
<summary>Απάντηση</summary>

**B) LAV**

LAV: Local ⊆ Global (local subset of global)
GAV: Global ⊇ Local (global superset)
</details>

---

## Q44
Σε ποια προσέγγιση είναι εύκολο να προσθέσεις νέες data sources;

a) GAV
b) LAV
c) Και στις δύο
d) Σε καμία

<details>
<summary>Απάντηση</summary>

**B) LAV**

LAV: Νέα source = νέο view definition, global δεν αλλάζει
</details>

---

## Q45
Σε ποια προσέγγιση το query processing είναι απλό "unfold";

a) GAV
b) LAV
c) Both
d) Neither

<details>
<summary>Απάντηση</summary>

**A) GAV**

GAV: Unfold = αντικατάστησε το global με τον ορισμό του
LAV: Query rewriting (πιο δύσκολο)
</details>

---

## Q46
Στο Open-World Assumption:

a) Ό,τι δεν υπάρχει στη βάση είναι ψευδές
b) Ό,τι δεν υπάρχει μπορεί να είναι αληθές
c) Η βάση περιέχει όλη την αλήθεια
d) Δεν επιτρέπονται NULL values

<details>
<summary>Απάντηση</summary>

**B)**

OWA: Absence of information ≠ False
CWA: If not in DB, then False
</details>

---

# ΜΕΡΟΣ F: Query Processing & Joins (6 ερωτήσεις)

## Q47 [Εξέταση 2024-25]
In query processing, which describes the difference between pipelined evaluation and materialization?

a) Pipelined stores intermediate results, materialization passes directly
b) Pipelined processes one tuple at a time without storing, materialization stores intermediate results
c) Pipelined is only for joins, materialization is only for aggregation
d) They are the same process

<details>
<summary>Απάντηση</summary>

**B)**

Pipelining = tuple-by-tuple, no intermediate storage
Materialization = stores intermediate results
</details>

---

## Q48 [Εξέταση 2024-25]
Which join algorithm is NOT suitable for inequality joins (e.g., a < b)?

a) Hash Join
b) (Sort) Merge Join
c) Nested Loop Join
d) All of the above (none can do it)

<details>
<summary>Απάντηση</summary>

**A) Hash Join** (και B)

Hash Join & Sort-Merge: ΜΟΝΟ equi-joins (=)
Nested Loop: ALL join types (=, <, >, ≠)
</details>

---

## Q49
Pipelining processes intermediate results without storing them.

a) True
b) False

<details>
<summary>Απάντηση</summary>

**A) True**
</details>

---

## Q50
Which algorithm can perform R.a < S.b join?

a) Hash Join
b) Sort-Merge Join
c) Nested Loop Join
d) Both A and B

<details>
<summary>Απάντηση</summary>

**C) Nested Loop Join**

Only Nested Loop supports inequality conditions
</details>

---

## Q51
Which join algorithm has O(n × m) worst case complexity?

a) Hash Join
b) Sort-Merge Join
c) Nested Loop Join
d) Index Join

<details>
<summary>Απάντηση</summary>

**C) Nested Loop Join**

Nested Loop: O(n × m)
Hash Join: O(n + m) average
Sort-Merge: O(n log n + m log m)
</details>

---

## Q52
For joining two very large tables on equality, which is best?

a) Nested Loop Join
b) Hash Join
c) Cross Join
d) Self Join

<details>
<summary>Απάντηση</summary>

**B) Hash Join**

Hash Join: O(n+m), optimal for large equi-joins
</details>

---

# ΜΕΡΟΣ G: General Concepts (8 ερωτήσεις)

## Q53 [Εξέταση 2024-25]
Which of the following is true about cardinality in ER diagrams?

a) Cardinality describes the number of attributes an entity can have
b) Cardinality describes the number of instances of one entity that can/must be associated with each instance of another entity
c) [Option cut off]
d) [Option cut off]

<details>
<summary>Απάντηση</summary>

**B)**

Cardinality = πόσα instances μιας entity συνδέονται με instances άλλης
</details>

---

## Q54 [Εξέταση 2024-25]
Which of the following data are NOT considered to be ordered?

a) Video
b) Connections between individuals in an online social network
c) [not visible]
d) [not visible]

<details>
<summary>Απάντηση</summary>

**B) Social network connections**

Ordered: Video, Time series, DNA sequence, Text
Unordered: Social connections, Shopping baskets, Keywords
</details>

---

## Q55 [Εξέταση 2024-25]
You have a dataset with temperatures in Kelvin. What kind of attribute is that?

a) Nominal
b) Ordinal
c) Interval
d) Ratio

<details>
<summary>Απάντηση</summary>

**D) Ratio**

Kelvin has absolute zero (true zero point)
Celsius/Fahrenheit = Interval (0° δεν είναι "καθόλου")
</details>

---

## Q56 [Εξέταση 2024-25]
Which statements about HMMs is true?

a) The trainable parameters are initial state probabilities and state transition probabilities
b) HMMs can be used for clustering, classification, and outlier detection
c) The Baum-Welch algorithm is an expectation-maximization algorithm
d) The Viterbi Algorithm determines the most likely sequence of states

<details>
<summary>Απάντηση</summary>

**A, C, D are all true** (depends on which one the exam asks for)

- a) HMM params: π (initial) + A (transitions)
- c) Baum-Welch = EM algorithm
- d) Viterbi = best state sequence
</details>

---

## Q57
Η κλίμακα Celsius είναι:

a) Nominal
b) Ordinal
c) Interval
d) Ratio

<details>
<summary>Απάντηση</summary>

**C) Interval**

0°C δεν είναι "καθόλου θερμοκρασία" → no true zero → Interval
</details>

---

## Q58
Ο Viterbi algorithm χρησιμοποιείται για:

a) Training HMM parameters
b) Finding most likely state sequence
c) Generating observations
d) Counting states

<details>
<summary>Απάντηση</summary>

**B)**

Baum-Welch = Training
Viterbi = Decoding (best path)
</details>

---

## Q59
Ποια είναι subsequence του &lt;A, B, C, D&gt;;

a) &lt;B, A&gt;
b) &lt;C, D, A&gt;
c) &lt;A, C&gt;
d) &lt;D, B&gt;

<details>
<summary>Απάντηση</summary>

**C) &lt;A, C&gt;**

Subsequence διατηρεί τη σειρά αλλά όχι απαραίτητα συνεχόμενα
A→C: σειρά διατηρείται ✓
</details>

---

## Q60
Ποιο είναι ordered data;

a) Shopping basket items
b) Social network friends
c) DNA sequence
d) Set of hashtags

<details>
<summary>Απάντηση</summary>

**C) DNA sequence**

DNA = ordered (ATCG sequence matters)
</details>

---

# BONUS QUESTIONS

## B1
Για equal width binning με data [1, 5, 10, 12, 18, 20, 25, 30] και k=4 bins, ποιο είναι το width;

<details>
<summary>Απάντηση</summary>

**width = (30-1)/4 = 29/4 = 7.25**
</details>

---

## B2
Γράψε το MapReduce pseudocode για DISTINCT:

<details>
<summary>Απάντηση</summary>

```python
def Map(id, x):
    emit(x, null)

def Reduce(x, values):
    emit(x)
```
</details>

---

## B3
Γράψε SQL query για total QuantitySold per BookID:

<details>
<summary>Απάντηση</summary>

```sql
SELECT BookID, SUM(QuantitySold) AS TotalQuantitySold
FROM Sales
GROUP BY BookID;
```
</details>

---

# SCORE TRACKER

| Ενότητα | Ερωτήσεις | Σκορ |
|---------|-----------|------|
| A: OLAP | 12 | __/12 |
| B: SQL | 15 | __/15 |
| C: MapReduce | 8 | __/8 |
| D: Preprocessing | 6 | __/6 |
| E: GAV/LAV | 5 | __/5 |
| F: Query Processing | 6 | __/6 |
| G: General | 8 | __/8 |
| Bonus | 3 | __/3 |
| **ΣΥΝΟΛΟ** | **63** | **__/63** |

## Στόχοι:
- 50-55/63 = 8/10
- 55-60/63 = 9/10
- 60+/63 = 10/10
