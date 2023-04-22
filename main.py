import pygame as pg
import random


class FPS:
    def __init__(self, num: int):
        self.num = num

    def update(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.num = self.num - 1
        if keystate[pg.K_RIGHT]:
            self.num = self.num + 1



W, H = 800, 800
fps = FPS(60)
# ширина высота количество кадров в секунду
SIZE = (W, H)
# размер экрана
clock = pg.time.Clock()
# переменная которая отвечает за FPS
pg.init()
# необходимо
win = pg.display.set_mode(SIZE)


# создание экрана
class Circles:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad
        # радиус
        self.dx = random.choice([10])
        # random choice - вибирает из списка рандомый элемент
        self.dy = random.choice([10])
        self.color = random.choices(range(0, 256), k=3)

    def move(self):
        
        # движение объекта
        self.x += self.dx
        self.y += self.dy
        if self.x > W or self.x < 0:
            self.dx = -self.dx + random.randint(-1, 1)
        if self.y > H or self.y < 0:
            self.dy = -self.dy + random.randint(-1, 1)

    def show(self):
        pg.draw.circle(win, self.color, (self.x, self.y), self.rad)


circles = []
for i in range(100):
    circles.append(Circles(W // 2, H // 2, 50))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    # выход

    for circle in circles:
        circle.move()

    # заставляет каждый круг двигаться
    win.fill('white')

    for circle in circles:
        circle.show()

    fps.update()
    pg.display.flip()
    pg.display.update()
    clock.tick(fps.num)

# рендор экрана
