import faiss
import numpy as np


# Create a tiny IndexFlatIP with 3 dimensions
index = faiss.IndexFlatIP(3)

vectors = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
], dtype="float32")

index.add(vectors)

print("Before save:")
print("Dimension:", index.d)
print("Vectors:", index.ntotal)


# Save
faiss.write_index(index, "./index/test.faiss")

print("Saved.")


# Load
loaded = faiss.read_index("./index/test.faiss")

print("\nAfter load:")
print("Dimension:", loaded.d)
print("Vectors:", loaded.ntotal)