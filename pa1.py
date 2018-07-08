import requests
# http://tianqi.moji.com/
r = requests.get('http://tianqi.moji.com/')
print r.content
re = r.content
de = '"description" content'
pa = 'meta name="keywords" content='
a = re.find(de) #171
b = re.find(pa) #444 
print re[a+len(de)+1:b]