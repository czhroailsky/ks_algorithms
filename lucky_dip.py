#Imports
import random
import math
from tqdm import tqdm

#Define Variables

N = random.randint(1, 2 * math.pow(10, 4)) # Number of items in the bag

V = [] # Values of the items
for i in range(N):
	V.append(random.randint(1, 655321))

k = random.randint(1, 5 * math.pow(10, 4)) # Number of times to redip

def expected_value(V, N):

	E_k = (1.0/N) * (sum(V))

	return(E_k)


if __name__ == '__main__':

	for i in tqdm(range(k + 1)):

		if i == 0:

			E_k = (1.0/N) * (sum(V))

		else:

			V = [ x if x > E_k else E_k for x in V ]
			E_k = (1.0/N) * (sum(V))

	print('Expected value: %s' %(E_k))
