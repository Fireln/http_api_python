import requests
import hashlib
class GetUserInfo:
    def md(self,num):
        #print(hashlib.new('md5',num).hexdigest())
        return hashlib.new('md5',num).hexdigest()
    def login(self):
        '''
            生成token
        '''
        self.url = r'http://test.jishulink.com:8080/jishulink_test/user/authenticate/name?' \
                   r'name=13783783183&password=111111'

        self.res = requests.put(self.url)
        if self.res.status_code == 200:
            return self.res
        else:
            return self.res.status_code,self.res.headers


if __name__ == '__main__':
    print(GetToken().login())