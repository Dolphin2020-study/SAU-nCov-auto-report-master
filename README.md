# ucas-covid19
国科大疫情防控每日填报助手，用于解决忘记填写企业微信中身体状况每日打卡的问题。

本人不对因为滥用此程序的造成的后果负责，**请在合理且合法的范围内使用本程序**。

**本程序仅用于解决忘记打卡这一问题，如果身体状况发生变化或者地点发生变化，请务必在程序运行之前手动打卡。**

理论上来说本程序适用于**国内大多数高校**的每日打卡，只需要替换代码中的提交网址和其他的适配性工作即可，其他学校有需求的同学可以修改本代码，但请遵守`CC BY-NC-SA 3.0` 许可协议。

# 用法
1. 修改脚本内的sep账号和密码
2. （可选）填写[server酱](http://sc.ftqq.com/3.version)的api，填写之后可以在程序完成打卡之后通知到微信，如果不填写不影响使用
2. 放到服务器上，修改crontab，设定为每天八点半运行
```
30 8 * * * /usr/bin/python3  /root/ncov-ucas/yqfk.py >>/tmp/yqfk.log
```


# 建议
1. 定时时间设定到8:30，每天如果记起来了就手工填写，如果忘记了就由程序定时填写。填写的内容会和昨天的一致，地点也会保持昨天的地点不变。
2. 脚本运行所在的服务器的地理位置不会影响打卡的位置。
3. 如果手工完成了打卡，程序会显示今日已经打卡，不会影响之前手工打卡的结果。

# 注意
1. crontab会读取`/etc/localtime`的时区，而不是当前用户的时区，所以crontab里面的定时八点可能并不是UTC+8的早晨八点，解决方案是设置系统时区为UTC+8即可
```bash
TZ=Asia/Shanghai
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

# 跋

只接受PR，不接受需求。


<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">知识共享署名-非商业性使用-相同方式共享 3.0 未本地化版本许可协议</a>进行许可。


Les1ie
2020-4-5 23:56:52
