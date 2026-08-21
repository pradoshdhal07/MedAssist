from services.retriever import Retriever


# Create Retriever
retriever = Retriever(
    index_path="./index/medassist.faiss",
    chunks_path="./index/chunks.pkl"
)


# Take query from user
query = input("\nEnter your question: ")


# Retrieve top 5 relevant chunks
results = retriever.retrieve(
    query,
    top_k=7
)


# Display results
print("\n===== RETRIEVAL RESULTS =====")

for rank, result in enumerate(results, start=1):

    chunk = result["chunk"]

    print("\n-----------------------------")
    print("Rank:", rank)
    print("Chunk ID:", result["chunk_id"])
    print("Similarity Score:", round(result["score"], 4))
    print("Document:", chunk.document_name)
    print("Page:", chunk.page_number)

    print("\nText:")
    print(chunk.text)