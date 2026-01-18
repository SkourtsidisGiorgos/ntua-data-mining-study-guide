# Ροές Δεδομένων (Data Streams)

## Χαρακτηριστικά Data Streams

- **Άπειρα** (ή πολύ μεγάλα) δεδομένα
- **Μία διέλευση** (single pass) - δεν μπορούμε να επιστρέψουμε πίσω
- **Περιορισμένη μνήμη** - δεν χωράει όλο το stream
- **Real-time** επεξεργασία

---

## Bloom Filter

### Τι είναι;
Πιθανοτική δομή δεδομένων για **membership testing** (ανήκει ή όχι σε σύνολο).

### Συστατικά
- **m bits** (αρχικά όλα 0)
- **k hash functions** h₁, h₂, ..., hₖ

### Λειτουργίες

**INSERT(x):**
```
Για κάθε hash function hᵢ:
    bit[hᵢ(x)] = 1
```

**LOOKUP(x):**
```
Αν ΟΛΕΣ οι θέσεις hᵢ(x) είναι 1 → "ΙΣΩΣ στο σύνολο"
Αν ΟΠΟΙΑΔΗΠΟΤΕ θέση είναι 0 → "ΣΙΓΟΥΡΑ ΟΧΙ στο σύνολο"
```

### ΚΡΙΣΙΜΟ: Σφάλματα Bloom Filter

| Τύπος Σφάλματος | Είναι Δυνατό; |
|-----------------|---------------|
| **False Positive** | ✓ ΝΑΙ - Λέει "ίσως ναι" ενώ δεν ανήκει |
| **False Negative** | ❌ ΟΧΙ - ΠΟΤΕ δεν λέει "όχι" αν ανήκει |

**ΑΠΟΜΝΗΜΟΝΕΥΣΗ:** "No = Definitely NOT, Yes = Maybe"

---

### Τύποι Bloom Filter

**False Positive Rate (πιθανότητα):**
```
p ≈ (1 - e^(-kn/m))^k
```

Όπου:
- m = αριθμός bits
- n = αριθμός στοιχείων που εισήχθησαν
- k = αριθμός hash functions

**Optimal k (βέλτιστος αριθμός hash functions):**
```
k = (m/n) × ln(2) ≈ 0.693 × (m/n)
```

---

### Λυμένο Παράδειγμα: Bloom Filter

**Δεδομένα:**
- m = 10 bits
- k = 2 hash functions: h₁(x) = x mod 10, h₂(x) = (3x+1) mod 10

**Αρχικά:** `[0,0,0,0,0,0,0,0,0,0]`

**INSERT(5):**
- h₁(5) = 5 mod 10 = 5
- h₂(5) = (15+1) mod 10 = 6
- Bits: `[0,0,0,0,0,1,1,0,0,0]`

**INSERT(12):**
- h₁(12) = 12 mod 10 = 2
- h₂(12) = (36+1) mod 10 = 7
- Bits: `[0,0,1,0,0,1,1,1,0,0]`

**LOOKUP(5):** Θέσεις 5 και 6 → 1 και 1 → **"Ίσως ναι"** ✓

**LOOKUP(7):**
- h₁(7) = 7 mod 10 = 7 → bit[7] = 1
- h₂(7) = (21+1) mod 10 = 2 → bit[2] = 1
- **"Ίσως ναι"** - αλλά είναι **FALSE POSITIVE!** (το 7 δεν εισήχθη ποτέ)

---

## Count-Min Sketch

### Τι είναι;
Πιθανοτική δομή για **εκτίμηση συχνότητας** στοιχείων σε data stream.

### Συστατικά
- **d hash functions** (γραμμές)
- **w buckets** ανά γραμμή (στήλες)
- Πίνακας d × w με counters

### Λειτουργίες

**UPDATE(x):**
```
Για κάθε hash function hᵢ:
    count[i][hᵢ(x)] += 1
```

**QUERY(x):**
```
return min(count[1][h₁(x)], count[2][h₂(x)], ..., count[d][hₐ(x)])
```

### ΚΡΙΣΙΜΟ: Σφάλματα Count-Min Sketch

| Ιδιότητα | Τιμή |
|----------|------|
| Εκτίμηση | **Overestimate** (ποτέ underestimate) |
| Πραγματική τιμή | count(x) ≤ estimate(x) |
| Σφάλμα | estimate(x) - count(x) ≥ 0 |

**ΑΠΟΜΝΗΜΟΝΕΥΣΗ:** Το Count-Min Sketch μόνο **υπερεκτιμά** (overestimates).

---

### Error Bounds

**Με πιθανότητα τουλάχιστον 1 - δ:**
```
estimate(x) ≤ count(x) + ε × N
```

Όπου:
- N = συνολικός αριθμός στοιχείων στο stream
- ε = e/w (e = 2.718...)
- δ = e^(-d)

---

## Λυμένο Παράδειγμα HW2: Count-Min Sketch

**Δεδομένα:**
- h₁(x) = (Ax + 3) mod 10
- h₂(x) = (Bx + 7) mod 10
- A, B βάσει αριθμού μητρώου

**Έστω A=4, B=1** (για student ID που τελειώνει σε 14)

**Κατάσταση στο timestamp t:**
```
Row 1: [7, 38, 39, 5, 4, 10, 11, 15, 41, 47]  (indices 0-9)
Row 2: [14, 31, 25, 6, 5, 21, 22, 21, 33, 29]
```

**Ερώτημα 1: Πόσες φορές πέρασε το y=6;**

Υπολογισμός hash:
- h₁(6) = (4×6 + 3) mod 10 = 27 mod 10 = 7
- h₂(6) = (1×6 + 7) mod 10 = 13 mod 10 = 3

Τιμές:
- Row 1, position 7: 15
- Row 2, position 3: 6

**Απάντηση: min(15, 6) = 6**

**Ερώτημα 2: Πόσο σίγουροι είμαστε; Upper bound σφάλματος.**

Το Count-Min Sketch **υπερεκτιμά**. Άρα:
- Πραγματική τιμή ≤ 6
- Το upper bound του σφάλματος εξαρτάται από ε×N
- Αν N = συνολικές εισαγωγές, τότε:
  - estimate - actual ≤ ε×N

**Ερώτημα 3: Κατάσταση μετά x=2 στο t+1**

Υπολογισμός hash για x=2:
- h₁(2) = (4×2 + 3) mod 10 = 11 mod 10 = 1
- h₂(2) = (1×2 + 7) mod 10 = 9 mod 10 = 9

Update:
```
Row 1: [7, 39, 39, 5, 4, 10, 11, 15, 41, 47]  (position 1: 38→39)
Row 2: [14, 31, 25, 6, 5, 21, 22, 21, 33, 30] (position 9: 29→30)
```

---

## Σύγκριση Bloom Filter vs Count-Min Sketch

| Χαρακτηριστικό | Bloom Filter | Count-Min Sketch |
|----------------|--------------|------------------|
| Ερώτηση | Membership (ανήκει;) | Frequency (πόσες φορές;) |
| Απάντηση | Yes/No | Αριθμός |
| False Positives | ✓ Ναι | N/A |
| False Negatives | ❌ Όχι | N/A |
| Overestimate | N/A | ✓ Πάντα |
| Underestimate | N/A | ❌ Ποτέ |

---

## Άλλες Τεχνικές Data Streams

### Sampling
- **Reservoir Sampling:** Διατηρεί τυχαίο δείγμα μεγέθους k
- Κάθε στοιχείο έχει ίση πιθανότητα επιλογής

### Sliding Window
- Αναλύει μόνο τα τελευταία N στοιχεία
- Ξεχνάει τα παλιά δεδομένα

### Sketches (άλλα)
- **Flajolet-Martin:** Εκτίμηση distinct elements
- **HyperLogLog:** Βελτιωμένο distinct count

---

## Συχνά Λάθη στις Εξετάσεις

### 1. Bloom Filter: False Negatives
- ❌ "Bloom Filter μπορεί να έχει false negatives"
- ✓ **ΠΟΤΕ** false negatives - αν λέει "όχι", είναι σίγουρο

### 2. Count-Min Sketch: Underestimate
- ❌ "Count-Min μπορεί να υποεκτιμήσει"
- ✓ **ΠΟΤΕ** underestimate - πάντα estimate ≥ actual

### 3. Optimal k σε Bloom Filter
- Υπάρχει βέλτιστο k για δεδομένα m, n
- Πολύ λίγα k → υψηλό FP
- Πολλά k → γεμίζει γρήγορα → υψηλό FP

---

## Γρήγορη Αναφορά

```
╔══════════════════════════════════════════════════════════════════╗
║              DATA STREAMS CHEAT SHEET                            ║
╠══════════════════════════════════════════════════════════════════╣
║ BLOOM FILTER:                                                    ║
║   Λειτουργία: Membership test (ανήκει;)                          ║
║   False Positives: ΝΑΙ (maybe yes)                               ║
║   False Negatives: ΟΧΙ ΠΟΤΕ (no = definitely no)                 ║
║   FP Rate: p ≈ (1 - e^(-kn/m))^k                                 ║
║   Optimal k: k = (m/n) × ln(2)                                   ║
╠══════════════════════════════════════════════════════════════════╣
║ COUNT-MIN SKETCH:                                                ║
║   Λειτουργία: Frequency estimation                               ║
║   Update: count[i][hᵢ(x)] += 1                                   ║
║   Query:  min(count[i][hᵢ(x)]) για όλα τα i                      ║
║   Overestimate: ΠΑΝΤΑ (estimate ≥ actual)                        ║
║   Underestimate: ΠΟΤΕ                                            ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Ασκήσεις Εξάσκησης

### Άσκηση 1 (Bloom Filter)
Δίνεται Bloom Filter με m=8 bits, k=2:
- h₁(x) = x mod 8
- h₂(x) = (2x+1) mod 8

1. Εισάγετε τα στοιχεία: 3, 8, 15
2. Ποια είναι η τελική κατάσταση των bits;
3. Αν κάνουμε lookup(7), τι αποτέλεσμα παίρνουμε;

### Άσκηση 2 (Count-Min Sketch)
Δίνεται Count-Min Sketch 2×5 με:
- h₁(x) = x mod 5
- h₂(x) = (2x) mod 5

Αρχική κατάσταση:
```
Row 1: [3, 5, 2, 1, 4]
Row 2: [2, 3, 4, 5, 1]
```

1. Ποια είναι η εκτίμηση συχνότητας για x=7;
2. Ποια θα είναι η κατάσταση μετά την εισαγωγή x=3;

### Άσκηση 3 (Σύγκριση)
Ποια δομή θα χρησιμοποιούσατε για:
1. Έλεγχος αν ένα email είναι spam (από λίστα spam)
2. Μέτρηση πόσες φορές εμφανίστηκε κάθε IP σε network traffic
3. Έλεγχος αν username είναι ήδη κατειλημμένο
