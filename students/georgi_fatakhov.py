def main(n):
    a = list(map(int, list(str(n))))
    pr = 1
    for i in a:
        pr *= i
    return pr - sum(a)
