#导入 json
import json
class ReadJSON():
    def readJson(self):
        with open("../DataPool/sjxJSON.json",'r',encoding="utf-8") as f:
            jsonname=json.load(f)
            return jsonname['data']


# print(ReadJSON().readJson())