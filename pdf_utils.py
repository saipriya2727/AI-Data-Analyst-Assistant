from pypdf import PdfReader

def extract_pdf_text(uploaded_pdf):

    reader = PdfReader(uploaded_pdf)

    pdf_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            pdf_text += text

    return pdf_text