def sum_of_primes_below(n):
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(i for i, prime in enumerate(is_prime) if prime)


# Final answer for primes below 2 million
print(sum_of_primes_below(2_000_000))