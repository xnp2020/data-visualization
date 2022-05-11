from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个D6
die_1= Die(8)
die_2 = Die(8)

# 存储结果到一个list

list1 = [ die_1.roll() for m in range(500)]
list2 = [ die_2.roll() for m in range(500)]
results = [ m * n for m in list1 for n in list2 ]


#print(results)
#for roll_num in range(50_000):
#    result = die_1.roll() * die_2.roll()
#    results.append(result)

# 分析每个点的次数
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

#dtick置为1让x轴显示所有的刻度值
x_axis_config = {'title': '结果','dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷1个D8和D8骰子各50000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8Xd8_50000.html')
