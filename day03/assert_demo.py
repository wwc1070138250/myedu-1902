# try except 用来捕捉异常
def try_demo():
    a = "123456"
    # try 用于异常处理；如果出现异常则执行except内的代码
    try:
        # 判断a 是否包含 5
        assert '7' not in a
    # except 报错执行
    except:
        print('a里面没有7')
    #  不管是否有异常，finally里面的代码都会被执行
    finally:
        print('最后------')
if __name__ == '__main__':
    try_demo()