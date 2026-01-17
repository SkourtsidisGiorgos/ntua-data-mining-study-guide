# ER Diagrams & Cardinality - Πλήρης Οδηγός Μελέτης

## 1. Entity-Relationship (ER) Model

### 1.1 Βασικές Έννοιες

**Entity (Οντότητα)**:
- Ένα "πράγμα" ή αντικείμενο στον πραγματικό κόσμο
- Έχει **attributes** (χαρακτηριστικά)
- Παραδείγματα: Student, Course, Employee, Department

**Attribute (Χαρακτηριστικό)**:
- Ιδιότητα μιας entity
- Παραδείγματα: name, age, student_id, salary

**Relationship (Σχέση)**:
- Σύνδεση μεταξύ δύο ή περισσότερων entities
- Παραδείγματα: "Student ENROLLS_IN Course", "Employee WORKS_FOR Department"

### 1.2 ER Diagram Notation

```
┌──────────────┐                    ┌──────────────┐
│              │                    │              │
│   STUDENT    │──── ENROLLS_IN ────│    COURSE    │
│              │                    │              │
└──────────────┘                    └──────────────┘
   Rectangle                           Rectangle
   (Entity)        Diamond            (Entity)
                 (Relationship)
```

### Σύμβολα

| Σύμβολο | Νόημα |
|---------|-------|
| **Rectangle** | Entity |
| **Diamond** | Relationship |
| **Ellipse** | Attribute |
| **Double Ellipse** | Multi-valued Attribute |
| **Dashed Ellipse** | Derived Attribute |
| **Underlined** | Primary Key |

---

## 2. Cardinality (Πληθικότητα)

### Ορισμός

**Cardinality**: Περιγράφει **πόσα instances** μιας entity μπορούν/πρέπει να **συσχετιστούν** με κάθε instance μιας άλλης entity.

### ⚠️ ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΗΣ 2024-25
```
Q: Which of the following is true about cardinality in ER diagrams?

a) Cardinality describes the number of attributes an entity can have
b) Cardinality describes the number of instances of one entity that
   can/must be associated with each instance of another entity ✓
c) Option cut off
d) Option cut off

ΑΠΑΝΤΗΣΗ: B
```

---

## 3. Τύποι Cardinality

### 3.1 One-to-One (1:1)

**Κάθε instance** του Α συνδέεται με **ακριβώς ένα** instance του Β, και αντίστροφα.

```
┌──────────────┐      1        1      ┌──────────────┐
│   PERSON     │─────────────────────│   PASSPORT   │
└──────────────┘                      └──────────────┘

- Κάθε person έχει ένα passport
- Κάθε passport ανήκει σε ένα person
```

**Παραδείγματα 1:1**:
- Person ↔ Passport
- Country ↔ Capital
- Employee ↔ Company Car (αν κάθε employee έχει το δικό του)
- Manager ↔ Department (αν κάθε dept έχει ακριβώς 1 manager)

### 3.2 One-to-Many (1:N)

**Ένα instance** του Α μπορεί να συνδέεται με **πολλά** instances του Β, αλλά κάθε instance του Β συνδέεται με **ένα μόνο** instance του Α.

```
┌──────────────┐      1        N      ┌──────────────┐
│  DEPARTMENT  │────────────────────<│   EMPLOYEE   │
└──────────────┘                      └──────────────┘

- Κάθε department έχει πολλούς employees
- Κάθε employee ανήκει σε ένα department
```

**Παραδείγματα 1:N**:
- Department → Employees
- Mother → Children
- Publisher → Books
- Course → Students (για course enrollment χωρίς πολλαπλές εγγραφές)

### 3.3 Many-to-Many (M:N)

**Πολλά instances** του Α μπορούν να συνδέονται με **πολλά instances** του Β, και αντίστροφα.

```
┌──────────────┐      M        N      ┌──────────────┐
│   STUDENT    │>───────────────────<│    COURSE    │
└──────────────┘                      └──────────────┘

- Κάθε student μπορεί να εγγραφεί σε πολλά courses
- Κάθε course μπορεί να έχει πολλούς students
```

**Παραδείγματα M:N**:
- Students ↔ Courses
- Authors ↔ Books
- Actors ↔ Movies
- Doctors ↔ Patients

---

## 4. Notation Styles

### Crow's Foot Notation

```
┌───────┐                          ┌───────┐
│ENTITY │───────────────────────o──│ENTITY │
│   A   │                      |   │   B   │
└───────┘                      |   └───────┘
                              /|\

Symbols:
─────    = mandatory one
────o    = optional one (0 or 1)
────<    = mandatory many (1 or more)
───o<    = optional many (0 or more)
```

### Min-Max Notation

```
┌───────┐                          ┌───────┐
│ENTITY │────(min,max)──────────────│ENTITY │
│   A   │                          │   B   │
└───────┘                          └───────┘

(0,1) = zero or one
(1,1) = exactly one
(0,*) = zero or more
(1,*) = one or more
(0,N) = zero to N
```

---

## 5. Participation Constraints

### Total Participation (Mandatory)

**Κάθε** instance της entity **πρέπει** να συμμετέχει στη σχέση.

```
┌──────────┐                    ┌──────────┐
│ EMPLOYEE │════════════════════│  DEPT    │
└──────────┘                    └──────────┘
  (total)                        (partial)

Double line = Total participation
Single line = Partial participation

- Κάθε employee ΠΡΕΠΕΙ να ανήκει σε department (total)
- Ένα department ΜΠΟΡΕΙ να μην έχει employees (partial)
```

### Partial Participation (Optional)

**Κάποια** instances της entity **μπορεί** να μη συμμετέχουν στη σχέση.

---

## 6. Weak Entities

### Ορισμός

**Weak Entity**: Entity που δεν μπορεί να υπάρξει χωρίς μια άλλη (owner) entity.

### Χαρακτηριστικά
- Δεν έχει δικό της Primary Key
- Εξαρτάται από **identifying relationship** με strong entity
- Partial key + Owner's key = Primary key

```
┌──────────────┐                    ┌──────────────┐
│   BUILDING   │════════════════════║    ROOM      ║
│  (Strong)    │      HAS           ║   (Weak)     ║
└──────────────┘                    └──────────────┘
                                     Double rectangle
                                     Double diamond

- Room δεν έχει νόημα χωρίς Building
- Room number μόνο του δεν είναι unique (Room 101 σε κάθε building)
- Building_ID + Room_Number = Unique identification
```

### Παραδείγματα Weak Entities

| Weak Entity | Owner Entity | Partial Key |
|-------------|--------------|-------------|
| Room | Building | room_number |
| Dependent | Employee | dependent_name |
| Order_Item | Order | item_number |
| Chapter | Book | chapter_number |

---

## 7. Keys in ER Model

### Primary Key
- **Μοναδικός** αναγνωριστής για κάθε entity instance
- Υπογραμμισμένο στο ER diagram

### Candidate Key
- Attribute ή σύνολο attributes που μπορεί να είναι primary key
- Μπορεί να υπάρχουν πολλά candidate keys

### Foreign Key
- Attribute που αναφέρεται στο primary key άλλης entity
- Χρησιμοποιείται για να υλοποιήσει relationships

---

## 8. Converting ER to Relational Schema

### Rules

**1:1 Relationship**:
- Βάλε το FK σε οποιαδήποτε πλευρά
- Ή merge τα δύο tables (αν total participation και στις δύο πλευρές)

**1:N Relationship**:
- Βάλε το FK στην πλευρά N (many)

**M:N Relationship**:
- Δημιούργησε **νέο table** (junction/bridge table)
- Το νέο table έχει FKs και στις δύο entities

### Παράδειγμα M:N

```
ER:
STUDENT ────M:N──── COURSE

Relational Schema:
Student(student_id, name, ...)
Course(course_id, title, ...)
Enrollment(student_id, course_id, grade, date)  ← Junction table
           └── FK ───┘ └── FK ──┘
```

---

## 9. Ερωτήσεις Εξετάσεων

### Ερώτηση 1: Cardinality Type
```
Σε ένα πανεπιστήμιο, κάθε φοιτητής μπορεί να εγγραφεί σε πολλά μαθήματα
και κάθε μάθημα έχει πολλούς φοιτητές. Ποιο είναι το cardinality;

A) 1:1
B) 1:N
C) M:N ✓
D) None

ΑΠΑΝΤΗΣΗ: C (Many-to-Many)
```

### Ερώτηση 2: Weak Entity Identification
```
Ποια από τα παρακάτω είναι weak entity;

A) Student
B) Department
C) Room ✓
D) Employee

ΑΠΑΝΤΗΣΗ: C
ΕΞΗΓΗΣΗ: Room εξαρτάται από Building - δεν έχει νόημα μόνο του
```

### Ερώτηση 3: FK Placement
```
Σε 1:N relationship μεταξύ Department(1) και Employee(N),
πού τοποθετούμε το Foreign Key;

A) Department table
B) Employee table ✓
C) Νέο table
D) Και στα δύο

ΑΠΑΝΤΗΣΗ: B
ΕΞΗΓΗΣΗ: Σε 1:N, το FK πηγαίνει στην πλευρά "N" (many)
```

### Ερώτηση 4: Junction Table
```
Πότε δημιουργούμε junction table;

A) 1:1 relationship
B) 1:N relationship
C) M:N relationship ✓
D) Πάντα

ΑΠΑΝΤΗΣΗ: C
```

---

## 10. Σύνοψη - Key Points

### Cardinality Types

| Type | Notation | FK Placement |
|------|----------|--------------|
| **1:1** | Person ── Passport | Either side |
| **1:N** | Dept ──< Employee | N side (Employee) |
| **M:N** | Student >──< Course | Junction table |

### Cardinality Definition (για εξέταση)
```
Cardinality = πόσα instances μιας entity μπορούν να συσχετιστούν
              με κάθε instance μιας άλλης entity
```

### Weak Entity Characteristics
- Δεν έχει δικό της PK
- Εξαρτάται από owner entity
- Partial key + Owner's PK = Composite PK

### ER to Relational Conversion

| Relationship | Action |
|--------------|--------|
| 1:1 | FK σε οποιαδήποτε πλευρά |
| 1:N | FK στη "many" πλευρά |
| M:N | Νέο junction table |
