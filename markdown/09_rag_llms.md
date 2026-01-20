# RAG & LLMs (Retrieval-Augmented Generation)

## Τι είναι το RAG;

**Retrieval-Augmented Generation (RAG)** είναι μια τεχνική που συνδυάζει:
1. **Retrieval:** Ανάκτηση σχετικών εγγράφων από μια βάση γνώσης
2. **Generation:** Χρήση LLM για παραγωγή απάντησης βασισμένης στα ανακτημένα έγγραφα

### Γιατί χρειαζόμαστε RAG;

**Προβλήματα LLMs χωρίς RAG:**
- **Hallucinations:** Παράγουν ψευδείς πληροφορίες
- **Outdated knowledge:** Γνώση μέχρι την ημερομηνία training
- **No domain-specific knowledge:** Δεν γνωρίζουν ιδιωτικά/εταιρικά δεδομένα
- **No attribution:** Δεν δίνουν πηγές

**Πλεονεκτήματα RAG:**
- **Grounded responses:** Βασισμένες σε πραγματικά έγγραφα
- **Up-to-date:** Ανανεώνεται η βάση γνώσης χωρίς re-training
- **Attribution:** Μπορούμε να δείξουμε τις πηγές
- **Domain-specific:** Προσαρμογή σε εξειδικευμένα domains

---

## Αρχιτεκτονική RAG

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Query     │────►│  Retriever  │────►│  Retrieved  │
│   (User)    │     │  (Search)   │     │  Documents  │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Answer    │◄────│    LLM      │◄────│   Prompt    │
│  (Response) │     │ (Generator) │     │ (Q + Docs)  │
└─────────────┘     └─────────────┘     └─────────────┘
```

### Βήματα

1. **Indexing:** Μετατροπή εγγράφων σε embeddings και αποθήκευση
2. **Query:** Ο χρήστης θέτει ερώτηση
3. **Retrieval:** Εύρεση πιο σχετικών εγγράφων
4. **Augmentation:** Προσθήκη εγγράφων στο prompt
5. **Generation:** LLM παράγει απάντηση με βάση τα έγγραφα

---

## Embeddings (Διανυσματικές Αναπαραστάσεις)

### Τι είναι;
Αριθμητικές αναπαραστάσεις κειμένου σε υψηλής διάστασης χώρο.

### Ιδιότητες
- **Σημασιολογική ομοιότητα:** Παρόμοια κείμενα → κοντινά vectors
- **Dense vectors:** Συνήθως 768-4096 διαστάσεις
- **Similarity:** Μετριέται με cosine similarity ή dot product

### Διαδικασία

```
"The cat sat on the mat" → Embedding Model → [0.1, -0.3, 0.7, ...]
```

---

## Vector Database (Διανυσματική Βάση Δεδομένων)

### Τι είναι;
Βάση δεδομένων βελτιστοποιημένη για αποθήκευση και αναζήτηση vectors.

### Λειτουργίες
- **Store:** Αποθήκευση embeddings με metadata
- **Search:** Εύρεση k-nearest neighbors (kNN)
- **Index:** Δομές για γρήγορη αναζήτηση (HNSW, IVF, etc.)

### Παραδείγματα
- Pinecone
- Weaviate
- Chroma
- Milvus
- FAISS (Facebook AI Similarity Search)

---

## Chunking (Τεμαχισμός Εγγράφων)

### Γιατί χρειάζεται;
- LLMs έχουν περιορισμένο context window
- Μικρότερα chunks = πιο ακριβές retrieval
- Μεγαλύτερα chunks = περισσότερο context

### Στρατηγικές Chunking

| Μέθοδος | Περιγραφή | Πλεονεκτήματα | Μειονεκτήματα |
|---------|-----------|---------------|---------------|
| Fixed-size | Σταθερός αριθμός χαρακτήρων/tokens | Απλό | Μπορεί να κόψει προτάσεις |
| Sentence-based | Ανά πρόταση | Semantic boundaries | Πολύ μικρά chunks |
| Paragraph-based | Ανά παράγραφο | Φυσικά όρια | Ανομοιόμορφο μέγεθος |
| Recursive | Ιεραρχικός διαχωρισμός | Ευέλικτο | Πιο πολύπλοκο |
| Semantic | Βάσει νοήματος | Καλύτερο context | Computationally expensive |

### Overlap (Επικάλυψη)
Συνήθως χρησιμοποιούμε overlap μεταξύ chunks για να μην χαθεί context:
```
Chunk 1: [----tokens 0-500----]
Chunk 2:     [----tokens 400-900----]  (100 tokens overlap)
Chunk 3:         [----tokens 800-1300----]
```

---

## Retrieval Strategies

### Dense Retrieval
- Χρήση embeddings
- Semantic similarity
- Παράδειγμα: Cosine similarity σε vector space

### Sparse Retrieval
- Keyword matching (BM25, TF-IDF)
- Lexical similarity
- Γρήγορο, interpretable

### Hybrid Retrieval
- Συνδυασμός dense + sparse
- Καλύτερο coverage

---

## Re-ranking

### Τι είναι;
Δεύτερο στάδιο ranking μετά το initial retrieval.

### Διαδικασία
1. Retrieve top-k (π.χ. 100) documents
2. Re-rank με πιο ακριβές μοντέλο
3. Κράτησε top-n (π.χ. 5) για generation

### Πλεονεκτήματα
- Καλύτερη ακρίβεια
- Χρήση cross-encoders

---

## Prompt Engineering για RAG

### Βασική Δομή

```
You are a helpful assistant. Answer the question based ONLY on the
following context. If the answer is not in the context, say
"I don't have enough information."

Context:
{retrieved_documents}

Question: {user_question}

Answer:
```

### Best Practices

1. **Explicit instructions:** Καθοδήγηση να χρησιμοποιήσει μόνο τα documents
2. **Citation:** Ζήτησε να αναφέρει πηγές
3. **Uncertainty:** Να αναγνωρίζει όταν δεν ξέρει
4. **Format:** Καθορισμός format απάντησης

---

## Evaluation Metrics για RAG

### Retrieval Metrics

| Metric | Περιγραφή |
|--------|-----------|
| **Recall@k** | % σχετικών docs στα top-k results |
| **Precision@k** | % top-k που είναι σχετικά |
| **MRR** (Mean Reciprocal Rank) | 1/rank του πρώτου σχετικού |
| **NDCG** | Λαμβάνει υπόψη graded relevance |

### Generation Metrics

| Metric | Περιγραφή |
|--------|-----------|
| **Faithfulness** | Η απάντηση υποστηρίζεται από τα docs; |
| **Answer Relevance** | Απαντά στην ερώτηση; |
| **Context Relevance** | Τα ανακτημένα docs είναι σχετικά; |

---

## Large Language Models (LLMs)

### Βασικές Έννοιες

**Transformer Architecture:**
- Self-attention mechanism
- Positional encoding
- Encoder-decoder ή decoder-only

**Pre-training:**
- Next token prediction
- Masked language modeling
- Τεράστια corpora (internet text)

**Fine-tuning:**
- Instruction tuning (FLAN, InstructGPT)
- RLHF (Reinforcement Learning from Human Feedback)

### Τύποι Μοντέλων

| Τύπος | Παραδείγματα | Χρήση |
|-------|--------------|-------|
| **Encoder-only** | BERT, RoBERTa | Classification, NER |
| **Decoder-only** | GPT, LLaMA, Claude | Text generation |
| **Encoder-Decoder** | T5, BART | Translation, Summarization |

---

## Limitations of LLMs

### 1. Hallucinations
Παράγουν πληροφορίες που δεν είναι αληθείς.

### 2. Context Window
Περιορισμένος αριθμός tokens που μπορούν να επεξεργαστούν.

### 3. Outdated Knowledge
Γνώση μέχρι την ημερομηνία training (knowledge cutoff).

### 4. Computational Cost
Απαιτούν σημαντικούς υπολογιστικούς πόρους.

### 5. Bias
Αναπαράγουν biases από τα training data.

---

## RAG vs Fine-tuning

| Πτυχή | RAG | Fine-tuning |
|-------|-----|-------------|
| Knowledge update | Εύκολο (αλλαγή docs) | Απαιτεί re-training |
| Attribution | Δυνατή (πηγές) | Δύσκολη |
| Cost | Χαμηλότερο | Υψηλότερο |
| Customization | Περιορισμένη | Πλήρης |
| Hallucinations | Μειωμένες | Μπορεί να συνεχίζονται |

---

## Συχνά Θέματα Εξετάσεων

### 1. Γιατί RAG αντί για fine-tuning;
- Ενημέρωση γνώσης χωρίς re-training
- Attribution/provenance
- Μείωση hallucinations

### 2. Ρόλος του Vector Database
- Αποθήκευση embeddings
- Efficient similarity search
- Scaling to millions of documents

### 3. Chunking considerations
- Trade-off μεγέθους: μικρά = ακριβές retrieval, μεγάλα = περισσότερο context
- Overlap για συνέχεια

---

## Γρήγορη Αναφορά

```
╔══════════════════════════════════════════════════════════════════╗
║                   RAG & LLMs CHEAT SHEET                         ║
╠══════════════════════════════════════════════════════════════════╣
║ RAG PIPELINE:                                                    ║
║   1. Index documents → embeddings → vector DB                    ║
║   2. Query → embed → retrieve similar docs                       ║
║   3. Augment prompt with docs                                    ║
║   4. Generate answer with LLM                                    ║
╠══════════════════════════════════════════════════════════════════╣
║ ΠΛΕΟΝΕΚΤΗΜΑΤΑ RAG:                                               ║
║   • Grounded responses (λιγότερα hallucinations)                 ║
║   • Up-to-date (χωρίς re-training)                               ║
║   • Attribution (αναφορά πηγών)                                  ║
║   • Domain-specific (ιδιωτικά δεδομένα)                          ║
╠══════════════════════════════════════════════════════════════════╣
║ CHUNKING:                                                        ║
║   Small chunks: Ακριβές retrieval, λιγότερο context              ║
║   Large chunks: Περισσότερο context, λιγότερο ακριβές            ║
║   Overlap: Διατήρηση context μεταξύ chunks                       ║
╠══════════════════════════════════════════════════════════════════╣
║ EMBEDDINGS:                                                      ║
║   • Dense vector representations                                 ║
║   • Semantic similarity = cosine similarity                      ║
║   • Αποθήκευση σε Vector Database                                ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Ασκήσεις Εξάσκησης

### Άσκηση 1 (Σχεδιασμός RAG)
Σχεδιάστε RAG pipeline για Q&A σύστημα τεχνικής υποστήριξης με 10,000 PDF manuals.
- Ποιο chunk size θα επιλέγατε;
- Τι overlap;
- Ποια retrieval strategy;

### Άσκηση 2 (Comparison)
Εξηγήστε γιατί μια εταιρεία θα προτιμούσε RAG αντί για fine-tuning ενός LLM για customer support chatbot.

### Άσκηση 3 (Evaluation)
Αν ένα RAG σύστημα επιστρέφει 5 documents για μια ερώτηση και μόνο 2 είναι σχετικά:
1. Ποιο είναι το Precision@5;
2. Αν τα σχετικά documents είναι στις θέσεις 2 και 4, ποιο είναι το MRR;
