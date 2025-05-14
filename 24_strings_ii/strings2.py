# for suffix array, DUMMY character must be
# lexicographically less than all other characters
DUMMY = '$'


def kmp(pattern, text):
    m, n = len(pattern), len(text)
    # prefix function pref(s) = length of longest
    # prefix of s that is also a suffix of s

    S = pattern + DUMMY + text
    # pf[i] is pref(S[:i])
    pf = [-1] * (m + n + 1)
    for i in range(1, len(S)):
        k = pf[i - 1]  # length of pref(S[:i - 1])

        # find largest k such that
        # S[:k] == S[:i-1][-k:] and S[k] == S[i]
        # use previous values in pf to
        # check candidate prefixes quickly

        while k >= 0 and S[i] != S[k]:
            # assert S[:k] == S[:i][i - k:]
            k = pf[k]
        pf[i] = k + 1

    return pf


def closest_power_2(n):
    return 1 << (n - 1).bit_length()


def get_suffix_array(s):
    # sort suffix cyclic shifts instead of suffixes
    t = s + DUMMY
    powtwo = closest_power_2(len(t))
    n = len(t)
    
    # k = 0, compare strings of length 1
    p = [(y, x) for x, y in enumerate(t)]
    p.sort()
    pos = [0] * n
    for i in range(n):
        pos[p[i][1]] = i
    

    k = 1
    while k <= powtwo:
        comp = [0]
        for i in range(1, n):
            comp.append(comp[-1] if p[i][0] == p[i - 1][0] else comp[-1] + 1)

        # compare pairs of ints in O(1) instead of substrings themselves
        p = [((comp[pos[i]], comp[pos[(i + k) % n]]), i) for i in range(n)]
        p.sort()
        pos = [0] * n
        for i in range(n):
            pos[p[i][1]] = i
        k *= 2

    return [tup[1] for tup in p]


def get_lcp_array(s):
    # Kasai et al. algorithm
    sfx_array = get_suffix_array(s)
    s = s + DUMMY
    n = len(sfx_array)
    pos = [0] * n
    for i in range(n):
        pos[sfx_array[i]] = i

    l = [-1] * n
    k = 0
    for i in range(n):
        if pos[i] > 0:
            j = sfx_array[pos[i] - 1]
            while s[i + k] == s[j + k]:
                k += 1
            l[pos[i]] = k
            if k > 0:
                k -= 1
    return l


p = 'abb'
T = 'abbaabbab'
res = kmp(p, T)

start_idxs = [i - (2 * len(p)) for i in range(len(res)) if res[i] == len(p)]
print(start_idxs)
for j in start_idxs:
    print(T[j:j + len(p)])

S = 'banana'
ans = get_suffix_array(S)
print(ans)
for i in ans:
    print((S + DUMMY)[i:])
L = get_lcp_array(S)
print(L)