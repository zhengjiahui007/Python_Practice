from docx import Document
import os
infos = [
    ['00001',2030,12,12,12,0,'闯红灯',300],
    ['00002',2031,12,12,12,0,'违反禁令',300],
    ['00003',2032,12,12,12,0,'违章停车',300],
]

for info in infos:
    doc1 = Document('./base_data/word_模板.docx')
    for p in doc1.paragraphs:
        for run in p.runs:
            run.text = run.text.replace('{0}',info[0])
            run.text = run.text.replace('{1}',str(info[1]))
            run.text = run.text.replace('{2}',str(info[2]))
            run.text = run.text.replace('{3}',str(info[3]))
            run.text = run.text.replace('{4}',str(info[4]))
            run.text = run.text.replace('{5}',str(info[5]))
            run.text = run.text.replace('{6}',info[6])
            run.text = run.text.replace('{7}',str(info[7]))
        # 注意：直接修改段落内容，会丢失样式
        # p.text = p.text.replace('{0}',info[0])
        # p.text = p.text.replace('{1}',str(info[1]))
        # p.text = p.text.replace('{2}',str(info[2]))
        # p.text = p.text.replace('{3}',str(info[3]))
        # p.text = p.text.replace('{4}',str(info[4]))
        # p.text = p.text.replace('{5}',str(info[5]))
        # p.text = p.text.replace('{6}',info[6])
        # p.text = p.text.replace('{7}',str(info[7]))
    if not os.path.exists('./create_data/生成word'):
        os.makedirs('./create_data/生成word')
    doc1.save(f'./create_data/生成word/车辆{info[0]}.docx')

'''

str  = 'abc'
temp = str.raplace('a','A') Abc
str = str.raplace('a','A')
'''