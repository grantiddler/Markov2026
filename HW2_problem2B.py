import random
import matplotlib.pyplot as plt
import numpy as np
import time

t0 = time.time()


def F(x):
	return 1- x * np.exp(-x) - np.exp(-x)

def Finv(u):
	x = 1
	for i in range(20):
		xnew = x- (F(x) - u) / f(x)

		if xnew < 0:
			xnew = x/2

		
		if abs(x - xnew) < (10 ** -6):
			break

		x = xnew

	return x

def f(x):
	return x * np.exp(-x)



N = 1000000
list = []

for i in range(N):
	u = random.random()
	list.append( Finv(u))

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

