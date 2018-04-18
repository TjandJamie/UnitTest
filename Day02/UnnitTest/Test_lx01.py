# 导入UnnitTest包
import unittest
from unittest import TestCase
from Day02.Code.lx01 import Calc

# 实例化一个对象
ca = Calc()


# 定义一个类
class Testlx01(TestCase):

    def setUp(self):
        print("开始...")

    def test001(self):
        # 使用匿名函数方法,不使用实例化对象时使用
        # r = Calc().add(10, 10)
        r = ca.add(10, 10)
        self.assertEqual(r, 20)

    def test002(self):
        # 使用匿名函数方法,不使用实例化对象时使用
        # r = Calc().sub(2, 1)
        r = ca.sub(2, 1)
        self.assertEqual(r, 1)

    def tearDown(self):
        print("结束...")


if __name__ == '__main__':
    unittest.main()
