import time
import turtle

time_line = 15
while (time_line) > 0:

    time.sleep(0.5)
    print(time_line)

    disp = turtle.Screen()

    turtle_ins = turtle.Turtle()

    turtle_ins.hideturtle()
    turtle_ins.pencolor("blue")
    turtle_ins.write(time_line, font=("Arial", 14, "normal"))
    time.sleep(0.5)


    time_line -= 1
    turtle_ins.clear()
    if time_line == 0:
        turtle_ins.write("Game Over", font=("Arial", 14, "normal"))

turtle.done()
