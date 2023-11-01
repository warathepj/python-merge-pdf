import PyPDF2

def merge_pdfs(pdf_files):
  """Merges a list of PDF files into a single PDF file.

  Args:
    pdf_files: A list of PDF file paths.

  Returns:
    A PDF file object.
  """

  merger = PyPDF2.PdfMerger()
  for pdf_file in pdf_files:
    merger.append(pdf_file)

  return merger.write('merged.pdf')


if __name__ == '__main__':
  pdf_files = ['ฉันคือ pdf file 1.pdf', 'ฉันคือ pdf file 2.pdf', 'ฉันคือ pdf file 3.pdf']
  merged_pdf = merge_pdfs(pdf_files)

  print('The PDFs have been merged successfully.')