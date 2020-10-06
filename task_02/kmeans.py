import numpy as np
import matplotlib.pyplot as plt

from task_02.dot import Dot


def create_dots(low: int, high: int, dot_count: int) -> []:
    x = np.random.randint(low=low, high=high, size=dot_count)
    y = np.random.randint(low=low, high=high, size=dot_count)

    dots = []

    for i in range(0, dot_count):
        dot: Dot = Dot(x=x[i], y=y[i])
        dots.append(dot)

    plt.scatter(x, y)
    plt.show()

    return dots


def get_centers(dots: [], k: int) -> []:
    max_distance: float = 0

    center_dots = []

    dot_a: Dot = None
    dot_b: Dot = None

    for i in range(0, len(dots) - 1):
        dot_from = dots[i]
        for j in range(i + 1, len(dots) - 1):
            dot_to = dots[j]
            distance = np.math.sqrt(pow((dot_from.x - dot_to.x), 2) + pow((dot_from.y - dot_to.y), 2))
            print(distance, dot_from, dot_to)
            if distance > max_distance:
                max_distance = distance
                dot_a = dot_from
                dot_b = dot_to

    center_dots.append(dot_a)
    center_dots.append(dot_b)

    dots.remove(dot_a)
    dots.remove(dot_b)

    for i in range(0, k-len(center_dots)):
        max_distance = 0
        for j in range(0, len(center_dots)-1):
            dot_from = center_dots[j]
            for k in range(0, len(dots)-1):
                dot_to = dots[k]
                distance = np.math.sqrt(pow((dot_from.x - dot_to.x), 2) + pow((dot_from.y - dot_to.y), 2))
                if distance > max_distance:
                    dot_b = dot_to

        center_dots.append(dot_b)
        dots.remove(dot_b)

    return center_dots


dots = create_dots(0, 100, 100)
center = get_centers(dots.copy(), 3)

print(center[0], center[1], center[2])
print(len(dots))