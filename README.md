# GUI_Tools

![](https://img.shields.io/github/stars/ghealer/GUI_Tools) ![](https://img.shields.io/github/forks/ghealer/GUI_Tools)  ![](https://img.shields.io/github/issues/ghealer/GUI_Tools)
> 一个由各种图形化渗透工具组成的工具集，环境已配置完成，自带Java1.8与Java9
工具会持续添加，欢迎提交新工具到 Issues

### ✨ Demo
![](https://raw.githubusercontent.com/ghealer/GUI_Tools/main/img/demo.png)

### 🚀 快速使用
- 下载程序源代码

  `git clone https://github.com/ghealer/GUI_Tools.git`
  
  `pip install -r requirements.txt`
  
- 下载工具包

  `aHR0cHM6Ly9wYW4uYmFpZHUuY29tL3MvMXk1aGZRWV9Qa3JiSkE1RVl1dzJXNHcgICAgIGhnaTg=`
    
  将工具包解压(密码:GUI_Tools)放在GUI_Tools根目录下
  
  PS.工具包里的Cobalt Strike内置了很多插件（包含了很多病毒程序，请自行甄别使用），如有需要可以自行加载；工具包较大，后续会持续补充。

- 目录结构
```markdown
├── GUI_Tools.py
├── GUI_Tools_wxpython_gui.py
├── JAR_Management.fbp
├── gui_other
├── gui_scan
├── gui_shouji
├── gui_webshell
├── Java_path
└── setting.py
```

- 执行程序

	`python3 GUI_Tools.py`

### 🐾  更新日志

- 2021年9月7日 V1.0
	- 添加 Windows 和 MacOS 的 java1.8 与 java9 环境，可直接打开 jar 程序
	- 添加 Behinder、Godzilla 等 webshell 管理工具
	- 添加 Burp Suite Pro、Cobalt Strike 等渗透工具
	- 添加 Dirscan、Webfinder、Fofa Viewer、御剑dirscan 等信息收集工具
	- 添加 shiro、thinkphp、weblogic 等漏洞利用工具

- 近期发布 V2.0
	- 重构框架，将工具进行分组分类
	- 增加自定义添加工具功能
   	- 新增大量工具 

### 📝 免责声明

	本工具仅面向合法授权的企业安全建设行为，在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。  

	如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。 

	在使用本工具前，请您务必审慎阅读、充分理解各条款内容，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本工具。
    
    您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。 

### 🙋 问题反馈

- 反馈渠道
	- 如有问题请提交 Issues，我看到会及时解决。

- 关于工具
	- 工具刚写出来，可能BUG比较多，还望各位大佬多多包涵。
	- 后面会定期更新添加工具，各位在使用的时候如果有什么比较好用的想要添加到工具里的也可以提交 Issues。
	- **所有工具的收集均来自互联网，请自行甄别是否存在后门等程序，建议在虚拟机里运行本程序下的工具。**
	- 在2.0出来之前，可以通过修改源码来自定义武器库。
	- 后面会出一个纯命令行的工具集，尽情期待。
