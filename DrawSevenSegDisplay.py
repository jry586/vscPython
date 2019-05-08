#DrawSevenSegDisplay.py
import turtle,datetime,time
def drawLine(draw):
    turtle.penup()
    turtle.fd(5)
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(30)
    turtle.penup()
    turtle.fd(5)
    turtle.right(90)
def drawSeg(d,numlist):
    drawLine(True) if d in numlist else drawLine(False)
def drawDigit(d):
    drawSeg(d,[2,3,4,5,6,8,9,])
    drawSeg(d,[0,1,3,4,5,6,7,8,9])
    drawSeg(d,[0,2,3,5,6,8,9])
    drawSeg(d,[0,2,6,8])
    turtle.left(90)
    drawSeg(d,[0,4,5,6,8,9])
    drawSeg(d,[0,2,3,5,6,7,8,9])
    drawSeg(d,[0,1,2,3,4,7,8,9])
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawPoint():
    turtle.fd(-10)
    turtle.right(90)
    turtle.fd(40)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(1)
    turtle.penup()
    turtle.left(90)
    turtle.fd(40)
    turtle.right(90)
    turtle.fd(10)
def drawDate(date):
    if date.isnumeric():
        year = date[:4]
        month = date[4:6]
        day = date[6:8]
        turtle.pencolor("red")
        for d in year:
            drawDigit(eval(d))
        drawPoint()
        turtle.pencolor("green")
        for d in month:
            drawDigit(eval(d))
        drawPoint()
        turtle.pencolor("blue")
        for d in day:
            drawDigit(eval(d))
    else:
        turtle.pencolor("red")
        n=0
        colorStr=["green","blue"]
        colorNum=0
        date.strip(" ")
        for d in date:
            if d.isnumeric():
                drawDigit(eval(d))
            else:
                '''
                if n==4:
                    turtle.write("年",font=("Arial",28,"normal"))
                    turtle.pencolor("green")
                elif n==7:
                    turtle.write("月",font=("Arial",28,"normal"))
                    turtle.pencolor("blue")
                elif n==10:
                    turtle.write("日",font=("Arial",28,"normal"))
                '''
                turtle.write(d,font=("Arial",28,"normal"))
                turtle.fd(60)
                turtle.color(colorStr[colorNum%2])
                colorNum+=1
            n+=1
                
                

def main():
    turtle.setup(1300,350)
    turtle.penup()
    turtle.speed(0)
    turtle.Turtle().screen.delay(0)
    turtle.fd(-620)
    startpos=turtle.position()
    turtle.pensize(5)
    while True:
        drawDate("{0:%Y}年{0:%m}月{0:%d}日 {0:%H}时{0:%M}分{0:%S}秒".format(datetime.datetime.now()))
        #drawDate(datetime.datetime.now().strftime("%Y%m%d"))
        turtle.hideturtle()
        time.sleep(1)
        turtle.goto(startpos)
        turtle.clear()
    #turtle.done()
main()
