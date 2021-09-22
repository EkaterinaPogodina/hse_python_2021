import random, time
import matplotlib.pyplot as plt

'''Основная часть с анализом строк'''
first_program_times = []
second_program_times = []
for i in range(1, 100010, 1000):
    print(i)
    first_program_time = 0
    second_program_time = 0
    array_of_strings = []
    for j in range(i):
        string = str(random.randint(0, 9))
        array_of_strings.append(string)
    # print(array_of_strings[:5])
    '''1-я програма'''
    start = time.time()
    all_strings = ''

    # print(array_of_strings)
    for j in range(len(array_of_strings)):
        all_strings += array_of_strings[j]
    ans = max(all_strings, key=all_strings.count)
    end = time.time()
    first_program_time += end - start
    '''2-я программа'''
    start = time.time()
    dict_of_elements = {}
    for j in range(len(array_of_strings)):
        for k in array_of_strings[j]:
            if k in dict_of_elements:
                dict_of_elements[k] += 1
            else:
                dict_of_elements[k] = 1
    ans_ = max(dict_of_elements, key=dict_of_elements.get)
    end = time.time()
    second_program_time += end - start
    '''Завершение 2-й программы'''
    # print(ans, ans_)
    if ans != ans_:
        print("Что-то не так")
    # print(first_program_time, second_program_time)
    first_program_times.append(first_program_time)
    second_program_times.append(second_program_time)
'''Конец основной части'''

# print(first_program_times)
# print(second_program_times)
plt.title('Сравнение двух алгоритмов', fontsize=20)
plt.plot(
    first_program_times,
    label='Время работы тупой программы'
)
plt.plot(
    second_program_times,
    label='Время работы умной программы'
)
plt.xlabel('Номер теста')
plt.ylabel('Время работы')
plt.grid(True)
plt.legend(
    loc='upper left',
    borderaxespad=4
)
plt.show()
