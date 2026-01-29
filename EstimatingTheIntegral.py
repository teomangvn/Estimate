#Teoman Guven 23050151039
import numpy as np
import random
import time
from scipy.stats import norm

def estimate_integral(N, rng_func):
    x = rng_func(N) * np.pi # Generate random points in the interval 0 to pi
    y = np.sin(x)
    integral_estimate = np.pi * np.mean(y) #sin(x)
    return integral_estimate

def rng_uniform(N):
    return np.random.uniform(0, 1, N)

def rng_rand(N):
    return np.random.rand(N)

def rng_randn(N):
    z = np.random.randn(N) # Use CDF to transform values from randn to [0,1]
    return norm.cdf(z)

def rng_system_random(N):
    return np.array([random.SystemRandom().uniform(0, 1) for _ in range(N)])

def rng_power(N):
    return np.random.power(1, N)

def rng_poisson(N):
    lam = 1
    max_value = 10
    x = np.random.poisson(lam, N)
    return x / max_value

N_values = [10**3, 10**4, 10**5]
rng_functions = {
    'np.random.uniform': rng_uniform,
    'np.random.rand': rng_rand,
    'np.random.randn (CDF)': rng_randn,
    'random.SystemRandom': rng_system_random,
    'np.random.power': rng_power,
    'np.random.poisson': rng_poisson
}

for N in N_values:
    print(f"\nEstimating Integral with N = {N}")
    for name, func in rng_functions.items():
        start_time = time.time()
        integral_est = estimate_integral(int(N), func)
        elapsed_time = time.time() - start_time
        error = abs(2.0 - integral_est)  # The integral result is 2
        print(f"{name}: Integral ≈ {integral_est:.6f}, Error = {error:.6f}, "
              f"Time = {elapsed_time:.4f}s")
