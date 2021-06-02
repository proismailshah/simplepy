#不生成密码本破解：
#4位数字字母密码：
import os,time
from subprocess import Popen
def Jy():
    print('开始破解：')
    for a in range(len(string)):
        for b in range(len(string)):
            for c in range(len(string)):
                for d in range(len(string)):
                    myStr=string[a]+string[b]+string[c]+string[d]#生成压缩包密码
                    #这里修改WinRAR.exe所在路径、压缩包路径和解压目录（C:\Program Files (x86)\WinRAR\WinRAR.exe、D:\test.rar、D:\test）
                    jy=r'"C:\Program Files (x86)\WinRAR\WinRAR.exe" -ibck -y x -p%s "D:\test.rar" "D:\test"'%myStr
                    if Popen(jy).wait()==0:
                        print('密码正确!',myStr)
                        ent=time.time()
                        print('破解成功！用时%f分'%((ent-stm)/60))
                        return
                    else:
                        print('密码错误：',myStr)
    ent=time.time()
    print('破解失败，用时%f分'%((ent-stm)/60))
stm=time.time()
string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#这里加上你想要的字符
if os.path.exists(r'D:\test')==False:#判断当前py文件所在目录下是否存在test文件夹，如果没有则建立
    os.mkdir(r'D:\test')
Jy()