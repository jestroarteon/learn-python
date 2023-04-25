from tkinter import *
from tkinter import messagebox
from random import shuffle  

root = Tk()
root.geometry('900x700+300+200')

questions = [['Как заканчивается присказка: "Мы и сами с..."?', 'с волосами', 'с усами','с часами', 'с долгами', 'с усами'],
['Как в обиходе называют растение, которое часто \n дарят женщинам к празднику 8 марта?', 'оливье', 'винегрет', 'мимоза', 'селёдка под шубой', 'мимоза'],
['На каком курсе школы Хогвартс учился Гарри Поттер,\n когда раскрыл секрет Тайной комнаты?', 'на первом', 'на втором', 'на третьем', 'на четвёртом','на втором']]

numQue = 0
btns = questions[numQue][1:5]
shuffle(btns)

pic = PhotoImage(file='.\milioner\logo.gif')
picle = Label(root, image=pic)

queL = Label(root, text=questions[numQue][0], font='Verdana 22')
btn1 = Button()