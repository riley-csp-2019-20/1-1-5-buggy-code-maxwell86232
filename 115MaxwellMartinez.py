#   a115_buggy_image.py

# import turtle
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 6
length = 70
spacing = 380 / legs
spider.pensize(5)
start = -2
while (start < legs):
  spider.goto(0,0)
  spider.setheading(spacing*start)
  spider.forward(length)
  start = start + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()