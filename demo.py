import requests
p={"value":"mani","valu2":"kotla"}
res=requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata", params=p)
print(res.url)


















#print(res.request.url)
#print(type(res.text))
#print(type(res))
#import json
#print(res.json(),type(res.json()))
#print(res.content,type(res.content))
#print(json.loads(res.content),type(json.loads(res.content))
#print(res.request.url)
#print(res.request.body)
