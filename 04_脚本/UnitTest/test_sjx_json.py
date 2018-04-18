import unittest
from CodeHost.sxj02 import SJX
from ReadData.readJSON import ReadJSON

sjx=SJX()
readjson=ReadJSON()

class TestJSON(unittest.TestCase):
    def test001(self):
        for i in range(len(readjson.readJson())):
            result=sjx.sjxTest(readjson.readJson()[i]['b2'],
                        readjson.readJson()[i]['b1'],
                        readjson.readJson()[i]['b3'])
            self.assertEqual(result,readjson.readJson()[i]['except'])
