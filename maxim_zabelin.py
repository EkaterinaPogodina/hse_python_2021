def isSelfD(left, right):
    res = []
    for num in range(left, right + 1):
        num_s = str(num)
        key = True
        for char in num_s:
            char = int(char)

            if char == 0:
                key = False
            elif num % char != 0:
                key = False
        if key:
            res.append(num)
    return res
