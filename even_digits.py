# Imports
import random
import math

# Generate digit
input = random.randint(1, 100000)

# Get digit and its position (unit, tens, hundreds, ...)
def get_digits(number):

    input = int(number)
    dig_list = list(reversed([ int(x) for x in list(str(input)) ]))

    return(dig_list)

# Evaluate if all digits are even
def evaluate_even(list):

    even = []
    odd_index = []

    index = 0
    for i in dig_list:
        if (i % 2) == 0:
            even.append(i)
            index += 1
        else:
            odd_index.append(index)
            index += 1

    if len(even) == len(list):
        state = True
    else:
        state = False

    # State true if all even, min odd digit position
    if odd_index:
        return({'state': state, 'min_odd': min(odd_index)})
    else:
        return({'state': state})

if __name__ == "__main__":

    print('Digit: %s' %(input))
    dig_list = get_digits(input)
    dig_eva = evaluate_even(dig_list)

    # Search and update odd digit
    press = 0
    while not dig_eva['state']:
        if dig_eva['min_odd'] == 0:
            input = input + (1 * math.pow(10, dig_eva['min_odd']))
            press = press + math.pow(10, dig_eva['min_odd'])
            dig_list = get_digits(input)
            dig_eva = evaluate_even(dig_list)
        else:
            input = input + (1 * math.pow(10, dig_eva['min_odd'] - 1))
            press = press + math.pow(10, dig_eva['min_odd'] - 1)
            dig_list = get_digits(input)
            dig_eva = evaluate_even(dig_list)

    print('Digit all even: %s' %(int(input)))
    print('Press the button %s times.' %(int(press)))
