import unittest
from CodeHost.sxj02 import SJX
from ReadData.readCSV import ReadCSV
sjx=SJX()
readCsv=ReadCSV()
class TestCSV(unittest.TestCase):
    def test001(self):
        for i in range(len(readCsv.readCSV())):
                result=sjx.sjxTest(int(readCsv.readCSV()[i][0]),
                             int(readCsv.readCSV()[i][1]),
                             int(readCsv.readCSV()[i][2]))
                self.assertEqual(result,readCsv.readCSV()[i][3])

