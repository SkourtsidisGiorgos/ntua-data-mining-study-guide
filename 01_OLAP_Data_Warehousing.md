# OLAP & Data Warehousing - Πλήρης Οδηγός Μελέτης

## 1. OLAP Operations

### 1.1 Slice
- **Τι είναι**: Επιλογή μιας "φέτας" του cube φιλτράροντας σε **ΜΙΑ διάσταση**
- **Αποτέλεσμα**: Μείωση κατά μία διάσταση

**Παράδειγμα**:
```
Data Cube: Sales(Product, Time, Location)

Slice: Time = "Q1 2024"
Αποτέλεσμα: 2D πίνακας Sales(Product, Location) μόνο για Q1 2024
```

### 1.2 Dice
- **Τι είναι**: Επιλογή υπο-κύβου φιλτράροντας σε **ΔΥΟ ή ΠΕΡΙΣΣΟΤΕΡΕΣ διαστάσεις**
- **Διαφορά από Slice**: Slice = 1 διάσταση, Dice = 2+ διαστάσεις

**Παράδειγμα**:
```
Data Cube: Sales(Product, Time, Location)

Dice: Product IN ('TV', 'Radio') AND Location IN ('Athens', 'Patras')
Αποτέλεσμα: Υπο-κύβος με 2 products × 2 locations × all times
```

### 1.3 Roll-up (Drill-up)
- **Τι είναι**: Aggregation - μετάβαση σε **υψηλότερο επίπεδο** ιεραρχίας
- **Αποτέλεσμα**: Λιγότερη λεπτομέρεια, περισσότερη σύνοψη

**Παράδειγμα**:
```
Ιεραρχία Time: Day → Month → Quarter → Year

Roll-up από Day σε Month:
  Πριν: Sales per day (365 rows)
  Μετά: Sales per month (12 rows) - με SUM/AVG aggregation
```

### 1.4 Drill-down
- **Τι είναι**: **Αντίστροφο του Roll-up** - μετάβαση σε χαμηλότερο επίπεδο
- **Αποτέλεσμα**: Περισσότερη λεπτομέρεια

**Παράδειγμα**:
```
Ιεραρχία Location: Country → Region → City → Store

Drill-down από Country σε Region:
  Πριν: Sales per country (1 row για Greece)
  Μετά: Sales per region (Attica, Macedonia, Peloponnese, etc.)
```

### 1.5 Pivot (Rotate)
- **Τι είναι**: Περιστροφή των αξόνων του cube
- **Αποτέλεσμα**: Διαφορετική οπτική γωνία, ίδια δεδομένα

**Παράδειγμα**:
```
Πριν:           Μετά Pivot:
     Q1  Q2         Athens  Patras
TV   100 150    Q1    100     80
PC   200 180    Q2    150    120
                TV    ...    ...
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25
```
Q: Which OLAP operation allows users to view data from different
   perspectives by rotating axes of the data cube?

a) Slice and Dice
b) Roll-up
c) Pivot ✓
d) Drill-down

ΑΠΑΝΤΗΣΗ: C - Pivot
```

---

## 2. Data Warehouse Schemas

### 2.1 Star Schema
```
                    ┌─────────────┐
                    │  DIM_TIME   │
                    │─────────────│
                    │ time_id (PK)│
                    │ day         │
                    │ month       │
                    │ year        │
                    └──────┬──────┘
                           │
┌─────────────┐    ┌───────┴───────┐    ┌─────────────┐
│ DIM_PRODUCT │    │  FACT_SALES   │    │DIM_LOCATION │
│─────────────│    │───────────────│    │─────────────│
│prod_id (PK) │────│time_id (FK)   │────│loc_id (PK)  │
│name         │    │prod_id (FK)   │    │city         │
│category     │    │loc_id (FK)    │    │region       │
└─────────────┘    │amount         │    │country      │
                   │quantity       │    └─────────────┘
                   └───────────────┘
```

**Χαρακτηριστικά**:
- Fact Table στο κέντρο (μετρήσεις/measures)
- Dimension Tables γύρω-γύρω (denormalized)
- **Ταχύτερα queries** (λιγότερα JOINs)
- Περισσότερος χώρος (redundancy)

### 2.2 Snowflake Schema
```
┌─────────┐    ┌─────────────┐
│CATEGORY │    │  DIM_TIME   │
│─────────│    │─────────────│
│cat_id   │    │ time_id (PK)│
│cat_name │    │ day         │
└────┬────┘    │ month_id(FK)│
     │         └──────┬──────┘
     │                │
┌────┴────────┐    ┌──┴──────────┐
│ DIM_PRODUCT │    │  DIM_MONTH  │
│─────────────│    │─────────────│
│prod_id (PK) │    │ month_id    │
│name         │    │ month_name  │
│cat_id (FK)  │    │ quarter_id  │
└─────────────┘    └─────────────┘
```

**Χαρακτηριστικά**:
- Dimension tables είναι **normalized**
- Λιγότερο redundancy
- **Πιο αργά queries** (περισσότερα JOINs)

### Σύγκριση Star vs Snowflake

| Χαρακτηριστικό | Star Schema | Snowflake Schema |
|----------------|-------------|------------------|
| Normalization | Denormalized | Normalized |
| Query Speed | **Ταχύτερο** | Πιο αργό |
| Storage | Περισσότερος χώρος | Λιγότερος χώρος |
| JOINs | Λιγότερα | Περισσότερα |
| Maintenance | Πιο εύκολο | Πιο δύσκολο |
| **Προτίμηση** | **Συνήθως αυτό** | Σπάνια |

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: How is the snowflake schema different from the star schema?

a) Snowflake does not contain a fact table
b) Dimension tables are split into further tables in the snowflake schema ✓
c) Star schema has dimension tables, snowflake does not
d) The fact table in snowflake is smaller than in star

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Στο snowflake, τα dimension tables είναι normalized
         (σπασμένα σε επιμέρους tables)
```

---

## 3. Υπολογισμοί Cuboids

### 3.1 Χωρίς Ιεραρχίες

**Τύπος**: `Αριθμός Cuboids = 2^n`

όπου n = αριθμός dimensions

**Παράδειγμα 1**:
```
Dimensions: Product, Time, Location (n=3)
Cuboids = 2³ = 8

Τα 8 cuboids:
1. ()              - apex cuboid (πλήρης aggregation)
2. (Product)
3. (Time)
4. (Location)
5. (Product, Time)
6. (Product, Location)
7. (Time, Location)
8. (Product, Time, Location) - base cuboid
```

### 3.2 Με Ιεραρχίες

**Τύπος**: `Αριθμός Cuboids = L₁ × L₂ × ... × Lₙ`

όπου Lᵢ = αριθμός επιπέδων στη διάσταση i (συμπεριλαμβανομένου του "all")

**Παράδειγμα 2**:
```
Dimension Time: Day → Month → Year → All (4 επίπεδα)
Dimension Location: City → Country → All (3 επίπεδα)
Dimension Product: Item → Category → All (3 επίπεδα)

Cuboids = 4 × 3 × 3 = 36
```

**Παράδειγμα 3** (Τύπος εξέτασης):
```
Δίνεται:
- Time: 3 levels (L₁ = 3)
- Location: 4 levels (L₂ = 4)
- Product: 2 levels (L₃ = 2)

Cuboids = 3 × 4 × 2 = 24
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23 & 2024-25
```
Q: Let a data warehouse cube consist of 4 dimensions, each of which
   has 5 hierarchy levels (including all). How many cuboids exist?

a) 4^5
b) 5^4 ✓
c) 2^4
d) 20

ΑΠΑΝΤΗΣΗ: B (5^4 = 625)
ΕΞΗΓΗΣΗ: Με ιεραρχίες, cuboids = L₁ × L₂ × L₃ × L₄ = 5 × 5 × 5 × 5 = 5^4
```

---

## 4. Υπολογισμοί Cells στο Base Cuboid

**Τύπος**: `Cells = p₁ × p₂ × ... × pₙ`

όπου pᵢ = αριθμός distinct τιμών στη διάσταση i

**Παράδειγμα 1**:
```
Products: 100 διαφορετικά
Locations: 50 διαφορετικές
Times: 365 days

Max Cells = 100 × 50 × 365 = 1,825,000 cells
```

**Παράδειγμα 2**:
```
Αν p7=10, c7=5, t5=3:
Cells in base cuboid = 10 × 5 × 3 = 150
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: A data cube has n dimensions, and each dimension has exactly p
   distinct values in the base cuboid. What is the maximum number
   of cells possible in the base cuboid?

a) p^n ✓
b) p
c) pn
d) 2^n

ΑΠΑΝΤΗΣΗ: A (p^n)
ΕΞΗΓΗΣΗ: n dimensions, καθένα με p τιμές → p × p × ... × p (n φορές) = p^n
```

---

## 5. Dimension Hierarchies

### Ορισμός
**Dimension Hierarchy**: Δομή που οργανώνει τα δεδομένα σε **διαφορετικά επίπεδα λεπτομέρειας (granularity)**.

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25
```
Q: What is a dimension hierarchy in OLAP?

a) A method of indexing data for faster retrieval
b) A structure that organizes data at different levels of granularity ✓
c) A process of normalizing fact tables in a data warehouse
d) A relationship between primary keys and foreign keys

ΑΠΑΝΤΗΣΗ: B
```

### Granularity
- **Ορισμός**: Το επίπεδο λεπτομέρειας στο οποίο αποθηκεύονται τα δεδομένα
- **Finest granularity** = base cuboid (π.χ. individual transactions)
- **Coarsest granularity** = apex cuboid (ένα μόνο aggregate value)

### Κοινές Ιεραρχίες

**Time Hierarchy**:
```
Second → Minute → Hour → Day → Week → Month → Quarter → Year → All
```

**Location Hierarchy**:
```
Store → City → Region → Country → Continent → All
```

**Product Hierarchy**:
```
SKU → Product → Subcategory → Category → Department → All
```

---

## 6. OLAP vs OLTP

| Χαρακτηριστικό | OLTP | OLAP |
|----------------|------|------|
| **Σκοπός** | Day-to-day operations | Analysis & reporting |
| **Users** | Clerks, operators | Analysts, managers |
| **Queries** | Simple, predefined | Complex, ad-hoc |
| **Data** | Current, detailed | Historical, summarized |
| **Design** | ER-based, normalized | Star/Snowflake |
| **Operations** | INSERT, UPDATE, DELETE | Mainly SELECT |
| **Response time** | Milliseconds | Seconds to minutes |

**Γιατί δεν τρέχουμε OLAP queries σε OLTP systems**:
- OLAP queries είναι resource-intensive (full table scans)
- Θα επιβραδύνουν τα transactions
- Διαφορετικό optimization (indexes, partitioning)
- OLTP χρειάζεται ACID, OLAP χρειάζεται read performance

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25
```
Q: Which of the following is a major disadvantage of running OLAP
   queries on an OLTP system?

a) It reduces the effectiveness of dimensional modeling
b) It increases transactional throughput but slows down ETL processing
c) It introduces high query latency and can negatively impact
   real-time transactional performance ✓
d) It prevents the use of star and snowflake schemas

ΑΠΑΝΤΗΣΗ: C
```

---

## 7. Data Cube Query Notation

### Πώς διαβάζουμε C(p, c, t) notation

- **Συγκεκριμένη τιμή**: `p7` = product με id 7
- **Wildcard (*)**: `*` = ALL values (aggregation σε αυτή τη διάσταση)

**Παραδείγματα**:

```
C(p7, c7, *) = Sales για product 7, customer 7, όλους τους χρόνους
             → Aggregated across time dimension

C(*, *, *) = Total sales (apex cuboid)
           → Aggregated across ALL dimensions

C(p7, *, t5) = Sales για product 7, όλους τους customers, time 5
             → Aggregated across customer dimension
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Let data cube C consist of 3 dimensions: product, customer, time.
   What is the correct query to find the total sales for product p7
   by customer c7 for all time?

a) C(*, *, *)
b) C(p7, *, *)
c) C(p7, c7, *) ✓
d) C(*, c7, *)

ΑΠΑΝΤΗΣΗ: C
ΕΞΗΓΗΣΗ: p7 = συγκεκριμένο product, c7 = συγκεκριμένος customer,
         * = aggregation σε όλους τους χρόνους
```

---

## 8. Επιλογή Βέλτιστου Cuboid για Query

### Αρχή
Επιλέγουμε το cuboid που:
1. **Περιέχει τις απαραίτητες dimensions** για το query
2. Έχει **το λιγότερο επίπεδο λεπτομέρειας** (fewest rows)
3. Είναι **ήδη materialized**

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: For query "find the total sales for all products and customers per day",
   which cuboid would answer this fastest?

Cuboids:
a) (product, customer)
b) (time) ✓
c) (product, customer, time)
d) ()

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ:
- Το query ζητάει "per day" → χρειαζόμαστε τη dimension time
- "All products and customers" → aggregation σε αυτές τις dimensions
- Το (time) cuboid έχει ήδη aggregated products και customers
- Είναι μικρότερο από το (product, customer, time)
```

---

## 9. OLAP Operations σε Combination

### Παράδειγμα από Εξέταση 2024-25

**Scenario**: Data warehouse με dimensions: date, spectator, location, game
και measures: count, charge

**Query**: "List the total charge paid by student spectators at 'G. Karaiskakis' for all games in 2024"

**Starting**: base cuboid {date, spectator, location, game}

**Required OLAP Operations**:
1. **Roll-up** on date: from date_id → year
2. **Roll-up** on game: from game_id → all (aggregation)
3. **Dice** με conditions:
   - spectator = 'students'
   - location_name = 'G. Karaiskakis'
   - year = 2024

---

## 10. Ερωτήσεις Εξετάσεων - Πλήρης Συλλογή

### Ερώτηση 1: Ποιο cuboid είναι ταχύτερο;
```
Query: "Total sales per product category για το 2024"

Cuboids:
A) (Product, Time, Location) - base cuboid
B) (Category, Year)
C) (Product, Year)
D) (Category, Time)

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Το (Category, Year) έχει ήδη aggregated τα products
σε categories και time σε years - λιγότερα rows να σκανάρει.
```

### Ερώτηση 2: Υπολογισμός Cuboids
```
Δίνεται cube με:
- Product: 2 ιεραρχικά επίπεδα + all = 3
- Location: 3 ιεραρχικά επίπεδα + all = 4
- Time: 4 ιεραρχικά επίπεδα + all = 5

Πόσα cuboids υπάρχουν;

ΑΠΑΝΤΗΣΗ: 3 × 4 × 5 = 60 cuboids
```

### Ερώτηση 3: OLAP Operations
```
Αρχικό query: Sales by Product by City by Month
Τελικό query: Sales by Product by Country by Year

Ποιες operations χρειάζονται;

ΑΠΑΝΤΗΣΗ:
1. Roll-up στο Location (City → Country)
2. Roll-up στο Time (Month → Year)
```

### Ερώτηση 4: Cells σε Base Cuboid
```
Dimensions:
- 10 products
- 5 stores
- 12 months

Πόσα cells έχει το base cuboid;

ΑΠΑΝΤΗΣΗ: 10 × 5 × 12 = 600 cells
```

### Ερώτηση 5: Slice vs Dice
```
Ποια είναι Slice operation;

A) Product = 'TV' AND Location = 'Athens'
B) Time = 'Q1'
C) Product IN ('TV', 'Radio')
D) Sales > 1000

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Slice = φιλτράρισμα σε ΜΙΑ μόνο διάσταση
```

---

## Σύνοψη - Key Points για 10/10

### Τύποι (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

| Τι υπολογίζω | Τύπος |
|--------------|-------|
| Cuboids χωρίς ιεραρχίες | **2^n** |
| Cuboids με ιεραρχίες | **L₁ × L₂ × ... × Lₙ** |
| Cells σε base cuboid | **p₁ × p₂ × ... × pₙ** |

### 5 OLAP Operations (ΑΠΟΜΝΗΜΟΝΕΥΣΕ!)

| Operation | Τι κάνει | Keyword |
|-----------|----------|---------|
| **Slice** | Φιλτράρισμα σε 1 dimension | "one filter" |
| **Dice** | Φιλτράρισμα σε 2+ dimensions | "sub-cube" |
| **Roll-up** | Aggregation (↑ level) | "summarize" |
| **Drill-down** | Disaggregation (↓ level) | "details" |
| **Pivot** | Rotate axes | "different view" |

### Star vs Snowflake

| | Star | Snowflake |
|--|------|-----------|
| Dimensions | Denormalized | Normalized |
| Queries | **Faster** | Slower |
| Storage | More | Less |

### Data Cube Notation

```
C(p7, c7, *) → p7 = specific product, c7 = specific customer, * = all times
C(*, *, *)   → apex cuboid (total aggregation)
```
