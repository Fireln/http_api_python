import requests
import hashlib
class GetUserInfo:
    def md(self,num):
        #print(hashlib.new('md5',num).hexdigest())
        return hashlib.new('md5',num).hexdigest()
    def login(self,*args):
        '''
            生成token
        '''
        self.url = r'http://test.jishulink.com:8080/jishulink_test/user/authenticate/name?' \
                   r'name=13783783183&password=111111'

        self.res = requests.put(self.url)
        if self.res.status_code == 200:
            return self.res.json()["ret"]["registerInfo"]["userId"]
        else:
            return "7515dec3-3668-4020-9777-9d5524bf89b9"


if __name__ == '__main__':
    g = GetUserInfo()
    print(g.login())