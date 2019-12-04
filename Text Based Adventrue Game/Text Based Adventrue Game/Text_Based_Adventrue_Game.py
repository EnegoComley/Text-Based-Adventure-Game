 
import random
location = [1,1]
mostRecentInput = ""
setting = 0
roomLayout = [["1","2","3"],["1","2","3"],["1","2","3"]]
hasKey = False
playerName = ""

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
    location = "3_0"
    rooms[3][0]();



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
    if (location[1] == 0):
        if (location[0] != 10):
            location[0] = str((int)(location[0] - 1))
        else:
            print("The door behind you is locked")
            return
    else:
        location[1] = 0;
    rooms[location[0]][location[1]]()

def EnterRoom():
    if (mostRecentInput[len(mostRecentInput)-1] != "1" and mostRecentInput[len(mostRecentInput)-1] != "2" and mostRecentInput[len(mostRecentInput)-1] != "3"):
        print (mostRecentInput[len(mostRecentInput)-1], "Is not a room")
        return
    if (location[1] == 0):
        if (location[0] == 3):
            if (mostRecentInput[len(mostRecentInput)-1] == "3"):
                print("There is no third room")
                return
        location[1] = roomLayout[location[0]][mostRecentInput[len(mostRecentInput)-1]]
        rooms[location[0]][location[1]]()
    else:
        print("I am sorry to tell you that you can't walk through walls")
        return

def GenerateRoomLayouts(Corridor):
    ReRunRoomLayout = True
    while ReRunRoomLayout:
        doorLayout = [str(random.randint(1,3)),str(random.randint(1,3)),str(random.randint(1,3))] 
        if (doorLayout[1] != doorLayout[0] and doorLayout[1] != doorLayout[2] and doorLayout[2] != doorLayout[0]):
            ReRunRoomLayout = False
            roomLayout[Corridor - 1] = doorLayout

def PlayBlackJack():
    pickAgain = True
    while pickAgaing:
        print("With my rules, an ace always means 1, '")
        print("As you sit down across from him, he hands you a card.")
        cards = {"Ace","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","JACK","QUEEN","KING"}
        print("On the card, is the word:")
        cardNumber = random.randint(0,12)
        print(cards[cardNumber])
        total = cardNumber
        print("He hands you a another card.")
        print("On the card, is the word:")
        cardNumber = random.randint(0,12)
        print(cards[cardNumber])
        total = total + cardNumber
        


rooms  = [[Room1_0,Room1_1,Room1_2,Room1_3],[Room2_0,Room2_1,Room2_2,Room2_3],[Room3_0,Room3_1,Room3_2,Room3_3]]
commands = {"go back":GoBack,"enter room":EnterRoom}

# setting 1 is the train, 2 is the haunted house and 3 is the cave.


setting = random.randint(1,3)
GenerateRoomLayouts(1)
GenerateRoomLayouts(2)
GenerateRoomLayouts(3)



name = input("What is your name young adventurer?\n")
print("When playing this game there are" + len(commands) + "commands that you can use.")
print("Go Back, this will let you leave a room or corridor/ junction.")
print("Enter room, this will allow you to enter a room, if you have the room number.")
print("Attack, this will let you attack monsters")
rooms[1][0]()