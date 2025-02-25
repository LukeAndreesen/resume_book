import os
from PyPDF2 import PdfMerger

folder_path = "resumes_to_merge"
output_pdf = "merged.pdf"

merger = PdfMerger()
count = 0
for pdf_file in sorted(os.listdir(folder_path)):
    print(f"Processing file {count + 1}")
    print(f"{pdf_file}")
    count += 1
    if pdf_file.endswith(".pdf"):
        merger.append(os.path.join(folder_path, pdf_file))

merger.write(output_pdf)
merger.close()
print(f"PDFs merged into {output_pdf}")

