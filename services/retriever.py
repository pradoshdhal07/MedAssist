import faiss

from services.embeddings import EmbeddingService
from services.chunk_store import load_chunks
from services.faiss_index import FAISSIndex


class Retriever:

    def __init__(
        self,
        index_path,
        chunks_path,
        embedding_model="all-MiniLM-L6-v2"
    ):
        # Load the embedding model
        self.embedding_service = EmbeddingService(
            embedding_model
        )

        # Create FAISS index object
        self.faiss_index = FAISSIndex(384)

        # Load the saved FAISS index
        self.faiss_index.load(index_path)

        # Load the original chunks
        self.chunks = load_chunks(chunks_path)

    def retrieve(self, query, top_k=7):

        # Convert user query into an embedding
        query_vector = self.embedding_service.embed_text(
            query
        )

        # Search FAISS
        scores, ids = self.faiss_index.search(
            query_vector,
            top_k
        )

        # Get the actual chunks using FAISS IDs
        results = []

        for score, chunk_id in zip(scores, ids):

            if chunk_id == -1:
                continue

            chunk = self.chunks[chunk_id]

            results.append(
                {
                    "score": float(score),
                    "chunk_id": int(chunk_id),
                    "chunk": chunk
                }
            )

        return results