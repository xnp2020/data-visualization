from operator import itemgetter

import requests
#from plotly.graph_objs import Bar
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[0:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        comments = int(response_dict['descendants'])
    except KeyError:
        submission_dict = {
            'sub_id': submission_id,
            'title': response_dict['title'],
            'hn_link': f"http://new.ycombinator.com/item?id={submission_id}",
            'comments': 0,
        }
        submission_dicts.append(submission_dict)
    else:
        submission_dict = {
            'sub_id': submission_id,
            'title': response_dict['title'],
            'hn_link': f"http://new.ycombinator.com/item?id={submission_id}",
            'comments': comments,
        }
        submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

titles , hn_links , Comments = [],[],[]
for submission_dict in submission_dicts:
    sub_title = submission_dict['title']
    sub_comment = submission_dict['comments']
    sub_link = submission_dict['hn_link']
    hn_link = f"<a href='{sub_link}'>{sub_title}</a>"
    
    titles.append(sub_title)
    hn_links.append(hn_link)
    Comments.append(sub_comment)

#repo_links, stars, labels = [], [], []
#
#for repo_dict in repo_dicts:
#    repo_name = repo_dict['name']
#    repo_url = repo_dict['html_url']
#    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
#    repo_links.append(repo_link)
#    stars.append(repo_dict['stargazers_count'])
#
#    owner = repo_dict['owner']['login']
#    description = repo_dict['description']
#    label = f"{owner}<br />{description}"
#    labels.append(label)

# 可视化
data = [{
    'type': 'bar',
    'x': hn_links,
    'y': Comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': f'Hacker News上最活跃的讨论',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Hacker News.html')