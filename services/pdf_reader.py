from pathlib import Path
from pypdf import PdfReader
from models.document import Document
# READ PDFS

def read_pdfs(directory):
    """
    Returns a list of all PDF Path objects inside the directory.
    """

    pdf_files = []

    directory_path = Path(directory)

    if not directory_path.exists() or not directory_path.is_dir():
        print(f"'{directory}' does not exist or is not a directory.")
        return pdf_files

    for file in directory_path.iterdir():

        if file.is_file() and file.suffix.lower() == ".pdf":
            pdf_files.append(file)

    return pdf_files

# READ TEXTS


def read_texts(directory):
    """
    Reads every PDF and stores the text page-wise.

    Returns:
    {
        "Stryker": [
            "Page 1 text...",
            "Page 2 text...",
            ...
        ],

        "GE": [
            "Page 1 text...",
            ...
        ]
    }
    """
    print(f"Reading PDFs from '{directory}'...")
    pdf_contents = {}

    pdf_files = read_pdfs(directory)   # CALL THE READ_PDFS FUNCTION TO GET ALL PDF FILES IN THE DIRECTORY

    for pdf in pdf_files:
        print(f"Reading '{pdf.name}'...")

        reader = PdfReader(pdf)

        pages = []

        for page_number, page in enumerate(reader.pages, start=1):

            page_text = page.extract_text()

            if page_text:
                pages.append( Document (
                    text=page_text, document_name=pdf.stem, page_number=page_number))
        pdf_contents[pdf.stem] = pages
        print(f"Completed reading '{pdf.name}'...")

    return pdf_contents
print("PDF_READER_LOADED")
