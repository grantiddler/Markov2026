import numpy as np
import random

import matplotlib.pyplot as plt

global a
a = .99

def p(i,j):
    if(i+j == 4):
        return 0
    if((i + j) % 3 == 0):
        return a
    return 1 - a

def run(n,N):
    chains = np.ones(N)
    fn = []

    for t in range(n):
        fs = 0
        for c in range(N):

            rand = random.random()

            j = 1
            cumulative = 0
            
            while (rand >= cumulative):
                cumulative += p(chains[c], j)
                j += 1
            
            chains[c] = j-1

            fs += (j == 2)
        print(fs/N)
        fn.append(fs/N)
    return(fn)
        


# run(1000, 10000)
plt.plot(run(1000, 10000))
plt.show()