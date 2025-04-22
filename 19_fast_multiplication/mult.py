from cmath import cos, sin, exp, pi


def mul_brute(A, B):
    n = max(len(A), len(B))
    C = [0] * (2 * n)
    for a_i in range(len(A)):
        for b_i in range(len(B)):
            C[a_i + b_i] += A[a_i] * B[b_i]
    return C


def closest_power_2(n):
    return 1 << (n - 1).bit_length()


assert closest_power_2(1) == 1
assert closest_power_2(15) == 16
assert closest_power_2(16) == 16
assert closest_power_2(17) == 32


def fft(p, sgn):
    n = len(p)
    if n == 1:
        return p

    # if fft: exp(2j * pi / n)
    # if ifft: exp(-2j * pi / n)

    w = exp(sgn * 2j * pi / n)  # e^{\pm \frac{2 i \pi}{n}}
    p_e, p_o = p[::2], p[1::2]
    y_e, y_o = fft(p_e, sgn), fft(p_o, sgn)
    y = [0j] * n
    pw = 1
    for j in range(n // 2):
        y[j] = y_e[j] + (pw * y_o[j])
        y[j + (n // 2)] = y_e[j] - (pw * y_o[j])
        pw *= w
    return y


def mul(A, B):
    # prepare deg a + b coeff rep, use closest 2^k
    n = closest_power_2(len(A) + len(B))
    pA = [0] * n
    pB = [0] * n
    for i in range(len(A)):
        pA[i] = A[i]
    for i in range(len(B)):
        pB[i] = B[i]

    # evaluation: coeff rep -> value rep
    # evaluate on 2^k th roots of unity 
    vA, vB = fft(pA, 1), fft(pB, 1)

    # point-wise multiplication
    vC = [vA[i] * vB[i] for i in range(n)]

    # interpolation: value rep -> coeff rep
    # with scaling factor 1/n
    return [v / n for v in fft(vC, -1)]


# 1 + 2x + x^2, -1 + x^3
res = mul_brute([1, 2, 1, 0], [-1, 0, 0, 1])
print(res)
res = mul([1, 2, 1, 0], [-1, 0, 0, 1])
for n in res:
    print(f"{n:.3f}")
