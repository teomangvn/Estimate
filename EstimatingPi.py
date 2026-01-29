#Teoman Guven 23050151039
import numpy as np
import random
import time
from scipy.stats import norm

def estimate_pi(N, rng_func):
    x = rng_func(N)
    y = rng_func(N)
    inside = np.sum(x**2 + y**2 <= 1.0)
    pi_estimate = 4 * inside / N
    return pi_estimate

def rng_uniform(N):
    return np.random.uniform(0, 1, N)

def rng_rand(N):
    return np.random.rand(N)

def rng_randn(N):
    z = np.random.randn(N)
    return norm.cdf(z)  # Transform to uniform [0,1]

def rng_system_random(N):
    return np.array([random.SystemRandom().uniform(0, 1) for _ in range(N)])

def rng_power(N):
    return np.random.power(1, N)

def rng_poisson(N):
    lam = 1
    max_value = 10
    x = np.random.poisson(lam, N)
    return x / max_value  # Normalize to [0,1]

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
    print(f"\nEstimating Pi with N = {N}")
    for name, func in rng_functions.items():
        start_time = time.time()
        pi_est = estimate_pi(int(N), func)
        elapsed_time = time.time() - start_time
        error = abs(np.pi - pi_est)
        print(f"{name}: Pi ≈ {pi_est:.6f}, Error = {error:.6f}, "
              f"Time = {elapsed_time:.4f}s")
