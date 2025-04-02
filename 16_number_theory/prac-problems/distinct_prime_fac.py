def first_k_consecutive_with_k_prime_factors(k, limit=1000000):
    # Step 1: Create an array to count distinct prime factors for every number
    factor_count = [0] * (limit + 1)

    # Modified Sieve of Eratosthenes: for each prime p, mark all multiples of p
    for p in range(2, limit + 1):
        if factor_count[p] == 0:  # p is prime
            for multiple in range(p, limit + 1, p):
                factor_count[multiple] += 1

    # Step 2: Search for k consecutive numbers with exactly k distinct prime factors
    consecutive = 0
    for i in range(2, limit + 1):
        if factor_count[i] == k:
            consecutive += 1
            if consecutive == k:
                return i - k + 1  # start of the sequence
        else:
            consecutive = 0

    return -1  # not found within the limit