import requests
import json
from time import time

prompts = [
    '数学:一个自然数（0除外）， _ _的个数是有限的， _ _的个数是无限的．',
    '物理:如图1是某同学在测物体长度和液体体积时出现的情形，则物体的长度为 _ _ cm，为了使测量结果更准确，应采用 _ _方法． 图2中， _ _同学的读数方法正确，液体的体积为 _ _ cm3'
    '政治:下列关于“责任”的观点，正确的有（ ）  a. 只有成年人要负责任，未成年人无责任可言 b. 责任是强加在我们身上的，并不是我们成长的需要 c. 当我们排队买电影票时，这也是我们在履行责任的表现 d. 每个人都扮演着角色，每个人的责任也都是一样的',
    '生物:灰兔和白兔杂交，F1全是灰兔，F1雌雄个体相互交配，F2中有灰兔、黑兔和白兔，比例为9：3：4，则下列不正确的是 [ ] A．家兔的毛色受一对等位基因控制 B．F2灰兔中能稳定遗传的个体占1/16 C',
    '历史:在1922年3月的“十一大”上，列宁把对新经济政策的强调重点放到了从政治上把握社会主义与资本主义的关系问题方面，认为新经济政策“是两个不共戴天的敌对阶级（资产阶级与无产阶级）的又一斗争形式”。其实质含 a. 准备放弃新经济政策 b. 新经济政策要坚持社会主义方向 c. 重启战时共产主义政策 d. 以阶级斗争作为经济抗争的手段',
    '地理【自然灾害与防治】(10分)下图中的甲为某滑坡区域坡度面积频率分布图，乙为某滑坡区域土质分布图。读图回答有关问题。 (1)据图说明该区域什么坡度、土质发生滑坡可能性最大？(4分) (2)该区域滑坡多发',
    '化学:下列说法正确的是（ ）  a. 液氨汽化时要吸收大量的热，可用作制冷剂 b. 二氧化硫可广泛用于食品的漂白 c. 碘是人体必需微量元素，所以要多吃富含高碘酸的食物 d. 氯化铝是一种电解质，可用于电解法制铝',
    '语文:细菌和病毒 ①细菌和病毒都是可以致病的微生物，但它们的特征区别很大．细菌虽然小，要在光学显微镜下才能看得见，但它除了拥有生命的基本单位核酸之外，还有一大套赖以生存的配套设施．包括作为居住“公馆”的细胞',
    '英语:There _____ a ticket, a lamp and some keys on the table.  a. are b. is c. have d. has'
]
partial_knowledge = ''
n_predict = 32
t_total = 0
for prompt in prompts:
    print(prompt)
    t1 = time()
    p = prompt.index(":")
    subject = prompt[:p]
    prompt = prompt[p+1:]
    resp = requests.post('http://localhost:8081/completion', data = json.dumps({
        'prompt' : f'{prompt}\n知识点:\n{partial_knowledge}',
        'subject' : subject,
        'n_predict' : n_predict,
        'stop' : ['$'],
    }, ensure_ascii=False).encode('utf-8'))
    resp = json.loads(resp.text)
    content:str = resp['content']
    print(content)
    print(time() - t1)
    t_total += time() - t1
print(f'total {t_total}, avg {t_total/len(prompts)}')
