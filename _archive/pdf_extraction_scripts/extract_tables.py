import fitz
import sys

pdf_path = "/Users/ale.echeverri/Survey_Design/Relevant Literature/Exported Items/files/25684/Thomas and Grigsby - 2024 - Narrative transportation A systematic literature review and future research agenda.pdf"
doc = fitz.open(pdf_path)

for i in range(len(doc)):
    page = doc[i]
    tables = page.find_tables()
    if tables.tables:
        print(f"--- Page {i+1} Tables ---")
        for table in tables:
            for row in table.extract():
                if row:
                    print(" | ".join([cell.replace("\n", " ").strip() if cell else "" for cell in row]))
