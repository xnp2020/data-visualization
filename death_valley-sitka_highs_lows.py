import csv
from datetime import datetime

import matplotlib.pyplot as plt

# 显示中文标签
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

filename = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
 
    # 收集最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_day = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_day)
        highs.append(high)
        lows.append(low)

with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 收集最高温度
    dates2, highs2, lows2 = [], [], []
    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
            current_date = datetime.strptime(row[2],'%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs2.append(high)
            lows2.append(low)
            dates2.append(current_date)

# 根据最高、最低温度绘制图像
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

ax.plot(dates2, highs2, c='red', alpha=0.5)
ax.plot(dates2, lows2, c='blue',alpha=0.5)
ax.fill_between(dates2,highs2,lows2,facecolor='blue',alpha=0.1)


# 设置图形的格式
ax.set_title('High and Low temperature of year 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(axis='both', labelsize=16)

#设置每个坐标轴的取值范围
x_start = datetime.strptime('2017-12-01','%Y-%m-%d')
x_end = datetime.strptime('2019-01-31','%Y-%m-%d')
ax.axis([x_start, x_end, 20, 140])

plt.show()
