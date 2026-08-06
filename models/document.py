class Document:
    """
    Represents one page (or later, one chunk) of a document.
    """

    def __init__(self, text, document_name, page_number):
        self.text = text
        self.document_name = document_name
        self.page_number = page_number