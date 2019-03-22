import json

# 声明一个 dict 全量 (字典)

adict = {"name": "ysl", "pwd": "123456"}

# 这是一个字符串，不过他是json格式，也是字典的格式
adictStr = '{"name":"ysl","pwd":"123456","1":"数字"}'

if __name__ == '__main__':
    # adict.pop('name')
    # print(adict['name'])
    # print(adict)
    # print(type(adictStr))
    # dict_str = json.loads(adictStr)
    # str - -> dict
    print(type(adictStr))
    loads = json.loads(adictStr)
    print(type(loads))
    # json_dumps = json.dumps(loads)
    # print(json_dumps)
    # 字符转字符串含有中文时：ensure_ascii=False 指定编码格式不为ASCII吗
    # dumps = json.dumps(loads, ensure_ascii=False)
    # print(dumps)
    # dict - -> str
    dumps = json.dumps(adict)
    print(type(dumps))
