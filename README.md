# ucas-covid19
国科大疫情防控每日填报助手，用于解决忘记填写企业微信中身体状况每日打卡的问题。

本人不对因为滥用此程序造成的后果负责，**请在合理且合法的范围内使用本程序**。

**本程序仅用于解决忘记打卡这一问题，如果身体状况发生变化或者地点发生变化，请务必在程序运行之前手动打卡。**

理论上来说本程序适用于**国内大多数高校**的每日打卡，只需要替换代码中的提交网址并完成其他的适配性工作即可，其他学校有需求的同学可以修改本代码，但请遵守`CC BY-NC-SA 3.0` 许可协议。

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

# serverless 
如果你没有服务器，但是仍然想使用本程序，可以使用 serverless function，这里以腾讯云云函数为例。
1. 登录注册腾讯云
2. 打开`https://console.cloud.tencent.com/scf/`控制台的云函数页面，任选地区，点击`新建`
3. 输入函数名称`covid`，运行环境python3.6，创建方式空白函数
4. 全选然后删除下面cloud studio中正在编辑的`index.py`的文件的全部内容，然后将本项目中`serverless.py`的内容粘贴进去，同时修改自己的sep信息，如果有server酱api的可以填key没有的可以不写
5. 点击完成
6. 点击触发方式，选择添加触发方式，输入定时任务名称daily，触发周期为自定义触发周期， cron表达式 `0 30 8 * * * *`，点击完成

使用腾讯云的云函数打卡的计算量和调用量极低，不会收费。

# 使用 GitHub Actions
如果你不喜欢腾讯云, 就可以使用 GitHub Action 来进行运行, 使用步骤:
- 克隆这个仓库到你名下
- fork的仓库默认禁用了`workflow`，需要手动打开：点击 `actions`选项卡，点击`I understand my workflows, go ahead rand run them`。
- 在仓库设置里面, 设置 secrets 如下
  - `SEP_USER_NAME`: 你的 SEP 用户名(邮箱)
  - `SEP_PASSWD`: 你的 SEP 密码
  - `API_KEY`: 你的通知 api key (强烈建议设置, 因为不设置这个 api key 你无法及时知晓运行状态)

即可, 完成之后, 每天 UTC 0 点就会进行填报, (北京时间 8 点).

# 跋

只接受PR，不接受需求。

# 致谢
- 感谢 [karuboniru](https://github.com/IanSmith123/ucas-covid19/pull/1) 提供的github actions 支持

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">知识共享署名-非商业性使用-相同方式共享 3.0 未本地化版本许可协议</a>进行许可。


Les1ie

2020-4-5 23:56:52
