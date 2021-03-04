# 과제2 2062008 김경민

# 문제1: 0, 5 count 구하기
print('\n', '문제1: 0, 5 count 구하기')
a = [5, 0, 5, 0, 0, 4, 7, 1, 0, 5, 0, 0, 8]
count = 0
for i in range(13):
    if a[i] == 0 or a[i] == 5:
        count = count + 1
print('count =', count)

# 문제2: MInimum 구하기
print('\n', '문제2: MInimum 구하기')
alist = [3, 76, 44, 24, 5, 38, 64, 21, 1, 5, 7, 9]
m = a[0]
for i in alist:
    if i < m:
        m = i
print('Mininum number = ', m)


# 문제3: while 반복문 계산기
print('\n', '문제3: while 반복문 계산기')
import random
while 1:
    a = random.randint (1,100)
    b = random.randint (1,100)
    print('\n', 'Enter + or - or * or / or q: ')
    cmd = input()
    if cmd == '+':
        print('a =', a, ',', 'b =', b, ',', 'a+b =', a+b)
    elif cmd == '-':
        print('a =', a, ',', 'b =', b, ',', 'a-b =', a-b)
    elif cmd == '*':
        print('a =', a, ',', 'b =', b, ',', 'a*b =', a*b)
    elif cmd == '/':
        print('a =', a, ',', 'b =', b, ',', 'a/b =', a/b)
    elif cmd == 'q':
        break
    else:
        print('Only enter +, -, *, /, q')
        

