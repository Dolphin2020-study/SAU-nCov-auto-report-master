# SAU-nCov-auto-report
沈航情防控每日填报助手，用于解决忘记填写企业微信中身体状况每日打卡的问题。
修改自IanSmith123/ucas-covid19 https://github.com/IanSmith123/ucas-covid19


# 注意
本人不对因为滥用此程序造成的后果负责，**请在合理且合法的范围内使用本程序**。

**本程序仅用于解决忘记打卡这一问题，如果填报表中任意情况发生变化，比如地点发生变化，请务必在程序运行之前手动打卡。**




# 使用方法： 使用 GitHub Actions（推荐使用）
没有服务器的同学可以使用 GitHub Action 来进行运行此程序。

**请勿**直接修改`sub.py`内的登录账号和密码，Github的公开仓库的内容可以被所有人查看。

Github提供了一个secret功能，用于存储密钥等敏感信息，请按照以下步骤操作。

使用步骤:
- 点击右上角 `star` :)
- 克隆这个仓库到你名下
- fork的仓库默认禁用了`workflow`，需要手动打开：点击 `actions`选项卡，点击`I understand my workflows, go ahead and run them`。
- 在仓库设置里面, 设置 secrets 如下
   - `SEP_USER_NAME`: 你的学号 如 12345
  - `SEP_PASSWD`: 你的智慧沈航密码 如 12345
  - `XINGMING`: 你的 姓名 如 张三
  - `XUEYUAN`: 你的 学院 如 计算机学院
  - `TELNUM`: 你的 电话号码 如 123345
  - `SAUID`: 你的 SAUID 如 123211(需抓包获取)
  - server酱通知设置（需要server酱通知时设置）：
    - `API_KEY`: 你的通知[server酱](http://sc.ftqq.com/3.version)的api key，填写之后可以在程序完成打卡之后通知到微信，如果不填写不影响使用
- 测试actions是否可以正常工作：编辑本项目内任意文件，推荐修改`README.md`，比如添加一个空行，并提交以触发action运行，提交后的一分钟左右可以在action选项卡中看到运行记录


参考截图设定以上七个secrets，`API_KEY`可选。
![](setting.png)
![](secrets.jpg)

完成之后, 每天  (北京时间 8:00-9：00) 每半小时自动触发github actions进行填报 。
（存在问题，打卡时间不准不稳定，原因未知，挂vps正常，希望大佬可以解决）

以下粘贴自:https://github.com/IanSmith123/ucas-covid19
# 方法三：使用Windows的任务计划程序（适合每天需要打开电脑来学习的同学）
不需要服务器，不需要了解github actions, 本地运行，不需担心账号密码泄露。

需要本地电脑安装python3，并且安装依赖库pytz和requests，可以使用命令pip install -r requirements.txt 来进行一键安装，并设置好环境变量。 使用步骤：
- git clone 本仓库
- 修改sub.py中的账号密码
- 使用autosubWin.bat文件

- 搜索打开任务计划程序，按照下图在Windows目录下创建任务，事件设为执行autosubWin.bat,触发器设为每天早上固定时间就行
![image](https://user-images.githubusercontent.com/23693269/142963254-b3b82bf6-b072-4187-9b1c-d8ebc0f80262.png)
- 有一个需要注意的点，在条件那儿要注意看是否勾选了“只有在计算机使用交流电源时才启动此任务”，勾选了记得取消，不然电脑没在充电状态就不会执行这个任务
![image](https://user-images.githubusercontent.com/23693269/142963274-f0c9eba4-657c-4679-ab38-5fb47f5fafde.png)
任务计划程序的设置会很直观，你还可以设置如果任务执行失败后多长时间再次尝试执行。需要注意的一点是，设定的时间最好能切合自己常打开电脑的时间。


# 致谢
- 感谢ucas-covid19 https://github.com/IanSmith123/ucas-covid19


<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">知识共享署名-非商业性使用-相同方式共享 3.0 未本地化版本许可协议</a>进行许可。

Dolphin

2021-1-12


长时间不更新可能被禁用action，请更新yml文件(加个换行就好)

2021-6-26

github action不够稳定，推荐迁移到腾讯云函数，目前运行稳定。
sauid抓包地址: https://app.sau.edu.cn/form/wap/default?formid=10

2021-10-27
