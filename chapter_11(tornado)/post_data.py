# coding:utf-8
import requests
import json

data = json.dumps({"name":"yuki"})
# 用来发送数据检测
res = requests.post("http://127.0.0.1:8080/index",json=data)
print(res.text)