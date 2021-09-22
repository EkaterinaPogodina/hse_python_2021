used = [[False] * 8 for i in range(8)]
ok = True
for i in range(8):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if used[x][y]:
        ok = False
    used[x][y] = True
    route = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    for j in range(4):
        it = 1
        while (x + route[j][0] * it < 8) and (x + route[j][0] * it >= 0) and \
              (y + route[j][1] * it < 8) and (y + route[j][1] * it >= 0):
            posx = x + route[j][0] * it
            posy = y + route[j][1] * it
            if used[posx][posy]:
                ok = False
            it += 1
    for j in range(8):
        if (used[j][y] and x != j) or (used[x][j] and y != j):
            ok = False
if ok:
    print("NO")
else:
    print("YES")
