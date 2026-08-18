import faiss
import numpy as np


class FAISSIndex:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)

    def add(self, vectors):
        vectors = np.asarray(vectors, dtype="float32")
        vectors = np.ascontiguousarray(vectors)

        print("FAISS input shape:", vectors.shape)
        print("FAISS input dtype:", vectors.dtype)

        faiss.normalize_L2(vectors)

        self.index.add(vectors)

    def search(self, query_vector, top_k=5):
        query_vector = np.asarray(
            [query_vector],
            dtype="float32"
        )

        faiss.normalize_L2(query_vector)

        scores, ids = self.index.search(
            query_vector,
            top_k
        )

        return scores[0], ids[0]

    def save(self, path):
        faiss.write_index(
            self.index,
            path
        )

    def load(self, path):
        self.index = faiss.read_index(
            path
        )