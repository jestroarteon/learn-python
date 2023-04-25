from tkinter import *

window = Tk()
window.geometry("450x350")


choise = StringVar()

vibor = LabelFrame(text="vibor shrifta")
vibor.pack(fill=X)
tsezar = Radiobutton(vibor, text="Tsezar", value="code of tsezar", variable=choise, indicatoron=0)
atbash = Radiobutton(vibor, text="Atbash", value="code of atbash", variable=choise, indicatoron=0)
tsezar.grid(column=0, row=0)
atbash.grid(column=0, row=1)

labelframe1 = LabelFrame(text="data")
labeltext = Label(labelframe1, text="enter text:")
labeltext2 = Label(labelframe1, text="enter key:")
plaintextbox = Entry(labelframe1,bg="white", width=7)
keybox = Entry(labelframe1,bg="white", width=4)

labelframe2 = LabelFrame(text="ecrypted message")
label2text = Label(labelframe2, text="code of tsezar")
label3text = Label(labelframe2, text=" ")
#AtbashLabel = Label(labelframe2, text="atbash")
#atbashlabel = Label(labelframe2, text=" ")

buton = Button(text='incrypt')


labelframe1.pack(fill=X)
labeltext.grid(column=0, row=0, padx=50, pady=20)
labeltext2.grid(column=1, row=0, padx=50, pady=20)
plaintextbox.grid(column=0, row=2, padx=20)
keybox.grid(column=1, row=2, padx=20)

labelframe2.pack(fill=X)
label2text.grid(column=0, row=0, padx=150)
label3text.grid(column=0, row=1, padx=150)
#AtbashLabel.grid(column=0, row=2)
#atbashlabel.grid(column=0, row=3)

buton.pack(pady=30)

if __name__ == "__main__":
    window.mainloop()
