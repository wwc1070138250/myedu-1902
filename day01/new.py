# 这是一个注释
# model  模块
# main 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# return 返回
# 代码的层级关系 通过 缩进来表示
# class 类,类型
# str string 字符
# 合法标识符(变量名方法名) : 必须以字母或者_开头,剩下的可以是字母数字,下划线,大小写敏感, 不可用关键字做标识符
# ctrl+alt+L 格式化代码
# ctrl+K  commit 代码
# ctrl + shift + K  push 代码

bint = [2, 5, 9, '10', 8, 7]


# 声明一个int_demo 方法
def int_demo():
    # 声明aint变量 , 并赋值 1
    # aint = 1
    # 打印 aint 的值
    print(bint)
    # 打印 aint 的 类型; type(aint): 获取aint的类型
    print(type(bint))


# 声明一个 str_demo 方法
def str_demo():
    # 声明astr变量 , 并赋值 '1'
    astr = '1'
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))

    # 不写
    print('--------------')
    astr = 1
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))


# 演示字符串拼接 : +
def str_demo1():
    a = 'hello'
    b = ' world'
    return a + b


# 字符串拼接: %s
def str_demo2():
    a = 'hello '
    b = 250
    print(a + str(b))
    # print('a 是 : %s;b 是 : %s'%(a,b))


# 去掉两头空格
def str_demo3():
    astr = ' ysl '
    # astr 是变量 也叫 对象  ,对象 . 可以调用对象的方法
    print(astr)
    print(astr.strip())


# 12
# 声明一个add 方法 参数有两个 aint,bint
def add(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回 aint+bint
    return aint + bint


# 声明一个 float_demo 方法
def float_demo():
    # 声明afloat变量 , 并赋值 1.90
    afloat = 1.90
    # 打印 afloat 的值
    print(afloat)
    # 打印 afloat 的 类型; type(afloat): 获取afloat的类型
    print(type(afloat))


def str_demo5():
    a = 'hollo'
    b = 233
    print('%s %s' % (a, b))


def lnt_updata():
    bint[3] = 7
    print(bint)


# 讲列表排序的方法
def orderby_deom():
    pass


# 正序方法
def sort_demo():
    dlist.sort()
    print(dlist)
    pass


# 倒序方法
def reverse_demo():
    dlist.reverse()
    print(dlist)
    pass


if __name__ == '__main__':
    # str_demo3()
    # str_demo2()
    # print(str_demo1())
    # float_demo()
    # str_demo()
    # int_demo()
    # 提取变量  ctrl+alt+V
    # 调用add方法 传入1, 2,得到返回值 ,赋值给result变量
    # 指定参数传参
    # result = add(bint=2,aint=1)
    # print(result)
    # 默认参数传参
    # add(2,1)
    # lnt_updata()
    # str_demo5()
    # len() 获取变量长度
    # print(len(bint))
    # 删除方法bint.pop()
    # pop()方法两个作用 第一个取出最后一个值，第二个从列表中删除取出的值
    # print(bint.pop())
    # pop()带参数，参数被用作下标/索引，两个作用 第一个取出下标值代表元素，第二个从列表中删除取出的值
    # print(bint.pop(4))
    # print(bint)
    pass
