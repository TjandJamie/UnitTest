import unittest
from Code.sjx01 import SJX
from Read.sjxReadCsv import ReadCSV

sjx = SJX()
readCsv = ReadCSV()

class TestCSV(unittest.TestCase):
    def test001(self):
        for i in range(len(readCsv.readCsv())):
            result = sjx.sjx(int(readCsv.readCsv()[i][0]),
                    int(readCsv.readCsv()[i][1]),
                    int(readCsv.readCsv()[i][2]))
            self.assertEqual(result, readCsv.readCsv()[i][3])
