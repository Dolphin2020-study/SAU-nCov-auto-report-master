import os
import pytz
import requests
from time import sleep
from random import randint
from datetime import datetime

# 忽略网站的证书错误，这很不安全 :(
verify_cert = False

# 全局变量
#读取环境变量中的登录信息
user = os.environ['SEP_USER_NAME']  # 学号
passwd = os.environ['SEP_PASSWD']  # SAU密码
api_key = os.environ['API_KEY']  # server酱的api，填了可以微信通知打卡结果，不填没影响
xingming = os.environ['XINGMING'] 
telnum = os.environ['TELNUM'] 
xueyuan = os.environ['XUEYUAN'] 
sauid = os.environ['SAUID'] 
tg_token = os.environ['TG_TOKEN']   # tg酱通知token

def login(s: requests.Session, username, password):
    payload = {
        "username": username,
        "password": password
    }
    r = s.post("https://ucapp.sau.edu.cn/wap/login/invalid", data=payload)
    if r.json().get('m') != "操作成功":
        print("登录失败，错误信息: ", r.text)
    else:
        print("登录成功")

def submit(s: requests.Session):
    new_daily = {
        'xingming': xingming,
        'xuehao': user,
        'shoujihao': telnum,
        'danweiyuanxi': xueyuan,
        'dangqiansuozaishengfen': "河南省",
        'dangqiansuozaichengshi': "郑州市",
        'shifouyuhubeiwuhanrenyuanmiqie': "否",
        'shifoujiankangqingkuang': "是", 
        'shifoujiechuguohubeihuoqitayou': "是",
        'fanhuididian':"郑州",
        'shifouweigelirenyuan': "否",
        'shentishifouyoubushizhengzhuan': "否",
        'shifouyoufare': "否",
        'qitaxinxi': "",
        'tiwen': "36.2",
        'tiwen1': "36.2",
        'tiwen2': "36.2",
        'riqi': datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d"),
        'id': sauid}

    r = s.post("https://app.sau.edu.cn/form/wap/default/save?formid=10", data=new_daily)
    result = r.json()
    if result.get('m') == "操作成功":
        print("打卡成功")
        message(api_key, result.get('m'), new_daily)
        exit(0)
    else:
        print("打卡失败，错误信息: ", r.json())
        exit(1)

def message(key, title, body):
    """
    微信通知打卡结果
    """
    # 错误的key也可以发送消息，无需处理 :)
    msg_url = "https://sc.ftqq.com/{}.send?text={}&desp={}".format(key, title, body)
    tg_url = "https://dianbao.vercel.app/send/{}/{}".format(tg_token, body)
    requests.get(msg_url)
    requests.get(tg_url)

def report(username, password):
    s = requests.Session()
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10;  AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045136 Mobile Safari/537.36 wxwork/3.0.16 MicroMessenger/7.0.1 NetType/WIFI Language/zh"
    }
    s.headers.update(header)

    print(datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S %Z"))
    for i in range(randint(1, 5), 0, -1):
        print("\r等待{}秒后填报".format(i), end='')
        sleep(1)

    login(s, username, password)
    submit(s)

if __name__ == "__main__":
    report(username=user, password=passwd)
