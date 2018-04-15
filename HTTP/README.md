# 图解HTTP

## http
HTTP(HyperText Transfer Protocol)即超文本传输协议

客户端与服务器之间的通信基于HTTP

Web使用HTTP作为规范，完成从客户端到服务器等一系列运作流程

当我们在浏览器的地址栏中输入URL，通过HTTP，获得Web页面并呈现于屏幕上

1997年1月公布的HTTP/1.1是目前主流的HTTP协议版本

HTTP是(stateless)无状态协议, 不可保存发送过的请求或响应，使用Cookie技术解决这一问题

### HTTP方法
GET 获取资源

POST 传输实体主体

PUT

HEAD

CONNECT

DELETE

TRACE

OPTINOS

### HTTP报文

## TCP/IP
通常使用的网络（包括互联网）是在TCP/IP协议族的基础上运作的，而HTTP属于它内部的一个子集

TCP/IP可层次化为应用层、传输层、网络层、数字链路层

应用层：FTP(File Transfer Protocol), DNS(Domain Name System), HTTP

传输层：TCP(Transmission Control Protocol), UDP(User Data Protocol)

网络层：IP, ARP(Address Resolution Protocol)

## 附加 

SSL可提供通信加密处理，使用证书防止身份伪装

WebSocket使用浏览器进行全双工通信

DOM(Document Object Model,文档对象模型)可指定要发生动态变化的HTML

DOM是用以操作HTML文档和XML文档的API

RSS和Atom用于发布更新信息，两者都使用了XML
