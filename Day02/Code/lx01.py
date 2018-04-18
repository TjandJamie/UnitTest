# 定义一个类Calc
class Calc(object):

# 定义函数add
    def add(self, a, b):
        return a+b

# 定义函数sub
    def sub(self, a, b):
        return a-b

if __name__ == '__main__':
    c = Calc()
    print(c.add(10, 10))
    print(c.sub(11, 10))
