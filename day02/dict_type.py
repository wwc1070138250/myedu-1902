import json

# 声明一个 dict 全量 (字典)

adict = {"name":"ysl","pwd":"123456"}

# 这是一个字符串，不过他是json格式，也是字典的格式
adictStr = '{"name":"ysl","pwd":"123456"}'

if __name__ == '__main__':
    # adict.pop('name')
    # print(adict['name'])
    # print(adict)
    print(type(adictStr))
    dict_str = json.loads(adictStr)
    print(type(dict_str))
