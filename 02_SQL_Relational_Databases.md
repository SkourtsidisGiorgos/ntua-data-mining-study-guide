# SQL & Relational Databases - Πλήρης Οδηγός Μελέτης

## 1. Βασικές Έννοιες

### Relation (= Table)
- Ένα **relation** είναι ένας πίνακας με rows (tuples) και columns (attributes)
- Κάθε row είναι μοναδικό (no duplicates)
- Η σειρά των rows/columns δεν έχει σημασία

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: What is a relation in RDBMS?

a) Table ✓
b) Key
c) Data Types
d) Row

ΑΠΑΝΤΗΣΗ: A - Table
```

### Primary Key vs Unique Key

| Χαρακτηριστικό | Primary Key | Unique Key |
|----------------|-------------|------------|
| NULL values | **ΟΧΙ** | Ναι (ένα) |
| Πλήθος ανά table | 1 | Πολλά |
| Clustered index | Ναι (συνήθως) | Όχι |

**ΣΗΜΑΝΤΙΚΟ**: `Primary Key = Unique + NOT NULL`

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: The primary key must be?

a) Unique
b) Not Null
c) Both A and B ✓
d) None of the above

ΑΠΑΝΤΗΣΗ: C
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: What is the difference between PRIMARY KEY and UNIQUE KEY?

a) Primary key can store null, unique cannot
b) We can have only one primary key but multiple unique keys ✓
c) Primary key cannot be a date variable
d) None of these

ΑΠΑΝΤΗΣΗ: B
```

### Foreign Key

**Ορισμός**: Column που αναφέρεται στο Primary Key άλλου πίνακα και εξασφαλίζει **referential integrity**.

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25
```
Q: Which of the following sentences best describes a "foreign key"?

a) A key used to access data from an external database
b) A key that uniquely identifies a record in a table
c) A key that establishes a relationship between two tables
   by referencing a primary key ✓
d) A key used for indexing data

ΑΠΑΝΤΗΣΗ: C
```

```sql
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
```

### DML vs DDL

| DML (Data Manipulation) | DDL (Data Definition) |
|-------------------------|----------------------|
| SELECT | CREATE |
| INSERT | ALTER |
| UPDATE | DROP |
| DELETE | TRUNCATE |

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: The Select command is a part of what type of statement?

a) DML ✓
b) DDL
c) View
d) None of the above

ΑΠΑΝΤΗΣΗ: A
```

---

## 2. SELECT Queries

### Βασική Σύνταξη
```sql
SELECT column1, column2
FROM table_name
WHERE condition
GROUP BY column
HAVING aggregate_condition
ORDER BY column ASC/DESC;
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Which of the SQL statements is correct?

a) SELECT Username AND Password FROM Users
b) SELECT Username, Password FROM Users ✓
c) SELECT Username, Password WHERE Username = 'user1'
d) None of these

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Τα columns χωρίζονται με κόμμα, όχι AND
```

### SELECT DISTINCT

Αφαιρεί duplicates:
```sql
SELECT DISTINCT city FROM Customers;
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Which SQL keyword is used to retrieve only unique values?

A) DISTINCTIVE
B) UNIQUE
C) DISTINCT ✓
D) DIFFERENT

ΑΠΑΝΤΗΣΗ: C
```

---

## 3. WHERE με Operators

### AND, OR - ΠΡΟΣΟΧΗ: Operator Precedence!

**ΚΡΙΣΙΜΟ**: `AND` έχει **υψηλότερη προτεραιότητα** από `OR`

```sql
-- ΠΡΟΣΟΧΗ: AND έχει προτεραιότητα από OR
SELECT * FROM Products
WHERE price > 100 AND category = 'Electronics' OR category = 'Books';
-- Ισοδύναμο με: (price > 100 AND category = 'Electronics') OR (category = 'Books')

-- Σωστά με παρενθέσεις:
SELECT * FROM Products
WHERE price > 100 AND (category = 'Electronics' OR category = 'Books');
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Find cities from 'weather' table where condition = 'sunny' or 'cloudy'
   but temperature >= 60.

a) ... WHERE condition = 'cloudy' AND condition = 'sunny' OR temperature >= 60
b) ... WHERE condition = 'cloudy' OR condition = 'sunny' OR temperature >= 60
c) ... WHERE condition = 'sunny' OR condition = 'cloudy' AND temperature >= 60 ✓
d) ... WHERE condition = 'sunny' AND condition = 'cloudy' AND temperature >= 60

ΑΠΑΝΤΗΣΗ: C
ΕΞΗΓΗΣΗ: Με AND precedence, διαβάζεται ως:
         condition = 'sunny' OR (condition = 'cloudy' AND temperature >= 60)

ΣΗΜΕΙΩΣΗ: Αν θέλαμε (sunny OR cloudy) AND temp>=60, θα χρειαζόμασταν παρενθέσεις
```

### BETWEEN (inclusive)

```sql
SELECT * FROM Orders WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Display all cities whose humidity is in the range 60 to 75.

a) SELECT * FROM weather WHERE humidity IN (60 to 75)
b) SELECT * FROM weather WHERE humidity BETWEEN 60 AND 75 ✓
c) SELECT * FROM weather WHERE humidity NOT IN (60 AND 75)
d) SELECT * FROM weather WHERE humidity NOT BETWEEN 60 AND 75

ΑΠΑΝΤΗΣΗ: B
```

### LIKE Patterns

```sql
SELECT * FROM Customers WHERE name LIKE 'A%';      -- Ξεκινάει με A
SELECT * FROM Customers WHERE name LIKE '%son';    -- Τελειώνει σε son
SELECT * FROM Customers WHERE name LIKE '%ann%';   -- Περιέχει ann
SELECT * FROM Customers WHERE name LIKE '_ohn';    -- ?ohn (4 χαρακτήρες)
SELECT * FROM Customers WHERE name LIKE '__n%';    -- 3ος χαρακτήρας = n
```

### LIKE Pattern Reference

| Pattern | Matches |
|---------|---------|
| `'A%'` | Starts with A |
| `'%A'` | Ends with A |
| `'%A%'` | Contains A |
| `'A_B'` | A + any single char + B |
| `'__%'` | At least 2 characters |
| `'p%'` | Starts with p |

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Get all data from student table whose name starts with p.

a) SELECT * FROM student WHERE name LIKE '%p%';
b) SELECT * FROM student WHERE name LIKE 'p%'; ✓
c) SELECT * FROM student WHERE name LIKE '_p%';
d) SELECT * FROM student WHERE name LIKE '%p';

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: 'p%' = starts with p
```

---

## 4. JOINs

### NATURAL JOIN

Αυτόματη σύνδεση σε **κοινά column names**:
```sql
SELECT * FROM Orders NATURAL JOIN Customers;
-- Συνδέει αυτόματα στο customer_id (αν υπάρχει και στους δύο)
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Which of the following can replace the below query?
   SELECT name, course_id
   FROM instructor, teaches
   WHERE instructor_ID = teaches_ID;

a) SELECT name, course_id FROM instructor NATURAL JOIN teaches; ✓
b) SELECT name, course_id FROM teaches, instructor WHERE instructor_id=course_id;
c) SELECT name, course_id FROM instructor;
d) SELECT course_id FROM instructor JOIN teaches;

ΑΠΑΝΤΗΣΗ: A
```

### INNER JOIN

Explicit σύνδεση:
```sql
SELECT *
FROM Orders o
INNER JOIN Customers c ON o.customer_id = c.customer_id;
```

### OUTER JOINs

```sql
-- LEFT OUTER JOIN: Όλα τα rows από αριστερά + matches
SELECT * FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id;
-- Επιστρέφει και customers χωρίς orders (με NULL στα order columns)

-- RIGHT OUTER JOIN: Όλα τα rows από δεξιά + matches
SELECT * FROM Customers c
RIGHT JOIN Orders o ON c.customer_id = o.customer_id;

-- FULL OUTER JOIN: Όλα τα rows από αμφότερα
SELECT * FROM Customers c
FULL OUTER JOIN Orders o ON c.customer_id = o.customer_id;
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Which type of JOIN is used to return rows that do NOT have matching values?

a) Natural JOIN
b) Outer JOIN ✓
c) EQUI JOIN
d) All of the above

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Outer JOINs επιστρέφουν και non-matching rows (με NULLs)
```

### Self-Join

Ένας πίνακας με τον εαυτό του:
```sql
-- Βρες υπαλλήλους που έχουν τον ίδιο manager
SELECT e1.name, e2.name
FROM Employees e1
JOIN Employees e2 ON e1.manager_id = e2.manager_id
WHERE e1.employee_id < e2.employee_id;
```

---

## 5. Aggregation Functions

### Βασικές Συναρτήσεις
```sql
SELECT
    COUNT(*),           -- Αριθμός rows
    COUNT(column),      -- Αριθμός non-NULL values
    COUNT(DISTINCT col),-- Αριθμός unique values
    SUM(amount),        -- Άθροισμα
    AVG(amount),        -- Μέσος όρος
    MIN(price),         -- Ελάχιστο
    MAX(price)          -- Μέγιστο
FROM Orders;
```

### GROUP BY

Ομαδοποίηση για aggregation:
```sql
SELECT category, SUM(sales) as total_sales
FROM Products
GROUP BY category;
```

### HAVING vs WHERE

| WHERE | HAVING |
|-------|--------|
| Φιλτράρει **rows** | Φιλτράρει **groups** |
| Πριν το GROUP BY | Μετά το GROUP BY |
| Δεν δέχεται aggregates | Δέχεται aggregates |

```sql
-- WHERE: Φιλτράρει πριν την ομαδοποίηση
SELECT category, SUM(sales)
FROM Products
WHERE price > 10           -- Αποκλείει products με price <= 10
GROUP BY category;

-- HAVING: Φιλτράρει μετά την ομαδοποίηση
SELECT category, SUM(sales) as total
FROM Products
GROUP BY category
HAVING SUM(sales) > 1000;  -- Αποκλείει categories με total <= 1000
```

**Σειρά εκτέλεσης**:
1. FROM
2. WHERE (φιλτράρει rows)
3. GROUP BY (ομαδοποίηση)
4. HAVING (φιλτράρει groups)
5. SELECT
6. ORDER BY

---

## 6. Exam SQL Queries - ΑΠΟΜΝΗΜΟΝΕΥΣΕ!

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25 - Total QuantitySold per BookID
```sql
-- Schema: Sales(SaleID, BookID, SaleDate, QuantitySold)

SELECT BookID, SUM(QuantitySold) AS TotalQuantitySold
FROM Sales
GROUP BY BookID;
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25 - Title and Total Sales > 100
```sql
-- Schema: Books(BookID, Title, AuthorID, Genre, Price)
--         Sales(SaleID, BookID, SaleDate, QuantitySold)

SELECT Books.Title, SUM(Sales.QuantitySold) AS TotalSales
FROM Books
JOIN Sales ON Books.BookID = Sales.BookID
GROUP BY Books.Title
HAVING SUM(Sales.QuantitySold) > 100;
```

**ΠΡΟΣΟΧΗ**:
- Χρησιμοποίησε `JOIN` για να συνδέσεις τους πίνακες
- `GROUP BY` το attribute που δεν είναι aggregate
- `HAVING` για condition στο aggregate

---

## 7. UPDATE & INSERT

### INSERT
```sql
INSERT INTO Customers (customer_id, name, city)
VALUES (1, 'John', 'Athens');

-- Insert multiple rows
INSERT INTO Customers (customer_id, name, city)
VALUES (1, 'John', 'Athens'),
       (2, 'Maria', 'Patras'),
       (3, 'Nikos', 'Thessaloniki');
```

### UPDATE

```sql
UPDATE Products
SET price = price * 1.10    -- Αύξηση 10%
WHERE category = 'Electronics';
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23 - ΚΡΙΣΙΜΟ!
```
Q: What does the following query do?
   UPDATE student
   SET marks = marks * 1.20;

a) Increases marks by 120%
b) Decreases marks by 20%
c) Increases marks by 20% ✓
d) None of the above

ΑΠΑΝΤΗΣΗ: C
ΕΞΗΓΗΣΗ: marks * 1.20 = marks + (marks * 0.20) = αύξηση 20%
         Αν marks = 80, νέο marks = 80 × 1.20 = 96

ΣΥΧΝΟ ΛΑΘΟΣ: Πολλοί νομίζουν ότι * 1.20 = 120% αύξηση!
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: How can you change "Thomas" into "Michel" in the "LastName" column?

a) UPDATE User SET LastName = 'Thomas' INTO LastName = 'Michel'
b) MODIFY Users SET LastName = 'Michel' WHERE LastName = 'Thomas'
c) MODIFY Users SET LastName = 'Thomas' INTO LastName = 'Michel'
d) UPDATE Users SET LastName = 'Michel' WHERE LastName = 'Thomas' ✓

ΑΠΑΝΤΗΣΗ: D
ΕΞΗΓΗΣΗ: UPDATE table SET column = new_value WHERE condition
```

### DELETE
```sql
DELETE FROM Orders
WHERE order_date < '2020-01-01';
```

---

## 8. CASE Statement

IF-THEN-ELSE στην SQL:

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: A CASE SQL statement is ______?

a) A way to establish a loop in SQL
b) A way to establish an IF-THEN-ELSE in SQL ✓
c) A way to establish a data definition in SQL
d) All of the above

ΑΠΑΝΤΗΣΗ: B
```

```sql
SELECT name, salary,
    CASE
        WHEN salary > 50000 THEN 'High'
        WHEN salary > 30000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM Employees;

-- Με aggregation
SELECT
    SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) as completed,
    SUM(CASE WHEN status = 'Pending' THEN 1 ELSE 0 END) as pending
FROM Orders;
```

---

## 9. SQL Logical Operators

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2022-23
```
Q: Which of the following are valid logical operators in SQL?

A) SOME
B) ALL
C) AND
D) All of the above ✓

ΑΠΑΝΤΗΣΗ: D
```

---

## 10. NULL Handling - ΚΡΙΣΙΜΟ!

```sql
-- ΠΡΟΣΟΧΗ: NULL comparisons
SELECT * FROM Products WHERE price = NULL;  -- ΛΑΘΟΣ! Επιστρέφει 0 rows
SELECT * FROM Products WHERE price IS NULL; -- ΣΩΣΤΟ

-- Aggregates αγνοούν NULLs
SELECT AVG(price) FROM Products;  -- NULLs δεν μετράνε
SELECT COUNT(price) FROM Products; -- Μόνο non-NULL
SELECT COUNT(*) FROM Products;     -- Όλα τα rows
```

**ΘΥΜΗΣΟΥ**:
- `NULL = NULL` → UNKNOWN (όχι TRUE!)
- Χρησιμοποίησε `IS NULL` / `IS NOT NULL`
- `COUNT(*)` μετράει ΟΛΕΣ τις rows
- `COUNT(column)` μετράει μόνο non-NULL

---

## 11. Relational Algebra

### Βασικοί Operators

| Σύμβολο | Όνομα | Λειτουργία | SQL Equivalent |
|---------|-------|------------|----------------|
| σ (sigma) | Selection | Επιλογή **rows** | WHERE |
| π (pi) | Projection | Επιλογή **columns** | SELECT |
| × | Cartesian Product | Όλοι οι συνδυασμοί | FROM A, B |
| ⋈ | Natural Join | Join σε κοινά attributes | NATURAL JOIN |
| ∪ | Union | Ένωση (χωρίς duplicates) | UNION |
| ∩ | Intersection | Κοινά tuples | INTERSECT |
| − | Difference | Tuples στο 1ο αλλά όχι στο 2ο | EXCEPT |

### Παραδείγματα

```
σ_price>100(Products)
= SELECT * FROM Products WHERE price > 100

π_name,price(Products)
= SELECT name, price FROM Products

π_name(σ_price>100(Products))
= SELECT name FROM Products WHERE price > 100
```

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25
```
Q: Suppose you have R(A, B, C) and apply:
   π_{A,C}(σ_{B='X'}(R)) ∩ π_{A,C}(σ_{B='Y'}(R))

What does the result represent?

a) All (A, C) pairs that appear for both B='X' and B='Y' ✓
b) All (A, C) pairs that appear for either B='X' or B='Y'
c) All (A, C) pairs that appear only when B='X' but not when B='Y'
d) All tuples from R that satisfy both B='X' and B='Y' simultaneously

ΑΠΑΝΤΗΣΗ: A
ΕΞΗΓΗΣΗ:
- Πρώτο μέρος: (A,C) pairs όπου B='X'
- Δεύτερο μέρος: (A,C) pairs όπου B='Y'
- INTERSECT: Κοινά σε ΑΜΦΟΤΕΡΑ

SQL equivalent:
SELECT A, C FROM R WHERE B = 'X'
INTERSECT
SELECT A, C FROM R WHERE B = 'Y'
```

---

## 12. Σύνθετες Ερωτήσεις Εξετάσεων

### Second Highest Salary
```sql
SELECT MAX(salary)
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees);

-- Ή με LIMIT/OFFSET
SELECT DISTINCT salary
FROM Employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

### Customers που αγόρασαν από ΚΑΘΕ category
```sql
SELECT c.customer_id, c.name
FROM Customers c
WHERE NOT EXISTS (
    SELECT category FROM Categories
    EXCEPT
    SELECT DISTINCT p.category
    FROM Orders o
    JOIN Products p ON o.product_id = p.product_id
    WHERE o.customer_id = c.customer_id
);
```

### Correlated Subquery
```sql
-- Employees που κερδίζουν περισσότερο από τον μέσο όρο του department τους
SELECT e1.name, e1.salary, e1.dept
FROM Employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM Employees e2
    WHERE e2.dept = e1.dept
);
```

---

## Σύνοψη - Key Points για 10/10

### SQL Execution Order
```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

### Operator Precedence
```
AND πριν από OR!

a OR b AND c = a OR (b AND c)
```

### Quick Reference

| Τι θέλω | Χρησιμοποιώ |
|---------|-------------|
| Φιλτράρισμα rows | WHERE |
| Φιλτράρισμα groups | HAVING |
| Unique values | DISTINCT |
| Pattern matching | LIKE |
| Range check | BETWEEN |
| NULL check | IS NULL / IS NOT NULL |
| Αύξηση 20% | * 1.20 |
| Μείωση 20% | * 0.80 |

### Relational Algebra
```
σ (sigma) = SELECT (rows)
π (pi) = PROJECT (columns)
```

### Join Types
- **NATURAL JOIN**: Automatic on common columns
- **INNER JOIN**: Only matching rows
- **OUTER JOIN**: Include non-matching (with NULL)

### Aggregation
- **GROUP BY**: Ομαδοποίηση
- **HAVING**: Φίλτρο μετά την ομαδοποίηση
- **COUNT(*)**: Όλες οι rows
- **COUNT(col)**: Non-NULL μόνο
