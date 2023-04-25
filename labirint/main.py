from levels import levels
from playground import window, canvas, create_level, players, walls, keys, doors, exits

currentLevel = 0
create_level(levels[currentLevel])

def playerMove(event):
    global currentLevel
    player = players[0]
    key = event.keysym
    x = 0
    y = 0
    if key == "Right":
        x = 25
    if key == "Left":
        x = -25
    if key == "Up":
        y = -25
    if key == "Down":
        y = 25
    canvas.move(player, x, y)
    for wall in walls:
        x1, x2, x3, x4 = canvas.coords(wall)
        if player in canvas.find_overlapping(x1, x2, x3, x4):
            canvas.move(player, -x, -y)
    for key in keys:
        x1, y1, x2, y2 = canvas.coords(key)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete(key)
            keys.remove(key)
            if len(keys) == 0:
                for door in doors:
                    canvas.itemconfig(door, fill='green', outline="green")
    for door in doors:
        x1, y1, x2, y2 = canvas.coords(door)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            if canvas.itemcget(door, 'fill') == 'red':
                canvas.move(player, -x, -y)
    for exit in exits:
        x1, y1, x2, y2 = canvas.coords(exit)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete("all")
            currentLevel += 1
            if currentLevel < len(levels):
                create_level(levels[currentLevel])
            else: 
                canvas.create_text(225,225,text="YOU WON THE GAME!", fill="green")
                return
            

canvas.bind_all('<Key>', playerMove)

window.mainloop()