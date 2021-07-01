#8位数字字母密码本：
import time
string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#这里加上你想要的字符
stm=time.time()
with open('password.txt','a') as dic:#在当前目录生成password.txt文件
    for a in range(len(string)):
        for b in range(len(string)):
            for c in range(len(string)):
                for d in range(len(string)):
                    for e in range(len(string)):
                        for f in range(len(string)):
                            for g in range(len(string)):
                                for h in range(len(string)):
                                    pwd=string[a]+string[b]+string[c]+string[d]+string[e]+string[f]+string[g]+string[h]#生成8位数字字母密码
                                    dic.write(pwd)
                                    dic.write('\n')
                                    print('密码正在写入文件：',pwd)
ent=time.time()
print('成功生成密码本！用时%f分'%((ent-stm)/60))