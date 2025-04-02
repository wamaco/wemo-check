from math import gcd

def count_fractions_between(limit):
    count = 0
    for d in range(2, limit + 1):
        # 1/3 < a/d < 1/2 ⇒ ceil(d/3) < a < floor(d/2)
        for a in range(d // 3 + 1, (d + 1) // 2):
            if gcd(a, d) == 1:
                count += 1
    return count