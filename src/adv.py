from room import Room
from item import Item
from player import Player

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

#
# Main



# Make a new player object that is currently in the 'outside' room.
player = Player("Tim", currentRoom = room["outside"] )
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

input_key = input("[N] North, [S] South, [E] East, [W] West, [Q] Quit, [Y] Yes, [N] No")

while True: 
    if input_key == "N" and hasattr(player.currentRoom, "n_to"): 
        print("\nCurrent room:", {player.currentRoom})
        player.currentRoom = player.room.n_to

    elif input_key == "S" and hasattr(player.currentRoom, "s_to"):
        print("\nCurrent room:", {player.currentRoom})
        player.currentRoom = player.room.s_to


    #The option of leaving the game
    elif input_key == "Q":
        print("Are you sure you want to leave?")

    elif input_key == "N":
        player.currentRoom = player.currentRoom

    elif input_key == "Y":
        print("See you later! Goodbye!")
        break 