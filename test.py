import requests
import json
from time import time
t1 = time()
prompt = '（2014秋•益阳校级期末）现有常温时浓度相同的五种电解质溶液：①CH3COOH ②Na2CO3 ③HNO3④CH3COONa ⑤NaOH （1）五种溶质中是弱电解质的是 _ _（填编号）； （2）④溶液中离子与分子共 _ _种（包括水分子）； （3）这五种溶液的pH由小到大的顺序是 _ _（填编号）； （4）将CH3COONa溶液稀释100倍时，其pH变化如图中 _ _曲线（填字母）． （5）上'
partial_knowledge = ''
n_predict = 32
while True:
    resp = requests.post('http://localhost:8080/completion', data = json.dumps({
        'prompt' : f'{prompt}\n知识点:\n{partial_knowledge}',
        'subject' : '化学',
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
        n_predict = 32 - len(partial_knowledge)
    else:
        knowledge = partial_knowledge + content
        break

print(knowledge)
print(time() - t1)
