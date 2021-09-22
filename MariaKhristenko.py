def subtract_product_and_sum(n):
    product, summa = 1, 0
    for digit in str(n):
        product *= int(digit)
        summa += int(digit)
    return product - summa
