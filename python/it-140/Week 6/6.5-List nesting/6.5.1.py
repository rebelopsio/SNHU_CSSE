'''
zyDE 6.5.1: Two-dimensional list example: Driving distance between cities.
The following example illustrates the use of a two-dimensional list in a distance between cities example.

Run the following program, entering the text '1 2' as input to find the distance between LA and Chicago. Try other pairs. Next, try modifying the program by adding a new city, Anchorage, that is 3400, 3571, and 4551 miles from Los Angeles, Chicago, and Boston, respectively.

Note that the styling of the nested list in this example makes use of indentation to clearly indicate the elements of each list -- the spacing does not affect how the interpreter evaluates the list contents.
'''

# direct driving distances between cities, in miles
# 0: Boston    1: Chicago    2: Los Angeles

distances = [
    [
        4551,  # Boston-Achorage
        960,  # Boston-Chicago
        2960  # Boston-Los Angeles
    ],
    [
        960,  # Chicago-Boston
        3571,  # Chicago-Achorage
        2011  # Chicago-Los Angeles
    ],
    [
        2960,  # Los Angeles-Boston
        2011,  # Los-Angeles-Chicago
        3400   # Los-Angeles- Achorage
    ]
]

user_input = input('Enter city pair (Ex: 1 2) -- ').strip()
city1, city2 = user_input.split()

print('Distance: {} miles'.format(distances[int(city1)][int(city2)]))
