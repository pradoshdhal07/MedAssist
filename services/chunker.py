from models.chunk import Chunk


def split_documents(documents):
   

    chunks = []

    chunk_size = 500
    overlap = 150
    boundary_buffer = 50

    for document in documents:

        text = document.text
        start = 0
        chunk_number = 1

        while start < len(text):

            end = min(start + chunk_size, len(text))

            # If we haven't reached the end,
            # try to find a natural word boundary.
            if end < len(text):

                search_start = max(start, end - boundary_buffer)

                boundary = text.rfind(" ", search_start, end)

                if boundary > start:
                    end = boundary

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append(
                    Chunk(
                        document_name=document.document_name,
                        page_number=document.page_number,
                        text=chunk_text,
                        chunk_number=chunk_number
                    )
                )

                chunk_number += 1
            if end == len(text):
                break

            # Move forward while keeping the overlap.
            start = end - overlap

            if start < 0:
                start = 0

    return chunks