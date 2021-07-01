#生成密码本，然后破解：
import os,time
from subprocess import Popen
def Jy():
    print('开始破解：')
    with open(path,'r',errors='ignore') as myfile:
        for myStr in myfile:
            myStr=myStr.replace('\n','')
            # 这里修改WinRAR.exe所在路径、压缩包路径和解压目录（C:\Program Files (x86)\WinRAR\WinRAR.exe、D:\test.rar、D:\test）
            jy=r'"C:\Program Files (x86)\WinRAR\WinRAR.exe" -ibck -y x -p%s "D:\test.rar" "D:\test"'%myStr
            if Popen(jy).wait()==0:
                print('密码正确!',myStr)
                break
            else:
                print('密码错误：',myStr)
    ent=time.time()
    print('用时%f分'%((ent-stm)/60))
stm=time.time()
path='password.txt'
if os.path.exists(r'D:\test')==False:#判断当前py文件所在目录下是否存在test文件夹，如果没有则建立
    os.mkdir(r'D:\test')
Jy()