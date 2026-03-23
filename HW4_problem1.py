import random

p = 0.35
q = 0.4

N = 100_000

retirement_total = 0


for n in range(N):
    i = 10

    while(i > 0):
        r = random.random()
        if(r > p+q):
            retirement_total += i;
            break

        if(r < p):
            i += 1
        else:
            i -= 1


print(retirement_total / N)