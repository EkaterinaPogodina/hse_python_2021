def countLargestGroup(n):
    summ = dict()
    for i in range(1, n + 1):
        s = 0
        while i > 0:
            s += i % 10
            i = i // 10
        summ[s] = summ.get(s, 0) + 1
    max_size = 0
    count = 0
    for i in summ.keys():
        if summ[i] > max_size:
            max_size = summ[i]
            count = 0
        if summ[i] == max_size:
            count += 1
    return count


