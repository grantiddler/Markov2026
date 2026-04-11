import numpy as np
import matplotlib.pyplot as plt
import math


def p_tie(t):
    sum = 0
    for i in range(10):
        sum += ((4/3 * (t **2)) ** i) / (math.factorial(i)) ** 2

    return sum * np.exp(-7/3 * t)

def p_tie_after_goal(t):
    sum = 0
    for i in range(10):
        sum += ((4/3 * (t **2)) ** i) / (math.factorial(i) * math.factorial(i + 1))

    return sum * np.exp(-7/3 * t) * t

t = np.linspace(0, 60)
p = []

for i in t:
    T = 1.5 - i/60
    p.append(p_tie(T))


t2 = np.linspace( 60,90)
p2 = []

for i in t2:
    T = 1.5 - i/60
    p2.append(p_tie_after_goal(T))


plt.plot(t,p)
plt.plot(t2,p2)

plt.title("Probability of a tie vs Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Probability")
plt.legend(["Before team A scores a goal", "After team A scores a goal"])
plt.ylim(0,1)
plt.show()