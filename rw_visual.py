import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个randomwalk实例
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,
               c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=1) #edgecolors='none' 删除点周围的轮廓

    #突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
