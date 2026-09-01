from services.retriever import Retriever
from services.context_builder import ContextBuilder


retriever = Retriever(
    index_path="./index/medassist.faiss",
    chunks_path="./index/chunks.pkl"
)

builder = ContextBuilder()


query = input("Enter your question: ")

results = retriever.retrieve(query, top_k=7)

context = builder.build(results)


print("\n===== GENERATED CONTEXT =====\n")
print(context)