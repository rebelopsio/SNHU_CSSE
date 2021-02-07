'''
zyDE 6.3.1: Iterating through a list example: Finding the sum of a list's elements.
Here is another example computing the sum of a list of integers. Note that the code is somewhat different than the code computing the max even value. For computing the sum, the program initializes a variable sum to 0, then simply adds the current iteration's list element value to that sum.

Run the program below and observe the output. Next, modify the program to calculate the following:

Compute the average, as well as the sum. Hint: You don't actually have to change the loop, but rather change the printed value.
Print each number that is greater than 21.
'''

# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
above_21 = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print('{}: {}'.format(pos, token))
    if int(token) > 21:
        above_21.append(int(token))

sum = 0
for num in nums:
    sum += num

print('Sum:', sum)
print('Average:', sum // len(nums))
print('Numbers greater than 21:', above_21)
