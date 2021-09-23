def change_digit(number, dig_num):
    if number // 10**dig_num - number // 10**(dig_num + 1) * 10 == 6:
        number += 3 * 10**dig_num

    elif number // 10 ** dig_num - number // 10 ** (dig_num + 1) * 10 == 9:
        number -= 3 * 10 ** dig_num

    return number


def max_69_number(input_number):
    ans = input_number
    for i in range(5):
        ans = max(ans, change_digit(input_number, i - 1))
    return ans


num = int(input())
print(max_69_number(num))
