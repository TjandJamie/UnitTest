# 导包 unittest
import unittest

# 导要测得类
from UnitTest02.Day02.CodeHost.lx01 import Calc

# ca=Calc()
# 创建单元测试类
class TestLX01(unittest.TestCase):
    def setUp(self):
        print("开始...")

    def test001(self):
        result=Calc().sub(11, 10)
        self.assertEqual(result, 1)
    def test002(self):
        result=Calc.add(1,1)
        self.assertEqual(result, 2)
    def tearDown(self):
        print("结束..")

if __name__ == '__main__':
    unittest.main()