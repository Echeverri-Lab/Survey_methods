import fitz
pdf_path = "/Users/ale.echeverri/Survey_Design/Relevant Literature/Exported Items/files/25684/Thomas and Grigsby - 2024 - Narrative transportation A systematic literature review and future research agenda.pdf"
doc = fitz.open(pdf_path)

for i in range(2, 6):
    print(f"--- Page {i+1} Text ---")
    print(doc[i].get_text())
