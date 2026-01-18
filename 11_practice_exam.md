# Εξάσκηση Εξετάσεων - Practice Exam

## Οδηγίες
- Διάρκεια: 75 λεπτά
- Multiple Choice: 5 μόρια ανά ερώτηση
- Open-ended: 8 μόρια ανά ερώτηση
- Σύνολο: 100 μόρια

---

# ΜΕΡΟΣ Α: Multiple Choice (60 μόρια)

## Ερώτηση 1 (OLAP)
Ποια λειτουργία OLAP μετατρέπει τα δεδομένα από επίπεδο ημέρας σε επίπεδο μήνα;

a) Slice
b) Drill-down
c) **Roll-up**
d) Pivot

<details>
<summary>Απάντηση</summary>

**Σωστό: (c) Roll-up**

Roll-up = aggregation = λιγότερη λεπτομέρεια (day → month → year)
</details>

---

## Ερώτηση 2 (Query Processing)
Ποιος join αλγόριθμος είναι κατάλληλος για τη συνθήκη `A.price > B.price`?

a) Hash Join
b) Sort-Merge Join
c) **Nested Loop Join**
d) Κανένας από τους παραπάνω

<details>
<summary>Απάντηση</summary>

**Σωστό: (c) Nested Loop Join**

Hash Join και Sort-Merge δουλεύουν μόνο για equality (=). Για inequality (>, <, ≤, ≥) χρειάζεται Nested Loop.
</details>

---

## Ερώτηση 3 (Attribute Types)
Η θερμοκρασία σε βαθμούς Celsius είναι:

a) Nominal
b) Ordinal
c) **Interval**
d) Ratio

<details>
<summary>Απάντηση</summary>

**Σωστό: (c) Interval**

Το 0°C δεν σημαίνει "καμία θερμοκρασία". Δεν μπορούμε να πούμε "20°C είναι διπλάσια θερμοκρασία από 10°C". Αντίθετα, θερμοκρασία σε Kelvin είναι Ratio (0K = απόλυτο μηδέν).
</details>

---

## Ερώτηση 4 (Bloom Filter)
Τι ισχύει για τα Bloom Filters;

a) Μπορεί να έχουν false negatives αλλά όχι false positives
b) **Μπορεί να έχουν false positives αλλά όχι false negatives**
c) Μπορεί να έχουν και false positives και false negatives
d) Δεν μπορεί να έχουν κανένα σφάλμα

<details>
<summary>Απάντηση</summary>

**Σωστό: (b)**

Bloom Filter: "No" = ΣΙΓΟΥΡΑ δεν ανήκει, "Yes" = ΙΣΩΣ ανήκει. Άρα false positives ναι, false negatives ΠΟΤΕ.
</details>

---

## Ερώτηση 5 (SQL)
Ποια είναι η σωστή σειρά εκτέλεσης SQL clauses;

a) SELECT → FROM → WHERE → GROUP BY → HAVING
b) FROM → SELECT → WHERE → GROUP BY → HAVING
c) **FROM → WHERE → GROUP BY → HAVING → SELECT**
d) WHERE → FROM → GROUP BY → SELECT → HAVING

<details>
<summary>Απάντηση</summary>

**Σωστό: (c) FROM → WHERE → GROUP BY → HAVING → SELECT**

(Και μετά ORDER BY)
</details>

---

## Ερώτηση 6 (E-R Diagrams)
Για μια M:N relationship μεταξύ δύο entities, η μετατροπή σε σχεσιακό σχήμα απαιτεί:

a) Προσθήκη FK σε ένα από τα entities
b) Προσθήκη FK και στα δύο entities
c) **Δημιουργία νέου πίνακα με τα PKs και των δύο entities**
d) Χρήση composite primary key σε ένα entity

<details>
<summary>Απάντηση</summary>

**Σωστό: (c)**

M:N relationship → νέος πίνακας (junction table) με composite PK από τα PKs και των δύο entities.
</details>

---

## Ερώτηση 7 (Count-Min Sketch)
Το Count-Min Sketch:

a) Μπορεί να υποεκτιμήσει τη συχνότητα
b) **Μπορεί μόνο να υπερεκτιμήσει τη συχνότητα**
c) Δίνει πάντα ακριβή αποτελέσματα
d) Χρησιμοποιείται για membership testing

<details>
<summary>Απάντηση</summary>

**Σωστό: (b)**

Count-Min Sketch: estimate ≥ actual (πάντα overestimate, ποτέ underestimate)
</details>

---

## Ερώτηση 8 (HMM)
Στον αλγόριθμο Forward για HMM, η αναδρομική σχέση είναι:

a) αₜ(j) = Σᵢ αₜ₋₁(i) × aᵢⱼ
b) **αₜ(j) = [Σᵢ αₜ₋₁(i) × aᵢⱼ] × bⱼ(oₜ)**
c) αₜ(j) = maxᵢ [αₜ₋₁(i) × aᵢⱼ] × bⱼ(oₜ)
d) αₜ(j) = πⱼ × bⱼ(oₜ)

<details>
<summary>Απάντηση</summary>

**Σωστό: (b)**

Forward: ΑΘΡΟΙΣΗ (Σ) και ΜΗΝ ΞΕΧΝΑΣ το emission probability bⱼ(oₜ)!

Η (c) είναι για Viterbi (max αντί Σ), η (d) είναι η αρχικοποίηση.
</details>

---

## Ερώτηση 9 (Pipelining)
Ποιος από τους παρακάτω τελεστές είναι blocking;

a) Selection (σ)
b) Projection (π)
c) **Sort**
d) Nested Loop Join (outer loop)

<details>
<summary>Απάντηση</summary>

**Σωστό: (c) Sort**

Sort χρειάζεται να δει ΟΛΑ τα δεδομένα πριν παράγει output. Selection, Projection και NL outer είναι pipelined.
</details>

---

## Ερώτηση 10 (OLAP Schemas)
Ποια είναι η διαφορά μεταξύ Star Schema και Snowflake Schema;

a) **Star έχει αποκανονικοποιημένα dimensions, Snowflake κανονικοποιημένα**
b) Star έχει κανονικοποιημένα dimensions, Snowflake αποκανονικοποιημένα
c) Star χρησιμοποιείται για OLTP, Snowflake για OLAP
d) Δεν υπάρχει ουσιαστική διαφορά

<details>
<summary>Απάντηση</summary>

**Σωστό: (a)**

Star = denormalized dimensions (λιγότερα joins, πιο γρήγορο)
Snowflake = normalized dimensions (λιγότερο redundancy, περισσότερα joins)
</details>

---

## Ερώτηση 11 (Relational Algebra)
Τι επιστρέφει η έκφραση: `π_A(R) − π_A(S)`?

a) Όλες τις τιμές του A που υπάρχουν και στο R και στο S
b) **Όλες τις τιμές του A που υπάρχουν στο R αλλά ΟΧΙ στο S**
c) Όλες τις τιμές του A που υπάρχουν στο S αλλά ΟΧΙ στο R
d) Καμία από τις παραπάνω

<details>
<summary>Απάντηση</summary>

**Σωστό: (b)**

Η διαφορά συνόλων R − S επιστρέφει τα στοιχεία που υπάρχουν στο R αλλά ΟΧΙ στο S.
</details>

---

## Ερώτηση 12 (Data Preprocessing)
Equal-width binning με min=10, max=50, k=4 bins. Ποιο είναι το πλάτος κάθε bin;

a) 4
b) **10**
c) 12.5
d) 40

<details>
<summary>Απάντηση</summary>

**Σωστό: (b) 10**

Width = (max - min) / k = (50 - 10) / 4 = 40 / 4 = 10
</details>

---

# ΜΕΡΟΣ Β: Open-Ended Questions (40 μόρια)

## Ερώτηση 13 (8 μόρια)

**Schema:**
- Employee(eid, name, dept_id, salary)
- Department(did, dname, budget)

**Ερώτημα:** Γράψτε SQL query για να βρείτε τα τμήματα με μέσο μισθό πάνω από 50000.

<details>
<summary>Απάντηση</summary>

```sql
SELECT D.dname, AVG(E.salary) AS avg_salary
FROM Employee E
JOIN Department D ON E.dept_id = D.did
GROUP BY D.dname
HAVING AVG(E.salary) > 50000;
```

**Εξήγηση:**
- JOIN για σύνδεση Employee με Department
- GROUP BY για ομαδοποίηση κατά τμήμα
- HAVING (όχι WHERE!) για φιλτράρισμα με aggregate function
</details>

---

## Ερώτηση 14 (8 μόρια)

**Schema:**
- Student(sid, name, major)
- Course(cid, title, credits)
- Enrolls(sid, cid, grade)

**Ερώτημα:** Γράψτε σε Relational Algebra τους φοιτητές που έχουν πάρει ΟΛΑ τα μαθήματα με credits ≥ 4.

<details>
<summary>Απάντηση</summary>

```
π_sid,name(Student ⋈ (π_sid,cid(Enrolls) ÷ π_cid(σ_credits≥4(Course))))
```

**Εξήγηση βήμα-βήμα:**
1. `σ_credits≥4(Course)` - Μαθήματα με ≥4 credits
2. `π_cid(...)` - Μόνο τα course IDs
3. `π_sid,cid(Enrolls)` - Ζεύγη φοιτητή-μαθήματος
4. `÷` - Division: φοιτητές που έχουν ΟΛΑ τα μαθήματα
5. Join με Student για να πάρουμε τα ονόματα
</details>

---

## Ερώτηση 15 (8 μόρια)

**Δίνεται HMM με:**
- States: S = {s₁, s₂}
- Symbols: Σ = {a, b}
- Initial: Π = {0.6, 0.4}
- Transition: A = [[0.7, 0.3], [0.4, 0.6]]
- Emission: B = [[0.9, 0.1], [0.2, 0.8]]

**Υπολογίστε:** P(O = {a, b} | λ) χρησιμοποιώντας τον Forward Algorithm.

<details>
<summary>Απάντηση</summary>

**Βήμα 1: Αρχικοποίηση (o₁ = a)**
```
α₁(s₁) = π₁ × b₁(a) = 0.6 × 0.9 = 0.54
α₁(s₂) = π₂ × b₂(a) = 0.4 × 0.2 = 0.08
```

**Βήμα 2: Επαγωγή (o₂ = b)**
```
α₂(s₁) = [α₁(s₁) × a₁₁ + α₁(s₂) × a₂₁] × b₁(b)
       = [0.54 × 0.7 + 0.08 × 0.4] × 0.1
       = [0.378 + 0.032] × 0.1
       = 0.41 × 0.1
       = 0.041

α₂(s₂) = [α₁(s₁) × a₁₂ + α₁(s₂) × a₂₂] × b₂(b)
       = [0.54 × 0.3 + 0.08 × 0.6] × 0.8
       = [0.162 + 0.048] × 0.8
       = 0.21 × 0.8
       = 0.168
```

**Βήμα 3: Τερματισμός**
```
P(O|λ) = α₂(s₁) + α₂(s₂) = 0.041 + 0.168 = 0.209
```

**Απάντηση: P({a, b}) = 0.209 ή 20.9%**
</details>

---

## Ερώτηση 16 (8 μόρια)

**Δίνεται data warehouse με διαστάσεις:**
- Time (day, month, year)
- Product (product_id, category, department)
- Store (store_id, city, region)
- Measure: sales_amount

**Ξεκινώντας από cuboid {day, product_id, store_id}:**

Ποιες OLAP λειτουργίες χρειάζονται για να βρούμε τις συνολικές πωλήσεις ανά κατηγορία προϊόντος και περιοχή για το 2024;

<details>
<summary>Απάντηση</summary>

1. **Roll-up on Time:** day → month → year
   - Cuboid: {year, product_id, store_id}

2. **Roll-up on Product:** product_id → category
   - Cuboid: {year, category, store_id}

3. **Roll-up on Store:** store_id → city → region
   - Cuboid: {year, category, region}

4. **Slice:** year = 2024
   - Cuboid: {year=2024, category, region}

**Τελικό αποτέλεσμα:** Πωλήσεις ανά (category, region) για το 2024

**Σημείωση:** Θα μπορούσαμε να κάνουμε Dice αντί για Slice αν θέλαμε να φιλτράρουμε και άλλες διαστάσεις ταυτόχρονα.
</details>

---

## Ερώτηση 17 (8 μόρια)

**Σχεδιάστε E-R διάγραμμα για ένα σύστημα βιβλιοθήκης:**

Απαιτήσεις:
- Βιβλία με ISBN, τίτλο, έτος έκδοσης
- Συγγραφείς με ID, όνομα, εθνικότητα
- Ένα βιβλίο μπορεί να έχει πολλούς συγγραφείς
- Ένας συγγραφέας μπορεί να έχει γράψει πολλά βιβλία
- Μέλη βιβλιοθήκης με ID, όνομα, διεύθυνση
- Ένα μέλος μπορεί να δανειστεί πολλά βιβλία (με ημερομηνία δανεισμού)

Μετατρέψτε το E-R σε σχεσιακό σχήμα.

<details>
<summary>Απάντηση</summary>

**E-R Entities:**
- Book(ISBN, title, year)
- Author(author_id, name, nationality)
- Member(member_id, name, address)

**E-R Relationships:**
- writes: Author -- M:N -- Book
- borrows: Member -- M:N -- Book (με ημερομηνία)

**Σχεσιακό Σχήμα:**

```sql
Book(ISBN, title, year)
    PK: ISBN

Author(author_id, name, nationality)
    PK: author_id

Member(member_id, name, address)
    PK: member_id

-- M:N: Author-Book
WrittenBy(ISBN, author_id)
    PK: (ISBN, author_id)
    FK: ISBN REFERENCES Book(ISBN)
    FK: author_id REFERENCES Author(author_id)

-- M:N: Member-Book με attribute
Borrows(member_id, ISBN, borrow_date)
    PK: (member_id, ISBN, borrow_date)
    FK: member_id REFERENCES Member(member_id)
    FK: ISBN REFERENCES Book(ISBN)
```

**Σημείωση:** Το borrow_date περιλαμβάνεται στο PK του Borrows για να επιτρέπονται πολλαπλοί δανεισμοί του ίδιου βιβλίου από το ίδιο μέλος σε διαφορετικές ημερομηνίες.
</details>

---

# Κλείδα Βαθμολόγησης

| Μέρος | Ερωτήσεις | Μόρια |
|-------|-----------|-------|
| Α (MC) | 1-12 | 12 × 5 = 60 |
| Β (Open) | 13-17 | 5 × 8 = 40 |
| **Σύνολο** | | **100** |

---

# Επιπλέον Ασκήσεις Εξάσκησης

## Άσκηση Α: SQL Division
Βρείτε τα ονόματα των πελατών που έχουν αγοράσει ΟΛΑ τα προϊόντα.

## Άσκηση Β: Bin Smoothing
Εφαρμόστε smoothing by bin means στα δεδομένα: 2, 4, 6, 8, 15, 20, 22, 25 με bin depth = 4.

## Άσκηση Γ: Viterbi
Χρησιμοποιήστε το HMM της ερώτησης 15 για να βρείτε το πιο πιθανό path για O = {a, b}.

## Άσκηση Δ: OLAP Cube
Αν έχουμε 3 διαστάσεις με 10, 20, 30 τιμές αντίστοιχα:
1. Πόσα cuboids υπάρχουν;
2. Πόσα κελιά έχει ο πλήρης cube (με ALL)?
