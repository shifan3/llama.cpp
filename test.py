import requests
import json
from time import time
t1 = time()
prompt = '阅读《江城子 密州出猎》，完成下列各题． 江城子 密州出猎 苏轼 老夫聊发少年狂，左牵黄，右擎苍．锦帽貂裘，千骑卷平冈． 为报倾城随太守，亲射虎，看孙郎． 酒酣胸胆尚开张．鬓微霜，又何妨！持节云中，何日遣冯唐？ 会挽雕弓如满月，西北望，射天狼． （1）对牌名这首词理解有误的一项，是 _ _． A．“江城子”为词，“密州出猎”是这首词的题目． B．上阕首句中的“老夫”为作者自称． C．词的结句表达了'
partial_knowledge = ''
n_predict = 32
while True:
    resp = requests.post('http://localhost:8080/completion', data = json.dumps({
        'prompt' : f'{prompt}\n知识点:\n{partial_knowledge}',
        'subject' : '语文',
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
