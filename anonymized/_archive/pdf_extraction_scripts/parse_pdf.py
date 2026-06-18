import fitz # PyMuPDF
pdf_path = "/Users/ale.echeverri/Survey_Design/Relevant Literature/Exported Items/files/25684/Thomas and Grigsby - 2024 - Narrative transportation A systematic literature review and future research agenda.pdf"
doc = fitz.open(pdf_path)

for i, page in enumerate(doc):
    text = page.get_text()
    if "Table 1" in text or "Table I" in text:
        print(f"Page {i+1}:\n{text}")
