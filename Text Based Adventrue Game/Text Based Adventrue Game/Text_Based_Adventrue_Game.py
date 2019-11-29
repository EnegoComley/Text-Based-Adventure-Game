 


def Room1_0():
    print("You find yourself at a juction, infront of you there are three doors labeld 1,2 and 3")

def Room1_1():
    print("As you open the door infront of you, you notice a table, and lying on that table is a shiny golden key")

def Room1_2():
    print ("As you open this door a monster greets you.")

def Room1_3():
    print ("This door is locked.")



def Room2_0():
    print("You find yourself at a juction, infront of you there are three doors labeld 1,2 and 3")

def Room2_1():
    print("In this room you find a tied up human")

def Room2_2():
    print("As you open the door to this room you find that it is not infact a room but a long windng corridor")

def Room2_3():
    print("This door opens to another set of 3 doors")
    Location = "3_0"
    Rooms[3][0]();



def Room3_0():
    print("You find yourself at a juction, infront of you there are three doors labeld 1,2 and 3")

def Room3_1():
    print("As you enter this room you notice all sorts of equipment from ropes to swords.")

def Room3_2():
    print("As you enter this room you look up to see a number orcs, armed with knives. \n You are dead in an instant.")

def Room3_3():
    print("You open this room to find DAYLIGHT")
    print ("You have managed to beat the dungeon;\n You are free.")

def GoBack():
    if (Location[2] == "0"):
        if (Location[0] != 10):
            Location[0] = str((int)(Location[0] - 1))
        else:
            print("The door behind you is locked")
    else:
        Location[2] = "0";


Rooms  = [[Room1_0,Room1_1,Room1_2,Room1_3],[Room2_0,Room2_1,Room2_2,Room2_3],[Room3_0,Room3_1,Room3_2,Room3_3]]
Location = "1_1"


Rooms[1][0]()
