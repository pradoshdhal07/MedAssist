class Chunk:

    def __init__(self, document_name, page_number, text,chunk_number):
        self.chunk_number = chunk_number
        self.text = text
        self.document_name = document_name
        self.page_number = page_number