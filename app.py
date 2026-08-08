from services.pdf_reader import read_texts
from services.chunker import split_documents


if __name__ == "__main__":

    documents = read_texts("./docs")

    for document_name, pages in documents.items():

        chunks = split_documents(pages)

        print("=" * 70)
        print(document_name)
        print(f"Total Pages Extracted : {len(pages)}")
        print(f"Total Chunks : {len(chunks)}")
        print("=" * 70)

        if pages:
            print("\nFirst 500 characters of Page 1:\n")
            print(pages[0].text[:500])
            print(pages[0].document_name)
            print(pages[0].page_number)

        if chunks:
            print("\nFirst Chunk:\n")
            print(chunks[5].text)
            print("\nDocument:", chunks[5].document_name)
            print("Page:", chunks[5].page_number)
            print("Chunk Number:", chunks[5].chunk_number)

        print("\n\n")