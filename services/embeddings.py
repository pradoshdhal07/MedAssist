from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text):
        return self.model.encode(text)