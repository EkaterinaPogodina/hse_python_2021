def f(x, steps):
    steps += 1
    if x == 0:
        return steps
    elif x % 2 == 0:
        return f(x // 2, steps)
    return f(x - 1, steps)
