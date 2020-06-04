import chardet
# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        content = f.read()
        return chardet.detect(content)['encoding']
import os
for root,dir_list,file_list in os.walk('.'):  
    for file_name in file_list:
        path = os.path.join(root, file_name)
        print(path)
        if os.path.isfile(path):
            # print(path)
            if path.endswith('h') or path.endswith('cpp'):
                if(get_encoding(path)!='utf-8'):
                    with open(path,'r',encoding='gbk') as f:
                        content = f.read()
                    with open(path,'w',encoding='utf-8') as f:
                        f.write(content)
