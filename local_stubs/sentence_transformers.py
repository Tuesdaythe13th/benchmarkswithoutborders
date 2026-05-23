
"""
Local fallback sentence_transformers using sklearn TF-IDF + TruncatedSVD.
Used when no internet connection is available for downloading models.
"""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize

class SentenceTransformer:
    """Drop-in replacement using TF-IDF + SVD (384-dim output like MiniLM)."""
    
    def __init__(self, model_name_or_path=None, *args, **kwargs):
        self.model_name = model_name_or_path
        self.n_components = 384
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2), max_features=5000, 
            sublinear_tf=True, strip_accents="unicode"
        )
        self.svd = TruncatedSVD(n_components=min(self.n_components, 383), random_state=42)
        self._fitted = False
        print(f"[offline] Using TF-IDF+SVD fallback for: {model_name_or_path}")
    
    def encode(self, sentences, batch_size=32, show_progress_bar=False, **kwargs):
        if isinstance(sentences, str):
            sentences = [sentences]
        
        sentences = [str(s) for s in sentences]
        
        if not self._fitted:
            tfidf_matrix = self.vectorizer.fit_transform(sentences)
            n = min(self.svd.n_components, tfidf_matrix.shape[1] - 1, tfidf_matrix.shape[0] - 1)
            if n < 2:
                n = 2
            self.svd.n_components = n
            self._fitted = True
            embeddings = self.svd.fit_transform(tfidf_matrix)
        else:
            try:
                tfidf_matrix = self.vectorizer.transform(sentences)
                embeddings = self.svd.transform(tfidf_matrix)
            except Exception:
                tfidf_matrix = self.vectorizer.fit_transform(sentences)
                n = min(self.svd.n_components, tfidf_matrix.shape[1] - 1, tfidf_matrix.shape[0] - 1)
                if n < 2: n = 2
                self.svd.n_components = n
                embeddings = self.svd.fit_transform(tfidf_matrix)
        
        # Pad to 384 dimensions
        if embeddings.shape[1] < self.n_components:
            padding = np.zeros((embeddings.shape[0], self.n_components - embeddings.shape[1]))
            embeddings = np.hstack([embeddings, padding])
        
        embeddings = normalize(embeddings, norm="l2")
        return embeddings.astype(np.float32)
    
    def __call__(self, sentences, *args, **kwargs):
        return self.encode(sentences, *args, **kwargs)


class util:
    @staticmethod
    def cos_sim(a, b):
        from sklearn.metrics.pairwise import cosine_similarity
        a = np.array(a)
        b = np.array(b)
        if a.ndim == 1: a = a.reshape(1, -1)
        if b.ndim == 1: b = b.reshape(1, -1)
        return cosine_similarity(a, b)
    
    @staticmethod
    def semantic_search(query_embeddings, corpus_embeddings, top_k=5):
        from sklearn.metrics.pairwise import cosine_similarity
        sims = cosine_similarity(query_embeddings, corpus_embeddings)
        results = []
        for row in sims:
            indices = row.argsort()[::-1][:top_k]
            results.append([{"corpus_id": int(i), "score": float(row[i])} for i in indices])
        return results
