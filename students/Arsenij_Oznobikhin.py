def solution(numbers):
    cnt = 0
    for number in numbers:
        cnt += (numbers.count(number) - 1)
    return cnt // 2
