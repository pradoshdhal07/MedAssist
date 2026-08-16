from services.pdf_reader import read_texts
from services.chunker import split_documents
from services.embeddings import EmbeddingService


if __name__ == "__main__":

    documents = read_texts("./docs")

    all_chunks = []

    for pages in documents.values():
        chunks = split_documents(pages)
        all_chunks.extend(chunks)

    print(f"Total chunks: {len(all_chunks)}")

    embedding_service = EmbeddingService("all-MiniLM-L6-v2")

    vector = embedding_service.embed_text(all_chunks[0].text)

    print(f"Vector type: {type(vector)}")
    print(f"Vector shape: {vector.shape}")
    print(f"First 10 values: {vector[:10]}")