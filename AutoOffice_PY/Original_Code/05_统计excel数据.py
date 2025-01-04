import xlrd
from xlutils.copy import copy

def read_data():
    wb = xlrd.open_workbook('./base_data/data01.xlsx')
    sh = wb.sheet_by_index(0)
    fen_type = {}       # {a:110,b:300}
    count_price = []    # [1,2,3,4,5,6]

    for r in range(sh.nrows):
        count = sh.cell_value(r,3) * sh.cell_value(r,4)
        count_price.append(count)
        key = sh.cell_value(r,0)
        if fen_type.get(key):
            fen_type[key] += count
        else:
            fen_type[key] = count
    return fen_type,count_price # 各分类的总价值, 每个单品的总价值

def save(fen,count):
    wb = xlrd.open_workbook('./base_data/data01.xlsx')
    sh_t = wb.sheet_by_index(0)
    wb2 = copy(wb)
    sh = wb2.get_sheet(0)
    for r in range(sh_t.nrows):
        sh.write(r,sh_t.ncols,count[r])
    
    sh2 = wb2.add_sheet('汇总的数据')
    for i,key in enumerate(fen.keys()):
        sh2.write(i,0,key)
        sh2.write(i,1,fen.get(key))
    wb2.save('./create_data/05_汇总数据.xlsx')

if __name__ == "__main__":
    f,c = read_data()
    save(f,c)