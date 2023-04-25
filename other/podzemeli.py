room_list = []
room = ["koridor", 1, None, None, 4]
room1 = ["holl", 2, None, 0, 3]
room2 = ["balkon", None, None, 1, None]
room3 = ["kuhnya", None, 1, 4, 6]
room4 = ["podzemeli", 3, 0, None, 5]
room5 = ["oruzhenya", 6, 4, None, None]
room6 = ["kabina", None, 3, 5, None]

current_room = 0

room_list.append(room)
room_list.append(room1)
room_list.append(room2)
room_list.append(room3)
room_list.append(room4)
room_list.append(room5)
room_list.append(room6)

print("vi ochutilis v koridore. on ochen dliniy in po bocam vesyat fakela")

while current_room != 6:
    print("vi nahodites v " + room_list[current_room][0])
    print()
    if room_list[current_room][1] != None:
        print("Vi mozhete iti na North")
    if room_list[current_room][2] != None:
        print("vi mozhete iti na East")
    if room_list[current_room][3] != None:
        print("vi mozhete iti na South")
    if room_list[current_room][4] != None:
        print("vi mozhete iti na West")
    otvet = input("kuda iti: ")
    if otvet == 'north':
        next_room = room_list[current_room][1]
        if next_room == None:
            print("Вы не можете идти сюда")
        else:
            current_room = next_room
            print(current_room)
    elif otvet == 'east':
        next_room = room_list[current_room][2]
        if next_room==None:
            print("Вы не можете идти сюда")
        else:
            current_room = next_room
            print(current_room)
    elif otvet == 'south':
        next_room = room_list[current_room][3]
        if next_room == None:
            print("Вы не можете идти сюда")
        else:
            current_room = next_room
            print(current_room)
    elif otvet == 'west':
        next_room = room_list[current_room][4]
        if next_room == None:
            print("Вы не можете идти сюда")
        else:
            current_room = next_room
            print(current_room)
    if current_room == 6:
        print("vi doshli do kabina!\nmolodtsi!\nvso poka.")









    #if room_list[current_room][1] != None:
        #print("Vi mozhete iti na North(holl)")
        #next_room = room_list[current_room][1]