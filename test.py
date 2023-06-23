import requests
import json
from time import time
t1 = time()
prompt = '在电能输送的过程中，如果输送的电功率一定，将输电电压升到原来的10倍，则输电线上损失的功率将变为原来的 __ 倍，由此可见，若想有效的减小电能在输电线路上的损失应采用 __ （选填“高压”或“低压”）输电．'
partial_knowledge = ''
n_predict = 32
while True:
    resp = requests.post('http://localhost:8080/completion', data = json.dumps({
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
