# Archive

This folder contains one-off scripts and their outputs that were used during the initial literature review and theory table construction. They are preserved here for reference but are **not part of the active workflow**.

## Contents

### `pdf_extraction_scripts/`
Scripts used to extract text and tables from the Thomas & Grigsby (2024) narrative transportation PDF:

| Script | Purpose |
| :--- | :--- |
| `extract_tables.py` | Extracts tables from the PDF using PyMuPDF |
| `parse_pdf.py` | Searches the PDF for pages containing "Table 1" |
| `page34.py` | Extracts raw text from pages 3–5 |
| `format.py` | Formats a theory list into a Markdown table |
| `generate_table.py` | Similar to `format.py`; generates a 3-column Markdown table |

### `pdf_extraction_outputs/`
Text and table outputs produced by the scripts above:

| File | Contents |
| :--- | :--- |
| `extracted_table.md` | Early draft theory table (superseded by `Step_02_Theory_Grounding/theory_summary.md`) |
| `page34.txt` | Raw text extracted from pages 3–5 of the PDF |
| `pdf_output.txt` | Raw text from pages containing "Table 1" |
| `tables.txt` | Raw table extraction output |
