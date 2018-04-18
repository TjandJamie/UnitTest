import unittest
from Code.sjx01 import SJX
from Read.sjxReadJson import ReadJSON

sjx = SJX()
readJson = ReadJSON()

class TestJSON(unittest.TestCase):

    def test001(self):
        for i in range(len(readJson.readJson())):
            result = sjx.sjx(int(readJson.readJson()[0]['b1']),
                             int(readJson.readJson()[0]['b2']),
                             int(readJson.readJson()[0]['b3']))
            self.assertEqual(result, readJson.readJson()[0]['except'])