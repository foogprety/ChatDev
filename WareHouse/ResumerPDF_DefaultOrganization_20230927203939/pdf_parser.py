'''
This file contains functions to parse the content of a PDF file.
'''
import PyPDF2
def parse_pdf(file_path):
    '''
    Parse the PDF file and extract the content.
    Args:
        file_path (str): The path to the PDF file.
    Returns:
        str: The extracted content from the PDF file.
    '''
    content = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            content += page.extractText()
    return content