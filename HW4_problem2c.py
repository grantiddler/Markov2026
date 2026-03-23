import math

def p(i,j):
    if(i == 0):
        return int(j == 5)
    return math.comb(i,j) * (9**j) / (10**i)

def sd(i, prev = [1]): 
    sum = 0;
    for j in range(i):
        if(len(prev) < j+1):
            prev.append(sd(j, prev))
        sum += p(i,j) * prev[j]

    
    print("sd(" + str(i)+ ") = " + str(sum / (1 - p(i,i))))

    return sum / (1 - p(i,i))

# print("[")
# for i in range(6):
#     string = ""
#     for j in range(6):

        
#         string = string + " " + (" " * (8 - len(str(p(i,j))))) + str(p(i,j))[0:8] 
#     print(string + " ;")


print("]\n")

sd(5)

