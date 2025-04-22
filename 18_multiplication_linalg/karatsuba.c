#include <stdio.h>
#include <math.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

// Helper function to calculate the power of 10
int power10(int n) {
    int result = 1;
    while (n--) result *= 10;
    return result;
}

// Karatsuba recursive multiplication
long long karatsuba(long long x, long long y) {
    // Base case: for small numbers, just multiply directly
    if (x < 10 || y < 10)
        return x * y;

    // Get the size of the numbers
    int n = max(log10(x) + 1, log10(y) + 1);
    int half = n / 2;

    long long high1 = x / power10(half);
    long long low1 = x % power10(half);
    long long high2 = y / power10(half);
    long long low2 = y % power10(half);

    // Recursive steps
    long long z0 = karatsuba(low1, low2);
    long long z1 = karatsuba(low1 + high1, low2 + high2);
    long long z2 = karatsuba(high1, high2);

    return z2 * power10(2 * half) + (z1 - z2 - z0) * power10(half) + z0;
}

// Example usage
int main() {
    long long a = 31415926;
    long long b = 27182818;
    printf("Result: %lld\n", karatsuba(a, b)); // Expected: 853973398759468
    return 0;
}
