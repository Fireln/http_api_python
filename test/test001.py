

files={'authorId':['None','7515dec3-3668-4020-9777-9d5524bf89b9'],
    'subject':['None','dfgfdhghgjh?'],
    'bodyText':['None','sadsad43110'],
    'postType':['None','QA'],
    'coins':['None','20']
     }

import requests

r = requests.post(url = 'http://test.jishulink.com:8080/jishulink_test/post/publish',files=files)
print(r.text)