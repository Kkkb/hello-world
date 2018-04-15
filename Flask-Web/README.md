What's User-Agent?

- Flask上下文全局变量，在程序实例上调用app.app_context()一个可获得一个程序上下文
- 请求调度
- 请求钩子

/static/<filename>路由是Flask添加的特殊路由，用于访问静态文件

可以使用过滤器修改变量

{% include 'common.html' %}

url_for()辅助函数，它可以使用程序URL映射中保存的信息生成URL

flask-wtf

SQL数据库，结构化查询语言数据库

使用Flask-Migrate实现数据库迁移

app.config字典可用来存储框架、扩展、程序本身的配置变量

create_app()函数是程序的工厂函数，接收一个参数，是程序使用的配置名

app = Flask(__name__)

存储密码的散列值，而不是存储密码本身，可以保证数据库中用户密码的安全

使用Werkzeug实现密码散列

将创建程序的过程移入工厂函数后，可以使用蓝本在全局作用域中定义路由。对不同程序功能使用不同的蓝本，可保持代码整齐有序

@property

闭包closure

Redis MongoDB

更新表更好的方法是使用数据库迁移框架

```
def send_email(to, subject, template, **kwargs):
```

FLASKY_ADMIN

变量current_user由Flask-Login定义，且在视图函数和模板中自动可用

Flask上下文全局变量，请求上下文request是请求对象，封装了客户端发出的HTTP请求中的内容

表现层状态转移(Representation State Transfer, REST)

缓存是数据交换的缓冲区(Cache)

采用REST(Representational State Transfer)架构进行RIA(Rich Internet Application)和Web服务器之间的通信，轻量化的Flask是开发REST的理想框架。

资源是REST架构的核心概念，每个，每类资源有唯一的URL

客户端使用请求方法如GET, POST, PUT, DELETE及资源URL发起请求，获得服务器响应

REST Web服务器常用的两种编码方式是JavaScript对象表示法(JavaScript Object Notation)和可扩展标记语言(Extensible Markup Language, XML)

JavaScript是Web浏览器使用的客户端脚本语言，采用联系紧密的JSON表示资源

程序的工厂函数在app包的构造文件中定义

werkzeug.local

from greenlet import getcurrent as get_ident

trigger 触发

access 访问

modify 修改