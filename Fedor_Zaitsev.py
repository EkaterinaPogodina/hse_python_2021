def max_69_number(num):
    ans = num
    for i in range(4):
        new_num = num // 10**(i + 1) * 10**(i + 1) + 9 * 10**i + num % 10**i
        ans = max(ans, new_num)
    return ans
