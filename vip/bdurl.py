import urllib
import httplib
conn=httplib.HTTPConnection('dwz.cn')
params = urllib.urlencode({'url':'http://www.baidu.com/'})
conn.request('POST', '/create.php', headers={"Content-Type":"application/x-www-form-urlencoded"}, body=params)
result = conn.getresponse()
resultContent = result.read()
print(resultContent)