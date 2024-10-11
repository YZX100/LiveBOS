# LiveBOS
LiveBOS文件上传漏洞批量检测脚本

![image](https://github.com/user-attachments/assets/e26cbe3d-4317-4072-81f2-a9b940fa36a7)


```shell
LiveBOS UploadFile.do 接口存在任意文件上传漏洞，未经身份验证的攻击者可通过该漏洞在服务器端任意执行代码，写入后门，获取服务器权限，进而控制整个 web 服务器。 
检测该漏洞所需要的FOFA语句：
body="Power by LiveBOS"
使用说明：
-u 单个URL检测
-f 批量检测文本文件中的URL
解析器为python3 
```
