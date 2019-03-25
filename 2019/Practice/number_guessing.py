# Imports
import random

# Debug
#import pdb
#pdb.set_trace()


## Global parameters
low = 1 # Min number
high = 100  # Max number
G = random.randint(1, 100)  # Number to guess

N = 5 # Number of attemps

sequence = list(range(int(low), int(high) + 1)) # Initial sequence

LB = 0  # Lower bound in array
UB = len(sequence)  # Upper bound in array

# States
LMT = 'Let me think. :/'
WAD = 'We are done. :)'

# Guess number function
def guess_number(LB, UB):

    space = sequence[LB  : UB]  # Search space
    g_hat = random.choice(space) # g proposed
    index = sequence.index(g_hat) # index in original sequence

    return({'g_hat': g_hat, 'index': index})

if __name__ == "__main__":

    state = LMT

    for i in range(N):

        if state != WAD:

            gi = guess_number(LB, UB)
            G_HAT = gi['g_hat']
            index = gi['index']

            if G_HAT == G:

                state = WAD

            elif G_HAT < G:

                print(state)
                print('G: %s' %(G))
                print('G_HAT: %s' %(G_HAT))

                # Update search space
                LB = index
                UB = UB

            elif G_HAT > G:

                print(state)
                print('G: %s' %(G))
                print('G_HAT: %s' %(G_HAT))

                # Update search space
                LB = LB
                UB = index

        else:

            # Number found
            print(state)
            print('G: %s' %(G))
            print('G_HAT: %s' %(G_HAT))

            break
