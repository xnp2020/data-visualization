import json
import plotly.express as px
import pandas as pd

# 探索数据的结构
filename = 'data/all_month.geojson'
with open(filename,encoding='UTF-8') as f:
    all_eq_data = json.load(f)

#readable_file = 'data/readable_eq_data.json'
#with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
mags,titles,lons,lats = [],[],[],[]
for eq_dict  in all_eq_dicts:
    mag = abs(eq_dict['properties']['mag'])
    mags.append(mag)
    titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

print(mags[:5])
print(lons[:5])
print(lats[:5])
data = pd.DataFrame(data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级'])
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title=all_eq_data['metadata']['title'],
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)
fig.write_html('global_earthquakes.html')
fig.show()