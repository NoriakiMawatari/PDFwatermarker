"""
PDF watermarker
Description:
Python code that watermarks selected .pdf files.
Execution:
Script is meant to be executed in the terminal:
- python3 PDFwatermarker.py watermark.pdf 1st_filename.pdf 2nd_filename.pdf ...
"""
import PyPDF2
import sys


def marker(watermark, pdf):
    watermark_obj = PyPDF2.PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(pdf)
    for page in range(pdf_reader.getNumPages()):
        pdf_page = pdf_reader.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)
    with open('watermarked.pdf', 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            if len(sys.argv) == 2:
                raise Exception('Only the watermark.pdf file was provided.')
            else:
                watermark = sys.argv[1]
                pdf = sys.argv[2]
                marker(watermark, pdf)

        else:
            print('Please select the .pdf file to be watermarked.')

    except Exception as error:
        print(f'Error detected: {error}')
