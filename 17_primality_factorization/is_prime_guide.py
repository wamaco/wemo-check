from random import randrange

# Brute-force primality test:
# Checks if n is divisible by any number from 2 up to n-1.
# Super slow for large n, but useful for validation.
def is_prime_brute(n):
    return n >= 2 and not any(n % d == 0 for d in range(2, n))


# Miller-Rabin primality test (probabilistic):
# Returns True if n is *probably* prime, False if definitely composite.
# The higher the value of `c`, the more accurate it is.
def is_prime(n, c=100):
    if n < 2:
        return False

    # Quick check for small divisors like 2 (just 2 here)
    for p in 2,:
        if n == p:
            return True
        if n % p == 0:
            return False

    # Write n - 1 as 2^k * m, where m is odd
    (k, m) = (0, n - 1)
    while m % 2 == 0:
        k += 1
        m //= 2

    # Just for sanity check, not necessary in production code
    assert n - 1 == 2**k * m
    assert k > 0
    assert m % 2 != 0

    # One round of the Miller-Rabin test using base a
    def mr_test(a):
        x = pow(a, m, n)  # a^m mod n
        for _ in range(k):
            if x == 1 or x == n - 1:
                return True
            if (x := x * x % n) == 1:
                return False
        return False

    # Run the test `c` times with random bases from [2, n-1]
    return all(mr_test(randrange(2, n)) for _ in range(c))


# Simple test suite that checks all integers from -10,000 to 10,000.
# Compares the output of Miller-Rabin with brute-force to verify correctness.
def test():
    N = 10**4
    for n in range(-N, N + 1):
        print(n, is_prime(n))
        assert is_prime_brute(n) == is_prime(n)

# Entry point for running the test when this file is executed directly
if __name__ == '__main__':
    test()