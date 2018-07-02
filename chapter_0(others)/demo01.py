import requests
import os
import hashlib
# requests.post("http://localhost:8080/ServletLeftCircle2.5/Hello",data={"name":"wang"})
print(hashlib.sha1(os.urandom(20)).hexdigest())
