import requests
import json
from time import time
t1 = time()
resp = requests.post('http://localhost:8080/completion', data = json.dumps({
    'prompt' : '阅读《江城子 密州出猎》，完成下列各题． 江城子 密州出猎 苏轼 老夫聊发少年狂，左牵黄，右擎苍．锦帽貂裘，千骑卷平冈． 为报倾城随太守，亲射虎，看孙郎． 酒酣胸胆尚开张．鬓微霜，又何妨！持节云中，何日遣冯唐？ 会挽雕弓如满月，西北望，射天狼． （1）对牌名这首词理解有误的一项，是 _ _． A．“江城子”为词，“密州出猎”是这首词的题目． B．上阕首句中的“老夫”为作者自称． C．词的结句表达了\n知识点:\n诗歌思想情感',
    'subject' : '语文',
    'n_predict' : 32,
    'stop' : ['END'],
    'top_k' : 3,
}, ensure_ascii=False).encode('utf-8'))

print(json.dumps(json.loads(resp.text), indent = 4, ensure_ascii=False))

print(time() - t1)
