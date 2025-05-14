# KMP1: Returns True if pattern p is a substring of text t, else False
def kmp1(p, t):
    if not p: return True  # Empty pattern is always a substring

    def prefix_function(p):
        m = len(p)
        pi = [0] * m
        i = 0
        for j in range(1, m):
            while i > 0 and p[i] != p[j]:
                i = pi[i - 1]
            if p[i] == p[j]:
                i += 1
            pi[j] = i
        return pi

    pi = prefix_function(p)
    i = 0  # current match length
    for c in t:
        while i > 0 and p[i] != c:
            i = pi[i - 1]
        if p[i] == c:
            i += 1
        if i == len(p):
            return True
    return False


# KMP2: Returns a list of all starting indices where pattern p occurs in text t
def kmp2(p, t):
    result = []
    if not p: return list(range(len(t) + 1))  # Match everywhere

    def prefix_function(p):
        m = len(p)
        pi = [0] * m
        i = 0
        for j in range(1, m):
            while i > 0 and p[i] != p[j]:
                i = pi[i - 1]
            if p[i] == p[j]:
                i += 1
            pi[j] = i
        return pi

    pi = prefix_function(p)
    i = 0
    for j in range(len(t)):
        while i > 0 and p[i] != t[j]:
            i = pi[i - 1]
        if p[i] == t[j]:
            i += 1
        if i == len(p):
            result.append(j - len(p) + 1)
            i = pi[i - 1]
    return result


# KMP3: Returns the prefix function (pi array) of pattern p
def kmp3(p):
    m = len(p)
    pi = [0] * m
    i = 0
    for j in range(1, m):
        while i > 0 and p[i] != p[j]:
            i = pi[i - 1]
        if p[i] == p[j]:
            i += 1
        pi[j] = i
    return pi


# KMP4: Computes the next match state given current state i and input char c
def kmp4(i, c, p, pi):
    while i > 0 and p[i] != c:
        i = pi[i - 1]
    if p[i] == c:
        i += 1
    return i


# KMP5: Uses next_match (kmp4-style) for checking if p is a substring of t
def kmp5(p, t):
    if not p: return True
    pi = kmp3(p)
    i = 0
    for c in t:
        i = kmp4(i, c, p, pi)
        if i == len(p):
            return True
    return False


# Example usage
if __name__ == "__main__":
    text = "abacabacabababa"
    pattern = "ababa"

    print("kmp1:", kmp1(pattern, text))        # True
    print("kmp2:", kmp2(pattern, text))        # [4, 10]
    print("kmp3:", kmp3(pattern))              # [0, 0, 1, 2, 3]
    print("kmp4:", kmp4(3, 'b', pattern, kmp3(pattern)))  # 4
    print("kmp5:", kmp5(pattern, text))        # True