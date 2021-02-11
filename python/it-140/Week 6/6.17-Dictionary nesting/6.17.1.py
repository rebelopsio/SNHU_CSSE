music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

# Get user input
print("1. Add an artist\n2. Add an album\n3. Add a song\n4. Exit")
user_input = int(input("What would you like to do?\n"))


while user_input != 4:
    if user_input == 1:
        name = input("Enter the artist's name:\n")
        music[name] = {}
        
        print("1. Add an artist\n2. Add an album\n3. Add a song\n4. Exit")
        user_input = int(input("What would you like to do?\n"))
    elif user_input == 2:
        name = input("Enter the artist's name:\n")
        if name in music.keys():
            album = input("Enter the album name:\n")
            music[name][album] = {}
            
            print("1. Add an artist\n2. Add an album\n3. Add a song\n4. Exit")
            user_input = int(input("What would you like to do?\n"))
            
        else:
            print("{} doesn't exist!\n".format(name))
            print("Please add {} first.\n".format(name))
            print("1. Add an artist\n2. Add an album\n3. Add a song\n4. Exit")
            user_input = int(input("What would you like to do?\n"))
        
    elif user_input == 3:
        name = input("Enter the artist's name:\n")
        if name in music.keys():
            album = input("Enter the album name:\n")
            if album in music[name].keys():
                song = input("Enter the song name:\n")
                music[name][album]['songs'] = [song]
                print("1. Add an artist\n2. Add an album\n3. Add a song\n4. Exit")
                user_input = int(input("What would you like to do?\n"))
            else:
                print("{} doesn't exist!\n".format(album))
                print("Please add {} first.\n".format(album))
                print("1. Add an artist\n2. Add an album\n3. Add a song\n4. Exit")
                user_input = int(input("What would you like to do?\n"))
        else:
            print("{} doesn't exist!\n".format(name))
            print("Please add {} first.\n".format(name))
            print("1. Add an artist\n2. Add an album\n3. Add a song\n4. Exit")
            user_input = int(input("What would you like to do?\n"))    
    elif user_input == 4:
        break
    else:
        print('Invalid input')
        
