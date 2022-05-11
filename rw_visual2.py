import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个randomwalk实例
    rw = RandomWalk(50)
    rw.fill_walk()

    plt.style.use('classic')
    # figsize指定图形大小，单位为英寸
    fig, ax = plt.subplots(figsize=(10,6),dpi=128)
    point_number = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    #突出起点和终点
    #ax.plot(0,0,c='green')
    #ax.plot(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    #ax.get_xaxis().set_visible(False)
    #ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
