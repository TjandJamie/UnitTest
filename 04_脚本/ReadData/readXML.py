# 导xml包
from xml.dom import minidom
class ReadXML():
    # self 实例化时指向自己
    def readXML(self,one,num,two):
        #解析文档
        root=minidom.parse('../DataPool/sjxXML.xml')
        #获取文档元素
        dom=root.documentElement
        #查找指定元素
        dys=dom.getElementsByTagName(one)[int(num)]
        data=dys.getElementsByTagName(two)[0].firstChild.data
        return data

# r=ReadXML()