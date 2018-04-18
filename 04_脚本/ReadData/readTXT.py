
class TestTXT():
    def readTxt(self):
        arr=[]
        with open("../DataPool/sjxTXT.txt",'r',encoding="utf-8") as f:
            for line in f:
                arr.append(line.strip().split(','))
            return arr

'''
strip:去除字符串前后(空格、回车、TAB)
split:分割符(,) 返回为列表
'''


# TestTXT().readTxt()