#include <stdio.h>

// Count the number of digits in a number
int count_digits(long long x) {
    int count = 0;
    while (x > 0) {
        count++;
        x /= 10;
    }
    return count;
}

// Compute 10 raised to the power of n (integer only)
long long power10(int n) {
    long long result = 1;
    for (int i = 0; i < n; i++)
        result *= 10;
    return result;
}

long long karatsuba(long long x, long long y) {
    if (x < 10 || y < 10)
        return x * y;

    int n = count_digits(x > y ? x : y);
    int half = n / 2;

    long long p = power10(half);

    long long high1 = x / p;
    long long low1  = x % p;
    long long high2 = y / p;
    long long low2  = y % p;

    long long z0 = karatsuba(low1, low2);
    long long z1 = karatsuba((low1 + high1), (low2 + high2));
    long long z2 = karatsuba(high1, high2);

    return z2 * power10(2 * half) + (z1 - z2 - z0) * p + z0;
}

int main() {
    long long a = 31415926;
    long long b = 27182818;

    printf("Karatsuba result: %lld\n", karatsuba(a, b));  // should print 853973398759468

    return 0;
}
