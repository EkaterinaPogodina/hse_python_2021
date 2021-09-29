def how(hour):
    beer = 0
    while hour != 0:
        if hour % 2 == 0:
            hour = hour / 2
        else:
            hour = hour - 1
        beer += 1
    return beer
