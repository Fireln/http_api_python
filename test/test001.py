# -*- coding: utf-8 -*-
__author__ = 'Fireln'
"""
    @auther : Fireln
    @time : 
"""


b ={
                    "Parames":
                        {
                            "query": "?name=13783783183&password=111111",
                            "body": {},
                        },
                    "path": "/user/authenticate/name",
                    "type": ["query"],
                    "usepath": False,
                    "pathkey": [],
                    "uselastact": False,
                    "lastactkey": [],
                    "styact":  False,
                    "styactkey": [],
                    "randomNum": False,
                    "randomkey": []
                  }
c = ['Parames','query']

def test(data,t):

    if len(t) == 0:
        return data
    else:
        da = data.get(t[0])
        tt = t[1:]  #用切片的原因是因为pop后如果只有一个元素的话就会变成String类型
        return test(da,tt)


print(test(b,c))