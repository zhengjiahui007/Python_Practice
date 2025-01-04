def chai_pdf(path):
    from PyPDF2 import PdfFileWriter,PdfFileReader

    pdf = PdfFileReader(open(path,'rb'))
    for i,page in enumerate(pdf.pages):
        write = PdfFileWriter()
        write.addPage(page)
        with open(f'./create_data/24_拆分pdf_{i+1}.pdf','wb') as out:
            write.write(out)

if __name__ == "__main__":
    chai_pdf('./create_data/23_合并pdf.pdf')
