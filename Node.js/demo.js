var http = require("http")
var app = http.createServer(function(req,res){
    // req请求信息   res 响应信息  
    console.log(req.url);
    if(req.url == '/zhangben'){
        res.setHeader("Content-type","text/html;charset=utf-8");
        res.write("欢迎来到网站首页")
        res.end()
    }
})
app.listen(3000)
