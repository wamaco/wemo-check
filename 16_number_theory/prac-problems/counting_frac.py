def compute_totients_up_to(n):
    phi = list(range(n + 1))  # Start with phi[i] = i

    for i in range(2, n + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i

    return phi

def count_reduced_proper_fractions(limit):
    phi = compute_totients_up_to(limit)
    return sum(phi[2:])  # Skip phi[0] and phi[1]