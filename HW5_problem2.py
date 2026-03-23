import numpy as np
import math
import random

def pn(n):
    if(n > 4):
        return 0
    
    a = 0.04
    K = 0.1
    return K * math.exp(a * n)

def qn(n):
    if(n <= 1):
        return 0
    b = 0.16
    K = 0.1
    return K * math.exp(b * (n-1))

def pself(n):

    return 1 - pn(n) - qn(n)

def p(i,j):
    if(abs(i - j) > 1):
        return 0

    if(i == j):
        return pself(i+1)

    if(i <j):
        return pn(i+1)
    
    return qn(i+1)


mat = ""
for i in range(5):
    string = ""
    for j in range(5):

        
        string = string + " " + (" " * (8 - len(str(p(i,j))))) + str(p(i,j))[0:8] 
    mat += string + ";\n"

mat = mat[0:-2]
print(mat)

matrix = np.matrix(mat)
print(matrix)

print(np.linalg.eig(np.transpose(matrix)))
    

state = 0;
times = [0,0,0,0,0]
total_time = 0


for i in range(10**6):
    rand = random.random()

    j = -1
    cumulative = 0
    while (rand >= cumulative):
        j += 1
        cumulative += p(state, j)
    
    state = j
    times[j] += 1
    total_time += 1

for i in range(5):
    times[i] /= total_time
    

print(times)

# a= .04
# b= .16
# pi = [1, 0, 0, 0, 0]
# p_tot = 1
# for n in range(1,5):

#     pi[n] = pi[n-1] * math.exp((n) * (a-b))
#     p_tot += pi[n]
    
# print(pi) 

# for n in range(5):

#     pi[n] /= p_tot 

# print(pi)


