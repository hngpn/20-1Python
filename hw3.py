# 과제3 2062008 김경민

# 문제1: List 요소 합 구하기
print('\n', '문제1: List 요소 합 구하기')
def find_sum(List_a):
    sum = 0
    for b in List_a:
        sum = sum + b
    return sum

List_a = [3, 76, 44, 24, 5, 38, 64, 21]
sum_num = find_sum(List_a)
print('sum number =', sum_num)

# 문제2: while 반복문, 함수 계산기
print('\n', '문제2: while 반복문, 함수 계산기')
def add_func(a, b):
    return a + b

def minus_func(a, b):
    return a - b

def mult_func(a, b):
    return a * b

def divide_func(a, b):
    return a / b

import random
while 1:
    a = random.randint (1,100)
    b = random.randint (1,100)
    
    print('\n', 'Enter + or - or * or / or q: ')
    cmd = input()
    
    if cmd == '+':
        print('a =', a, 'b =', b, 'a+b =', add_func(a, b))
    elif cmd == '-':
        print('a =', a, 'b =', b, 'a-b =', minus_func(a, b))
    elif cmd == '*':
        print('a =', a, 'b =', b, 'a*b =', mult_func(a, b))
    elif cmd == '/':
        print('a =', a, 'b =', b, 'a/b =', divide_func(a, b))
    elif cmd == 'q':
        break
    else:
        print('Only enter +, -, *, /, q')

# 문제3: factorial n개 구하기
print('\n', '문제3: factorial n개 구하기')
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def func_2(n):
    for i in range (1, n+1):
        print(i, '!=', fact(i))
    return

n = int(input('Enter a number: '))
func_2(n)



