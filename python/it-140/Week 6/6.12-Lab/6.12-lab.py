l = []
user_input = input()
l = [int(s) for s in user_input.split()]

print((sum(l) // len(l)), max(l))
