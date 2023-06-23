import requests
import json
from time import time
t1 = time()
prompt = '一个自然数（0除外）， _ _的个数是有限的， _ _的个数是无限的．'
partial_knowledge = ''
n_predict = 32
while True:
    resp = requests.post('http://localhost:8080/completion', data = json.dumps({
        'prompt' : f'{prompt}\n知识点:\n{partial_knowledge}',
        'subject' : '数学',
        'n_predict' : n_predict,
        'stop' : ['END'],
    }, ensure_ascii=False).encode('utf-8'))
    resp = json.loads(resp.text)
    content:str = resp['content']
    print(json.dumps(content, indent = 4, ensure_ascii=False))
    if content.endswith('END'):
        knowledge = partial_knowledge + content[:-3]
        break
    if content.endswith("CONT"):
        partial_knowledge += content[:-4]
        if partial_knowledge.count('#') == 1:
            knowledge = partial_knowledge
            break
        partial_knowledge += '#'
        n_predict = 32 - len(partial_knowledge)
    else:
        knowledge = partial_knowledge + content
        break

print(knowledge)
print(time() - t1)
