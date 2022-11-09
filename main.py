# from scipy.optimize import curve_fit
# from numpy import array, exp
# import matplotlib.pyplot as plt
# from tabulate import tabulate
# 
# y = array([0.398, 0.328, 0.264, 0.211, 0.172, 0.14, 0.093])
# x = array([0.2053, 0.1684, 0.1355, 0.1078, 0.0876, 0.0715, 0.0615])
#
#
# def mapping1(x, a, b):
#     return a * x + b
#
#
# args, covar = curve_fit(mapping1, x, y)
# a, b = args[0], args[1]
# y_fit1 = a * x + b
#
# plt.plot(x, y_fit1)
# plt.scatter(x, y)
#
# # plt.plot(x, y, 'bo', label=" - построенные точки")
# # plt.plot(x, y_fit1, label="V = a * t + b")
# plt.xlabel('t, с')
# plt.ylabel('x, м')
# plt.legend(loc = 'best', fancybox = True, shadow = True)
# plt.grid(True)
# plt.show()
# #  # Источник: https://pythonpip.ru/examples/podgonka-krivoy-v-python-s-pomoschyu-biblioteki-scipy
# #
# def k(x, y):
#     s_xy = 0
#     s_x2 = 0
#     s_y2 = 0
#     for i in range(len(a)):
#         s_xy += x[i] * y[i]
#         s_x2 += x[i] ** 2
#         s_y2 += x[i] ** 2
#     k = s_xy / s_x2
#     sigma_k = ((s_y2 / s_x2 - k ** 2) ** (0.5))/(len(x)**(0.5))
#     return [k, sigma_k]
#
# def ab(x, y):
#     s_xy = 0
#     s_x2 = 0
#     s_y2 = 0
#     s_x = 0
#     s_y = 0
#     n = len(x)
#     for i in range(n):
#         s_xy += x[i] * y[i]
#         s_x2 += x[i] ** 2
#         s_y2 += y[i] ** 2
#         s_x += x[i]
#         s_y += y[i]
#     c_xy = s_xy / n
#     c_x2 = s_x2 / n
#     c_y2 = s_y2 / n
#     c_x = s_x / n
#     c_y = s_y / n
#     a = (c_xy - c_x * c_y) / (c_x2 - c_x ** 2)
#     sigma_a = (((c_y2 - c_y ** 2)/(c_x2 - c_x ** 2)) ** (0.5)) / (n ** (0.5))
#     b = c_y - a * c_x
#     sigma_b = sigma_a * (c_x2 - c_x ** 2) ** (0.5)
#     return [[a, sigma_a], [b, sigma_b]]
# print("a, b и их погрешности", ab(x, y))


# print(tabulate([[2, 5, 5, 5], [5, 5, 5, 5]], tablefmt='latex'))

import math
from random import choice, randint
import pygame
FPS = 30
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WIDTH = 800
HEIGHT = 600
class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        self.y -= self.vy
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((b.x - target.x)**2 + (b.y - target.y)**2) < (target.r + b.r) ** 2:
            return True
class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
    def fire2_start(self, event):
        self.f2_on = 1
    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (20, 500),
            50
        )
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY
class Target:
    def __init__(self):
        """ Конструктор класса Target
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.points = 0
        self.live = 1
        self.new_target()
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(2, 50)
        color = self.color = RED
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
    def draw(self):
        # create a surface object, image is drawn on it.
        imp = pygame.draw.circle(screen,
            self.color,
            (self.x, self.y),
            self.r
        )
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
clock =pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False
while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    target.live = 1
    for b in balls:
        b.move()
        if hittest(b, target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()
pygame.quit()