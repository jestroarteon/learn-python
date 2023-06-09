from tkinter import *
from random import randint
from time import sleep,time
from math import sqrt

HEIGHT = 500
WIDTH = 800

window = Tk()
window.title('Bubble blaster')

c = Canvas(window, width=WIDTH, height=HEIGHT, bg="darkblue")
c.pack()

ship_id = c.create_polygon(5,5,5,25,30,15, fill="red")
ship_id2 = c.create_oval(0,0,30,30, outline="red")
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)

SHIP_SPD = 10
def move_ship(event):
    if event.keysym == "Up":
        c.move(ship_id, 0, -SHIP_R)
        c.move(ship_id2, 0, -SHIP_R)
    if event.keysym == "Down":
        c.move(ship_id, 0, SHIP_R)
        c.move(ship_id2, 0, SHIP_R)
    if event.keysym == "Left":
        c.move(ship_id, -SHIP_R, 0)
        c.move(ship_id2, -SHIP_R, 0)
    if event.keysym == "Right":
        c.move(ship_id, SHIP_R, 0)
        c.move(ship_id2, SHIP_R, 0)
c.bind_all('<Key>', move_ship)

bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100

def create_bubble():
    x = WIDTH + GAP
    y = randint(0,HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x-r,y-r,x+r,y+r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1,MAX_BUB_SPD))
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)

def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x,y

def del_bubbles(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i] 

def clean_up_bubs():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubbles(i)

def distanse(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x2)**2 + (y2 - y1**2))

def collission():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distanse(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += bub_r([bub] + bub_speed[bub])
            del_bubbles(bub)
        return points

BUB_CHANGE = 10
score = 0
while True:
    if randint(1, BUB_CHANGE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collission()
    print(score)
    window.update()
    sleep(0.1)

window.mainloop()