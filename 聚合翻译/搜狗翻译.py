import hashlib,requests
string=input('输入字符串：')
fsheaders={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,image/apng,*/*;''q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
html=requests.get('https://fanyi.sogou.com',headers=fsheaders)
FUV=html.cookies.get_dict()['FUV']
SNUID=html.cookies.get_dict()['SNUID']
landata={'query':string}
lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
lan=lanhtml.json()['lan']
if lan=='zh':
    to='en'
else:
    to='zh-CHS'
sign=lan+to+string+'109984457'
m=hashlib.md5()
m.update(sign.encode('utf-8'))
data={'from':lan,'s':m.hexdigest(),'text':string,'to':to}
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,image/apng,*/*;''q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8','Cookie':'FUV=%s;SNUID=%s'%(FUV,SNUID)}
resp=requests.post('https://fanyi.sogou.com/api/transpc/text/result',data=data,headers=headers)
result=resp.json()['data']['translate']['dit']
print(result)