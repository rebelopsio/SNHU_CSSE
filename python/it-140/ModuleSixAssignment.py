import random as rm

room_list = {
    1: {'Name': "Children's Room", 'Clue': 'Tattered brown cloth', 'South': 'Natural History Room', 'East': 'Agricultural Room'},
    2: {'Name': "Natural History Room", 'Clue': 'Black shoes', 'North': "Children's Room"},
    3: {'Name': "Agricultural Room", 'West': "Children's Room"}
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


if __name__ == '__main__':
    user_input = ''
    items_collected = []
    rooms_available = {}
    current_room = 1
    villain_room = rm.randint(1, 3)

    # Main game loop
    while user_input.lower() != 'exit':
        print('Welcome to Scooby-Doo and the Black Knight!')
        print('Collect all of the clues to solve the mystery!')
        print('Move commands: go south, go north, go east, go west')
        print('Pick up a clue: get clue')

        # Game loop while all clues are not collected
        while len(items_collected) < 6 and user_input.lower() != 'exit':

            # Game loop when villain is not in the same room
            while villain_room != current_room:
                print(
                    "Scooby-Doo enters the {}".format(room_list[current_room]['Name']))
                if (has_items(current_room)) != False:
                    print("Look! A clue: {}".format(has_items(current_room)))
                rooms_available = get_rooms(current_room)
                print('Current rooms available to move to: {}'.format(
                    rooms_available))
                user_input = input('What would you like to do?\n')
                if user_input.lower() == 'exit':
                    break
                new_slice = user_input.split()
                while (new_slice[0] not in ['go', 'get']) or (len(new_slice) <= 1):
                    print('Invalid response.')
                    user_input = input('What would you like to do?\n')
                    if user_input.lower() == 'exit':
                        break
                    new_slice = user_input.split()
                # validate that the go command was used
                if new_slice[0].lower() == 'go':
                    while new_slice[1].capitalize() not in available_directions(rooms_available):
                        print('Invalid response.')
                        user_input = input('What would you like to do?\n')
                        if user_input.lower() == 'exit':
                            break
                        new_slice = user_input.split()
                    direction = new_slice[1].capitalize()
                    to_room = rooms_available[direction]
                    current_room = get_room_id(to_room)
                    villain_room = rm.randint(1, 3)

            # If player has indicated 'exit', skip this
            if user_input.lower() != 'exit':
                print('The Black Knight is in here! Run back to the beginning!')
                current_room = 1
                villain_room = rm.randint(1, 3)
