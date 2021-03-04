#과제1 2062008 김경민

#문제 1
import random
a = random.randint (1,100)
b = random.randint (1,100)
op = input('Enter an operator (Choose from +, -, *, /): ')
if op == '+':
    print('a =', a, ',', '', 'b =', b, ',', '', 'a + b =', int(a) + int(b))
elif op == '-':
    print('a =', a, ',', '', 'b =', b, ',', '', 'a - b =', int(a) - int(b))
elif op == '*':
    print('a =', a, ',', '', 'b =', b, ',', '', 'a * b =', int(a) * int(b))
elif op == '/':
    print('a =', a, ',', '', 'b =', b, ',', '', 'a / b =', int(a) / int(b))
else:
    print('Incorrect command entered')

#문제 2
a = 0b00001111
b = 0b10101010
a = a << 4
b = b >> 4
c = a ^ b
d = c & 0b01010101
print('', bin(a), '\n', bin(b), '\n', bin(c), '\n', bin(d))

#문제 3
a = input('Enter a number for "a": ')
b = input('Enter a number for "b": ')
x = int(a) - int(b)
if int(x) == 0:
    print('a - b =', x, ',', '', 'a - b는 0 입니다')
elif int(x) > 0:
    if int(x) % 2 == 0:
        print('a - b =', x, ',', '', 'a - b는 짝수, 양수입니다')
    elif int(x) % 2 == 1:
        print('a - b =', x, ',', '', 'a - b는 홀수, 양수입니다')
elif int(x) < 0:
    if int(x) % 2 == 0:
        print('a - b =', x, ',', '', 'a - b는 짝수, 음수입니다')
    elif -int(x) % 2 == 1:
        print('a - b =', x, ',', '', 'a - b는 홀수, 음수입니다') 
