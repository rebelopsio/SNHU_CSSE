import csv

user_input = input()

with open(user_input, 'r') as csvfile:
    line_reader = csv.reader(csvfile)
    l = []
    for row in line_reader:
        for i in row:
            if i not in l:
                count_occur = row.count(i)
                print(i, count_occur)
                l.append(i)
