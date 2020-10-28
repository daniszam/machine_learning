from task_02.dot import Dot
from math import hypot

import numpy as np


def calculate_distance(dots: []) -> []:
    for i in range(len(dots)):
        dot_from = dots[i]
        for j in range(len(dots) - i):
            dot_to = dots[j]
            distance_matrix[i][j] = hypot(dot_from.x - dot_to.x, dot_from.y - dot_to.y)

def find_neighbor(distance_matrix: [], added_dots_index: []):
    distance_matrix_slice = distance_matrix[list(added_dots_index), :]
    index_array = np.where(distance_matrix == min(distance_matrix_slice[np.nonzero(distance_matrix_slice)]))[0]
    (i, j) = index_array[0], index_array[1]

    print(np.min(distance_matrix, axis=tuple(added_dots_index), where=np.nonzero))
    (i, j) = np.where(distance_matrix == np.min(distance_matrix[np.nonzero(distance_matrix)], axis=added_dots_index))[0]
    graph_matrix[i, j] = distance_matrix[i, j]
    distance_matrix[i][j] = 0
    added_dots_index.append(i, j)


dots = [Dot(np.random.randint(low=0, high=150), np.random.randint(low=0, high=150)) for i in range(100)]
dots.extend([Dot(np.random.randint(low=180, high=300), np.random.randint(low=180, high=300)) for i in range(100)])
dots.extend([Dot(np.random.randint(low=0, high=150), np.random.randint(low=180, high=300)) for i in range(100)])

distance_matrix = np.zeros((len(dots), len(dots)))
graph_matrix = np.zeros((len(dots), len(dots)))

calculate_distance(dots.copy())

index_array = np.where(distance_matrix == min(distance_matrix[np.nonzero(distance_matrix)]))[0]
(i, j) = index_array[0], index_array[1]
added_dots_index = set([i, j])
graph_matrix[i, j] = distance_matrix[i, j]
distance_matrix[i][j] = 0


while len(added_dots_index) != len(dots):
    find_neighbor(distance_matrix.copy(), added_dots_index)