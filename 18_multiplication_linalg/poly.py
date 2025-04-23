def poly_add(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]

def poly_sub(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) - (q[i] if i < len(q) else 0) for i in range(n)]

def pad(poly, length):
    return poly + [0] * (length - len(poly))

def poly_multiply(p, q):
    n = max(len(p), len(q))
    if n == 1:
        return [p[0] * q[0]]

    m = (n + 1) // 2
    p = pad(p, 2 * m)
    q = pad(q, 2 * m)

    low_p, high_p = p[:m], p[m:]
    low_q, high_q = q[:m], q[m:]

    z0 = poly_multiply(low_p, low_q)
    z2 = poly_multiply(high_p, high_q)
    z1 = poly_multiply(poly_add(low_p, high_p), poly_add(low_q, high_q))
    z1 = poly_sub(poly_sub(z1, z0), z2)

    # combine results
    result = [0] * (4 * m)
    for i in range(len(z0)): result[i] += z0[i]
    for i in range(len(z1)): result[i + m] += z1[i]
    for i in range(len(z2)): result[i + 2 * m] += z2[i]

    return result[:2 * n - 1]