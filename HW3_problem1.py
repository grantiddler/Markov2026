import random
import matplotlib.pyplot as plt
import math 

def cg(x):
    a = math.sqrt(3) - 1
    c = math.exp(-a) / (3 * a * a * (1-a))
    return c * a * a * x * math.exp(-a * x)

def f(x):
    return (1/3) * x * (1 + x) * math.exp(-x)


f_list = []
cg_list = []
x = []


for i in range(1, 300):
    x.append(i/20)
    f_list.append(f(i/20))
    cg_list.append(cg(i/20))


plt.plot(x,f_list)
plt.plot(x,cg_list)
plt.xlabel("x")
plt.ylabel("Probability density")
plt.title("f(x) vs scaled PDF c*g(x) for acceptance/rejection sampling")
plt.legend(["f(x) probability density funciton", "c*g(x) - scaled pdf"])
plt.show()