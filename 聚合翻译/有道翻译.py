import requests
string=input('输入字符串：')
data={'doctype':'json','i':string}
resp=requests.post('http://fanyi.youdao.com/translate',data=data)
result=resp.json()['translateResult'][0][0]['tgt']
print(result)