import time
import turtle

time_line = 10
while (time_line) > 0:

    time.sleep(1)
    print(time_line)

    disp = turtle.Screen()
    turtle_ins = turtle.Turtle()
    turtle_ins.hideturtle()
    turtle_ins.write(time_line, font=("Arial", 14, "normal"))
    time.sleep(0.5)
    turtle_ins.clear()

    time_line -= 1

    if time_line == 0:
        turtle_ins.write("Game Over", font=("Arial", 14, "normal"))

turtle.done()