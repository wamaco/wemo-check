#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Helper function to calculate the maximum of two numbers
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Pad zeros to the left of a number
char* padZeroes(char* str, int n) {
    char* result = (char*)malloc(n + 1);
    for (int i = 0; i < n; i++) {
        result[i] = '0';
    }
    result[n] = '\0';
    return result;
}

// Add two large numbers represented as strings
char* addLargeNumbers(char* num1, char* num2) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int maxLen = max(len1, len2);
    
    // Pad the shorter number with zeroes
    char* padded1 = padZeroes(num1, maxLen - len1);
    char* padded2 = padZeroes(num2, maxLen - len2);
    strcat(padded1, num1);
    strcat(padded2, num2);
    
    char* result = (char*)malloc(maxLen + 2);
    int carry = 0;

    for (int i = maxLen - 1; i >= 0; i--) {
        int sum = (padded1[i] - '0') + (padded2[i] - '0') + carry;
        result[i + 1] = (sum % 10) + '0';
        carry = sum / 10;
    }
    
    if (carry) {
        result[0] = carry + '0';
        result[maxLen + 1] = '\0';
    } else {
        result[0] = '0';
        result[maxLen + 1] = '\0';
    }
    
    free(padded1);
    free(padded2);
    return result;
}

// Multiply single-digit numbers
char* multiplySingleDigits(char a, char b) {
    int product = (a - '0') * (b - '0');
    char* result = (char*)malloc(3);
    if (product < 10) {
        result[0] = product + '0';
        result[1] = '\0';
    } else {
        result[0] = (product / 10) + '0';
        result[1] = (product % 10) + '0';
        result[2] = '\0';
    }
    return result;
}

// Karatsuba multiplication function
char* karatsuba(char* num1, char* num2) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);

    if (len1 == 1 && len2 == 1) {
        return multiplySingleDigits(num1[0], num2[0]);
    }

    int maxLen = max(len1, len2);
    int half = maxLen / 2;

    char* a = strndup(num1, len1 - half);
    char* b = strndup(num1 + len1 - half, half);
    char* c = strndup(num2, len2 - half);
    char* d = strndup(num2 + len2 - half, half);

    char* ac = karatsuba(a, c);
    char* bd = karatsuba(b, d);

    char* aPlusB = addLargeNumbers(a, b);
    char* cPlusD = addLargeNumbers(c, d);
    char* adPlusBc = karatsuba(aPlusB, cPlusD);

    // ad + bc = (a+b)(c+d) - ac - bd
    char* acPlusBd = addLargeNumbers(ac, bd);
    for (int i = 0; i < strlen(acPlusBd); i++) {
        adPlusBc[i] -= acPlusBd[i] - '0';
    }

    // Shift for final result
    int shift1 = 2 * half;
    int shift2 = half;

    char* result = addLargeNumbers(ac, adPlusBc);
    result = addLargeNumbers(result, bd);

    free(a); free(b); free(c); free(d);
    free(ac); free(bd); free(aPlusB); free(cPlusD); free(adPlusBc);
    
    return result;
}

// Main function for testing
int main() {
    char num1[1000], num2[1000];
    printf("Enter first number: ");
    scanf("%s", num1);
    printf("Enter second number: ");
    scanf("%s", num2);

    char* result = karatsuba(num1, num2);
    printf("Product: %s\n", result);

    free(result);
    return 0;
}