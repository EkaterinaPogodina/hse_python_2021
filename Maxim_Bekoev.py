def TaskOne(array):
    product = 1
    for el in array: product *= el
    if product > 0:
        return 1
    if product < 0:
        return -1
    return 0
