from math import hypot
import numpy as np
import matplotlib.pyplot as plt

from task_02.dot import Dot


def dbscan(dots, eps, m, distance):

    cluster_num = 0
    NOT_NEIGHBOURS = "not_neighbours"

    visited_dots = set()
    clustered_dots = set()
    clusters = {NOT_NEIGHBOURS: []}

    def get_neighbours(p):
        return [q for q in dots if distance(p, q) < eps]

    def find_all_cluster_dots(p, neighbours):
        if cluster_num not in clusters:
            clusters[cluster_num] = []
        clusters[cluster_num].append(p)
        clustered_dots.add(p)
        while neighbours:
            q = neighbours.pop()
            if q not in visited_dots:
                visited_dots.add(q)
                neighbour_q = get_neighbours(q)
                if len(neighbour_q) > m:
                    neighbours.extend(neighbour_q)
            if q not in clustered_dots:
                clustered_dots.add(q)
                clusters[cluster_num].append(q)
                if q in clusters[NOT_NEIGHBOURS]:
                    clusters[NOT_NEIGHBOURS].remove(q)

    for dot in dots:
        if dot not in visited_dots:
            visited_dots.add(dot)
            neighbours = get_neighbours(dot)
            if len(neighbours) < m:
                clusters[NOT_NEIGHBOURS].append(dot)
            else:
                cluster_num += 1
                find_all_cluster_dots(dot, neighbours)
    return clusters


dots = [Dot(np.random.randint(low=0, high=150), np.random.randint(low=0, high=150)) for i in range(100)]
dots.extend([Dot(np.random.randint(low=180, high=300), np.random.randint(low=180, high=300)) for i in range(100)])
dots.extend([Dot(np.random.randint(low=0, high=150), np.random.randint(low=180, high=300)) for i in range(100)])

clusters = dbscan(dots, 20, 2, lambda dot_a, dot_b:  hypot(dot_a.x - dot_b.x, dot_a.y - dot_b.y))
for dots in clusters.values():
    X = [p.x for p in dots]
    Y = [p.y for p in dots]
    plt.scatter(X, Y, color=np.random.rand(3,))
plt.show()