#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

// Function to compute GCD using Euclidean algorithm.
// Keep reducing until the second number becomes 0.
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

// Extended Euclidean Algorithm wrapper.
// Finds integers x and y such that ax + by = gcd(a, b).
void extended_gcd(int a, int b, int* g, int* x, int* y);

// Helper function for extended GCD using recursion and coefficient tracking.
void _extended_gcd(int a, int xa, int ya, int b, int xb, int yb, int* g, int* x, int* y) {
    if (b == 0) {
        *g = a;
        *x = xa;
        *y = ya;
    } else {
        int q = a / b;
        _extended_gcd(b, xb, yb, a - q * b, xa - q * xb, ya - q * yb, g, x, y);
    }
}

void extended_gcd(int a, int b, int* g, int* x, int* y) {
    _extended_gcd(a, 1, 0, b, 0, 1, g, x, y);
}

// Function to find all prime factors of a number.
// Instead of using generators, we store factors in an array.
int find_prime_factors(int n, int* factors) {
    int count = 0;
    int p = 2;
    while (p <= n) {
        if (p * p > n) p = n;
        while (n % p == 0) {
            factors[count++] = p;
            n /= p;
        }
        p++;
    }
    return count; // number of prime factors stored
}

// Checks if a number is prime using trial division via its smallest prime factor.
// A number is prime if its only prime factor is itself.
bool is_prime(int n) {
    if (n < 2) return false;
    int factors[64]; // enough for reasonably sized n
    return find_prime_factors(n, factors) == 1 && factors[0] == n;
}

// Sieve of Eratosthenes:
// Precomputes primes up to m. Also stores smallest prime factor for each number.
void primes(int m, bool* is_prime, int* pf) {
    for (int i = 0; i <= m; i++) {
        is_prime[i] = true;
        pf[i] = -1;
    }

    is_prime[0] = is_prime[1] = false;

    for (int n = 2; n <= m; n++) {
        if (is_prime[n]) {
            pf[n] = n;
            for (int x = 2 * n; x <= m; x += n) {
                is_prime[x] = false;
                if (pf[x] == -1) pf[x] = n;
            }
        }
    }
}

// Returns all divisors for numbers from 1 to m.
// divs[i] holds the count of divisors of i.
// Each row in the 2D array `out` holds the divisors.
void divisors(int m, int** out, int* count) {
    for (int i = 0; i <= m; i++) count[i] = 0;

    for (int d = 1; d <= m; d++) {
        for (int n = d; n <= m; n += d) {
            out[n][count[n]++] = d;
        }
    }
}

// Example usage
int main() {
    int g, x, y;
    extended_gcd(30, 20, &g, &x, &y);
    printf("gcd(30, 20) = %d; x = %d, y = %d\n", g, x, y);

    int n = 84;
    int factors[64];
    int count = find_prime_factors(n, factors);
    printf("Prime factors of %d: ", n);
    for (int i = 0; i < count; i++) printf("%d ", factors[i]);
    printf("\n");

    printf("Is %d prime? %s\n", 29, is_prime(29) ? "Yes" : "No");

    int m = 20;
    bool* is_p = malloc((m + 1) * sizeof(bool));
    int* pf = malloc((m + 1) * sizeof(int));
    primes(m, is_p, pf);
    printf("Primes up to %d: ", m);
    for (int i = 2; i <= m; i++) {
        if (is_p[i]) printf("%d ", i);
    }
    printf("\n");

    int** divs = malloc((m + 1) * sizeof(int*));
    int* div_counts = calloc(m + 1, sizeof(int));
    for (int i = 0; i <= m; i++) {
        divs[i] = malloc(32 * sizeof(int));  // assume max 32 divisors per number
    }
    divisors(m, divs, div_counts);
    printf("Divisors of %d: ", 12);
    for (int i = 0; i < div_counts[12]; i++) printf("%d ", divs[12][i]);
    printf("\n");

    // Free allocated memory
    free(is_p);
    free(pf);
    for (int i = 0; i <= m; i++) free(divs[i]);
    free(divs);
    free(div_counts);

    return 0;
}