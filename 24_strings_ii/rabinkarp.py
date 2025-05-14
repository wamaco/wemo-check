# Version 1: Check if a pattern exists in the text at least once
# Returns True if the pattern `p` is found in text `t`, else False
def is_substring(p, t):
    n = len(t)
    m = len(p)
    if m > n:
        return False

    base = 256
    mod = 10**9 + 7
    base_m = pow(base, m - 1, mod)

    def hash_string(s):
        h = 0
        for c in s:
            h = (h * base + ord(c)) % mod
        return h

    h_p = hash_string(p)
    h_t = hash_string(t[:m])

    for i in range(n - m + 1):
        if h_t == h_p:
            if t[i:i + m] == p:
                return True
        if i < n - m:
            h_t = (h_t - ord(t[i]) * base_m) % mod
            h_t = (h_t * base + ord(t[i + m])) % mod
            h_t = (h_t + mod) % mod

    return False


# Version 2: Count how many times the pattern appears in the text
# Returns an integer count of how many times `p` appears in `t`
def is_substring2(p, t):
    n = len(t)
    m = len(p)
    if m > n:
        return 0

    base = 256
    mod = 10**9 + 7
    base_m = pow(base, m - 1, mod)

    def hash_string(s):
        h = 0
        for c in s:
            h = (h * base + ord(c)) % mod
        return h

    h_p = hash_string(p)
    h_t = hash_string(t[:m])
    count = 0

    for i in range(n - m + 1):
        if h_t == h_p:
            if t[i:i + m] == p:
                count += 1
        if i < n - m:
            h_t = (h_t - ord(t[i]) * base_m) % mod
            h_t = (h_t * base + ord(t[i + m])) % mod
            h_t = (h_t + mod) % mod

    return count


# Version 3: Return all positions where the pattern appears
# Returns a list of starting indices in `t` where `p` occurs
def is_substring3(p, t):
    n = len(t)
    m = len(p)
    if m > n:
        return []

    base = 256
    mod = 10**9 + 7
    base_m = pow(base, m - 1, mod)

    def hash_string(s):
        h = 0
        for c in s:
            h = (h * base + ord(c)) % mod
        return h

    h_p = hash_string(p)
    h_t = hash_string(t[:m])
    result = []

    for i in range(n - m + 1):
        if h_t == h_p:
            if t[i:i + m] == p:
                result.append(i)
        if i < n - m:
            h_t = (h_t - ord(t[i]) * base_m) % mod
            h_t = (h_t * base + ord(t[i + m])) % mod
            h_t = (h_t + mod) % mod

    return result