from services.pdf_reader import read_texts
if __name__ == "__main__":

    documents = read_texts("./docs")

    for document_name, pages in documents.items():

        print("=" * 70)
        print(document_name)
        print(f"Total Pages Extracted : {len(pages)}")
        print("=" * 70)

        if pages:
            print("\nFirst 500 characters of Page 1:\n")
            print(pages[0].text[:500])
            print(pages[0].document_name)
            print(pages[0].page_number)

        print("\n\n")