def change_digit(number, digit_num):
    if number // 10**digit_num - number // 10**(digit_num + 1) * 10 == 6:
        number += 3 * 10**digit_num

    if number // 10 ** digit_num - number // 10 ** (digit_num + 1) * 10 == 9:
        number += 3 * 10 ** digit_num

    return number


def max_69_number(input_number):
    ans = input_number
    for i in range(4):
        ans = max(ans, change_digit(input_number, i - 1))
    return ans

