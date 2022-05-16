import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# s表示点的size，c表示颜色，用一个元组表示，cmap表示颜色映射
ax.scatter(x_values, y_values, s=1, c=y_values, cmap=plt.cm.Blues)

ax.set_title('squres', fontsize=24)
ax.set_xlabel('number', fontsize=14)
ax.set_ylabel('values', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()
