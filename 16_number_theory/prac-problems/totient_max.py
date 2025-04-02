def maximize_n_over_phi(limit):
    result = 1
    prime = 2

    # Multiply primes while staying under the limit
    while result * prime <= limit:
        result *= prime
        # Go to next prime manually
        prime = next(p for p in range(prime + 1, limit) if is_prime(p))

    return result

# Helper to check if a number is prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print(maximize_n_over_phi(1_000_000))  # Output: 510510