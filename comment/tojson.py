import json

class ToJson:
    def strToJson(self,strobj):
        data = strobj.replace('\n','')
        try:
            jsonobj = json.loads(data)
            return jsonobj
        except Exception as e:
             return strobj


if __name__ == '__main__':
    a = '''
    {
    "Parames": "",
    "Type": "Parames",
    "Actkey": [
        "OrderNumber"
    ],
    "Jsonkey": "False",
    "RandomNum": "False"
}
    '''
    t = ToJson()
    print(t.strToJson(a))