import unittest
from ReadData.HTMLTestRunner import HTMLTestRunner
import time

# 运行那些py文件
dirpath="./"
discover=unittest.defaultTestLoader.discover(dirpath,pattern="test*.py")

if __name__ == '__main__':
    filePath="../Report"
    strftime=time.strftime("%Y-%m-%d %H_%M_%S")
    namePath=filePath+"/"+strftime+"Report.html"

    with open(namePath,'wb') as f:
        runner=HTMLTestRunner(stream=f,title="Tile 三角形单元测试",description="三角形单元测试共计8条用例，执行结果")
        #运行
        runner.run(discover)