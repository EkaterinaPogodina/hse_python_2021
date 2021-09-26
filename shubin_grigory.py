def when(peer):
    beer = 0
    while peer != 0:
        if peer % 2 == 0:
            peer = peer / 2
        else:
            peer = peer - 1
        beer += 1
    return beer


fun = int(input())
print(when(fun))