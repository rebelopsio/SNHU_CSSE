'''
zyDE 6.3.2: Using built-in functions with lists.
Complete the following program using functions from the table above to find some statistics about basketball player Lebron James. The code below provides lists of various statistical categories for the years 2003-2013. Compute and print the following statistics:

Total career points
Average points per game
Years of the highest and lowest scoring season
Use loops where appropriate.
'''


#Lebron James: Statistics for 2003/2004 - 2012/2013
years = ['2003/2004', '2004/2005', '2005/2006', '2006/2007', '2007/2008', '2008/2009', '2009/2010', '2010/2011', '2011/2012', '2012/2013']
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points

print(sum(points))

# Print Average PPG

print(sum(points) / sum(games_played))

# Print best scoring years (Ex: 2004/2005)

var = max(points)
i = points.index(var)
print(years[i])

# Print worst scoring years (Ex: 2004/2005)
var2 = min(points)
j = points.index(var2)
print(years[j])


