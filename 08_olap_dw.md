# OLAP & Αποθήκες Δεδομένων (Data Warehousing)

## OLTP vs OLAP - ΚΡΙΣΙΜΟ!

| Χαρακτηριστικό | OLTP | OLAP |
|----------------|------|------|
| Σκοπός | Καθημερινές συναλλαγές | Ανάλυση & αποφάσεις |
| Λειτουργίες | INSERT, UPDATE, DELETE | SELECT (aggregates) |
| Δεδομένα | Τρέχοντα, λεπτομερή | Ιστορικά, συγκεντρωτικά |
| Χρήστες | Υπάλληλοι, εφαρμογές | Αναλυτές, managers |
| Schema | Κανονικοποιημένο (3NF) | Αποκανονικοποιημένο (star/snowflake) |
| Queries | Απλά, συχνά | Πολύπλοκα, ad-hoc |
| Απόδοση | Γρήγορα transactions | Γρήγορα aggregations |

---

## Ερώτηση Εξέτασης 2025 (Q2)

**Ερώτηση:** Ποιο είναι κύριο μειονέκτημα της εκτέλεσης OLAP queries σε OLTP σύστημα;

**Απάντηση: (c)** "Εισάγει υψηλή καθυστέρηση στα queries και μπορεί να επηρεάσει αρνητικά την απόδοση των real-time transactions."

**Γιατί:**
- OLAP queries είναι **βαριά** (full table scans, aggregations)
- OLTP χρειάζεται **γρήγορες μικρές** συναλλαγές
- Μοιράζονται πόρους → αργούν και τα δύο

---

## Dimensional Modeling

### Fact Table (Πίνακας Γεγονότων)
- **Περιέχει:** Μετρήσεις (measures), FKs προς dimensions
- **Μετρήσεις:** Ποσοτικά δεδομένα (sales, revenue, count)
- **Grain:** Το επίπεδο λεπτομέρειας (π.χ. ανά ημέρα/πελάτη/προϊόν)

### Dimension Tables (Πίνακες Διαστάσεων)
- **Περιέχουν:** Περιγραφικά attributes
- **Παραδείγματα:** Time, Product, Customer, Location
- **Ιεραρχίες:** Day → Month → Quarter → Year

---

## Ερώτηση Εξέτασης 2025 (Q3)

**Ερώτηση:** Τι είναι μια dimension hierarchy στο OLAP;

**Απάντηση: (b)** "Μια δομή που οργανώνει τα δεδομένα σε διαφορετικά επίπεδα λεπτομέρειας."

**Παραδείγματα Ιεραρχιών:**
- **Time:** day → month → quarter → year
- **Location:** city → state → country → region
- **Product:** product → subcategory → category → department

---

## Star Schema vs Snowflake Schema

### Star Schema (Αστεροειδές)
```
        [Time Dim]
             ↓
[Product Dim] ← [FACT TABLE] → [Customer Dim]
             ↓
        [Location Dim]
```
- **Δομή:** Fact στο κέντρο, dimensions απευθείας συνδεδεμένες
- **Πλεονέκτημα:** Απλά queries, γρήγορα joins
- **Μειονέκτημα:** Redundancy στα dimensions

### Snowflake Schema (Χιονονιφάδα)
```
[Category] → [Subcategory] → [Product Dim] ← [FACT] → [Customer Dim]
                                                   ↓
                               [City] → [State] → [Location Dim]
```
- **Δομή:** Dimensions κανονικοποιημένες (normalized)
- **Πλεονέκτημα:** Λιγότερο redundancy
- **Μειονέκτημα:** Περισσότερα joins, πιο αργό

---

## OLAP Operations - ΑΠΟΜΝΗΜΟΝΕΥΣΗ!

| Λειτουργία | Περιγραφή | Παράδειγμα |
|------------|-----------|------------|
| **Roll-up** | Aggregation (ΛΙΓΟΤΕΡΗ λεπτομέρεια) | day → month → year |
| **Drill-down** | Disaggregation (ΠΕΡΙΣΣΟΤΕΡΗ λεπτομέρεια) | year → month → day |
| **Slice** | Επιλογή **ΕΝΟΣ** επιπέδου μίας διάστασης | Time = 2024 |
| **Dice** | Επιλογή **ΠΟΛΛΩΝ** διαστάσεων | Time=2024 AND Product='A' |
| **Pivot (Rotate)** | Αλλαγή οπτικής γωνίας / περιστροφή αξόνων | Rows↔Columns |

---

## Ερώτηση Εξέτασης 2025 (Q1)

**Ερώτηση:** Ποια λειτουργία OLAP επιτρέπει στους χρήστες να δουν δεδομένα από διαφορετικές οπτικές γωνίες περιστρέφοντας τους άξονες του data cube;

**Απάντηση: (c) Pivot**

---

## OLAP Cube

### Τι είναι;
Πολυδιάστατη αναπαράσταση δεδομένων με:
- N διαστάσεις (dimensions)
- Μετρήσεις (measures) σε κάθε κελί

### Cuboids

**Base Cuboid:** Πλήρης λεπτομέρεια (όλες οι διαστάσεις)

**Apex Cuboid:** Πλήρης συγκέντρωση (0 διαστάσεις, μόνο totals)

**Αριθμός Cuboids:**
Για n διαστάσεις: **2ⁿ cuboids**

### Αριθμός Κελιών με ALL

Αν κάθε διάσταση dᵢ έχει |dᵢ| τιμές, συνολικά (συμπεριλαμβανομένου "ALL"):
```
(|d₁|+1) × (|d₂|+1) × ... × (|dₙ|+1)
```

**Παράδειγμα:**
- Time: 12 months → 12+1 = 13
- Product: 100 products → 100+1 = 101
- Store: 50 stores → 50+1 = 51

Σύνολο κελιών: 13 × 101 × 51 = 67,029

---

## Λυμένο Παράδειγμα: Εξέταση 2025 Q15

**Σενάριο:**
Data warehouse με:
- **Διαστάσεις:** date, spectator, location, game
- **Measures:** count, charge
- Spectators: students, adults, seniors

**Ερώτημα:** Ξεκινώντας από {date, spectator, location, game}, ποιες λειτουργίες χρειάζονται για να βρούμε το **total charge** των **student** spectators στο **"Γ. Καραϊσκάκης"** για **όλα τα games του 2024**;

**Λύση:**

1. **Roll-up on date:** date_id → year
   - Συγκεντρώνουμε τα δεδομένα σε επίπεδο έτους

2. **Roll-up on game:** game_id → ALL
   - Θέλουμε ΟΛΑ τα games, άρα aggregation

3. **Roll-up on location:** location_id → location_name (αν χρειάζεται)
   - Ή διατηρούμε αν το όνομα είναι ήδη διαθέσιμο

4. **Dice:**
   - spectator = "students"
   - location_name = "Γ. Καραϊσκάκης"
   - year = 2024

**Σημείωση:** Dice (όχι Slice) γιατί φιλτράρουμε ΠΟΛΛΕΣ διαστάσεις.

---

## Λυμένο Παράδειγμα: HW1 2023-24

**Σενάριο:**
Star schema με:
- Fact Table: ID, Doctor_ID, Patient_ID, Time_ID, Category, Charge
- Doctor Dimension: ID, Name, Specialty, Phone
- Patient Dimension: ID, Name, Gender, DoB, Phone, SSN, Smoker
- Time Dimension: ID, Year, Month, Day, Time, Day_of_Week

**Ερώτημα:** Από cuboid {day, doctor, patient}, βρες total charges ανά doctor για το 2022.

**Λύση:**
1. **Roll-Up:** day → month → year
   - Νέο cuboid: {year, doctor, patient}

2. **Slice:** year = 2022
   - Νέο cuboid: {year=2022, doctor, patient}

3. **Roll-Up:** patient → ALL
   - Νέο cuboid: {year=2022, doctor}

**Τελική απάντηση:** Roll-up day→year, Slice year=2022, Roll-up patient

---

## Materialized Views

### Τι είναι;
Προ-υπολογισμένα αποτελέσματα queries που αποθηκεύονται φυσικά.

### Πλεονεκτήματα
- Γρήγορη απάντηση σε queries
- Δεν χρειάζεται re-computation

### Μειονεκτήματα
- Χώρος αποθήκευσης
- Ανανέωση όταν αλλάζουν τα source data
- Trade-off: Ποια views να materialized;

---

## Συχνά Λάθη στις Εξετάσεις

### 1. Roll-up vs Drill-down σύγχυση
```
❌ Roll-up = περισσότερη λεπτομέρεια
✓ Roll-up = ΛΙΓΟΤΕΡΗ λεπτομέρεια (aggregation)
✓ Drill-down = ΠΕΡΙΣΣΟΤΕΡΗ λεπτομέρεια
```

**Μνημονικό:** Roll-UP = go UP the hierarchy = less detail

### 2. Slice vs Dice σύγχυση
```
❌ Slice για πολλές διαστάσεις
✓ Slice = ΜΙΑ διάσταση, ΕΝΑΣ value
✓ Dice = ΠΟΛΛΕΣ διαστάσεις ή πολλά values
```

### 3. Star vs Snowflake
```
❌ Star είναι κανονικοποιημένο
✓ Star = αποκανονικοποιημένο (denormalized)
✓ Snowflake = κανονικοποιημένο (normalized)
```

### 4. OLTP για analytics
```
❌ OLTP είναι κατάλληλο για heavy analytics
✓ OLTP για transactions, OLAP για analytics
```

---

## Γρήγορη Αναφορά

```
╔══════════════════════════════════════════════════════════════════╗
║              OLAP & DATA WAREHOUSING CHEAT SHEET                 ║
╠══════════════════════════════════════════════════════════════════╣
║ OLAP OPERATIONS:                                                 ║
║   Roll-up:    Λιγότερη λεπτομέρεια (day→month→year)              ║
║   Drill-down: Περισσότερη λεπτομέρεια (year→month→day)           ║
║   Slice:      Φίλτρο ΜΙΑ διάσταση (Time=2024)                    ║
║   Dice:       Φίλτρο ΠΟΛΛΕΣ διαστάσεις                           ║
║   Pivot:      Περιστροφή αξόνων                                  ║
╠══════════════════════════════════════════════════════════════════╣
║ SCHEMAS:                                                         ║
║   Star:      Fact στο κέντρο, dimensions απευθείας               ║
║   Snowflake: Normalized dimensions (περισσότερα joins)           ║
╠══════════════════════════════════════════════════════════════════╣
║ CUBE CALCULATIONS:                                               ║
║   Cuboids:    2ⁿ (n = αριθμός διαστάσεων)                        ║
║   Cells:      (|d₁|+1) × (|d₂|+1) × ... × (|dₙ|+1)               ║
╠══════════════════════════════════════════════════════════════════╣
║ OLTP vs OLAP:                                                    ║
║   OLTP: Transactions, current data, normalized                   ║
║   OLAP: Analytics, historical data, denormalized                 ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Ασκήσεις Εξάσκησης

### Άσκηση 1 (OLAP Operations)
Δίνεται cuboid {year, month, product, store} με measure: total_sales.

Ποιες λειτουργίες χρειάζονται για:
1. Συνολικές πωλήσεις ανά έτος (χωρίς product/store)
2. Πωλήσεις μόνο για το 2024, ανά product
3. Σύγκριση μηνών ως στήλες και products ως γραμμές

### Άσκηση 2 (Cube Calculations)
Data warehouse με 4 διαστάσεις:
- Time: 365 days
- Product: 1000 items
- Store: 100 locations
- Customer: 50000 customers

1. Πόσα cuboids υπάρχουν;
2. Πόσα κελιά έχει ο πλήρης cube (με ALL);

### Άσκηση 3 (Schema Design)
Σχεδιάστε star schema για σύστημα πωλήσεων με:
- Γεγονότα: πωλήσεις (quantity, amount, discount)
- Διαστάσεις: χρόνος, προϊόν, πελάτης, κατάστημα, πωλητής
