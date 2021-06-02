import requests
string=input('输入一段要翻译的文字：')
html=requests.post('https://fanyi.qq.com/api/reauth1232f')
qtv=html.json()['qtv']
qtk=html.json()['qtk']
landata={'query':string}
lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
lan=lanhtml.json()['lan']
if lan=='zh':
    to='en'
else:
    to='zh'
data={'source':'auto','target':to,'sourceText':string,'qtv':'%s'%qtv,'qtk':'%s'%qtk}
headers={'Referer':'https://fanyi.qq.com/'}
resp=requests.post('https://fanyi.qq.com/api/translate',data=data,headers=headers)
result=resp.json()['translate']['records'][0]['targetText']
print(result)