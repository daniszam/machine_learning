import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from task_02.dot import Dot

dots = [Dot(np.random.randint(low=0, high=150), np.random.randint(low=0, high=150)) for i in range(100)]
dots_1 = [(np.random.randint(low=0, high=150), np.random.randint(low=0, high=150)) for i in range(100)]

frame = pd.DataFrame(dots_1)
X = frame.iloc[:, 0]
Y = frame.iloc[:, 1]

plt.scatter(X, Y)
plt.show()

m = 0
c = 0

L = 0.0001
epochs = 1000  # количество итераци

n = float(len(X))

# градиентный спуск
for i in range(epochs):
    Y_pred = m * X + c  # Предсказанное значение
    D_m = (-2 / n) * sum(X * (Y - Y_pred))  # Производная wrt m
    D_c = (-2 / n) * sum(Y - Y_pred)  # Производная wrt c
    m = m - L * D_m  # обновляем m
    c = c - L * D_c  # обновляем c

# Предсказание
Y_pred = m * X + c

plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # линия регрессии
plt.show()
