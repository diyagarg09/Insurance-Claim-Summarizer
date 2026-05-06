import PyPDF2

def extract_text_from_pdf(file_path):
    """PDF se saara text extract karne ke liye logic"""
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        # 500 pages tak loop chalega
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text