import unittest
from CodeHost.sxj02 import SJX
from ReadData.readXML import ReadXML
sjx=SJX()
readXML=ReadXML()
class TestXML(unittest.TestCase):
    def test001(self):
        for i in range(3):
            re=sjx.sjxTest(int(readXML.readXML("dy",i,"b1")),
                        int(readXML.readXML("dy",i,"b2")),
                        int(readXML.readXML("dy",i,"b3")))
            self.assertEqual(re,readXML.readXML("dy",i,"except"))
    # def test002(self):
    #     re=sjx.sjxTest(int(readXML.readXML("db","b1")),
    #                 int(readXML.readXML("db", "b2")),
    #                 int(readXML.readXML("db", "b3")))
    #     self.assertEqual(re,readXML.readXML("db","except"))
    # def test003(self):
    #     re=sjx.sjxTest(int(readXML.readXML("pt","b1")),
    #                 int(readXML.readXML("pt", "b2")),
    #                 int(readXML.readXML("pt", "b3")))
    #     self.assertEqual(re,readXML.readXML("pt","except"))

