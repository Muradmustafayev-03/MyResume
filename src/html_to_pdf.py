import sys

import fitz
import pdfkit


# Function to convert HTML to PDF
def html_to_pdf(input_url, output_pdf):
    options = {
        'enable-local-file-access': None,  # This enables local file access
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
        'page-size': 'A4',
    }
    pdfkit.from_url(input_url, output_pdf, options=options)


def extract_first_page(input_pdf):
    doc = fitz.open(input_pdf)
    new_doc = fitz.open()  # Create a new empty PDF
    new_doc.insert_pdf(doc, from_page=0, to_page=0)  # Insert only the first page
    new_doc.save(input_pdf)


def get_pdf(input_url, output_pdf):
    html_to_pdf(input_url, output_pdf)
    extract_first_page(output_pdf)
    return output_pdf


if __name__ == '__main__':
    get_pdf(sys.argv[1], sys.argv[2])
