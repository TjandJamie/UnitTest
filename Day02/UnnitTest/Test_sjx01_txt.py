import unittest
# import os,sys
# sys.path.append(os.getcwd())
from Code.sjx01 import SJX
from Read.sjxReadTxt import ReadText

sjx = SJX()
readText = ReadText()

class TestTXT(unittest.TestCase):

    def test001(self):
        for i in range(len(readText.readText())):
            result = sjx.sjx(readText.readText()[0][0],
                             readText.readText()[0][1],
                             readText.readText()[0][2])
            self.assertEqual(result, readText.readText()[0][3])
