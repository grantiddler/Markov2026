import random
import matplotlib.pyplot as plt

def F(u):
	return 10 * (u ** -(1/3))

def f(x):
    return ((3/ 10) * ((x/10) ** -4))



N = 10000
list = []

for i in range(N):
    list.append(F(random.random()))


x = []
y = []
for i in range(10, 61):
	y.append(f(i))
	x.append(i)



plt.plot(x, y, color='r')
plt.hist(list, density=True, bins = 100)

plt.xlabel("X")
plt.ylabel("Probability density")
plt.legend(["Theoretical probability density", "Sampled probability density (" + str(N) + " trials)" ])
plt.title("Power-law sampling")

ax = plt.gca()
ax.set_xlim([0, 60])

plt.show()
