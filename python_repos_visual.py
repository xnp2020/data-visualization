import requests

from plotly.graph_objs import Bar
from plotly import offline

print('The program will create a html file which describes the most popular repos on GitHub for each Language.')
selection = input("Please select the Language: ")
# 执行api调用并存储响应
url = f'https://api.github.com/search/repositories?q=language:{selection}&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# 将api响应赋给一个变量，r.json()方法把json转成python字典
response_dict = r.json()
print(f"Total repos: {response_dict['total_count']}")

repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# 可视化
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': f'Github上最受欢迎的{selection}项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'{selection}_repos.html')
