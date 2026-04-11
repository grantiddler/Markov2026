import random
import math
import numpy as np

def binomial_pmf(x,n, p = 0.5):
    return (p ** x) * ((1-p) ** (n-x)) * math.comb(n,x)


rng = np.random.default_rng()
np.random.default_rng()

n = 0
for k in range(10**10):
    i = 0
    pop = 1
    while(i < 200):
        i += 1
        if(pop == 0 or pop > 2 ** 8):
            i = 200

        rand = rng.binomial(pop, 0.51)
        pop = rand * 2


    if(pop >0 ):
        n+=1
        print(n)
        print(1- (n/ k))
        print()
