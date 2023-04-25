from tkinter import *

okToPressReturn = True
bomb = 100
day = 0

def start(event):
    global okToPressReturn
    if okToPressReturn == False:
        pass
    else:
        startLabel.config(text="")
        updateBomb()
        updateDay()
        updateDisplay()

        okToPressReturn == False

def updateDisplay():
    global day, bomb



root = Tk()
root.title("Bomba")
root.geometry("500x500")

startLabel = Label(root, text="clik Enter, and game start!", font="Helvetica, 12")
bombLabel = Label(root, text="fitil:", font="Helvetica, 12")
dayLabel = Label(root, text="day:", font="Helvetica, 12")

noPhoto = PhotoImage(file="bomb_no.gif")
normalPhoto = PhotoImage(file="bomb_normal.gif")
bangPhoto = PhotoImage(file="bang.gif")

bomb_normal = Label(root, image=normalPhoto)

btn_no_bomb = Button(root, text="clik me!")


startLabel.pack()
bombLabel.pack()
dayLabel.pack()

bomb_normal.pack()
btn_no_bomb.pack()

root.bind('<Return>', start)

root.mainloop()