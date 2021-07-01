import os,sys,time,ctypes,winreg,random,base64,requests
import tkinter as tk
from tkinter import ttk
from threading import Thread
from tkinter import filedialog,messagebox
class Scan:
    def __init__(self):
        self.fp=fp
        self.Root()
        if self.fp!=None:
            if os.path.isfile(self.fp):
                self.Getfiles(self.fp)
                self.root.mainloop()
            else:
                self.Getdir(self.fp)
                self.root.mainloop()
        else:
            self.root.mainloop()
    def Getfiles(self,filesname=''):
        if self.fp==None:
            filesname=filedialog.askopenfilenames()
            self.evar.set(';'.join(filesname))
            self.num=len(filesname)
        else:
            filesname=filesname.replace('\\','/')
            self.evar.set(filesname)
            self.num=1
        if filesname!='':
            self.win=tk.Toplevel()
            self.win.withdraw()
            self.win.iconbitmap(iicon)
            self.win.title('扫描结果')
            self.xgd=tk.Scrollbar(self.win,orient='horizontal')
            self.ygd=tk.Scrollbar(self.win)
            self.xgd.pack(side='bottom',fill='x')
            self.ygd.pack(side='right',fill='y')
            self.count=0
            self.flag=True
            self.starttime=time.time()
            if self.fp==None:
                for file in filesname:
                    self.Scanvirus(file)
            else:
                self.Scanvirus(filesname)
    def Getdir(self,dirname=''):
        if self.fp==None:
            dirname=filedialog.askdirectory()
        if dirname!='':
            self.evar.set(dirname)
            filesname=os.walk(dirname)
            self.win=tk.Toplevel()
            self.win.withdraw()
            self.win.iconbitmap(iicon)
            self.win.title('扫描结果')
            self.xgd=tk.Scrollbar(self.win,orient='horizontal')
            self.ygd=tk.Scrollbar(self.win)
            self.xgd.pack(side='bottom',fill='x')
            self.ygd.pack(side='right',fill='y')
            self.num=0
            self.count=0
            self.flag=True
            self.starttime=time.time()
            for rootdir,subdir,files in filesname:
                for file in files:
                    self.num+=1
                    self.Scanvirus(os.path.join(rootdir,file).replace('\\','/'))
    def Scanvirus(self,file):
        Thread(target=self.Threadtotalscan,args=[file],daemon=True).start()
    def Threadtotalscan(self,filepath):
        self.lvar.set('开始扫描...')
        timestamp='%s-ZG9udCBiZSBldmls-%.3f'%(''.join(random.choices('1234567890',k=11)),time.time())
        base64timestamp=base64.b64encode(timestamp.encode()).decode()
        headers={'accept-ianguage':'en-US,en;q=0.9,es;q=0.8','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36','x-tool':'vt-ui-main','x-vt-anti-abuse-header':'%s'%base64timestamp}
        urlhtml=requests.get('https://www.virustotal.com/ui/files/upload_url',headers=headers)
        uploadurl=urlhtml.json()['data']
        filename=filepath[filepath.rfind('/')+1:len(filepath)]
        fpfiles={'file':open(filepath,'rb')}
        fpdata={'filename':filename}
        fpheaders={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36'}
        self.lvar.set('正在上传...')
        fphtml=requests.post(uploadurl,files=fpfiles,data=fpdata,headers=fpheaders)
        fpid=fphtml.json()['data']['id']
        while True:
            self.lvar.set('正在扫描...，用时%s秒'%int(time.time()-self.starttime))
            resp=requests.get('https://www.virustotal.com/ui/analyses/%s'%fpid,headers=headers)
            fpstatus=resp.json()['data']['attributes']['status']
            if fpstatus=='completed':
                break
        ltmp1=[]
        vendornums=resp.json()['data']['attributes']['stats']['malicious']
        if vendornums==0:
            ltmp1.append('No security vendors flagged this file as malicious')
        else:
            ltmp1.append('%s security vendors flagged this file as malicious'%vendornums)
        results=resp.json()['data']['attributes']['results']
        if self.flag:
            ltmp2=[]
            for i in range(len(results.values())+1):
                ltmp2.append('%s'%i)
            self.tree=ttk.Treeview(self.win,columns=ltmp2,xscrollcommand=self.xgd.set,yscrollcommand=self.ygd.set)
            self.xgd.config(command=self.tree.xview)
            self.ygd.config(command=self.tree.yview)
            self.tree.pack(expand=1,fill='both')
            self.flag=False
        self.tree.heading('0',text='扫描结果')
        self.tree.column('0',anchor='center')
        n=1
        for vendornames,vendorresults in results.items():
            self.tree.heading('%s'%n,text=vendornames)
            self.tree.column('%s'%n,anchor='center')
            ltmp1.append(vendorresults['category'])
            n+=1
        self.tree.insert('',index='end',text=filepath,values=ltmp1)
        self.count+=1
        if self.count==self.num:
            self.lvar.set('扫描完成，用时%s秒'%int(time.time()-self.starttime))
            self.win.deiconify()
    def menuf(self,event,x,y):
        if event=='WM_RBUTTONDOWN':
            self.menu.tk_popup(x,y)
        if event=='WM_LBUTTONDOWN':
            self.root.deiconify()
        if event=='WM_MBUTTONDOWN':
            self.root.withdraw()
    def about(self):
        messagebox.showinfo('关于','作者：cnzb\nGithub：https://github.com/cnzbpy/simplepy\nGitee：https://gitee.com/cnzbpy/simplepy')
    def allquit(self):
        self.root.call('winico','taskbar','delete',self.icon)
        self.root.quit()
    def Root(self):
        self.root=tk.Tk()
        self.root.iconbitmap(iicon)
        self.root.title('Cvirus')
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'Cvirus')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'显示主页面',command=self.root.deiconify)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'隐藏主页面',command=self.root.withdraw)
        self.menu.add_command(label=u'退出',command=self.allquit)
        self.evar=tk.StringVar()
        self.lvar=tk.StringVar()
        panel=tk.Frame(self.root)
        panel1=tk.Frame(panel)
        tk.Label(panel1,text='目标路径:',font=('',16)).pack(side='left')
        tk.Entry(panel1,textvariable=self.evar,font=('',16)).pack(side='left',expand=1,fill='both')
        panel1.pack(fill='both')
        panel2=tk.Frame(panel)
        tk.Label(panel2,textvariable=self.lvar,font=('',16)).pack()
        panel2.pack()
        panel3=tk.Frame(panel)
        tk.Button(panel3,text='选择文件',font=('',16),command=self.Getfiles).pack(side='left')
        tk.Button(panel3,text='选择文件夹',font=('',16),command=self.Getdir).pack(side='left')
        panel3.pack()
        panel.pack(expand=1)
if getattr(sys,'frozen',False):
    odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'Cvirus.ico')
exepath=sys.executable
idirCviruspy=os.path.abspath(__file__)
try:
    fp=sys.argv[1]
except:
    fp=None
if ctypes.windll.shell32.IsUserAnAdmin():
    menu_name='用Cvirus扫描病毒'
    if 'Cvirus.exe' in exepath:
            command=r'"%s"'%exepath
    else:
        command=r'"%s" "%s"'%(exepath,idirCviruspy)
    key1=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'*\\shell')
    winreg.SetValue(key1,menu_name,winreg.REG_SZ,menu_name)
    sub_key1=winreg.OpenKey(key1,menu_name)
    winreg.SetValue(sub_key1,'command',winreg.REG_SZ,command+' "%v"')
    winreg.CloseKey(sub_key1)
    winreg.CloseKey(key1)
    key2=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Directory\\shell')
    winreg.SetValue(key2,menu_name,winreg.REG_SZ,menu_name)
    sub_key2=winreg.OpenKey(key2,menu_name)
    winreg.SetValue(sub_key2,'command',winreg.REG_SZ,command+' "%v"')
    winreg.CloseKey(sub_key2)
    winreg.CloseKey(key2)
    key3=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Directory\\Background\\shell')
    winreg.SetValue(key3,menu_name,winreg.REG_SZ,menu_name)
    sub_key3=winreg.OpenKey(key3,menu_name)
    winreg.SetValue(sub_key3,'command',winreg.REG_SZ,command+' "%v"')
    winreg.CloseKey(sub_key3)
    winreg.CloseKey(key3)
    key4=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Drive\\shell')
    winreg.SetValue(key4,menu_name,winreg.REG_SZ,menu_name)
    sub_key4=winreg.OpenKey(key4,menu_name)
    winreg.SetValue(sub_key4,'command',winreg.REG_SZ,command+' "%v"')
    winreg.CloseKey(sub_key4)
    winreg.CloseKey(key4)
else:
    tmp=ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,__file__,None,0)
    if tmp!=5:
        Scan()