l = []
user_input = input()
l = [int(s) for s in user_input.split()]
m = [i for i in l if i >= 0]
m.sort()
for i in m:
    print(i, end=' ')
