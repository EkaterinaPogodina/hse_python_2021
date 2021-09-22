import random
import matplotlib.pyplot as plt
import numpy as np
import time


def gen(tests):
    cur_len_test = 1
    for i in range(100):
        for j in range(cur_len_test):
            tests[i].append(str(random.randint(1, 100000)))
        cur_len_test += 1000


def stupid(test):
    best_cnt = None
    best_sym = ""
    prev_symbols = ""
    cnt_symbols = []
    for i in range(len(test)):
        for j in range(len(test[i])):
            if test[i][j] not in prev_symbols:
                prev_symbols += test[i][j]
                cnt_symbols.append(1)
            else:
                for x in range(len(prev_symbols)):
                    if prev_symbols[x] == test[i][j]:
                        cnt_symbols[x] += 1
    for i in range(len(cnt_symbols)):
        if (best_cnt is None) or (cnt_symbols[i] > best_cnt) or \
           (cnt_symbols[i] == best_cnt) and (prev_symbols[i] < best_sym):
            best_cnt = cnt_symbols[i]
            best_sym = prev_symbols[i]
    return best_sym


def smart(test):
    sym_cnt = dict()
    for i in range(len(test)):
        for j in range(len(test[i])):
            if test[i][j] not in sym_cnt:
                sym_cnt[test[i][j]] = 1
            else:
                sym_cnt[test[i][j]] += 1
    answer = sorted(list(sym_cnt.items()), key=lambda x: (-x[1], x[0]))
    return answer[0][0]

print(smart(['1', '12', '1222']))
# tests = [[] for i in range(100)]
# gen(tests)
# time_stupid = []
# time_smart = []
# for i in range(len(tests)):
#     start = time.time()
#     res_stupid = stupid(tests[i])
#     end = time.time()
#     time_stupid.append(end - start)
#     start = time.time()
#     res_smart = smart(tests[i])
#     end = time.time()
#     time_smart.append(end - start)
#     print("Test case #", i + 1, "res_stupid:", res_stupid, "res_smart:", \
#           res_smart, "ok" if res_stupid == res_smart else "wa")
#
# #строим графики
# x = range(100)
# y1 = time_stupid
# y2 = time_smart
# fig = plt.figure(figsize=(16, 9))
# plt.title('Сравение решения без dict с решением с dict', fontsize=20)
# plt.plot(x, y1, color='red', linewidth=3, label='Решение без словаря')
# plt.plot(x, y2, color='green', linewidth=3, label='Решение со словарем')
# plt.legend(loc='best')
# plt.xlabel('$Номер\,теста$')
# plt.ylabel('$Время\,работы\,в\,секундах$')
# plt.show()
