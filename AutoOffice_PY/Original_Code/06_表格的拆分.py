import xlrd
from xlutils.copy import copy

def get_data():
    wb = xlrd.open_workbook('./base_data/data01.xlsx')
    sh = wb.sheet_by_index(0)
    '''
    {
      a: [{},{},{}],
      b:[{},{},{}],
      c:[{},{},{}],
    }

    '''
    all_data = {}
    for r in range(sh.nrows):
        d = {'type':sh.cell_value(r,1),'name':sh.cell_value(r,2),'count':sh.cell_value(r,3),'price':sh.cell_value(r,4)}
        key = sh.cell_value(r,0)
        if all_data.get(key):
            all_data[key].append(d)
        else:
            all_data[key] = [d]
    return all_data
def save(data):
    wb = xlrd.open_workbook('./base_data/data01.xlsx')
    wb2 = copy(wb)
    for key in data.keys():
        temp_sheet = wb2.add_sheet(key)
        for i, d in enumerate(data.get(key)):
            temp_sheet.write(i,0,d.get('type'))
            temp_sheet.write(i,1,d.get('name'))
            temp_sheet.write(i,2,d.get('count'))
            temp_sheet.write(i,3,d.get('price'))
    wb2.save('./create_data/06_表格的拆分.xlsx')

if __name__ == "__main__":
    all_data = get_data()
    # save(all_data)
    print(all_data)