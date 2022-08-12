import json

def get_data():
    with open('C:\\Users\\长颈鹿蓝调\\Desktop\\学习\\黑马_软件测试\\代码\\Python学习代码\\2022.8.11_考试\\test_05\\data\\data.json', encoding = 'utf-8') as f:
        data = json.load(f)
    
    new_data = []
    for d in data:
        for k in list(d.keys()):
            if k not in ('name', 'school'):
                d.pop(k)
        new_data.append(tuple(d.values()))
    return new_data

print(get_data())