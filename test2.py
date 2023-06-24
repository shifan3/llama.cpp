import requests
import json
from time import time
t1 = time()
prompt = '如图1是某同学在测物体长度和液体体积时出现的情形，则物体的长度为 _ _ cm，为了使测量结果更准确，应采用 _ _方法． 图2中， _ _同学的读数方法正确，液体的体积为 _ _ cm3'
partial_knowledge = ''
n_predict = 32
while True:
    resp = requests.post('http://localhost:8081/completion', data = json.dumps({
        'prompt' : f'{prompt}\n知识点:\n{partial_knowledge}',
        'subject' : '物理',
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
