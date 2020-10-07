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


    return dots


def get_centers(dots: [], k: int) -> []:
    max_distance: float = 0

    center_dots = []

    dot_a: Dot = None
    dot_b: Dot = None

    for i in range(0, len(dots)):
        dot_from = dots[i]
        for j in range(i + 1, len(dots)):
            dot_to = dots[j]
            distance = np.math.sqrt(pow((dot_from.x - dot_to.x), 2) + pow((dot_from.y - dot_to.y), 2))
            if distance > max_distance:
                max_distance = distance
                dot_a = dot_from
                dot_b = dot_to

    center_dots.append(dot_a)
    center_dots.append(dot_b)

    dots.remove(dot_a)
    dots.remove(dot_b)

    for i in range(0, k - len(center_dots)):
        max_distance = 0
        new_center_dot = None

        for j in range(0, len(dots)):
            dot_from = dots[j]
            min_distance = 0
            for q in range(0, len(center_dots)):
                dot_to = center_dots[q]
                distance = np.math.sqrt(pow((dot_from.x - dot_to.x), 2) + pow((dot_from.y - dot_to.y), 2))
                if min_distance == 0 or distance < min_distance:
                    min_distance = distance

            if max_distance < min_distance:
                max_distance = min_distance
                new_center_dot = dot_from
        center_dots.append(new_center_dot)
        dots.remove(new_center_dot)
    return center_dots


def create_cluster(dots: [], center_dots: []) -> {}:
    clusters = {}
    for dot in dots:
        min_distance_to_center_dot = 0
        cluster = None

        for center_dot in center_dots:
            distance = np.math.sqrt(pow((dot.x - center_dot.x), 2) + pow((dot.y - center_dot.y), 2))
            if min_distance_to_center_dot == 0 or distance < min_distance_to_center_dot:
                min_distance_to_center_dot = distance
                cluster = center_dot

        cluster_dots = clusters.get(cluster) if clusters.get(cluster) is not None else []
        cluster_dots.append(dot)
        clusters.update({cluster: cluster_dots})

    return clusters


def recenter(clusters: {}) -> []:
    cluster_center_dots = clusters.keys()
    new_cluster_center = []
    for cluster_center_dot in cluster_center_dots:
        cluster_dots = clusters.get(cluster_center_dot)
        center_x = 0
        center_y = 0
        for cluster_dot in cluster_dots:
            center_x += cluster_dot.x
            center_y += cluster_dot.y

        center_x = center_x / len(cluster_dots)
        center_y = center_y / len(cluster_dots)
        new_cluster_center.append(Dot(x=center_x, y=center_y))

    return new_cluster_center


k = 3
dots = create_dots(0, 100, 100)
center = get_centers(dots.copy(), k)

clusters = create_cluster(dots.copy(), center.copy())
print(clusters)

new_center = recenter(clusters)

# print(recenter(clusters))
#
while center != new_center:
    clusters = create_cluster(dots.copy(), new_center.copy())
    center = new_center
    new_center = recenter(clusters)

for key in clusters.keys():
    dots = clusters.get(key)
    x = []
    y = []
    for dot in dots:
        x.append(dot.x)
        y.append(dot.y)

    plt.scatter(x, y, color=np.random.rand(3,))
    plt.scatter(key.x, key.y, color="red")

plt.show()


