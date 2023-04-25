alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
al = len(alphabet)

#pl = input("word: ")
#ke = int(input("key: "))

def caesar_encrypt(plaintext,key):
    cyphertext = ""
    plaintext = plaintext.lower() 
    for simbol in plaintext:
        if simbol == " ":
            cyphertext += " "
            continue
        index = alphabet.find(simbol)
        new_index = (index + key) % al
        new_letter = alphabet[new_index]
        cyphertext += new_letter
    return cyphertext

def caesar_crypt(plaintext,key):
    cyphertext = ""
    plaintext = plaintext.lower()
    for simbol in plaintext:
        if simbol == " ":
            cyphertext += " "
            continue
        index = alphabet1.find(simbol)
        new_index = (index - key) % al
        new_letter = alphabet1[new_index]
        cyphertext += new_letter
    return cyphertext

def caesar_vzlopt(plaintext,key):
    cyphertext = ""
    plaintext = plaintext.lower()
    for simbol in plaintext:
        if simbol == " ":
            cyphertext += " "
            continue
        index = alphabet1.find(simbol)
        new_index = (index - key) % al
        new_letter = alphabet1[new_index]
        cyphertext += new_letter
    return cyphertext

#for i in range(33):
    print(caesar_vzlopt(pl,i))

#print(caesar_encrypt(pl,ke))
# print(caesar_crypt(pl,ke))

def atbash_encrypt(plaintext):
    cyphertext = ""
    plaintext = plaintext.lower() 
    a = alphabet[::-1]
    for i in plaintext:
        if i == " ":
            cyphertext += " "
            continue
        cyphertext += a[alphabet.find(i)]
    return cyphertext