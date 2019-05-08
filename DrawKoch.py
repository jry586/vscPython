#DrawKoch.py

import turtle

def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    #level=eval(input("请输入雪花的递归层次："))
    level=5
    turtle.setup(800,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,150)
    turtle.pendown()
    koch(400,level)
    turtle.left(-120)
    koch(400,level)
    turtle.left(-120)
    koch(400,level)
    turtle.hideturtle()
    turtle.done()

main()
