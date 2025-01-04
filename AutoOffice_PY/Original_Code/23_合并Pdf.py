def merger_pdf(path1,path2):
    from PyPDF2 import PdfFileReader,PdfFileWriter
    write = PdfFileWriter()
    for path in [path1,path2]:
        tmp_pdf = PdfFileReader(open(path,'rb'))
        for page in tmp_pdf.pages:
            write.addPage(page)
    
    with open('./create_data/23_合并pdf.pdf','wb') as out:
        write.write(out)


if __name__ == "__main__":
    merger_pdf('./create_data/21_word2pdf.pdf','./create_data/21_word2pdf.pdf')