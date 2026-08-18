from services.faiss_index import FAISSIndex
from services.chunk_store import load_chunks


faiss_index = FAISSIndex(384)
faiss_index.load("./index/medassist.faiss")

chunks = load_chunks("./index/chunks.pkl")

print(f"Vectors loaded from FAISS: {faiss_index.index.ntotal}")
print(f"Chunks loaded: {len(chunks)}")


faiss_id = 1234

vector = faiss_index.index.reconstruct(faiss_id)
chunk = chunks[faiss_id]


print("\n--- FAISS ID 1234 ---")
print(f"Vector shape: {vector.shape}")
print(f"First 10 vector values: {vector[:10]}")

print("\n--- CHUNK 1234 ---")
print(chunk)