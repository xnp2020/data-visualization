from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 起始点
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        self.direction = choice([1, -1])
        self.distance = choice([0, 1, 2, 3, 4])
        return self.direction * self.distance

    def fill_walk(self):
        """计算所有的点"""

        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
