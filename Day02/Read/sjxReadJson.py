# 导包
import json


class ReadJSON():
    def readJson(self):
        # 打开文件
        with open('../Datapool/sjxJson.json', 'r' , encoding='utf-8') as f:
            jsonname = json.load(f)
            return jsonname['data']

if __name__ == '__main__':
    print(ReadJSON().readJson())