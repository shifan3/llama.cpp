import requests
import json
resp = requests.post('http://localhost:8080/completion', data = {
    'prompt' : '生物:根生长具有向 _ _生长、向 _ _生长和向 _ _生长的特性．\n知识点:',
    'n_predict' : 32,
    'stop' : ['END']
})
print(resp.text)
print(json.dumps(json.loads(resp.text), indent = 4, ensure_ascii=False))

