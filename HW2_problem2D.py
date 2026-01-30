import random
import matplotlib.pyplot as plt
import numpy as np

import time

t0 = time.time()

def F(u):
	return -np.log(u)
def g(x):
    return 2 * np.exp(-(x/2) - 1)

def f(x):
	return x * np.exp(-x)



N = 1000000
list = []

for i in range(N):
	u = random.random()
	v = random.random()
	list.append( F(u)+F(v))

t1 = time.time()

total = t1-t0
print(total)


x = []
y = []
for i in range(0, 61):
	y.append(f(i))
	x.append(i)



plt.plot(x, y, color='r')
plt.hist(list, density=True, bins = 100)

plt.xlabel("X")
plt.ylabel("Probability density")
plt.legend(["Theoretical probability density", "Sampled probability density (" + str(N) + " trials)" ])
plt.title("Gamma distribution")

plt.show()
