from math import isqrt
from itertools import product

# Simple Sieve of Eratosthenes
def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, isqrt(limit) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def count_expressible_numbers(limit):
    max_p = isqrt(limit)
    max_q = int(limit ** (1/3)) + 1
    max_r = int(limit ** (1/4)) + 1

    primes_p = generate_primes(max_p)
    primes_q = generate_primes(max_q)
    primes_r = generate_primes(max_r)

    numbers = set()

    for p in primes_p:
        p2 = p * p
        if p2 >= limit:
            break
        for q in primes_q:
            q3 = q ** 3
            if p2 + q3 >= limit:
                break
            for r in primes_r:
                r4 = r ** 4
                total = p2 + q3 + r4
                if total < limit:
                    numbers.add(total)
                else:
                    break

    return len(numbers)

print(count_expressible_numbers(50_000_000))