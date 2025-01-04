from zipfile import ZipFile
import os
def passwd(path,pwd):
    type_ = os.path.splitext(path)[-1][1:]
    if type_ == 'zip':
        with ZipFile(path,'r') as zip:
           
            print(f'正在尝试密码: {pwd}')
            try:
                zip.extractall('./create_data/生成压缩文件',pwd=str(pwd).encode('utf-8'))
                print(f'解压成功,密码是:{pwd}')
                return True
            except Exception as e:
                pass

def create_pwd(length):
    import itertools as its
    words='1234567890asd'
    for i in range(1,length):
        base = its.product(words,repeat=i)
        for i in base:
            yield ''.join(i)



if __name__ == "__main__":
    # passwd('./base_data/aa.zip')
    for p in create_pwd(5):
        flag = passwd('./base_data/aa.zip',p)
        if flag:
            break