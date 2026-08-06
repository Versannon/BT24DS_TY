# Natural Language Processing (NLP) - Comprehensive Theory Notes

## 1. Introduction to Natural Language Processing
Natural Language Processing (NLP) is an interdisciplinary subfield of Computer Science, Artificial Intelligence, and Computational Linguistics concerned with the interactions between computers and human languages.

* **Core Goal:** To enable computers to read, decipher, understand, process, and generate human languages in a valuable and contextually meaningful way.
* **Key Challenges in NLP:**
  * **Ambiguity:** Lexical (polysemy), Syntactic, and Semantic ambiguities.
  * **Context Dependence:** Pragmatics and subtle contextual shifts (irony, sarcasm).
  * **Unstructured Nature:** Human text lacks pre-defined schema or strict database structures.
* **Real-world Applications:**
  * Automated Chatbots & Conversational AI
  * Email Spam Filtering & Categorization
  * Sentiment Analysis & Opinion Mining
  * Automated Resume Parsing and Candidate Matching
  * Machine Translation (e.g., Google Translate)
  * Text Summarization and Question Answering Systems

---

## 2. The General NLP Pipeline
Processing natural language follows a multi-stage data flow:

```
[Raw Text Ingestion] ➔ [Text Preprocessing] ➔ [Feature Extraction] ➔ [Modeling & Analysis] ➔ [Evaluation & Deployment]
```

1. **Text Ingestion & Data Collection:** Fetching raw text from APIs, databases, web scraping, or document parsing (PDF, DOCX, TXT).
2. **Text Preprocessing & Normalization:**
   * Noise Removal (removing HTML tags, special characters, URLs).
   * Lowercasing text to enforce uniformity.
   * Tokenization (splitting text into smaller units).
   * Stop Word Removal & Stemming/Lemmatization.
3. **Feature Extraction (Vectorization):** Converting text into numeric representations readable by machine learning models.
   * Frequency-based: Bag of Words (BoW), Term Frequency-Inverse Document Frequency (TF-IDF).
   * Prediction-based / Embeddings: Word2Vec, FastText, GloVe, Transformer Embeddings.
4. **Model Training & Text Analysis:** Training statistical models, machine learning algorithms, or deep neural networks to perform tasks (Classification, Clustering, Named Entity Recognition).
5. **Evaluation & Deployment:** Validating performance using metrics like Accuracy, Precision, Recall, F1-Score, BLEU, or ROUGE, followed by REST API deployment or batch inference pipelines.

---

## 3. Unit 1: Finding the Structure of Words (Lexical & Morphological Analysis)

### Words and Their Components
* **Word:** The smallest independent unit of language that carries meaning.
* **Morpheme:** The smallest grammatical unit in a language that carries meaning (e.g., in "unbreakable", `un-` is a prefix morpheme, `break` is a root morpheme, `-able` is a suffix morpheme).
* **Morphology:** The study of the internal structure of words and how words are formed from smaller units.

### Key Word Processing Techniques
1. **Tokenization:** The process of breaking a stream of text into tokens (words, phrases, symbols, or subwords).
   * *Word Tokenization:* Splitting sentences into individual words.
   * *Sentence Tokenization:* Segmenting paragraphs into distinct sentences.
   * *Subword Tokenization:* Used in modern LLMs (Byte-Pair Encoding, WordPiece) to handle out-of-vocabulary (OOV) words.
2. **Stemming:** A crude heuristic process that chops off word endings (suffixes/prefixes) to reduce words to their base stem form.
   * *Rule-based:* Does not use a dictionary (e.g., Porter Stemmer, Lancaster Stemmer).
   * *Drawbacks:* Over-stemming (reducing distinct words to the same stem like "universe" and "university" -> "univers") and Under-stemming.
3. **Lemmatization:** Algorithmic process of determining the canonical form (lemma) of a word based on its intended meaning and Part of Speech (POS).
   * *Dictionary-backed:* Uses morphological analysis and vocabularies like WordNet.
   * *Example:* "better" -> "good" (Adjective), "running" -> "run" (Verb).
4. **Part-of-Speech (POS) Tagging:** Assigning grammatical labels (Noun, Verb, Adjective, Adverb, Preposition) to each word based on context and syntax.

---

## 4. Comprehensive Guide to Common Libraries in NLP

### 1. NLTK (Natural Language Toolkit)
* **Overview:** A leading platform for building Python programs to work with human language data. It provides user-friendly interfaces to over 50 corpora and lexical resources (e.g., WordNet), along with a suite of text processing libraries.
* **Primary Role:** Academic research, teaching classical NLP algorithms, prototyping, and educational demonstrations.
* **Key Features:**
  * Wide variety of classical tokenizers, stemmers (Porter, Snowball, Lancaster), and lemmatizers (WordNet).
  * Built-in corpora (Gutenberg, Brown, Stopwords datasets).
  * Rule-based grammars, parsing algorithms, and Chunking/POS tagging modules.
* **Strengths & Limitations:**
  * *Strengths:* Highly modular, extensive documentation, complete coverage of foundational NLP theory.
  * *Limitations:* Slower performance on large production datasets; lacks modern deep-learning optimized pipelines out-of-the-box.

### 2. spaCy
* **Overview:** An industrial-strength NLP library written in Cython, designed specifically for production usage and computational efficiency.
* **Primary Role:** Enterprise NLP pipelines, high-throughput text processing, entity extraction, and production applications.
* **Key Features:**
  * **Pre-trained Statistical & Neural Models:** Out-of-the-box support for Named Entity Recognition (NER), Dependency Parsing, and POS Tagging.
  * **Optimized Pipeline Architecture:** Processes text through a sequential pipeline object (`nlp(text)`).
  * **Built-in Word Vectors & Embeddings:** Direct access to dense vector representations.
  * **Cython Integration:** C-level execution speed for tokenization and parsing.
* **Applications:** Resume parsing systems (e.g., recruitment platforms like LinkedIn), entity extraction from unstructured legal/medical records, knowledge graph construction.

### 3. scikit-learn
* **Overview:** A premier machine learning library in Python providing tools for data mining, data analysis, and predictive modeling.
* **Primary Role:** Classical statistical machine learning pipelines for text classification, clustering, and regression.
* **Key Features:**
  * `CountVectorizer`: Implements Bag-of-Words (BoW) feature extraction.
  * `TfidfVectorizer`: Converts raw text documents into a TF-IDF feature matrix, balancing word frequency against document frequency.
  * Classifiers: Naive Bayes (`MultinomialNB`), Logistic Regression, Support Vector Machines (`LinearSVC`), Random Forests.
  * Pipelines & Evaluation: `Pipeline` abstraction for combining vectorizers and estimators, metric utilities (`classification_report`, `confusion_matrix`).
* **Applications:** Spam email filtering, news topic classification, customer sentiment classification.

### 4. Gensim
* **Overview:** An open-source Python library specializing in unsupervised topic modeling and natural language document indexing.
* **Primary Role:** Semantic analysis, document similarity, vector space modeling, and topic discovery.
* **Key Features:**
  * **Word Embeddings:** Efficient implementations of Word2Vec (Skip-gram, CBOW), FastText, and Doc2Vec.
  * **Topic Modeling:** Latent Dirichlet Allocation (LDA), Latent Semantic Indexing (LSI/LSA), Hierarchical Dirichlet Process (HDP).
  * **Memory Efficiency:** Streaming algorithms capable of processing text corpora larger than available RAM.
* **Applications:** Automated document clustering, semantic search engines, content recommendation systems.

### 5. Pandas
* **Overview:** A core data manipulation and analysis library built on top of NumPy.
* **Primary Role:** Wrangling, cleaning, filtering, and organizing tabular text datasets (e.g., CSV, JSON, Parquet files).
* **Key Features:**
  * `DataFrame` and `Series` text methods via the `.str` accessor (`.str.lower()`, `.str.replace()`, `.str.contains()`, `.str.split()`).
  * Text dataset loading, missing data handling (`dropna`, `fillna`), and merging/grouping operations.
* **Applications:** Structuring raw survey responses, filtering customer feedback datasets, preparing text data before vectorization.

### 6. Matplotlib & Seaborn
* **Overview:** Standard Python data visualization libraries.
* **Primary Role:** Graphical representation of text statistics, corpus distributions, and model performance metrics.
* **Key Features:**
  * Plotting n-gram frequency distributions (top 20 most frequent words/bigrams).
  * Visualizing document length and sentence length distributions (histograms, box plots).
  * Plotting model confusion matrices, ROC curves, and classification performance graphs.
* **Applications:** Exploratory Data Analysis (EDA) of NLP datasets.

### 7. WordCloud
* **Overview:** A specialized Python visualization library for generating word clouds where word size corresponds to frequency or weight.
* **Primary Role:** High-level visual summarization of text corpora.
* **Key Features:**
  * Configurable parameters for stopwords, max words, font scale, background color, and custom image masks.
  * Quick identification of dominant themes in text bodies.
* **Applications:** Executive marketing dashboards, customer feedback visualization, social media trend analysis.

### 8. Hugging Face Transformers & PyTorch / TensorFlow
* **Overview:** Modern state-of-the-art deep learning ecosystem for NLP built on the Transformer architecture.
* **Primary Role:** Neural NLP, Large Language Models (LLMs), deep contextual embeddings, fine-tuning pre-trained models.
* **Key Features:**
  * Access to thousands of pre-trained models (BERT, RoBERTa, T5, GPT, LLaMA).
  * Advanced Tokenizers (BPE, WordPiece, SentencePiece) aligned with pre-trained model vocabularies.
  * Fine-tuning pipelines for sequence classification, token classification (NER), question answering, and text generation.
* **Applications:** Modern conversational agents, contextual search, zero-shot classification, automated translation.

---

## 5. Comparative Summary Matrix of NLP Libraries

| Library | Focus / Domain | Primary Strengths | Best Used For |
| :--- | :--- | :--- | :--- |
| **NLTK** | Academia & Learning | Educational, modular, built-in corpora | Learning NLP theory, building prototypes |
| **spaCy** | Industrial NLP | High speed (Cython), pre-trained pipelines | Production NER, POS tagging, parser pipelines |
| **scikit-learn** | Classical ML | Simple API, TF-IDF vectorization, classifiers | Text classification (Spam, Sentiment, Topic) |
| **Gensim** | Semantic Vector Space | Memory efficient, LDA topic modeling, Word2Vec | Document similarity, topic extraction |
| **Pandas** | Data Wrangling | Rich string methods (`.str`), tabular data ops | Cleaning, tabular text management |
| **Matplotlib/Seaborn** | Data Visualization | Highly customizable charts | EDA, plotting distributions & confusion matrices |
| **WordCloud** | Visual Summarization | Intuitive frequency-based word visualization | Dashboards, marketing insights |
| **Hugging Face** | Deep Learning / LLMs | Pre-trained Transformers (BERT, GPT), state-of-the-art | Neural NLP, fine-tuning, generative tasks |