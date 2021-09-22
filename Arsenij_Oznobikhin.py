def solution(*args):
    cnt = 0
    numbers = list(*args)
    for number in numbers:
        cnt += (numbers.count(number) - 1)
    return cnt // 2


