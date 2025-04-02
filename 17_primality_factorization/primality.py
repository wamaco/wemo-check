import random
import math

# Checks if n is prime using Fermat's original test
# Warning: fails for Carmichael numbers!
def fermat_primality_test(n):
    if n <= 1:
        return False
    for a in range(2, n):  # try all a from 2 to n-1
        if pow(a, n-1, n) != 1:
            return False  # not prime
    return True

# Randomized version of Fermat test (faster, probabilistic)
# Run 'k' times to reduce error chance
def randomized_fermat_primality_test(n, k=100):
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)  # random base
        if pow(a, n, n) != a:
            return False  # composite
    return True  # probably prime

# Miller-Rabin primality test
# More reliable than Fermat, still probabilistic
def miller_rabin_primality_test(n, k=100):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Express n-1 as 2^r * d (d is odd)
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)  # random base
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue  # possibly prime
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break  # still possibly prime
        else:
            return False  # definitely composite
    return True  # probably prime

# Fermat's Factorization Method
# Works best when factors are close together
def fermat_factorization(n):
    if n % 2 == 0:
        return 2  # even number, factor is 2
    a = math.isqrt(n)
    while True:
        b2 = a*a - n
        b = math.isqrt(b2)
        if b*b == b2:
            return a - b  # found factor
        a += 1
        if a > (n + 1) // 2:
            return n  # likely prime (no nontrivial factor found)

# Pollard's Rho Algorithm for Factorization
# Uses cycle detection (like tortoise and hare)
def pollards_rho(n):
    if n % 2 == 0:
        return 2
    f = lambda x: (x*x + 1) % n  # simple polynomial function
    x, y, d = 2, 2, 1  # x = tortoise, y = hare
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)  # check for collision in mod world
    if d == n:
        return None  # failed to find factor
    return d  # found nontrivial factor
