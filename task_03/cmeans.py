import math

import numpy as np, numpy.random
from math import hypot

from task_02.dot import Dot

k = 2
m = 2
e = 2.718281828459045

dots = [Dot(np.random.randint(low=0, high=150), np.random.randint(low=0, high=150)) for i in range(100)]

C = [[0, 0], [0, 0]]

weight = np.random.dirichlet(np.ones(k), size=len(dots))
SSE_OLD = 0
SSE_NEW = 0
while SSE_NEW == 0 or math.fabs(SSE_NEW - SSE_OLD) > e:

    SSE_OLD = SSE_NEW
    for j in range(k):
        denoSum = sum(np.power(weight[:, j], m))

        # for x
        sumMM = 0
        for i in range(len(dots)):
            mm = np.multiply(np.power(weight[i, j], m), dots[i].x)
            sumMM += mm
        cc = sumMM / denoSum
        C[0][j-1] = cc

        # for y
        for i in range(len(dots)):
            mm = np.multiply(np.power(weight[i, j], m), dots[i].x)
            sumMM += mm
        cc = sumMM / denoSum
        C[1][j-1] = cc

    for i in range(len(dots)):
        denoSumNext = 0
        for j in range(k):
            denoSumNext += np.power(1 / hypot(dots[i].x - C[0][j-1], dots[i].y - C[1][j-1]), 1 / (m - 1))
        for j in range(k):
            w = np.power((1 / hypot(dots[i].x - C[0][j-1], dots[i].y - C[1][j-1])), 1 / (m - 1)) / denoSumNext
            weight[i, j] = w

    SSE_NEW = 0
    for j in range(k):
        for i in range(len(dots)):
            SSE_NEW += np.power(weight[i, j], m) * hypot(dots[i].x - C[0][j - 1], dots[i].y - C[1][j - 1])
#
print("\nThe weights: \n", weight)

