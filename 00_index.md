# Οδηγός Μελέτης - Εξόρυξη Γνώσης από Δεδομένα (Data Mining)

## DSML851 - ΕΜΠΜΣ ΕΜΠ 2024-2025

**Διδάσκοντες:** Δ. Τσουμάκος, Γ. Αλεξανδρίδης
**Περίοδος:** Χειμερινό Εξάμηνο 2025

---

## Περιεχόμενα Ύλης

| # | Θέμα | Αρχείο | Διαφάνειες |
|---|------|--------|------------|
| 1 | Μοντέλο E-R & Σχεδιασμός ΒΔ | [01_er_model.md](01_er_model.md) | 1_ModelingER.pdf |
| 2 | Σχεσιακό Μοντέλο & Άλγεβρα | [02_relational_model.md](02_relational_model.md) | 2_ModelingRelational_RA.pdf |
| 3 | SQL (Βασικά & Προχωρημένα) | [03_sql.md](03_sql.md) | 3_SQLIntro.pdf, 4_AdvancedSQL.pdf |
| 4 | Επεξεργασία & Βελτιστοποίηση Ερωτημάτων | [04_query_processing.md](04_query_processing.md) | 5_QueryExecution.pdf |
| 5 | Προεπεξεργασία Δεδομένων | [05_data_preprocessing.md](05_data_preprocessing.md) | 6_1 Data Preprocessing.pdf |
| 6 | Ροές Δεδομένων (Data Streams) | [06_data_streams.md](06_data_streams.md) | 6_2 Mining Data Streams.pdf |
| 7 | Ακολουθίες & HMM | [07_hmm_sequences.md](07_hmm_sequences.md) | 6_3 Mining Discrete Sequences.pdf |
| 8 | OLAP & Αποθήκες Δεδομένων | [08_olap_dw.md](08_olap_dw.md) | 6_7_DW+OLAP.pdf |
| 9 | RAG & LLMs | [09_rag_llms.md](09_rag_llms.md) | 7_Retrieval-based Language Models.pdf |
| 10 | Συγκεντρωτικός Τύπων | [10_formulas.md](10_formulas.md) | - |
| 11 | Εξάσκηση Εξετάσεων | [11_practice_exam.md](11_practice_exam.md) | - |

---

## Θέματα που ΔΕΝ περιλαμβάνονται (εκτός ύλης 2024-25)

- ~~MapReduce~~ (αφαιρέθηκε)
- ~~Decision Trees / Classification~~
- ~~Clustering (DBSCAN, K-Means)~~
- ~~Association Rules / Apriori~~
- ~~Bayesian Networks~~
- ~~Privacy / K-Anonymity~~
- ~~DTW / Similarity Measures~~
- ~~TF-IDF / Text Mining~~

---

## Κατανομή Βαρύτητας στις Εξετάσεις (Ιαν. 2025)

Με βάση την εξέταση Ιανουαρίου 2025:

| Θέμα | Ερωτήσεις | Βαρύτητα |
|------|-----------|----------|
| OLAP & Data Warehousing | Q1, Q2, Q3, Q15 | ~25% |
| E-R Διαγράμματα | Q4 | ~5% |
| Query Processing | Q5, Q7 | ~10% |
| Relational Algebra | Q6 | ~5% |
| Foreign Keys | Q8 | ~5% |
| Τύποι Δεδομένων (NOIR) | Q9, Q10 | ~10% |
| Ακολουθίες & HMM | Q11, Q12 | ~10% |
| SQL Queries | Q13, Q14 | ~16% |
| Data Preprocessing (Discretization) | Q16 | ~8% |

---

## Πηγές Υλικού

### Εργασίες 2025-26 (Φθινόπωρο)
- **HW1:** E-R διαγράμματα, Relational Algebra, SQL
- **HW2:** Data Preprocessing (bin smoothing), HMM (πιθανότητα ακολουθίας), Count-Min Sketches

### Παλαιότερες Εργασίες (2023-24)
- **1η Σειρά:** E-R, SQL, Relational Algebra, OLAP
- **2η Σειρά:** Data Preprocessing, Bloom Filters, HMM

### Παλαιά Θέματα Εξετάσεων
- **2024-25:** 100% σχετικό (ίδιοι διδάσκοντες, ίδια ύλη)
- **2022-23:** ~60% σχετικό (εξαίρεση: MapReduce)
- **2021-22:** ~40% σχετικό
- **2020-21:** ~30% σχετικό

---

## Συμβουλές Μελέτης

### Προτεραιότητα Υψηλή
1. **OLAP Operations** - Roll-up, Drill-down, Slice, Dice, Pivot
2. **SQL Queries** - JOIN, GROUP BY, HAVING, subqueries
3. **HMM & Viterbi** - Υπολογισμός πιθανότητας ακολουθίας
4. **Τύποι Δεδομένων** - Nominal, Ordinal, Interval, Ratio

### Προτεραιότητα Μεσαία
5. **Query Processing** - Pipelining vs Materialization, Join αλγόριθμοι
6. **Relational Algebra** - σ, π, ⋈, ÷
7. **E-R Diagrams** - Cardinality, μετατροπή σε σχεσιακό

### Προτεραιότητα Χαμηλότερη
8. **Bloom Filters** - False positive probability
9. **Count-Min Sketch** - Frequency estimation
10. **RAG & LLMs** - Βασικές έννοιες

---

## Γρήγορη Αναφορά - Κρίσιμοι Τύποι

```
Bloom Filter FP Rate:     p ≈ (1 - e^(-kn/m))^k
Optimal Hash Functions:   k = (m/n) × ln(2) ≈ 0.693 × (m/n)

Viterbi Recursion:        δ_t(j) = max_i[δ_{t-1}(i) × a_ij] × b_j(o_t)

Equal-Width Binning:      width = (max - min) / k
Z-Score Normalization:    z = (x - μ) / σ
Min-Max Normalization:    x' = (x - min) / (max - min)

OLAP Cube Cells:          (d₁+1)(d₂+1)...(dₙ+1)
```

---

## Δομή Κάθε Κεφαλαίου

Κάθε αρχείο περιέχει:
1. **Βασικές Έννοιες** - Ορισμοί και θεωρία
2. **Τύποι** - Μαθηματικές σχέσεις
3. **Λυμένα Παραδείγματα** - Από εργασίες και εξετάσεις
4. **Ασκήσεις Εξάσκησης** - Για αυτοαξιολόγηση
5. **Συχνά Λάθη** - Τι να αποφύγετε

---

*Τελευταία ενημέρωση: Ιανουάριος 2025*
