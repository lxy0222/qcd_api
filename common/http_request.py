import requests
class HttpRequest:
    def http_request(self,url,data,http_method,cookie=None):
        if http_method.upper()=='GET':
            try:
                res=requests.get(url,data,cookies=cookie)
            except Exception as e:
                print("get请求出错了：{}".format(e))
        elif http_method.upper()=='POST':
            try:
                res=requests.post(url,data,cookies=cookie)
            except Exception as e:
                print("post请求出错了：{}".format(e))
        else:
            print('输入的请求方法不正确！')
        return res
if __name__ == '__main__':
    #注册
    register_url='http://test.lemonban.com/futureloan/mvc/api/member/register'
    register_data={'mobilephone':'13732371108','pwd':'123456','regname':'meson'}
    #登录
    login_url='http://test.lemonban.com/futureloan/mvc/api/member/login'
    login_data={'mobilephone':'13732371108','pwd':'123456'}
    #充值
    recharge_url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    recharge_data={'mobilephone':'13732371008','amount':'1000'}
    login_res=HttpRequest().http_request(login_url,login_data,'post')
    recharge_res=HttpRequest().http_request(recharge_url,recharge_data,'post',login_res.cookies)
    print(login_res.json(),recharge_res.json())