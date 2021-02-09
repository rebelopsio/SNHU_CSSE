'''
zyDE 6.11.1: Calculate voltage drops across series of resistors.
The following program uses a list to store a user-entered set of resistance values and computes I.

Modify the program to compute the voltage drop across each resistor, store each in another list voltage_drop, and finally print the results in the following format:

5 resistors are in series.
This program calculates the voltage drop across each resistor.
Input voltage applied to circuit: 12.0
Input ohms of 5 resistors
1) 3.3
2) 1.5
3) 2.0
4) 4.0
5) 2.2
Voltage drop per resistor is
1) 3.0 V
2) 1.4 V
3) 1.8 V
4) 3.7 V
5) 2.0 V
'''

num_resistors = 5
resistors = []
voltage_drop = []

print('%d resistors are in series.' % num_resistors)
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print(input_voltage)

print('Input ohms of {} resistors'.format(num_resistors))
for i in range(num_resistors):
    res = float(input('{})'.format(i + 1)))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

# Calculate voltage drop over each resistor
for i in resistors:
    tmp = i * current
    voltage_drop.append("{:.1f}".format(tmp))


# Print the voltage drop per resistor
print('Voltage drop per resistor is')
for i, val in enumerate(voltage_drop):
    print("{}) {} V".format(i + 1, val))
