import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    station_index = header_row.index('NAME')

    highs = []
    lows = []
    dates = []
    for row in reader:
        try:
            station = row[station_index]
            high = int(row[high_index])
            low = int(row[low_index])
            current_date = datetime.strptime(row[date_index],'%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
    print(station)
# 根据最高、最低温度绘制图像
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# 设置图形的格式
ax.set_title(f'High and Low temperature of {station} of year 2018', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(axis='both', labelsize=16)

#设置每个坐标轴的取值范围
x_start = datetime.strptime('2017-12-01','%Y-%m-%d')
x_end = datetime.strptime('2019-01-31','%Y-%m-%d')
ax.axis([x_start, x_end, 20, 140])

plt.show()