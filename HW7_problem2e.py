
import numpy as np




N = np.random.poisson(2*48*3, 10000)
NA = np.random.binomial(N, .5)
NB = N - NA
D = 2 * (NA - NB)

print(f"E[D(48)] = {np.mean(D)}")
print(f"Var[D(48)] = {np.var(D)}")

# this roughly matches the theoretical values: E[D(48)] = 0 & Var(D(48)) = 8λt = 1152
