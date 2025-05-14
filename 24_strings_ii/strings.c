#include <stdio.h>
#include <string.h>

#define BASE 256
#define MOD 1000000007

// Rabin–Karp: returns 1 if pattern p is found in text t, else 0
int rabin_karp(const char *p, const char *t) {
    int m = strlen(p), n = strlen(t);
    if (m > n) return 0;

    long long h_p = 0, h_t = 0, power = 1;

    // Precompute base^(m-1) % MOD
    for (int i = 0; i < m - 1; i++)
        power = (power * BASE) % MOD;

    // Compute initial hashes
    for (int i = 0; i < m; i++) {
        h_p = (h_p * BASE + p[i]) % MOD;
        h_t = (h_t * BASE + t[i]) % MOD;
    }

    for (int i = 0; i <= n - m; i++) {
        if (h_p == h_t) {
            if (strncmp(p, t + i, m) == 0)
                return 1; // Match found
        }
        if (i < n - m) {
            h_t = (h_t - t[i] * power % MOD + MOD) % MOD;
            h_t = (h_t * BASE + t[i + m]) % MOD;
        }
    }
    return 0;
}

// Compute prefix function π[] for KMP
void compute_prefix_function(const char *p, int *pi) {
    int m = strlen(p);
    pi[0] = 0;
    int i = 0;

    for (int j = 1; j < m; j++) {
        while (i > 0 && p[i] != p[j])
            i = pi[i - 1];
        if (p[i] == p[j])
            i++;
        pi[j] = i;
    }
}

// KMP: returns 1 if pattern p is found in text t, else 0
int kmp(const char *p, const char *t) {
    int m = strlen(p), n = strlen(t);
    if (m == 0) return 1;

    int pi[m];
    compute_prefix_function(p, pi);

    int i = 0;
    for (int j = 0; j < n; j++) {
        while (i > 0 && p[i] != t[j])
            i = pi[i - 1];
        if (p[i] == t[j])
            i++;
        if (i == m)
            return 1; // Match found
    }
    return 0;
}

// Example usage
int main() {
    const char *text = "abacabacabababa";
    const char *pattern = "ababa";

    printf("Rabin–Karp result: %s\n", rabin_karp(pattern, text) ? "FOUND" : "NOT FOUND");
    printf("KMP result: %s\n", kmp(pattern, text) ? "FOUND" : "NOT FOUND");

    return 0;
}