#导 csv
import csv
class ReadCSV():
    def readCSV(self):
        filecsv=csv.reader(open("../DataPool/sjxCSV.csv",'r',encoding='utf-8'))
        arrs=[]
        for i in filecsv:
            arrs.append(i)
        return arrs


# print(ReadCSV().readCSV())
