import random
import matplotlib.pyplot as plt

def func(u):
	return 1 / ( ( (1 / u) ** 6 + 1) * ( u ** 2) )

above = 0
below = 0

y = []
x = []

itr = 1;
i = 0

while (itr <= 5):
	xrand = random.random()
	yrand = random.random()

	if func(xrand) < yrand:
		above += 1
	else:
		below += 1
	
	if(i >= 10 ** itr):
		x.append(itr)
		y.append(below / i)
		itr += 0.1


	i += 1

print(y[-1])
plt.plot(x, y)

calc= 0.143425777448 # this is from desmos
plt.plot([1, 5], [calc, calc])
plt.xlabel("N (logarithmic)")
plt.ylabel("integral estimate")
plt.title("Monte Carlo simulation estimate vs. number of simulations")
plt.legend(["Value of Monte carlo simulation", "Numerically computed integral value"])
plt.show()
