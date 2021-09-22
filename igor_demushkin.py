def f(x):
    global steps
    steps += 1
    if x == 0:
        return
    elif x % 2 == 0:
        return f(x // 2)
    return f(x - 1)


steps = 0
f(int(input()))
print(steps - 1)
