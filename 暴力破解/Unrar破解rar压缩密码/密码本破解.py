#生成密码本，然后破解：
import time
from unrar import rarfile
stm=time.time()
file=rarfile.RarFile(r'D:\test.rar','r')#读取rar文件
path='password.txt'
with open(path,'r',errors='ignore') as myfile:
    print('开始破解：')
    for myStr in myfile:
        myStr=myStr.replace('\n','')
        try:
            file.extractall(path=r'D:\test',pwd=myStr)#解压到test文件夹内，修改path可自定义解压路径
        except:
            print('密码错误：',myStr)
        else:
            print('密码正确：',myStr)
            break
ent=time.time()
print('用时%f分'%((ent-stm)/60))