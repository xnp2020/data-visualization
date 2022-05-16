import csv
import plotly.express as px
import pandas as pd

# 探索数据的结构
filename = 'data/world_fires_1_day.csv'
with open(filename,encoding='UTF-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lat_index = header_row.index('latitude')
    lon_index = header_row.index('longitude')
    bri_index = header_row.index('brightness')

    lats, lons, bris = [], [], []
    for row in reader:
        lat = float(row[lat_index])
        lon = float(row[lon_index])
        bri = float(row[bri_index])
        lats.append(lat)
        lons.append(lon)
        bris.append(bri)

print(bris[:5])
print(lons[:5])
print(lats[:5])

data = pd.DataFrame(data=zip(lons,lats,bris),columns=['经度','纬度','强度'])
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='world_fires_1_day',
    size='强度',
    size_max=10,
    color='强度',
)
fig.write_html('world_fires_1_day.html')
fig.show()