import unittest
from CodeHost.sxj02 import SJX
from ReadData.readTXT import TestTXT

sjx=SJX()
readTxt=TestTXT()

class TestTXT(unittest.TestCase):
    def test001(self):
        for i in range(len(readTxt.readTxt())):
            result=sjx.sjxTest(int(readTxt.readTxt()[i][0]),
                        int(readTxt.readTxt()[i][1]),
                        int(readTxt.readTxt()[i][2]))
            self.assertEqual(result,readTxt.readTxt()[i][3])

'''
range:必须为int 
len:获取数组的长度
for循环：参数化数据为多行
'''