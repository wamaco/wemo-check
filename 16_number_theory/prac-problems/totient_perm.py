def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def phi(n):
    result = n
    i = 2
    while i*i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

def find_min_totient_permutation(limit):
    min_ratio = float('inf')
    best_n = -1

    for n in range(2, limit):
        phin = phi(n)
        if is_permutation(n, phin):
            ratio = n / phin
            if ratio < min_ratio:
                min_ratio = ratio
                best_n = n

    return best_n

print(find_min_totient_permutation(10_000_000))  # Final answer