# # try 语句的使用
# try:
#     print('程序运行')
#     raise KeyError  # 手动抛出 KeyErro 异常
# except KeyError:
#     print('key erro 错误...')
# else:
#     print('程序未产生异常时则运行当前代码...')
# finally:
#     print('程序无论是否出现异常都执行此语句')

# 在函数中使用try语句
def func_try_except():
    try:
        print('程序运行')
        raise KeyError  # 给出 KeyErro 错误
        return 1
    except KeyError:
        print('key erro 错误...')
        return 2
    else:
        print('程序未产生异常时则运行当前代码...')
        return 3
    finally:
        print('程序无论是否出现异常都执行此语句')
        # 如果finally中出现return则优先返回finally中的返回值
        # return 4

# res = func_try_except()
# print(res)

# try:
#     print('程序运行')
#     # 如果抛出的异常不是捕获语句中的指定异常则无法正常捕获
#     raise FileNotFoundError  # 给出 KeyErro 错误
# except KeyError:
#     print('key erro 错误...')
# else:
#     print('程序未产生异常时则运行当前代码...')
# finally:
#     print('程序无论是否出现异常都执行此语句')


# 上下文管理协议
class Sample:
    def __enter__(self):
        try:
            self.file_obj = open('LearniuH.txt')
        except:
            self.file_obj = None
        print('我被执行了:__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj == None:
            print('当前文件不存在')
        else:
            self.file_obj.close()
        print('我被执行了:__exit__')

    def run(self):
        print('程序启动...')

with Sample() as sample:
    sample.run()
    pass