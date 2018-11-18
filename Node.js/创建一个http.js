// 1 如何去使用node的模块 http  fs url path...  require
var myhttp = require('http');
// 实例化http对象出来
var app = myhttp.createServer(function (req, res) {
   // 1 次http请求就会有1次http响应
//    2 req 请求的信息放在req里面  浏览器向node服务器发送的信息
//    3 res 响应的信息放在res里面  node服务器向浏览器发送的信息
      res.write("hello world");
      res.end();
});
//监听端口
app.listen(3000);
