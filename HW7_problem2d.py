import random
import numpy as np

import matplotlib.pyplot as plt

def sample_exp(rate):
    rand = random.random()
    return - np.log(rand) / rate

def HPPP(rate, time):
    t = 0
    arr = []
    while True:
        sample = sample_exp(rate)
        t += sample
        
        if(t < time):
            arr.append(t)
        else:
            return arr
    

Both_teams = HPPP(6,48)
A = []
B = []

for i in Both_teams:
    rand = random.random()
    if(rand >0.5):
        A.append(i)
    else:
        B.append(i)



plt.vlines(A,1.2,2)
plt.vlines(B,0,.8,colors="red")
plt.xlabel("minute")
plt.title("Goals vs Time")
plt.legend(['Team A', 'Team B'])
plt.show()