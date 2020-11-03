import requests
from json import JSONDecoder

http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
key = "9DhuFyXf4mNICfztR7N5vXqvEQBIzoBw"
secret = "tMu1kXysisPKlg1yet5OWolAaQltWGUd"
#图片的位置
filepath = "/Users/neo/Downloads/sadpro.jpg"

data = {"api_key": key, "api_secret": secret, "return_landmark": "0","return_attributes":"emotion"}
files = {"image_file": open(filepath, "rb")}
#得到上传数据的返回值
response = requests.post(http_url, data=data, files=files)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

print(req_dict)
