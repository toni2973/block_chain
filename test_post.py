import urllib
import sys
import http.cookiejar
from bigchaindb_driver.crypto import generate_keypair
import json
alice = generate_keypair()

# cjhdr = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(cjhdr)

# owner=args['owner'], name=args['name'], util=args['util'], place=args['place'],
#                                        manufacturer=args['manufacturer'], detail=args['detail'], amount=args['args']),
url = "http://localhost:5020/task/produce"
# postdata = urllib.parse.urlencode(
#     )
# print(alice.verifying_key)
# print(alice.signing_key)
postdata={'owner': alice, 'name': 'elle', 'size': 1, 'util': 'ben', 'place': 'shenzhen', 'manufacturer': 'basha','detail':'','amount':1 }
# print(postdata)
postdata=json.dumps(postdata)
# print(json.dumps(postdata))
# postdata = postdata.encode('utf-8')
data=bytes(postdata,'utf8')
request=urllib.request.Request(url)
result=urllib.request.urlopen(request,data).read()
# res = urllib.request.urlopen(url, postdata)
# print(res.status, res.reason)

#
# import http.client,urllib.parse
# import json
#
# str = json.dumps({'userid':'381fccbd776c4deb'})
# print(str)
#
# #pararms = urllib.parse.urlencode({'userid':'381fccbd776c4deb'}).encode(encoding='UTF8')
# headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}
# url = "localhost"
# conn = http.client.HTTPConnection(url,5020)
# conn.request('POST', '/task/produce', str, headers)
# response = conn.getresponse()
# print(response.status, response.reason)
# data = response.read().decode('utf-8')
# print(data)
# conn.close()