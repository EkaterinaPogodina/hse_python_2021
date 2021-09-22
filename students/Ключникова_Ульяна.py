def check_if_self_dividing(number):
    try:
        digits = list(map(int, list(str(number))))
        for digit in digits:
            if number % digit != 0:
                return False
        return True
    except:  # some zeros probably or invalid input
        return False


def get_self_dividing_numbers(left, right):
    list_of_div_num = []
    for number in range(left, right + 1):
        if check_if_self_dividing(number):
            list_of_div_num.append(number)
    return list_of_div_num


if __name__ == "__main__":
    print(*get_self_dividing_numbers(1, 22))
    print(*get_self_dividing_numbers(47, 85))
