import random


def f(x):
    return x ** 3 - 4 * x ** 2 + 2 * x


def grad(x):
    return 3 * x ** 2 - 8 * x + 2


def next_x(x, l):
    return x - l * grad(x)


def downhill(x, e):
    a = 0
    b = 4
    l = 0.3
    while abs(f(x) - f(next_x(x, l))) > e:
        x = next_x(x, l)
        if x < a:
            x = a
        if x > b:
            x = b
    return x


def monte_carlo(a, b):
    mi = random.randint(a, b)
    for i in range(100):
        c = random.randint(a, b)
        if f(c) < f(mi):
            mi = c
    return mi

print downhill(monte_carlo(0, 4), 0.0005)
print f(downhill(monte_carlo(0, 4), 0.0005))