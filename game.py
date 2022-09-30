#!/usr/bin/python3
"""CarlCodes| CRWalker
Driving a simple game framework with gameplay in the Jedi Temple using
   a dictionary object"""


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''"Get to the Training Gym with a Kyber Crytal, 
    a Lightsaber and the Sith Wayfinder to defeat Darth Maul and win!
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      fight [Darth Maul]
    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You have entered the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Jedi Hall': {
        'south': 'Meditation Room',
        'west': 'Training Gym',
        'east': 'Garage',
    },

    'Garage': {
        'west': 'Jedi Hall',
        'south': 'Dining Room',
        'item': 'sith sxayfinder'
    },

    'Meditation Room': {
        'north': 'Jedi Hall',
        'west': 'Garden',
        'east': 'Dining Room',
        'item': 'kyber crystal'
    },
    'Dining Room': {
        'west': 'Meditation Room',
        'north': 'Garage',
        'item': 'Master Yoda'
    },
    'Garden': {
        'north': 'Training Gym',
        'east': 'Meditation Room',
        'item': 'lightsaber'
    },
    'Training Gym': {
        'east': 'Jedi Hall',
        'south': 'Garden',
        'item': 'Darth Maul'
    }
}

# start the player in the Jedi Hall
currentRoom = 'Jedi Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get the sith wayfinder" becomes ["get", "sith wayfinder"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and ['item'] is not None:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # If a player enters a room with Darth Maul
    if 'item' in rooms[currentRoom] and 'Darth Maul' in rooms[currentRoom]['item']:
        print('You\'re no match for Darth Maul... GAME OVER!')
        break

    # If a player enters a room with Yoda
    if 'item' in rooms[currentRoom] and 'Master Yoda' in rooms[currentRoom]['item']:
        print('Master Yoda says you must face Darth Maul in the Training Gym... MAY THE FORCE BE WITH YOU!')

    # Define how a player can win
    if currentRoom == 'Training Gym' and 'Sith Wayfinder' in inventory and 'Kyber Crystal' in inventory and 'Lightsaber' in inventory:
        print('You defeated Darth Maul and earned your place as a Jedi!... YOU WIN!')
        break
