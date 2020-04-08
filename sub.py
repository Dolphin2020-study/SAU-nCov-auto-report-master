"""
author: Les1ie
mail: me@les1ie.com
license: CC BY-NC-SA 3.0
"""

import pytz
import requests
from datetime import datetime


s = requests.Session()

user = "USERNAME"    # sep账号
passwd = "PASSWORD"   # sep密码
api_key = "API_KEY"  # server酱的api，填了可以微信通知打卡结果，不填没影响


def login(s: requests.Session, username, password):
    # r = s.get(
    #     "https://app.ucas.ac.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.ucas.ac.cn%2Fsite%2FapplicationSquare%2Findex%3Fsid%3D2")
    # print(r.text)
    payload = {
        "username": username,
        "password": password
    }
    r = s.post("https://app.ucas.ac.cn/uc/wap/login/check", data=payload)

    # print(r.text)
    if r.json().get('m') != "操作成功":
        print(r.text)
        print("登录失败")
        exit(1)


def get_daily(s: requests.Session):
    daily = s.get("https://app.ucas.ac.cn/ncov/api/default/daily?xgh=0&app_id=ucas")
    # info = s.get("https://app.ucas.ac.cn/ncov/api/default/index?xgh=0&app_id=ucas")
    j = daily.json()
    d = j.get('d', None)
    if d:

        return daily.json()['d']
    else:
        print("获取昨日信息失败")
        exit(1)


def submit(s: requests.Session, old: dict):
    new_daily = {
        'realname': old['realname'],
        'number': old['number'],
        'szgj_api_info': old['szgj_api_info'],
        'sfzx': old['sfzx'],
        'szdd': old['szdd'],
        'ismoved': old['ismoved'],
        'tw': old['tw'],
        'sftjwh': old['sfsfbh'],
        'sftjhb': old['sftjhb'],
        'sfcxtz': old['sfcxtz'],
        'sfjcwhry': old['sfjcwhry'],
        'sfjchbry': old['sfjchbry'],
        'sfjcbh': old['sfjcbh'],
        'sfcyglq': old['sfcyglq'],
        'sfcxzysx': old['sfcxzysx'],
        'old_szdd': old['szdd'],
        'geo_api_info': old['old_city'],
        'old_city': old['old_city'],
        'geo_api_infot': old['geo_api_infot'],
        'date': datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d"),
        'jcjgqk': old['jcjgqk'],
        'app_id': 'ucas'}

    r = s.post("https://app.ucas.ac.cn/ncov/api/default/save", data=new_daily)
    print("提交信息:", new_daily)
    # print(r.text)
    result = r.json()
    if result.get('m') == "操作成功":
        print("打卡成功")
        if api_key:
            message(api_key, result.get('m'), new_daily)
    else:
        print("打卡失败，错误信息: ", r.json().get("m"))
        if api_key:
            message(api_key, result.get('m'), new_daily)


def message(key, title, body):
    """
    微信通知打卡结果
    """
    msg_url = "https://sc.ftqq.com/{}.send?text={}&desp={}".format(key, title, body)
    requests.get(msg_url)


if __name__ == "__main__":
    print(datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S %Z"))
    login(s, user, passwd)
    yesterday = get_daily(s)
    submit(s, yesterday)
