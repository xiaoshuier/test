import requests
import time
r=requests.get("https://8cb4eb4a046b49b29a9e1cef1f77ab20.api.mockbin.io/"+time.time())
print(r.text)
