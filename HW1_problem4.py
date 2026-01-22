import random
import matplotlib.pyplot as plt

def analytic_pdf(t):
	return 3 * (t ** 2)


list = []

for i in range(0, 10 ** 5):
	a = random.random()
	b = random.random()
	c = random.random()
	
	list.append(max(a,b,c))

	

x = []
y = []
for i in range(100):
	y.append(analytic_pdf(i / 100))
	x.append(i/100)


plt.plot(x, y, color='r')
plt.hist(list, density=True, bins = 20)

plt.xlabel("Time (Hours after 6:00)")
plt.ylabel("Probability density")
plt.legend(["Theoretical probability density", "Simulated probability density (10^5 trials)"])
plt.title("PDF of the time which all 3 friends arrive")
plt.show()