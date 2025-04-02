# Computes the Greatest Common Divisor (GCD) of a and b using the Euclidean algorithm.
# Basically: keep doing a % b until b becomes 0.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Extended Euclidean Algorithm:
# Not only computes gcd(a, b), but also finds integers X and Y such that:
#     aX + bY = gcd(a, b)
# This is super useful for solving Diophantine equations and computing modular inverses.
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (y * (a // b))


# Solves ax + by = c for integers x and y (if possible).
# Returns (x, y) if there’s a solution, else (None, None).
# Key: a solution exists if and only if c is divisible by gcd(a, b).
def diophantine(a, b, c):
    g, x, y = extended_gcd(a, b)
    if c % g == 0:
        k = c // g
        return x * k, y * k
    else:
        return None, None


# Classic Sieve of Eratosthenes to find all primes from 2 to n.
# Also returns lpf[i] = the smallest prime factor of i.
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    lpf = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False
                lpf[j] = i

    return sieve, lpf


# Returns the prime factors of n using the precomputed smallest prime factors from the sieve.
# Repeated prime factors are included (e.g., 12 -> [2, 2, 3]).
def prime_factors(n):
    l = []
    _, lpf = sieve_of_eratosthenes(n)
    while n > 1:
        l.append(lpf[n])
        n //= lpf[n]
    return l


# Precomputes all divisors for numbers in the range [1, n].
# divs[k] gives you a list of all divisors of k.
def divisor_sieve(n):
    divs = [[] for _ in range(n + 1)]
    for d in range(1, n + 1):
        for k in range(d, n + 1, d):
            divs[k].append(d)
    return divs


# Computes Euler's Totient Function φ(n)
# Counts how many integers from 1 to n-1 are coprime with n.
# This version uses the divisor sieve (not the most efficient).
def totient(n):
    divs_n = divisor_sieve(n)
    return n - len(divs_n[n]) + 1


# Computes the modular inverse of a mod n:
# Returns a number a' such that (a * a') % n = 1
# Assumes that gcd(a, n) = 1 (i.e., a and n are coprime).
def mod_inv(a, n):
    g, x, y = extended_gcd(a, n)
    assert a * x + n * y == 1  # Sanity check
    return x


# Chinese Remainder Theorem (CRT) for 2 equations:
# Given: x ≡ a mod m, x ≡ b mod n with gcd(m, n) = 1
# Returns: the unique solution x mod (m*n)
def crt(a, m, b, n):
    assert gcd(m, n) == 1
    r = (b - a) * mod_inv(m, n) % n
    return a + r * m, m * n


# Sample assertions for testing:
assert diophantine(12, 8, 68) == (17, -17)
assert totient(22) == 19
# print(prime_factors(2 * 3 * 5 * 7 * 9 * 11 * 13))
# print(mod_inv(12, 7))
# print(crt(9, 12, 6, 7))