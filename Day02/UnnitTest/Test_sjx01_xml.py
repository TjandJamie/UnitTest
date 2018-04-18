import unittest
from Code.sjx01 import SJX
from Read.sjxReadXml import ReadXML

sjx = SJX()
readXml = ReadXML()


class TestXML(unittest.TestCase):

    def test001(self):
        for i in range(8):
            result = sjx.sjx(int(readXml.readXML('db', i, 'b1')),
                    int(readXml.readXML('db', i, 'b2')),
                    int(readXml.readXML('db', i, 'b3')))
            self.assertEqual(result, readXml.readXML('db', i, 'except'))
