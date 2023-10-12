# bilibili-auto-report-for-al
B站上碧蓝航线相关的敏感视频自动举报脚本，搞事的都414

# 使用方法
## 环境配置
1. 前往[Python官网]((https://www.python.org/downloads/windows/))下载`3.10`以上的版本，安装并配置好环境(网上有教程)  
2. 配置完成后打开终端，输入`pip install bilibili-api-python -i https://pypi.tuna.tsinghua.edu.cn/simple`并等待安装完成
3. 点击本页面蓝色的`Code` => `Download ZIP`下载源码并解压
4. 输入`python main.py`运行
   
## 使用
> 因为举报功能需要登录bilibili账户，所以需要使用cookie进行鉴权，本程序接收的cookie仅用于举报。**请务必保护好自己的cookie信息**，这东西非常重要，请勿泄露！(本软件运行后会产生一个`credential.json`用于保存鉴权数据避免每次都要输入，**这个也不要发给任何人，否则后果自负**)

1. 首先需要输入cookie以用于鉴权，教程：[get-credential](https://nemo2011.github.io/bilibili-api/#/get-credential)
2. 输入完成后脚本就可以自动执行了，设定是10min获取一次，可以愉快地挂机了。

# 特别注意
禁止将本程序用于其他用途，否则后果均由使用者承担