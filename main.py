import sys
from pathlib import Path
import fitz  # PyMuPDF
import pytest
import os
def merge_pdfs(source_folder_path):
    source_folder = Path(source_folder_path)
    parent_dir = source_folder.parent
    folder_name = source_folder.name
    output_file = parent_dir / f"{folder_name}.pdf"

    result = fitz.open()

    pdf_files = sorted([file for file in source_folder.glob("*.pdf")], key=lambda x: os.path.getmtime(x))

    # print out the files that are being merged in the order they are being merged

    print(f"Merging the following PDFs in this order:")
    for pdf_file in pdf_files:
        print(f"{pdf_file} ({os.path.getctime(pdf_file)})")

    for pdf_file in pdf_files:
        with fitz.open(str(pdf_file)) as mfile:
            result.insert_pdf(mfile)

    result.save(str(output_file))
    result.close()

    print(f"Merged PDF saved as {output_file}")
    return output_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <source_folder_path>")
        sys.exit(1)
    
    source_folder_path = sys.argv[1]
    merge_pdfs(source_folder_path)

