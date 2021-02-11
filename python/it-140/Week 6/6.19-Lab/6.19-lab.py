u = input().split('   ')
s = input()
d = {}
for i in u:
    tmp = i.split()
    d[tmp[0]] = tmp[1]

for k, v in d.items():
    s = s.replace(k, v)

print(s)