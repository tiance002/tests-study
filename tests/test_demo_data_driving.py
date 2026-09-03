import requests
import json
import os

# 获取当前脚本所在目录，再向上找到项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼接完整路径
config_path = os.path.join(BASE_DIR, "config", "config.json")
request_path = os.path.join(BASE_DIR, "data", "request_data.json")
response_path = os.path.join(BASE_DIR, "data", "response_data.json")

# 从配置文件夹获取测试配置
with open(config_path, "r", encoding="utf-8") as json_file:
    config = json.load(json_file)
# 从测试数据文件夹获取接口请求数据
with open(request_path, "r", encoding="utf-8") as json_file:
    request_data = json.load(json_file)
# 从测试数据文件夹获取接口响应数据
with open(response_path, "r", encoding="utf-8") as json_file:
    response_data = json.load(json_file)

class TestPytestDemo:
    def test_get_demo(self):
        host = config.get("host")
        get_api = config.get("getAPI")
        get_api_response_data = response_data.get("getAPI")
        # 发起请求
        response = requests.get(host+get_api)
        # 断言
        assert response.status_code == 200
        assert response.json() == get_api_response_data

    def test_post_demo(self):
        host = config.get("host")
        post_api = config.get("postAPI")
        post_api_request_data = request_data.get("postAPI")
        post_api_response_data = response_data.get("postAPI")
        # 发起请求
        response = requests.post(host + post_api, json=post_api_request_data)
        # 断言
        assert response.status_code == 201
        assert response.json() == post_api_response_data
