import requests

# 执行api调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# 将api响应赋给一个变量，r.json()方法把json转成python字典
response_dict = r.json()
print(f"Total repos: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repos returned: {len(repo_dicts)}")

# 处理结果
#print(response_dict.keys())

#研究第一个仓库
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)