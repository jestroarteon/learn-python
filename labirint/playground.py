from tkinter import *
from levels import level1

window = Tk()
window.geometry("470x470")

canvas = Canvas(height=450, width=450, relief=SOLID, bg="white")
canvas.pack(expand=True)

walls = []
doors = []
keys = []
exits = []
players = []
secrets = []

def create_level(level):
    walls.clear()
    doors.clear()
    keys.clear()
    exits.clear()
    players.clear()
    x = 0
    y = 0
    side = 25
    for line in level:
        for block in line:
            if block == "W":
                wall = canvas.create_rectangle(x, y, x + side, y + side, fill="black", outline="black")
                walls.append(wall)
            if block == "S":
                secret = canvas.create_rectangle(x, y, x + side, y + side, fill="black", outline="black")
                secrets.append(secret)
            if block == "K":
                key = canvas.create_rectangle(x, y, x + side, y + side, fill="yellow", outline="yellow")
                keys.append(key)
            if block == "D":
                door = canvas.create_rectangle(x, y, x + side, y + side, fill="red", outline="red")
                doors.append(door)
            if block == "E":
                exit = canvas.create_rectangle(x, y, x + side, y + side, fill="orange", outline="orange")
                exits.append(exit)
            if block == "P":
                player = canvas.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, fill="blue", outline="blue")
                players.append(player)
            x += side
        x = 0
        y += side


if __name__ == "__main__":
    create_level(level1)
    window.mainloop()