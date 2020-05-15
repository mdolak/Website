#  File: Project2.py
#  Description: This program uses object-oriented techniques to create
#  a simple map for an adventure game, similar to "Colossal Cave", with rooms
#  given in a txt file. It uses command-line interpreter as an interactive
#  user interface.
#  Student's Name: Maria Dolak
#  Course Name: CS 303E 
#
#  Date Created: 05/05/2020
#  Date Last Modified: 07/05/2020


# Create a class Room.
class Room:

    # Define an object  with the following attributes: name, rooms to the
    # north, east, south west, up and down and the contents of the room.
    
    def __init__(self,name,north,east,south,west,up,down,contents):
        self.name = name 
        self.north = north 
        self.east = east 
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.contents = contents

###############################################################################
# The following method and function are not meant to be used in the game.

    # Define a method that displays a name of the room and all possible
    # rooms with which it is connected.
    
    def displayRoom(self):
            
        print("Room name: ",self.name)

        if self.north != None:
            print(format("   Room to the north: ","22s"),self.north)
        if self.east != None:
            print(format("   Room to the east: ", "22s"),self.east)
        if self.south != None:
            print(format("   Room to the south: ", "22s"), self.south)
        if self.west != None:
            print(format("   Room to the west: ", "22s"), self.west)
        if self.up != None:
            print(format("   Room above: ","22s"), self.up)
        if self.down != None:
            print(format("   Room below: ", "22s"), self.down)
        if self.contents == None:
            print(format("   Room contents: ", "22s"), [])
        if self.contents != None:
            print(format("   Room contents: ", "22s"), self.contents)

# Define a function that displays all the rooms with all of the rooms
# they are connected to.
    
def displayAllRooms():
            
    for i in floorPlan:
        i.displayRoom()
        print()

###############################################################################


# Define a function that creates a new Room object with properties defined
# in a list given as roomData. Return the new object.

def createRoom(roomData):

        newRoom = Room(roomData[0],roomData[1],roomData[2],roomData[3],
                       roomData[4],roomData[5], roomData[6], roomData[7])
        return newRoom

# Define a function that displays a name of a room in which an user
# is currently in and the contents of the room.

def look():
    print("You are currently in the " + current.name + ".")
    print("Contents of the room:")
    if current.contents == []:
        print("   None")
    else:
        for item in current.contents:
            print("   " + item)
        
# Define a function that takes one argument, the name of a room (a string),
# and returns the corresponding Room object.

def getRoom(name):
    
    for i in range(len(floorPlan)):
        room = floorPlan[i]
        if name == room.name:
            return floorPlan[i]

        
# Define a function that takes as an argument a direction the player
# wants to move to from the current room. It displays a new location or informs
# that a player cannot move in a particular direction. Then, it returns
# a new location (or the same one if a move is impossible).

def move(direction):

    if direction == "north":
        if current.north != None:
            print("You are now in the " + current.north + ".")
            return getRoom(current.north)
        else:
            print("You can't move in that direction.")
            return current
            
    if direction == "east":
        if current.east != None:
            print("You are now in the " + current.east + ".")
            return getRoom(current.east)
        else:
            print("You can't move in that direction.")
            return current
            
    if direction == "south":
        if current.south != None:
            print("You are now in the " + current.south + ".")
            return getRoom(current.south)
        else:
            print("You can't move in that direction.")
            return current
            
    if direction == "west":
        if current.west != None:
            print("You are now in the " + current.west + ".")
            return getRoom(current.west)
        else:
            print("You can't move in that direction.")
            return current
        
    if direction == "up":
        if current.up != None:
            print("You are now in the " + current.up + ".")
            return getRoom(current.up)
        else:
            print("You can't move in that direction.")
            return current

    if direction == "down":
        if current.down != None:
            print("You are now in the " + current.down + ".")
            return getRoom(current.down)
        else:
            print("You can't move in that direction.")
            return current
        
# Define a function that allows an user to pick up an item from the current
# room and add it to her/his inventory. 

def pickup(item):

    # case when the item is in the room
    
    if item in current.contents:
        inventory.append(item)
        current.contents.remove(item)
        print("You now have the " + item + ".")

    # case when the item is not found (possibly it's not even in the house)
    else:
        print("That item is not in this room.")

# Define a function that allows an user to drop an item from their inventory
# into the current room.

def drop(item):
    
    if item in inventory:
        current.contents.append(item)
        inventory.remove(item)
        print("You have dropped the " + item + ".")
    else:
        print("You don't have that item.")

# Define a function that lists all the items an user currently has in the
# inventory or informs that nothing is stored there.

def listInventory():

    print("You are currently carrying:")
    if inventory == []:
        print("   nothing.")
    else:
        for item in inventory:
            print("   " + item)
    
# Define a function that reads the input file with all the rooms and their 
# contents' data, creates all the corresponding room objects and stores them 
# as a list in the floorPlan.

def loadMap():

    global floorPlan

    roomsFile = open("ProjectData.txt","r")
    line = roomsFile.readline()
    floorPlan = []

    while line != "":

        roomInfo = [eval(x) for x in line.split(",")]
        
        room = roomInfo[0:7]
        contents = roomInfo[7:]
        if contents == []:
            room.append([])
        else:
            room.append(contents)
            
        
        floorPlan.append(createRoom(room))
        
        line = roomsFile.readline()


    roomsFile.close()


# Define a function that displays all the possible commands an user can use
# to play the game.

def showHelp():
    
    print("\nlook:        display the name of the current room and\
its contents\nnorth:       move north\neast:        move east\n\
south:       move south\nwest:        move west\nup:          move up\
\ndown:        move down\ninventory:   list what items you're\
currently carrying\nget <item>:  pick up an item currently in the room\n\
drop <item>: drop an item you're currently carrying\nhelp:        print \
this list\nexit:        quit the game")


def main():

    global current          # make the variable "current" a global variable
    global inventory        # make the variable "inventory" a global variable

    
    inventory = []          # initialize inventory
    
    loadMap()               # load a map to get the floorPlan
    
    current = floorPlan[0]  # set a living room as the starting room
                            # it could be any other room stored as the
                            # first one in the input file

    look()                  # display the starting room
    print()

    showHelp()
    print()
    # initialize the command-line interpreter
    # start a loop until an user decides to quit the game
    # translate each user's command to an appropriate function

    # meake the game not case-sensitive
    # make sure the game doesn't crash when a wrong word is typed in,
    # instead, inform that a command is not found and allow to type in
    # another one
    
    command = ""

    while command != "exit":

        command = input("Enter a command: ")

        command = command.split()

        if len(command) == 1:
        
            if command[0].lower() == "look":
                look()
                print()
            elif command[0].lower()  == "north":
                current = move("north")
                print()
            elif command[0].lower()  == "east":
                current = move("east")
                print()
            elif command[0].lower()  == "south":
                current = move("south")
                print()
            elif command[0].lower()  == "west":
                current =  move("west")
                print()
            elif command[0].lower()  == "up":
                current = move("up")
                print()
            elif command[0].lower()  == "down":
                current = move("down")
                print()
            elif command[0].lower()  == "inventory":
                listInventory()
                print()
            elif command[0].lower()  == "help":
                showHelp()
                print()
                
            # The following command is not listed under "help" for an user and
            # its purpose is to demonstrate the change in displayRoom() from
            # project 1. It's an equivalent of "cheat" in Dr. Bulko's game.

            elif command[0].lower() == "display":
                displayAllRooms()
                print()
            elif command[0].lower()  == "exit":
                print("Quitting game.")
                break
            else:
                print("The command not found. Try again.\n")

        elif len(command) == 2:
            if command[0].lower()  == "get": 
                pickup(command[1].lower() )
                print()
            elif command[0].lower()  == "drop":
                drop(command[1].lower() )
                print()
            else:
                print("The command not found. Try again.\n")
        else:
            print("The command not found. Try again.\n")

main()



