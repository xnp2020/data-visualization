from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个D6
die = Die()

# 存储结果到一个list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析每个点的次数
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6骰子1000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
