import requests
import json
from time import time
resp = requests.post('http://localhost:8080/completion', data = json.dumps({
    'prompt' : '生物:根生长具有向 _ _生长、向 _ _生长和向 _ _生长的特性．\n知识点:',
    'n_predict' : 32,
    'stop' : ['END']
}, ensure_ascii=False).encode('utf-8'))
t1 = time()
print(json.dumps(json.loads(resp.text), indent = 4, ensure_ascii=False))

print(time.time() - t1)
