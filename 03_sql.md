# SQL - Βασικά & Προχωρημένα

## Σειρά Εκτέλεσης SQL - ΚΡΙΣΙΜΟ!

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

| Βήμα | Περιγραφή |
|------|-----------|
| FROM | Ποιοι πίνακες; (+ JOINs) |
| WHERE | Φιλτράρισμα γραμμών ΠΡΙΝ grouping |
| GROUP BY | Ομαδοποίηση |
| HAVING | Φιλτράρισμα ΜΕΤΑ grouping (με aggregates) |
| SELECT | Επιλογή στηλών/υπολογισμοί |
| ORDER BY | Ταξινόμηση αποτελεσμάτων |

---

## Βασικές Εντολές

### SELECT - Επιλογή Δεδομένων

```sql
-- Βασική σύνταξη
SELECT column1, column2
FROM table_name
WHERE condition;

-- Όλες οι στήλες
SELECT * FROM Employees;

-- Μοναδικές τιμές
SELECT DISTINCT department FROM Employees;

-- Με alias
SELECT name AS employee_name FROM Employees;
```

### WHERE - Φιλτράρισμα

```sql
-- Σύγκριση
WHERE salary > 50000
WHERE department = 'CS'
WHERE hire_date >= '2020-01-01'

-- Λογικοί τελεστές
WHERE salary > 50000 AND department = 'CS'
WHERE salary > 50000 OR department = 'HR'
WHERE NOT department = 'Sales'

-- Ειδικοί τελεστές
WHERE salary BETWEEN 40000 AND 60000
WHERE department IN ('CS', 'Math', 'Physics')
WHERE name LIKE 'A%'        -- Αρχίζει με A
WHERE name LIKE '%son'      -- Τελειώνει με son
WHERE name LIKE '%an%'      -- Περιέχει an
WHERE manager_id IS NULL
WHERE manager_id IS NOT NULL
```

---

## JOIN - Ένωση Πινάκων

### Τύποι JOIN

| Τύπος | Περιγραφή |
|-------|-----------|
| INNER JOIN | Μόνο matching rows |
| LEFT JOIN | Όλα από αριστερά + matching από δεξιά |
| RIGHT JOIN | Όλα από δεξιά + matching από αριστερά |
| FULL OUTER JOIN | Όλα από αμφότερα |
| CROSS JOIN | Καρτεσιανό γινόμενο |
| NATURAL JOIN | Αυτόματο join σε κοινές στήλες |

### Παραδείγματα JOIN

```sql
-- INNER JOIN (πιο συνηθισμένο)
SELECT E.name, D.dept_name
FROM Employees E
INNER JOIN Departments D ON E.dept_id = D.id;

-- LEFT JOIN
SELECT E.name, D.dept_name
FROM Employees E
LEFT JOIN Departments D ON E.dept_id = D.id;

-- Multiple JOINs
SELECT S.name, C.title, E.grade
FROM Students S
JOIN Enrolls E ON S.sid = E.sid
JOIN Courses C ON E.cid = C.cid;

-- NATURAL JOIN
SELECT *
FROM Students NATURAL JOIN Enrolls;
```

---

## Aggregate Functions (Συναθροιστικές Συναρτήσεις)

| Συνάρτηση | Περιγραφή |
|-----------|-----------|
| COUNT(*) | Πλήθος γραμμών |
| COUNT(col) | Πλήθος non-NULL τιμών |
| SUM(col) | Άθροισμα |
| AVG(col) | Μέσος όρος |
| MIN(col) | Ελάχιστη τιμή |
| MAX(col) | Μέγιστη τιμή |

```sql
SELECT COUNT(*) FROM Employees;
SELECT AVG(salary) FROM Employees WHERE department = 'CS';
SELECT department, COUNT(*) FROM Employees GROUP BY department;
```

---

## GROUP BY & HAVING

### GROUP BY

```sql
-- Πλήθος υπαλλήλων ανά τμήμα
SELECT department, COUNT(*) AS num_employees
FROM Employees
GROUP BY department;

-- Μέσος μισθός ανά τμήμα
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department;
```

### HAVING vs WHERE

| WHERE | HAVING |
|-------|--------|
| ΠΡΙΝ grouping | ΜΕΤΑ grouping |
| Φιλτράρει γραμμές | Φιλτράρει ομάδες |
| ΔΕΝ χρησιμοποιεί aggregates | ΧΡΗΣΙΜΟΠΟΙΕΙ aggregates |

```sql
-- ΛΑΘΟΣ: Aggregate στο WHERE
SELECT department, AVG(salary)
FROM Employees
WHERE AVG(salary) > 50000  -- ❌ ERROR!
GROUP BY department;

-- ΣΩΣΤΟ: Aggregate στο HAVING
SELECT department, AVG(salary)
FROM Employees
GROUP BY department
HAVING AVG(salary) > 50000;  -- ✓
```

---

## Subqueries (Υποερωτήματα)

### Τύποι Subqueries

```sql
-- Scalar subquery (μία τιμή)
SELECT name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);

-- IN subquery (σύνολο τιμών)
SELECT name
FROM Employees
WHERE dept_id IN (SELECT id FROM Departments WHERE budget > 1000000);

-- EXISTS subquery (ύπαρξη)
SELECT name
FROM Employees E
WHERE EXISTS (
    SELECT 1 FROM Projects P
    WHERE P.manager_id = E.id
);

-- NOT EXISTS
SELECT name
FROM Employees E
WHERE NOT EXISTS (
    SELECT 1 FROM Violations V
    WHERE V.employee_id = E.id
);
```

### Correlated vs Non-Correlated

**Non-correlated:** Το subquery εκτελείται ΜΙΑ φορά
```sql
SELECT * FROM E WHERE salary > (SELECT AVG(salary) FROM E);
```

**Correlated:** Το subquery εκτελείται για ΚΑΘΕ γραμμή του outer query
```sql
SELECT * FROM E e1
WHERE salary > (SELECT AVG(salary) FROM E e2 WHERE e2.dept = e1.dept);
```

---

## SQL Division (Για Όλα Queries)

### Πρόβλημα: "Βρες X που σχετίζονται με ΟΛΑ τα Y"

**Μέθοδος 1: Double NOT EXISTS**
```sql
-- Φοιτητές εγγεγραμμένοι σε ΟΛΑ τα μαθήματα
SELECT S.name
FROM Students S
WHERE NOT EXISTS (
    SELECT C.cid FROM Courses C
    WHERE NOT EXISTS (
        SELECT E.sid FROM Enrolls E
        WHERE E.sid = S.sid AND E.cid = C.cid
    )
);
```

**Μέθοδος 2: COUNT comparison**
```sql
-- Φοιτητές εγγεγραμμένοι σε ΟΛΑ τα μαθήματα
SELECT E.sid
FROM Enrolls E
GROUP BY E.sid
HAVING COUNT(DISTINCT E.cid) = (SELECT COUNT(*) FROM Courses);
```

---

## Λυμένα Παραδείγματα

### Παράδειγμα 1: Εξέταση 2025 Q13

**Schema:**
- Books(BookID, Title, AuthorID, Genre, Price)
- Authors(AuthorID, FirstName, LastName, Country)
- Sales(SaleID, BookID, SaleDate, QuantitySold)

**Ερώτημα:** Βρες το συνολικό QuantitySold για κάθε BookID. Επέστρεψε BookID και TotalQuantitySold.

**Λύση:**
```sql
SELECT BookID, SUM(QuantitySold) AS TotalQuantitySold
FROM Sales
GROUP BY BookID;
```

---

### Παράδειγμα 2: Εξέταση 2025 Q14

**Ερώτημα:** Βρες τον τίτλο και τις συνολικές πωλήσεις για κάθε βιβλίο όπου οι πωλήσεις ξεπερνούν τις 100 μονάδες.

**Λύση:**
```sql
SELECT Books.Title, SUM(Sales.QuantitySold) AS TotalSales
FROM Books
JOIN Sales ON Books.BookID = Sales.BookID
GROUP BY Books.Title
HAVING SUM(Sales.QuantitySold) > 100;
```

**Εξήγηση:**
1. JOIN Books με Sales για να συνδέσουμε τίτλους με πωλήσεις
2. GROUP BY Title για να ομαδοποιήσουμε κατά βιβλίο
3. HAVING (όχι WHERE!) για φιλτράρισμα με aggregate

---

### Παράδειγμα 3: HW1 2025 - Top 10 Καθηγητές

**Schema:**
- Professor(prof_id, pname, department, office_num)
- Publication(pub_id, title, venue, year)
- Writes(prof_id, pub_id)

**Ερώτημα:** Βρες τα ονόματα και IDs των 10 πιο παραγωγικών καθηγητών.

**Λύση:**
```sql
SELECT P.pname, P.prof_id
FROM Professor P
JOIN Writes W ON P.prof_id = W.prof_id
GROUP BY P.prof_id, P.pname
ORDER BY COUNT(*) DESC
LIMIT 10;
```

---

### Παράδειγμα 4: HW1 2025 - Τμήματα με Πρώτη Δημοσίευση μετά το 2005

**Ερώτημα:** Βρες τα τμήματα για τα οποία η πρώτη δημοσίευση καθηγητή του τμήματος ήταν μετά το 2005.

**Λύση:**
```sql
SELECT P.department
FROM Professor P
JOIN Writes W ON P.prof_id = W.prof_id
JOIN Publication Pub ON W.pub_id = Pub.pub_id
GROUP BY P.department
HAVING MIN(Pub.year) > 2005;
```

**Εξήγηση:**
- MIN(year) βρίσκει την πρώτη (παλαιότερη) δημοσίευση
- HAVING MIN(year) > 2005 κρατάει μόνο τμήματα που η πρώτη δημοσίευση ήταν μετά το 2005

---

### Παράδειγμα 5: HW1 2025 - Division με NOT EXISTS

**Ερώτημα:** Βρες τους τίτλους δημοσιεύσεων που έχουν συν-συγγραφεί από ΟΛΟΥΣ τους καθηγητές του 'EE' τμήματος.

**Λύση:**
```sql
SELECT Pub.title
FROM Publication Pub
WHERE NOT EXISTS (
    SELECT P.prof_id
    FROM Professor P
    WHERE P.department = 'EE'
      AND NOT EXISTS (
          SELECT W.prof_id
          FROM Writes W
          WHERE W.pub_id = Pub.pub_id
            AND W.prof_id = P.prof_id
      )
);
```

**Ανάγνωση:** "Βρες δημοσιεύσεις για τις οποίες ΔΕΝ υπάρχει καθηγητής EE που ΔΕΝ τις έχει γράψει"

---

## Συχνά Λάθη στις Εξετάσεις

### 1. WHERE αντί HAVING με aggregate
```sql
-- ❌ ΛΑΘΟΣ
WHERE COUNT(*) > 5

-- ✓ ΣΩΣΤΟ
HAVING COUNT(*) > 5
```

### 2. Ξεχνάω το GROUP BY
```sql
-- ❌ ΛΑΘΟΣ
SELECT department, AVG(salary) FROM Employees;

-- ✓ ΣΩΣΤΟ
SELECT department, AVG(salary) FROM Employees GROUP BY department;
```

### 3. SELECT στήλες εκτός GROUP BY
```sql
-- ❌ ΛΑΘΟΣ (name δεν είναι στο GROUP BY)
SELECT department, name, AVG(salary)
FROM Employees
GROUP BY department;

-- ✓ ΣΩΣΤΟ
SELECT department, AVG(salary)
FROM Employees
GROUP BY department;
```

### 4. JOIN χωρίς συνθήκη
```sql
-- ❌ ΛΑΘΟΣ (Καρτεσιανό γινόμενο!)
SELECT * FROM A, B;

-- ✓ ΣΩΣΤΟ
SELECT * FROM A JOIN B ON A.id = B.a_id;
```

---

## Γρήγορη Αναφορά

```
╔══════════════════════════════════════════════════════════════════╗
║                    SQL CHEAT SHEET                               ║
╠══════════════════════════════════════════════════════════════════╣
║ Σειρά Εκτέλεσης:                                                 ║
║   FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY           ║
╠══════════════════════════════════════════════════════════════════╣
║ WHERE vs HAVING:                                                 ║
║   WHERE:  ΠΡΙΝ grouping, ΔΕΝ δέχεται aggregates                  ║
║   HAVING: ΜΕΤΑ grouping, ΔΕΧΕΤΑΙ aggregates                      ║
╠══════════════════════════════════════════════════════════════════╣
║ Division Pattern (Για ΟΛΑ):                                      ║
║   SELECT ... WHERE NOT EXISTS (                                  ║
║       SELECT ... WHERE NOT EXISTS (...)                          ║
║   )                                                              ║
╠══════════════════════════════════════════════════════════════════╣
║ Aggregates: COUNT, SUM, AVG, MIN, MAX                            ║
╠══════════════════════════════════════════════════════════════════╣
║ JOINs: INNER, LEFT, RIGHT, FULL OUTER, CROSS, NATURAL            ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Ασκήσεις Εξάσκησης

### Άσκηση 1
Δίνονται οι πίνακες:
- Employee(eid, name, salary, dept_id)
- Department(did, dname, budget)

Γράψτε SQL για:
1. Μέσο μισθό ανά τμήμα
2. Τμήματα με budget > 1M και μέσο μισθό > 50000
3. Υπαλλήλους με μισθό πάνω από τον μέσο όρο του τμήματός τους

### Άσκηση 2
Δίνονται οι πίνακες:
- Student(sid, name)
- Course(cid, title)
- Enrolls(sid, cid, grade)

Γράψτε SQL για:
1. Φοιτητές που πήραν grade='A' σε τουλάχιστον 3 μαθήματα
2. Φοιτητές που είναι εγγεγραμμένοι σε ΟΛΑ τα μαθήματα
3. Μαθήματα χωρίς κανέναν εγγεγραμμένο φοιτητή
