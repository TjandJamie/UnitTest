# 建类Calc
class Calc():
    # add 返回 a+b
    def add(self,a,b):
        return a+b

    # sub 返回 a-b
    def sub(self,a,b):
        return a-b



if __name__ == '__main__':

    cal=Calc()
    print(cal.add(10,10))
    print(Calc().sub(20,5))