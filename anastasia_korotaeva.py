def maximum_69_number(num):
    str_num = str(num)
    if "6" in str_num:
        for i in range(len(str_num)):
            if str_num[i] == "6":
                power = len(str_num) - 1 - i
                num = num + (10 ** power) * 3
                break
    return num
