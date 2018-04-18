# 导包
from xml.dom import minidom
class ReadXML(object):
    def readXML(self, one, num, two):
        # 解析文档
        root = minidom.parse('../Datapool/sjxXml.xml')
        # 获取文档元素
        dom = root.documentElement
        # 查找指定元素
        sel = dom.getElementsByTagName(one)[int(num)]
        data = sel.getElementsByTagName(two)[0].firstChild.data
        # 返回数据
        return data