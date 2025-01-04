from zipfile import ZipFile
import os
def zip_in():
    with ZipFile('./create_data/39_zip_in.zip','w') as zip:
        zip.write('22_读取pdf.py')
        zip.write('23_合并pdf.py')
        zip.write('24_拆分pdf.py')
def zip_out():
    with ZipFile('./create_data/39_zip_in.zip','r') as zip:
        print(zip.namelist())
        # zip.extract('22_读取pdf.py','./create_data')
        zip.extractall('./create_data')

def compree_zip(zip_name,dir_name):
    with ZipFile(zip_name,'w') as zip:
        if os.path.isfile(dir_name):    # 判断是否是文件
            zip.write(dir_name)
        else:
            for root, dirs, files in os.walk(dir_name):
                # root 所指的当前正在遍历的这个文件夹的本身地址
                # dirs list ,是该文件夹中所有的目录的名字(不包含子目录)
                # files list ,是该文件夹中所有的文件名字
                for f in files:
                    if f != zip_name:
                        path = os.path.join(root,f)
                        zip.write(path)
                        print(f'正在压缩:{f}')

def add_file(zip_name,dir_name):
    if os.path.isfile(dir_name):    # 判断是否是文件
        with ZipFile(zip_name,'a') as zip:
            zip.write(dir_name)
    else:
        with ZipFile(zip_name,'a') as zip:
            for root, dirs, files in os.walk(dir_name):
                # root 所指的当前正在遍历的这个文件夹的本身地址
                # dirs list ,是该文件夹中所有的目录的名字(不包含子目录)
                # files list ,是该文件夹中所有的文件名字
                for f in files:
                    if f != zip_name:
                        path = os.path.join(root,f)
                        zip.write(path)
                        print(f'正在压缩:{f}')

import tarfile
def tar_in():
    with  tarfile.open('./create_data/39_tar_in.tar','w') as tar:
        tar.add('22_读取pdf.py',arcname='22_pdf.py')
        tar.add('23_合并pdf.py',arcname='23_pdf.py')
def tar_out():
    with  tarfile.open('./create_data/39_tar_in.tar','r') as tar:
        print(tar.getmembers())

if __name__ == "__main__":
    # zip_in()
    # zip_out()
    # compree_zip('./create_data/生成压缩文件/39_zip_all.zip','./base_data')
    # tar_in()
    tar_out()