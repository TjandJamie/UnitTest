# 导包
import csv
class ReadCSV(object):
    def readCsv(self):
        filecsv = csv.reader(open('../Datapool/sjxCsv.csv','r',encoding='utf-8'))
        arr = []
        for line in filecsv:
            arr.append(line)
        return arr

if __name__ == '__main__':
    print(ReadCSV().readCsv())