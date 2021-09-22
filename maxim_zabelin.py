def isSelfD(num):
    num_s = str(num)
    for char in num_s:
        char = int(char)
        if char == 0:
            return False
        if num % char != 0:
            return False
    return True


s = input().split(',')
for i in range(len(s)):
    s[i] = int(s[i].split()[2])


res = []
for n in range(s[0], s[1] + 1):
    if isSelfD(n):
        res.append(n)

print(res)
