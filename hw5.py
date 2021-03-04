# 과제5 2062008 김경민

# 문제1: Graphic 계산기
print('\n', '문제1: Graphic 계산기')
import turtle as t
import random
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

def factorial_func(a):
    return math.factorial(a)

def sin_func(a):
    return math.sin(math.radians(a))

def cos_func(a):
    return math.cos(math.radians(a))

def tan_func(a):
    return math.tan(math.radians(a))


def draw_cmd_area():
    t.forward(200);     t.right(90);     t.forward(50);     t.right(90)
    t.forward(200);     t.right(90);     t.forward(50);     t.right(90)


def draw_menu():    
    xcor=-400;      ycor=-250
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('ADD')
    xcor=xcor+200
    
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('SUB')
    xcor=xcor+200

    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('MULT')
    xcor=xcor+200
    
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('DIV')


    xcor=-400;      ycor=-300
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('POWER')
    xcor=xcor+200
    
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('LOG10')
    xcor=xcor+200

    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('FACTORIAL')
    xcor=xcor+200
    
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('SIN')

    
    xcor=-400;      ycor=-350
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('COS')
    xcor=xcor+200
    
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('TAN')
    xcor=xcor+200

    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('QUIT_CALC')
    xcor=xcor+200
    
    t.penup();       t.goto(xcor,ycor);       t.pendown();      draw_cmd_area()
    t.penup();       t.goto(xcor+20,ycor-20); t.pendown();      t.write('CLEAR')


def draw_pos(x,y):
    a = random.randint (1,100)
    b = random.randint (1,100)
    
    if (y>=-300) and (y<=-250):
        if (x>=-400) and (x<-200):
            print('\n', 'a =', a, 'b =', b, 'a+b =', add_func(a, b))
        elif (x>=-200) and (x<0):
            print('\n', 'a =', a, 'b =', b, 'a-b =', minus_func(a, b))
        elif (x>=0) and (x<200):
            print('\n', 'a =', a, 'b =', b, 'a*b =', mult_func(a, b))
        elif (x>=200) and (x<400):
            print('\n', 'a =', a, 'b =', b, 'a/b =', divide_func(a, b))

    elif (y>=-350) and (y<=-300):
        if (x>=-400) and (x<-200):
            print('\n', 'a =', a, 'b =', b, 'power(a,b) =', power_func(a,b))
        elif (x>=-200) and (x<0):
            print('\n', 'a =', a, 'log10(a) =', log_func(a))
        elif (x>=0) and (x<200):
            print('\n', 'a =', a, 'factorial(a) =', factorial_func(a))
        elif (x>=200) and (x<400):
            print('\n', 'a =', a, 'sin(a) =', sin_func(a))
    
    elif (y>=-400) and (y<=-350):
        if (x>=-400) and (x<-200):
            print('\n', 'a =', a, 'cos(a) =', cos_func(a))
        elif (x>=-200) and (x<0):
            print('\n', 'a =', a, 'tan(a) =', tan_func(a))
        elif (x>=0) and (x<200):
            quit()
        elif (x>=200) and (x<400):
            screen_clear(x,y)
    else:
        print('\n', 'Enter a command from the menu area')
            

def screen_clear(x,y):
    t.clear()
    draw_menu()

t.setup(800,800)
t.speed(0)
t.hideturtle()
draw_menu()
s=t.Screen()
s.onscreenclick(draw_pos, 1)
s.onscreenclick(screen_clear, 3)
