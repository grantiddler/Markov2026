import numpy as np
import matplotlib.pyplot as plt
import math


def p_tie(t):
    sum = 0
    for i in range(10):
        sum += ((4/3 * (t **2)) ** i) / (math.factorial(i)) ** 2

    return sum * np.exp(-7/3 * t)

t = np.linspace(0, 90)
p = []

for i in t:
    T = 1.5 - i/60
    p.append(p_tie(T))

plt.plot(t,p)

plt.title("Probability of a tie vs Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Probability")
plt.ylim(0,1)
plt.show()