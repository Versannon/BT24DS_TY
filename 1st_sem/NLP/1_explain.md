# Explanation of `1.ipynb`

The Jupyter Notebook [`1.ipynb`](file:///c:/Soham/Repositories/BT24DS_TY/1st_sem/NLP/1.ipynb) provides a side-by-side comparison of basic Natural Language Processing (NLP) text preprocessing techniques across **NLTK**, **spaCy**, and a **Pure Python** pipeline (without NLTK/spaCy), followed by a **WordCloud** visualization.

---

## 1. Overview & Workflow

### Step 1: Resource Download & Package Imports
- **NLTK Downloads**: Downloads essential corpora and models (`punkt`, `punkt_tab`, `stopwords`, and `wordnet`).
- **Imports**: Imports `pandas`, `spacy`, `re`, `matplotlib.pyplot`, `WordCloud`, and NLTK processing classes (`PorterStemmer`, `WordNetLemmatizer`, `word_tokenize`, `stopwords`).
- **Language Model**: Loads spaCy's standard small English pipeline model (`en_core_web_sm`).

### Step 2: Sample Input Text & Tool Init
```python
text = "Don't blink! The data scientists are buying new computers for their user studies."
```
Initializes stemmers/lemmatizers, NLTK stop-word sets, and a custom **Pure Python stop-word set** (`pure_python_stopwords`).

### Step 3: NLTK Preprocessing Pipeline
- **Tokenization**: Splits text into tokens using `word_tokenize(text)`.
- **Stop-Word Removal**: Checks lowercased tokens against NLTK's English stop-word list or non-alphanumeric check.
- **Stemming**: Applies `PorterStemmer().stem(token)` (e.g., `computers` $\rightarrow$ `comput`, `studies` $\rightarrow$ `studi`).
- **Lemmatization**: Applies `WordNetLemmatizer().lemmatize(token.lower())` without explicit POS tags.

### Step 4: spaCy Preprocessing Pipeline
- **Tokenization & Analysis**: Passes text through `nlp(text)` for integrated tokenization, tagging, and parsing.
- **Stop-Word Detection**: Uses native boolean flags `token.is_stop` and `token.is_punct`.
- **Lemmatization**: Context-aware POS tagging (`are` $\rightarrow$ `be`, `buying` $\rightarrow$ `buy`, `n't` $\rightarrow$ `not`).
- **Stemming**: `"N/A"` (spaCy omits heuristic stemming by design).

### Step 5: Pure Python Preprocessing Pipeline (No NLTK / spaCy)
- **Regex Tokenization**: Uses `re.findall(r"\b\w+(?:'\w+)?\b|[^\w\s]", text)` to split contractions and punctuation.
- **Pure Python Stop Words**: Checks tokens against `pure_python_stopwords` set and non-alphanumeric test.
- **Pure Python Stemming & Normalization**: Demonstrates basic string slicing rules (e.g., stripping suffix `-s` or `-ing` on lowercased tokens).

### Step 6: 3-Way Comparison Matrix Output
All three tokenized datasets (`df_nltk`, `df_spacy`, `df_pure`) are converted into Pandas DataFrames and concatenated side-by-side.

### Step 7: WordCloud Generation
Filters non-stop tokens from `pure_processed`, joins them into `cleaned_text`, and uses `WordCloud(width=800, height=400).generate(cleaned_text)` to render a visualization via `matplotlib`.

---

## 2. Pipeline Comparison Matrix

| Feature | NLTK Pipeline | spaCy Pipeline | Pure Python Pipeline |
| :--- | :--- | :--- | :--- |
| **Dependencies** | `nltk` | `spacy` | Python Standard Library (`re`, `set`) |
| **Tokenization** | `word_tokenize` | `nlp(text)` | Regex `re.findall()` |
| **Stop Words** | `stopwords.words('english')` | `token.is_stop` flag | Custom `set` lookup |
| **Stemming** | `PorterStemmer` (`comput`) | Not supported (`N/A`) | Pure Python suffix rules (`comput`, `buy`) |
| **Lemmatization** | `WordNetLemmatizer` (noun default) | Model POS-aware (`be`, `buy`) | Lowercase normalization |

---

## 3. Key Takeaways
1. **Zero External Dependencies**: Pure Python text processing provides a lightweight pipeline for basic cleaning, stop-word removal, and regex tokenization.
2. **WordCloud Integration**: Once text is cleaned of stop words and punctuation by the Pure Python pipeline, it feeds directly into `WordCloud().generate(cleaned_text)` for visual frequency analysis.
