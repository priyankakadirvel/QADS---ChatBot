from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load your local corpus (e.g., syllabus notes, PDFs)
corpus = [...]  # List of text snippets
corpus_embeddings = [...]  # Precomputed embeddings

def retrieve_context(question, top_k=3):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    question_embedding = model.encode(question, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(question_embedding, corpus_embeddings)[0]
    top_results = np.argpartition(-scores, range(top_k))[:top_k]
    return [corpus[idx] for idx in top_results]
