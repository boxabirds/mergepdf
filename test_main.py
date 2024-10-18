

# We're getting these deprecation warnings: not sure there's much we can do about them right now
# frozen importlib._bootstrap>:488
# <frozen importlib._bootstrap>:488
#   <frozen importlib._bootstrap>:488: DeprecationWarning: builtin type SwigPyPacked has no __module__ attribute

# <frozen importlib._bootstrap>:488
# <frozen importlib._bootstrap>:488
#   <frozen importlib._bootstrap>:488: DeprecationWarning: builtin type SwigPyObject has no __module__ attribute

# <frozen importlib._bootstrap>:488
#   <frozen importlib._bootstrap>:488: DeprecationWarning: builtin type swigvarlink has no __module__ attribute

# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# test_main.py
import pytest

from pathlib import Path
import fitz  # PyMuPDF
from main import merge_pdfs


@pytest.fixture(scope="module")
def test_data_folder():
    return Path(__file__).parent / "tests" / "data" / "e2e"

def test_merge_pdfs(test_data_folder):
    output_file = merge_pdfs(test_data_folder)
    
    # Check if the output file exists
    assert output_file.exists(), f"Output file {output_file} does not exist"
    
    # Count total pages in input PDFs
    total_input_pages = sum(fitz.open(str(file)).page_count for file in test_data_folder.glob("*.pdf"))
    
    # Count pages in the merged PDF
    with fitz.open(str(output_file)) as merged_doc:
        merged_pages = merged_doc.page_count
    
    # Compare page counts
    assert merged_pages == total_input_pages, f"Expected {total_input_pages} pages, got {merged_pages}"

def test_output_file_location(test_data_folder):
    output_file = merge_pdfs(test_data_folder)
    assert output_file.parent == test_data_folder.parent, "Output file is not in the correct location"

def test_output_file_name(test_data_folder):
    output_file = merge_pdfs(test_data_folder)
    expected_name = f"{test_data_folder.name}.pdf"
    assert output_file.name == expected_name, f"Expected output file name '{expected_name}', got '{output_file.name}'"
