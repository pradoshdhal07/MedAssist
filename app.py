from services.pdf_reader import read_texts
from services.chunker import split_documents
from services.embeddings import EmbeddingService
from services.faiss_index import FAISSIndex
from services.chunk_store import save_chunks


if __name__ == "__main__":

    # 1. Read all PDFs
    documents = read_texts("./docs")

    # 2. Create chunks from all documents
    all_chunks = []

    for pages in documents.values():
        chunks = split_documents(pages)
        all_chunks.extend(chunks)

    print(f"Total chunks: {len(all_chunks)}")

    # 3. Load embedding model
    embedding_service = EmbeddingService("all-MiniLM-L6-v2")

    # 4. Create embeddings for all chunks
    vectors = [
        embedding_service.embed_text(chunk.text)
        for chunk in all_chunks
    ]

    print(f"Total vectors: {len(vectors)}")
    print(f"Vector dimension: {vectors[0].shape}")

    # 5. Create FAISS index
    faiss_index = FAISSIndex(384)

    # 6. Add embeddings to FAISS
    faiss_index.add(vectors)

    print(f"Total vectors in FAISS: {faiss_index.index.ntotal}")

    print("Before saving:")
    print("Index type:", type(faiss_index.index))
    print("Dimension:", faiss_index.index.d)
    print("Total vectors:", faiss_index.index.ntotal)

    # 7. Save FAISS index
    faiss_index.save("./index/medassist.faiss")

    # 8. Save original chunks
    save_chunks(all_chunks, "./index/chunks.pkl")

    print("FAISS index saved.")
    print("Chunks saved.")