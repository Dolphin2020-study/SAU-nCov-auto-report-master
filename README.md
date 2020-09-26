# ucas-covid19
国科大疫情防控每日填报助手，用于解决忘记填写企业微信中身体状况每日打卡的问题。

# 注意
本人不对因为滥用此程序造成的后果负责，**请在合理且合法的范围内使用本程序**。

**本程序仅用于解决忘记打卡这一问题，如果填报表中任意情况发生变化，比如地点发生变化，请务必在程序运行之前手动打卡。**


理论上来说本程序适用于**国内大多数高校**的每日打卡，只需要替换代码中的提交网址并完成其他的适配性工作即可，其他学校有需求的同学可以修改本代码，但请遵守`CC BY-NC-SA 3.0` 许可协议。



# 方法一： 使用自己的服务器运行
## 用法
1. 点击右上角`star` :)
2. 下载本项目到本地
3. 修改本地项目里面`sub.py`代码里面的sep账号和密码
4. （可选）填写[server酱](http://sc.ftqq.com/3.version)的api，填写之后可以在程序完成打卡之后通知到微信，如果不填写不影响使用
5. 上传`sub.py`到自己的服务器上，修改crontab，设定为每天八点半运行，注意需要修改以下命令的路径为实际路径。
```
30 8 * * * /usr/bin/python3  /root/ucas-covid19/sub.py >>/tmp/yqfk.log
```


## 建议
1. 定时时间设定到8:30，每天如果记起来了就手工填写，如果忘记了就由程序定时填写。填写的内容会和昨天的一致，地点也会保持昨天的地点不变。
2. 脚本运行所在的服务器的地理位置不会影响打卡的位置。
3. 如果手工完成了打卡，程序会显示今日已经打卡，不会影响之前手工打卡的结果。

## 注意
1. crontab会读取`/etc/localtime`的时区，而不是当前用户的时区，所以crontab里面的定时八点可能并不是UTC+8的早晨八点，解决方案是设置系统时区为UTC+8即可
```bash
TZ=Asia/Shanghai
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```



# 方法二： 使用 GitHub Actions（推荐使用）
没有服务器的同学可以使用 GitHub Action 来进行运行此程序。

**请勿**直接修改`sub.py`内的登录账号和密码，Github的公开仓库的内容可以被所有人查看。

Github提供了一个secret功能，用于存储密钥等敏感信息，请按照以下步骤操作。

使用步骤:
- 点击右上角 `star` :)
- 克隆这个仓库到你名下
- fork的仓库默认禁用了`workflow`，需要手动打开：点击 `actions`选项卡，点击`I understand my workflows, go ahead and run them`。
- 在仓库设置里面, 设置 secrets 如下
  - `SEP_USER_NAME`: 你的 SEP 用户名(邮箱)
  - `SEP_PASSWD`: 你的 SEP 密码
  - `API_KEY`: 你的通知[server酱](http://sc.ftqq.com/3.version)的api key，填写之后可以在程序完成打卡之后通知到微信，如果不填写不影响使用
- 测试actions是否可以正常工作：编辑本项目内任意文件，推荐修改`README.md`，比如添加一个空行，并提交以触发action运行，提交后的一分钟左右可以在action选项卡中看到运行记录


参考截图设定以上三个secrets，`API_KEY`可选。
![](setting.png)


完成之后, 每天 UTC 23:50 (北京时间 7:50) 自动触发github actions进行填报 。

# 方法三：使用Windows的任务计划程序（适合每天需要打开电脑来学习的同学）
不需要服务器，不需要了解`github actions`, 本地运行，不需担心sep账号密码泄露。

需要本地电脑安装python3，并且安装库pytz和requests，并设置好环境变量。
使用步骤：
- git clone 本仓库
- 修改`sub.py`中的SEP账号密码
- 创建一个`autosubWin.bat`文件，写入以下内容
```
@echo off
python3 \path\to\sub.py %具体路径替换成sub.py的路径%
%py -3 \path\to\sub.py 如果电脑同时装了python3和python2的话就使用这个。%
pause
```
- 搜索打开任务计划程序，按照下图在Windows目录下创建任务，事件设为执行autosubWin.bat,触发器设为每天早上固定时间就行
  ![](setting2.png "任务计划程序设置")

- 有一个需要注意的点，在条件那儿要注意看是否勾选了“只有在计算机使用交流电源时才启动此任务”，勾选了记得取消，不然电脑没在充电状态就不会执行这个任务

  ![](setting3.png "取消勾选")
任务计划程序的设置会很直观，你还可以设置如果任务执行失败后多长时间再次尝试执行。需要注意的一点是，设定的时间最好能切合自己常打开电脑的时间。任务执行的时候，会弹出一个DOS窗口，执行完成之后关掉即可。
# 跋

只接受PR，不接受需求。

# changelog
- 2020年4月15日 添加了随机等待`10-600`秒之后再进行填报
- 2020年4月15日 添加了`user-agent`
- 2020年4月15日 更新了README，添加了设定secrets页面的截图
- 2020年6月12日 更新了README，提醒同学请勿直接在代码中填写密码
- 2020年6月14日 更新了README，添加有关触发action运行的说明
- 2020年6月24日 适配了网站的字段的更新；添加了 debug模式隐藏打卡信息；github action直接输出打卡结果；移除了 serverless 方式的支持
- 2020年9月16日 适配了网站的字段的更新
- 2020年9月26日 更新了README，添加了使用windows计划任务的操作步骤

# 致谢
- 感谢 [karuboniru](https://github.com/IanSmith123/ucas-covid19/pull/1) 提供的github actions 支持
- 感谢 [tyfulcrum](https://github.com/IanSmith123/ucas-covid19/pull/2) 对文档的完善工作
- 感谢 [HsimWong](https://github.com/IanSmith123/ucas-covid19/pull/3) 对文档的完善工作
- 感谢 [spwpun](https://github.com/IanSmith123/ucas-covid19/pull/6) 添加了使用 windows 计划任务的操作步骤

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">知识共享署名-非商业性使用-相同方式共享 3.0 未本地化版本许可协议</a>进行许可。


Les1ie

2020-4-5 23:56:52
