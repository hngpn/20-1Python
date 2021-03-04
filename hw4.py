# 과제4 2062008 김경민

# 문제1: List에 저장된 단어 순서 반대로 하기
print('\n', '문제1: List에 저장된 단어 순서 반대로 하기')
a = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
b = []
print('list a =', a)
for i in range(7):
    c=a.pop()
    b.append(c)
print('reversed list a =', b)

# 문제2: List에 저장된 단어 정렬하기
print('\n', '문제2: List에 저장된 단어 정렬하기')
a = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
print('list a =', a)
for passnum in range(len(a)-1,0,-1):
    for i in range(passnum):
        if a[i]>a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print('sorted list a =', a)

# 문제3: while 반복문, 함수 계산기
print('\n', '문제3: while 반복문, 함수 계산기')
import math

def add_func(a, b):
    return a + b

def minus_func(a, b):
    return a - b

def mult_func(a, b):
    return a * b

def divide_func(a, b):
    return a / b

def power_func(a,b):
    return math.pow(a, b)

def log_func(a):
    return math.log10(a)

def sqrt_func(a):
    return math.sqrt(a)

def factorial_func(a):
    return math.factorial(a)

def sin_func(a):
    return math.sin(math.radians(a))

def cos_func(a):
    return math.cos(math.radians(a))

def tan_func(a):
    return math.tan(math.radians(a))

import random
while 1:
    a = random.randint (1,100)
    b = random.randint (1,100)
    
    print('\n', 'Enter +, -, *, /, p, l, sq, f, s, c, t, q : ')
    cmd = input()
    
    if cmd == '+':
        print('a =', a, 'b =', b, 'a+b =', add_func(a, b))
    elif cmd == '-':
        print('a =', a, 'b =', b, 'a-b =', minus_func(a, b))
    elif cmd == '*':
        print('a =', a, 'b =', b, 'a*b =', mult_func(a, b))
    elif cmd == '/':
        print('a =', a, 'b =', b, 'a/b =', divide_func(a, b))
    elif cmd == 'p':
        print('a =', a, 'b =', b, 'power(a,b) =', power_func(a,b))
    elif cmd == 'l':
        print('a =', a, 'log10(a) =', log_func(a))
    elif cmd == 'sq':
        print('a =', a, 'sqrt(a) =', sqrt_func(a))
    elif cmd == 'f':
        print('a =', a, 'factorial(a) =', factorial_func(a))
    elif cmd == 's':
        print('a =', a, 'sin(a) =', sin_func(a))
    elif cmd == 'c':
        print('a =', a, 'cos(a) =', cos_func(a))
    elif cmd == 't':
        print('a =', a, 'tan(a) =', tan_func(a))
    elif cmd == 'q':
        break
    else:
        print('Only enter +, -, *, /, p, l, sq, f, s, c, t, q')
