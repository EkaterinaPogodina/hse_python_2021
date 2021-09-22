#!/usr/bin/env python
# coding: utf-8

# In[5]:


def check(number):
    flag = True
    copy_of_number = number
    while number > 0:
        digit = number % 10
        if digit == 0 or copy_of_number % digit != 0:
            flag = False
            break
        number //= 10
    return flag


def calculate_answer(left, right):
    answer = []
    for number in range(left, right + 1):
        if check(number):
            answer.append(number)
    return answer


# In[9]:


left, right = [int(element) for element in input().split()]
print(calculate_answer(left, right))

