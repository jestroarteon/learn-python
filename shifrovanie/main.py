import interface
from ciphers import caesar_encrypt,atbash_encrypt

def change_chifer():
    global currentchifer
    currentchifer = interface.choise.get()
    interface.label2text.config(text=currentchifer)
    if currentchifer == "code of atbash":
        interface.keybox.config(state="disabled")
    if currentchifer == "code of tsezar":
        interface.keybox.config(state="normal")

def encrypt():
    global currentchifer
    if currentchifer == "code of tsezar":
        plaintext = interface.plaintextbox.get()
        key = int(interface.keybox.get())
        message = caesar_encrypt(plaintext,key)
        interface.label3text.config(text=message)
    elif currentchifer == "code of atbash":
        plaintext = interface.plaintextbox.get()
        message1 = atbash_encrypt(plaintext)
        interface.label3text.config(text=message1)
    

interface.tsezar.config(command=change_chifer)
interface.atbash.config(command=change_chifer)

interface.buton.config(command=encrypt)
interface.window.mainloop()