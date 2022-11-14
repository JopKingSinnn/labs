from scipy.optimize import curve_fit
from numpy import array, exp
import matplotlib.pyplot as plt
from tabulate import tabulate

y = array([0.398, 0.328, 0.264, 0.211, 0.172, 0.14, 0.093])
x = array([0.2053, 0.1684, 0.1355, 0.1078, 0.0876, 0.0715, 0.0615])


def mapping1(x, a, b):
    return a * x + b


args, covar = curve_fit(mapping1, x, y)
a, b = args[0], args[1]
y_fit1 = a * x + b

plt.plot(x, y_fit1)
plt.scatter(x, y)

plt.plot(x, y, 'bo', label=" - построенные точки")
plt.plot(x, y_fit1, label="V = a * t + b")
plt.xlabel('t, с')
plt.ylabel('x, м')
plt.legend(loc = 'best', fancybox = True, shadow = True)
plt.grid(True)
plt.show()
 # Источник: https://pythonpip.ru/examples/podgonka-krivoy-v-python-s-pomoschyu-biblioteki-scipy

def k(x, y):
    s_xy = 0
    s_x2 = 0
    s_y2 = 0
    for i in range(len(a)):
        s_xy += x[i] * y[i]
        s_x2 += x[i] ** 2
        s_y2 += x[i] ** 2
    k = s_xy / s_x2
    sigma_k = ((s_y2 / s_x2 - k ** 2) ** (0.5))/(len(x)**(0.5))
    return [k, sigma_k]

def ab(x, y):
    s_xy = 0
    s_x2 = 0
    s_y2 = 0
    s_x = 0
    s_y = 0
    n = len(x)
    for i in range(n):
        s_xy += x[i] * y[i]
        s_x2 += x[i] ** 2
        s_y2 += y[i] ** 2
        s_x += x[i]
        s_y += y[i]
    c_xy = s_xy / n
    c_x2 = s_x2 / n
    c_y2 = s_y2 / n
    c_x = s_x / n
    c_y = s_y / n
    a = (c_xy - c_x * c_y) / (c_x2 - c_x ** 2)
    sigma_a = (((c_y2 - c_y ** 2)/(c_x2 - c_x ** 2)) ** (0.5)) / (n ** (0.5))
    b = c_y - a * c_x
    sigma_b = sigma_a * (c_x2 - c_x ** 2) ** (0.5)
    return [[a, sigma_a], [b, sigma_b]]
print("a, b и их погрешности", ab(x, y))


# print(tabulate([[2, 5, 5, 5], [5, 5, 5, 5]], tablefmt='latex'))
