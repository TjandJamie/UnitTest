# 确认三角形三条边，进行判断三角形类型（等边、等腰、普通）
# 并进行提示，否则提示不是三角形
# 提示：
# 三角形：两边之和大于第三边，
# 等腰三角形：两条边相等，
# 等边三角形：三条边相等

# 输入三条边的长度
class SJX():
    def sjx(self, a, b, c):
        if a+b>c and a+c>b and b+c>a:
            if a==b and b==c:
                return "等边三角形"
            elif a==b or a==c or b==c:
                return "等腰三角形"
            else:
                return "三角形"
        else:
            return "不是三角形"


