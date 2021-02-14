'''
Stephen Morgan
IT-140-X3215 - Introduction to Scripting - 21EW3
'''

import random as rm


room_list = {
    1: {'Name': "Children's Room", 'Clue': 'Tattered brown cloth', 'South': 'Natural History Room', 'East': 'Agricultural Room'},
    2: {'Name': "Natural History Room", 'Clue': 'Black shoes', 'North': "Children's Room"},
    3: {'Name': "Agricultural Room", 'West': "Children's Room", 'South': 'African History Room', 'North': 'Science Room', 'East': 'Marginalized People Room'},
    4: {'Name': "African History Room", 'East': "Medical Room", 'North': "Agricultural Room"},
    5: {'Name': "Medical Room", 'West': "African History Room", 'Clue': 'Black tie'},
    6: {'Name': 'Science Room', 'South': 'Agricultural Room', 'East': 'Military and War Room', 'Clue': 'Thick Framed Glasses'},
    7: {'Name': 'Military and War Room', 'West': 'Science Room', 'Clue': 'Tattered blue cloth'},
    8: {'Name': 'Marginalized People Room', 'West': 'Agricultural Room', 'North': 'Art Room'},
    9: {'Name': 'Art Room', 'South': 'Marginalized People Room', 'Clue': 'Brown Overcoat'}
}


def has_items(room_id):
    """
    Function to validate whether room has clues, if so, returns item name
    """
    if 'Clue' in room_list[room_id]:
        return room_list[room_id]['Clue']
    else:
        return False


def get_rooms(room_id):
    """
    Function to dictionary of available adjeacent rooms.
    """
    l = {}
    if 'South' in room_list[room_id]:
        l['South'] = room_list[room_id]['South']
    if 'North' in room_list[room_id]:
        l['North'] = room_list[room_id]['North']
    if 'East' in room_list[room_id]:
        l['East'] = room_list[room_id]['East']
    if 'West' in room_list[room_id]:
        l['West'] = room_list[room_id]['West']
    return l


def get_room_id(room_name):
    """
    Function to return integer of room id
    """
    for i in room_list:
        if room_list[i]['Name'] == room_name:
            return i


def available_directions(available_rooms):
    """
    Function to get list of available directions of adjacent rooms
    """
    l = []
    for i in available_rooms:
        l.append(i)
    return l


def game_instructions():
    """
    Function to print the game instructions
    """
    print()
    print()
    print('Welcome to Scooby-Doo and the Black Knight!')
    print('The members of the town have reported something creepy going on at the museum.')
    print('Professor Jameson Hyde White has also been reported as missing.')
    print('Scooby-Doo must figure out what is going on.\n')
    print('Collect all of the clues to solve the mystery!\n')
    print('Game instructions:')
    print()
    print('Move commands: go south, go north, go east, go west')
    print('Pick up a clue: get clue')
    print()


def game_ending(current_room):
    print('You have collected all of the clues.')
    print("The Black Knight enters {} but doesn't see you!".format(
        room_list[current_room]['Name']))
    print("Scooby-Doo looks at the items collected, and scream out, 'THE BLACK KNIGHT IS....!")
    print('Startled, the Black Knight loses their balance and they tumble over.')
    print("The Black Knight's helmet rolls across the room, revealing their true identity.")
    print("Scooby-Doo, finishing his sentence, exclaims, 'Mr. Wickles!'")
    print("Just then, the gang enters with the Sheriff who arrests Mr. Wickles.\n")
    print("Mr. Wickles admits to kidnapping Prof. White")
    print("You find the Professor tied up in the closet and rescue him.")
    print("Great job, Scooby-Doo!\n")
    print()


def main():
    """
    Main game function
    """
    user_input = ''
    items_collected = []
    rooms_available = {}
    current_room = 1
    villain_room = rm.randint(2, 9)

    # Main game loop
    while user_input.lower() != 'exit':

        # Game loop while all clues are not collected
        while len(items_collected) < 6 and user_input.lower() != 'exit':
            if user_input == '':
                game_instructions()

            # Game loop when villain is not in the same room
            while villain_room != current_room:

                if user_input == '':
                    print(
                        "Scooby-Doo enters the museum to find himself in the {}".format(room_list[current_room]['Name']))
                elif user_input.lower().strip() == 'get clue':
                    print(
                        "Scooby-Doo is still in the {}".format(room_list[current_room]['Name']))
                else:
                    print()
                    print(
                        "Scooby-Doo enters the {}".format(room_list[current_room]['Name']))
                if (has_items(current_room)) != False:
                    if has_items(current_room) not in items_collected:
                        print("Look! A clue: {}".format(
                            has_items(current_room)))
                rooms_available = get_rooms(current_room)
                print('Current rooms available to move to: {}'.format(
                    rooms_available))
                print('Scooby-Doo has collected: {}'.format(items_collected))
                print('---------------------------------------------------\n')
                user_input = input('What would you like to do?\n')
                if user_input.lower() == 'exit':
                    break
                new_slice = user_input.split()
                while new_slice == [] or new_slice == [] or (new_slice[0].lower() not in ['go', 'get']) or (len(new_slice) <= 1):
                    print('Invalid response.')
                    user_input = input('What would you like to do?\n')
                    if user_input.lower() == 'exit':
                        break
                    new_slice = user_input.split()

                # validate that the go command was used
                if new_slice[0].lower() == 'go':
                    while new_slice == [] or new_slice[1].capitalize() not in available_directions(rooms_available):
                        print('Invalid response.\n')
                        user_input = input('What would you like to do?\n')
                        if user_input.lower() == 'exit':
                            break
                        new_slice = user_input.split()
                    direction = new_slice[1].capitalize()
                    to_room = rooms_available[direction]
                    current_room = get_room_id(to_room)
                    villain_room = rm.randint(1, 9)

                # validate that get was used
                if new_slice[0].lower() == 'get':
                    while new_slice[1].lower() != 'clue':
                        print('Invalid response.\n')
                        user_input = input('What would you like to do?\n')
                        if user_input.lower() == 'exit':
                            break
                        new_slice = user_input.split()
                    if (has_items(current_room)) != False:
                        if has_items(current_room) not in items_collected:
                            items_collected.append(has_items(current_room))
                            print()
                            print('You picked up the clue {}!\n'.format(
                                has_items(current_room)))
                        else:
                            print('No clue available to collect!\n')
                if len(items_collected) == 6:
                    break

            # What happens when the Black Knight appears
            if user_input.lower() != 'exit' and len(items_collected) < 6:
                print()
                print('!!!!!!\n')
                print('The Black Knight is in here! Run back to the beginning!\n')
                print('!!!!!!')
                print()
                current_room = 1
                villain_room = rm.randint(1, 9)

        # Game ending
        if len(items_collected) == 6:
            game_ending(current_room)
            break


if __name__ == '__main__':
    main()
