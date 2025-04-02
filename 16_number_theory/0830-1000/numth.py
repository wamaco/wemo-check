# Classic Euclidean algorithm to find the Greatest Common Divisor (GCD) of two numbers.
# If b is 0, a is the GCD. Otherwise, recursively apply gcd(b, a % b).
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


# Wrapper for the extended Euclidean algorithm.
# Returns not just the GCD of a and b, but also integers x and y such that: ax + by = gcd(a, b)
def extended_gcd(a, b):
    return _extended_gcd(a, 1, 0, b, 0, 1)


# Helper function that performs the actual extended Euclidean algorithm using recursion.
# It keeps track of coefficients for a and b (xa, ya, xb, yb) so we can find x and y in ax + by = gcd(a, b).
def _extended_gcd(a, xa, ya, b, xb, yb):
    if b == 0:
        return a, xa, ya
    else:
        q = a // b
        return _extended_gcd(b, xb, yb, a - q * b, xa - q * xb, ya - q * yb)


# Generates the prime factors of n (with repetition), one by one, starting from 2.
# It's not the fastest method, but it avoids checking factors bigger than sqrt(n).
def find_prime_factors(n):
    p = 2
    while p <= n:
        if p**2 > n:
            p = n
        while n % p == 0:
            n //= p
            yield p
        p += 1


# Checks if a number is prime using the `find_prime_factors` generator.
# A number is prime if the first (and only) prime factor returned is the number itself.
def is_prime(n):
    return n >= 2 and next(find_prime_factors(n)) == n


# Uses the Sieve of Eratosthenes to find all primes up to m.
# Returns two lists:
# - is_prime[i] tells you if i is prime.
# - pf[i] tells you the smallest prime factor of i.
def primes(m):
    if m < 2:
        raise ValueError
    is_prime = [True]*(m + 1)
    is_prime[0] = is_prime[1] = False

    pf = [None]*(m + 1)

    for n in range(2, m + 1):
        if is_prime[n]:
            pf[n] = n
            for x in range(2 * n, m + 1, n):
                is_prime[x] = False
                pf[x] = n

    return is_prime, pf


# Returns a list of all divisors for every number from 1 to m.
# divs[n] will contain all numbers that divide n exactly.
def divisors(m):
    divs = [[] for _ in range(m + 1)]

    for d in range(1, m + 1):
        for n in range(d, m + 1, d):
            divs[n].append(d)

    return divs