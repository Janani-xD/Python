import pdfplumber
import pandas as pd

# Path to your bank statement PDF
pdf_path = "/Users/janani/PycharmProjects/Python/input_statement.pdf"

salary_rows = []

with pdfplumber.open(pdf_path,password="114666684") as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        tables = page.extract_tables()

        if tables:
            # 🧾 Case 1: Table-based PDF
            for table in tables:
                for row in table:
                    if not any(row):  # skip empty rows
                        continue
                    row_text = " ".join(str(cell).lower() for cell in row if cell)
                    if "salary" in row_text:
                        salary_rows.append(row)
        else:
            # 🧾 Case 2: Text-based PDF (line-by-line)
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    if "salary" in line.lower():
                        salary_rows.append([page_number, line])

        # ✅ Convert results to DataFrame and export
    if salary_rows:
        df = pd.DataFrame(salary_rows)
        output_file = "salary_transactions.xlsx"
        df.to_excel(output_file, index=False)
        print(f"\n✅ Extracted {len(salary_rows)} rows. Saved to '{output_file}'.")
    else:
        print("\n⚠️ No rows containing 'salary' were found in the PDF.")

# import fitz
# input_pdf = "/Users/janani/PycharmProjects/Python/input_statement.pdf"
# output_pdf = "output_statement.pdf"
# str_to_search = "salary"
#
# doc = fitz.open(input_pdf)
# print(doc.page_count)
# for page_num in range(doc.page_count):
#     page = doc[page_num]
#     print(page)