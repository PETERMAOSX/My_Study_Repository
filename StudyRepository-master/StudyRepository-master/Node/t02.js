var http = require("http");
var fs = require("fs");
http.createServer((req,res)=>{
    fs.readFile(__dirname+"/index01.html","utf-8",(err,data)=>{
        if(err){
            res.statusCode = 404;
            res.setHeader("Content-Type","text/plain");
            res.end("Not Found!");
        }
        else{
            res.statusCode = 200;
            res.setHeader("Content-Type","text/html");
            res.end(data);
        }
    });
}).listen(3000,'127.0.0.1',()=>{
    console.log("Successfully");
});