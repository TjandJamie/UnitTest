class ReadText(object):

    def readText(self):
        # 打开文件
        arr = []
        with open('../Datapool/sjxTxt.txt', 'r', encoding='utf-8') as f:
            for line in f:
                arr.append(line.strip().split(','))
            return arr


if __name__ == '__main__':
    ReadText().readText()
