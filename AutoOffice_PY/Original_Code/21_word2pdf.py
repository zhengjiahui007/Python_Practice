# pip install pywin32
from win32com.client import gencache
from win32com.client import constants, gencache
def createPdf(wordPath, pdfPath):
    """
    word转pdf
    :param wordPath: word文件路径
    :param pdfPath:  生成pdf文件路径
    """
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)

if __name__ == "__main__":
    # 路径填写绝对路径
    createPdf('E:/class/办公自动化/代码/base_data/word_模板.docx','E:/class/办公自动化/代码/create_data/21_word2pdf.pdf')