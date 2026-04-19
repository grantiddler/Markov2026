import numpy as np
import matplotlib.pyplot as plt




timestep = 0.01
t_max = 5
ts = np.linspace(0,5,int(t_max/timestep))

fig = plt.figure()

for k in range(5):
    num_in1 = np.zeros(int(t_max/timestep))
    
    N = 10 ** (k+2)
    print(N)

    for i in range(N):
        t = 0
        t_next = np.random.exponential(1)
        x = np.random.choice([1,2,2])

        for j in range(int(t_max/timestep)):
            t = j * timestep
            if(t > t_next):
                t_next = t + np.random.exponential(1)
                x = (x % 4) + 1

            if(x == 1):
                num_in1[j] += 1/N



            
    fig.add_subplot(int(f"32{k+1}"))
    plt.plot(ts,num_in1)

    plt.title(f"Simulated, {N} processes")
    plt.xlabel("time")
    plt.ylabel("probability that x(t) = 1")


    plt.ylim(0,1/2)
    
    

   
fig.add_subplot(326)

analytic = []
for i in ts:
    analytic.append(1/4 + (np.cos(i) - 2 * np.sin(i)) * np.exp(-i)/6 - np.exp(-2* i) / 12)

plt.plot(ts, analytic)
plt.title("Analytical solution")

plt.xlabel("time")
plt.ylabel("probability that x(t) = 1")


plt.ylim(0,1/2)
fig.tight_layout()

plt.show()






