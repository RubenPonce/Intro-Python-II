from room import Room
from player import Player
     
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], "Guy")


print(player.room)
key = input("[N] North   [E] East   [S] South   [W] West   [Q] Quit\n").upper()
# * Prints the current room name
def isValidRoom(room,prop):

    return hasattr(room, prop)

while not key == "Q":

    if key == "N" and isValidRoom(player.room, "n_to"):
        player.room = player.room.n_to
        print(player.room)

    elif key =="E" and isValidRoom(player.room, "e_to"):
        player.room = player.room.e_to
        print(player.room)

    elif key == "S" and isValidRoom(player.room,"s_to"):
        player.room = player.room.s_to
        print(player.room)

    elif key == "W" and isValidRoom(player.room,"w_to"):
        player.room = player.room.w_to
        print(player.room)
        
    else:
        print("can't go dat way big boi")
    key = input("[N] North   [E] East   [S] South   [W] West   [Q] Quit\n").upper()


        



