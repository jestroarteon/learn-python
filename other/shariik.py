from tkinter import *
import random

CLIKtheBALL = Tk()
CLIKtheBALL.geometry("500x500")

canvas = Canvas(width=450, height=450, relief=SOLID, bd=1, bg="white")
canvas.pack(expand=True)
points = 0
score = canvas.create_text(10, 20, anchor=W, font="Arial 24", text=points)

def new_ball():
    global after_id
    global ball
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    side = 50
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = f'#{red:02x}{green:02x}{blue:02x}'
    ball = canvas.create_oval(x,y, x+side, y+side, fill=color)
    after_id = canvas.after(1000, lose)
def click(event):
    global after_id
    global points
    if ball in canvas.find_overlapping(event.x, event.y, event.x, event.y):
        canvas.after_cancel(after_id)
        points += 1
        canvas.itemconfig(score, text=points)
        canvas.delete(ball)
        new_ball()
    else:
        points -= 1
        canvas.itemconfig(score, text=points)
def lose():
    global after_id
    global points
    canvas.delete(ball)
    points -= 1
    canvas.itemconfig(score, text=points)
    new_ball()

canvas.bind('<Button-1>', click)
new_ball()

canvas.mainloop()