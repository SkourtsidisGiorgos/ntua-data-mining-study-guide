# Μοντέλο E-R & Σχεδιασμός Βάσεων Δεδομένων

## Βασικές Έννοιες - ΑΠΟΜΝΗΜΟΝΕΥΣΗ!

### Στοιχεία E-R Διαγράμματος

| Σύμβολο | Όνομα | Περιγραφή | Παράδειγμα |
|---------|-------|-----------|------------|
| Ορθογώνιο | Entity | Αντικείμενο/οντότητα | Student, Course |
| Έλλειψη | Attribute | Ιδιότητα οντότητας | name, id |
| Ρόμβος | Relationship | Σύνδεση μεταξύ entities | enrolls |
| Υπογράμμιση | Primary Key | Μοναδικό αναγνωριστικό | _sid_ |

### Cardinality (Πληθικότητα)

| Τύπος | Περιγραφή | Παράδειγμα |
|-------|-----------|------------|
| 1:1 | Ένα-προς-Ένα | Person -- Passport |
| 1:N | Ένα-προς-Πολλά | Department -- Employee |
| M:N | Πολλά-προς-Πολλά | Student -- Course |

---

## Τύποι Οντοτήτων (Entity Types)

### Strong Entity vs Weak Entity

**Strong Entity:**
- Έχει δικό του Primary Key
- Υπάρχει ανεξάρτητα
- Παράδειγμα: `Employee`

**Weak Entity:**
- Εξαρτάται από Strong Entity
- Δεν έχει δικό του πλήρες PK
- Χρειάζεται το PK του owner + partial key
- Παράδειγμα: `Dependent` (εξαρτώμενο μέλος υπαλλήλου)
- Συμβολισμός: Διπλό ορθογώνιο

---

## Τύποι Attributes

| Τύπος | Συμβολισμός | Περιγραφή | Παράδειγμα |
|-------|-------------|-----------|------------|
| Simple | Απλή έλλειψη | Μία τιμή | name |
| Composite | Έλλειψη με υπο-ελλείψεις | Σύνθετο (αποτελείται από μέρη) | address (street, city) |
| Multivalued | Διπλή έλλειψη | Πολλές τιμές | phone (πολλά τηλέφωνα) |
| Derived | Διακεκομμένη έλλειψη | Υπολογίζεται | age (από birthdate) |

---

## Participation Constraints

### Total Participation (Ολική Συμμετοχή)
- Συμβολισμός: **Διπλή γραμμή**
- Σημαίνει: ΚΑΘΕ instance ΠΡΕΠΕΙ να συμμετέχει στη σχέση
- Παράδειγμα: Κάθε Employee ΠΡΕΠΕΙ να δουλεύει σε ένα Department

### Partial Participation (Μερική Συμμετοχή)
- Συμβολισμός: **Απλή γραμμή**
- Σημαίνει: Ένα instance ΜΠΟΡΕΙ να συμμετέχει (αλλά δεν είναι υποχρεωτικό)
- Παράδειγμα: Ένα Department ΜΠΟΡΕΙ να μην έχει employees

---

## Μετατροπή E-R σε Σχεσιακό Σχήμα

### Κανόνες Μετατροπής

| Στοιχείο E-R | Κανόνας Μετατροπής |
|--------------|-------------------|
| Strong Entity | Πίνακας με όλα τα simple attributes |
| Weak Entity | Πίνακας με (owner_PK + partial_key) ως composite PK |
| 1:1 Relationship | FK σε οποιαδήποτε πλευρά (προτίμηση: total participation) |
| 1:N Relationship | FK στην N-πλευρά (many side) |
| M:N Relationship | Νέος πίνακας με PKs και των δύο entities |
| Multivalued Attr | Ξεχωριστός πίνακας (entity_PK, value) |
| Composite Attr | Flatten: κάθε component γίνεται στήλη |
| Derived Attr | ΔΕΝ αποθηκεύεται (υπολογίζεται) |

---

## Λυμένα Παραδείγματα

### Παράδειγμα 1: Μετατροπή M:N Relationship

**E-R Διάγραμμα:**
```
Student(sid, name) ---M--- enrolls(grade) ---N--- Course(cid, title)
```

**Λύση - Βήμα προς βήμα:**

**Βήμα 1: Strong Entities → Πίνακες**
```
Student(sid, name)
Course(cid, title)
```

**Βήμα 2: M:N Relationship → Νέος Πίνακας**
```
Enrolls(sid, cid, grade)
    FK: sid REFERENCES Student(sid)
    FK: cid REFERENCES Course(cid)
```

**Τελικό Σχήμα:**
```sql
Student(sid, name)
Course(cid, title)
Enrolls(sid, cid, grade)
    PRIMARY KEY (sid, cid)
    FOREIGN KEY (sid) REFERENCES Student(sid)
    FOREIGN KEY (cid) REFERENCES Course(cid)
```

---

### Παράδειγμα 2: HW1 2025 - Music Streaming Service

**Απαιτήσεις:**
- Artist: unique ID, name, country
- Album: unique ID, title, release_year, genre (1 artist ανά album)
- Track: unique ID, title, duration (1 album ανά track)
- Collaborations: Artist featured σε Track (M:N)

**Σχεσιακό Σχήμα:**
```sql
Artist(artist_id, name, country)

Album(album_id, title, release_year, genre, artist_id)
    FK: artist_id REFERENCES Artist(artist_id)

Track(track_id, title, duration, album_id)
    FK: album_id REFERENCES Album(album_id)

FeaturedOn(artist_id, track_id)
    PK: (artist_id, track_id)
    FK: artist_id REFERENCES Artist(artist_id)
    FK: track_id REFERENCES Track(track_id)
```

**Εξήγηση Σχεδιαστικών Αποφάσεων:**
1. **Artist - Album:** 1:N → FK `artist_id` στο Album
2. **Album - Track:** 1:N → FK `album_id` στο Track
3. **Artist - Track (featured):** M:N → Νέος πίνακας `FeaturedOn`

---

### Παράδειγμα 3: Weak Entity

**Σενάριο:** Employee με Dependents (εξαρτώμενα μέλη)

**E-R:**
```
Employee(eid, name) ====== has ====== Dependent(name, birthdate)
                    1               N
```
(Διπλή γραμμή = Weak Entity, Διπλό identifying relationship)

**Σχεσιακό Σχήμα:**
```sql
Employee(eid, name)

Dependent(eid, dep_name, birthdate)
    PK: (eid, dep_name)  -- Composite key!
    FK: eid REFERENCES Employee(eid)
```

---

## Ερώτηση Εξέτασης 2025 (Q4)

**Ερώτηση:** Ποια από τις παρακάτω προτάσεις είναι σωστή για την cardinality στα E-R διαγράμματα;

a) Η cardinality περιγράφει τον αριθμό των attributes που μπορεί να έχει μια οντότητα.

b) **Η cardinality περιγράφει τον αριθμό των instances μιας οντότητας που μπορούν/πρέπει να συσχετιστούν με κάθε instance μιας άλλης οντότητας.** ✓

**Απάντηση: (b)**

---

## Συχνά Λάθη στις Εξετάσεις

### 1. M:N χωρίς νέο πίνακα
- ❌ **Λάθος:** Βάζω FK στη μία πλευρά
- ✓ **Σωστό:** Δημιουργώ junction table με composite key

### 2. Weak Entity μετατροπή
- ❌ **Λάθος:** Μόνο το partial key ως PK
- ✓ **Σωστό:** Composite key: (owner_PK + partial_key)

### 3. Multivalued attributes
- ❌ **Λάθος:** Πολλές στήλες (phone1, phone2, ...)
- ✓ **Σωστό:** Ξεχωριστός πίνακας με FK

### 4. Total Participation
- ❌ **Λάθος:** Αγνοώ τη διπλή γραμμή
- ✓ **Σωστό:** NOT NULL constraint στο FK

### 5. Foreign Key Ορισμός (Q8 Εξέτασης 2025)
- ❌ **Λάθος:** "Κλειδί για πρόσβαση σε εξωτερική βάση"
- ✓ **Σωστό:** "Κλειδί που δημιουργεί σχέση μεταξύ δύο πινάκων αναφερόμενο σε primary key"

---

## Ασκήσεις Εξάσκησης

### Άσκηση 1
Σχεδιάστε E-R διάγραμμα για ένα σύστημα νοσοκομείου με:
- Doctor (ID, name, specialty)
- Patient (ID, name, birthdate, SSN)
- Medical_Test (ID, test_name, test_type)
- Σχέσεις: Doctor attends Patient, Doctor orders tests, Doctor conducts tests

### Άσκηση 2
Μετατρέψτε το παρακάτω E-R σε σχεσιακό σχήμα:
```
Department(did, name) --1-- manages --N-- Project(pid, title, budget)
                                              |
                                              |
                                             M:N
                                              |
                                      Employee(eid, name, salary)
```

### Άσκηση 3
Ποιο είναι το σωστό σχήμα για:
- Book(ISBN, title) με πολλούς Authors
- Author(aid, name)
- Κάθε βιβλίο μπορεί να έχει πολλούς συγγραφείς, κάθε συγγραφέας πολλά βιβλία

---

## Γρήγορη Αναφορά

```
╔══════════════════════════════════════════════════════════════╗
║             E-R → RELATIONAL ΜΕΤΑΤΡΟΠΗ                       ║
╠══════════════════════════════════════════════════════════════╣
║ 1. Strong Entity    → Πίνακας με simple attributes           ║
║ 2. Weak Entity      → (owner_PK + partial_key) = PK          ║
║ 3. 1:1 Relationship → FK σε οποιαδήποτε πλευρά               ║
║ 4. 1:N Relationship → FK στην N-πλευρά (many side)           ║
║ 5. M:N Relationship → Νέος πίνακας με 2 FKs                  ║
║ 6. Multivalued Attr → Ξεχωριστός πίνακας (entity_PK, value)  ║
║ 7. Composite Attr   → Flatten σε πολλές στήλες               ║
║ 8. Derived Attr     → ΔΕΝ αποθηκεύεται                       ║
╚══════════════════════════════════════════════════════════════╝
```
