'''
#KochDrawV1.py
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1)
def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600,3)     # 0阶科赫曲线长度，阶数
    turtle.hideturtle()
main()
'''

#KochDrawV2.py
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3      # 3阶科赫雪花，阶数
    koch(400,level)     
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()
