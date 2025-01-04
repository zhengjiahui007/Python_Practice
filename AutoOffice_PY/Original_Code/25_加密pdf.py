from os import write


def jia_mi(path):
    from PyPDF2 import PdfFileWriter,PdfFileReader
    pdf = PdfFileReader(open(path,'rb'))
    #pdf.decrypt('123') # 当读取pdf有密码时，填写相应的密码
    write = PdfFileWriter()
    write.encrypt('123') # 设置密码
    for page in pdf.pages:
        write.addPage(page)
    
    with open('./create_data/25_加密pdf.pdf','wb') as target:
        write.write(target)

if __name__ == "__main__":
    jia_mi('./create_data/21_word2pdf.pdf')