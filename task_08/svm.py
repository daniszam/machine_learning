import sys

import pygame as pg
from sklearn import svm

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

sc = pg.display.set_mode((600, 600))
sc.fill(WHITE)
pg.display.update()

dots = []
k = []

fited = False
clf = None


while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN:

            if fited:
                y = clf.predict([[i.pos[0], i.pos[1]]])
                dots.append([i.pos[0], i.pos[1]])
                k.append(y[0])
                color = RED if y[0] == 1 else BLUE
                pg.draw.circle(
                    sc, color, i.pos, 10)
                pg.display.update()

            else:
                if i.button == 1:
                    pg.draw.circle(
                        sc, RED, i.pos, 10)

                    dots.append([i.pos[0], i.pos[1]])
                    k.append(1)

                    pg.display.update()
                elif i.button == 3:
                    pg.draw.circle(
                        sc, BLUE, i.pos, 10)

                    dots.append([i.pos[0], i.pos[1]])
                    k.append(2)

                    pg.display.update()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_RETURN:
                clf = svm.SVC(kernel='linear', C=1.0)
                clf.fit(X=dots, y=k)
                fited = True
                coef = clf.coef_[0]
                intercept = clf.intercept_
                n = -coef[0] / coef[1]
                m = intercept[0] / coef[1]
                Y_1_1 = -m
                X_1_1 = m / n
                Y_1_2 = 1 / coef[1] + Y_1_1
                X_1_2 = 1 / coef[0] + X_1_1
                Y_1_3 = -1 / coef[1] + Y_1_1
                X_1_3 = -1 / coef[0] + X_1_1

                y11 = ((0/X_1_1) * -Y_1_1) + Y_1_1
                y12 = ((600/X_1_1) * -Y_1_1) + Y_1_1

                y21 = ((0 / X_1_2) * -Y_1_2) + Y_1_2
                y22 = ((600 / X_1_2) * -Y_1_2) + Y_1_2

                y31 = ((0 / X_1_3) * -Y_1_3) + Y_1_3
                y32 = ((600 / X_1_3) * -Y_1_3) + Y_1_3

                print(Y_1_1, X_1_1, Y_1_2, X_1_2, Y_1_3, X_1_3)

                pg.draw.aaline(sc, GREEN, [0, y11], [600, y12], 1)
                pg.draw.aaline(sc, GREEN, [0, y21], [600, y22], 1)
                pg.draw.aaline(sc, GREEN, [0, y31], [600, y32], 1)

                pg.display.update()

    pg.time.delay(20)