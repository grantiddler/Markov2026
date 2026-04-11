import numpy as np
import matplotlib.pyplot as plt


def rate(t):
    return .5 + (t ** 2) / 1800


Ti = [] #interarrival times to sample from

t_cum = 0 #cumulative time

T = 120

max_rate = rate(T)


while True:
    rand = np.random.exponential(1/max_rate)
    t_cum += rand
    if t_cum > T:
        break
    else:
        Ti.append(rand)


times = []
for i in np.cumsum(Ti):
    rand = np.random.uniform(0,1)
    if(rand < rate(i)/max_rate):
        times.append(i)


print(f"{len(times)} cases in 120 days (380 expected)")

t = np.linspace(0,120)
rate_list = []

for i in t:
    rate_list.append(rate(i))
 
plt.plot(t,rate_list, color="black")
plt.hist(times,120)

plt.xlabel("Time (days)")
plt.ylabel("Cases per day")
plt.title("New daily cases vs time")

plt.legend(["instantaneous rate"])

plt.show()