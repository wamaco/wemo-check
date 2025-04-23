#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void add_poly(int* a, int* b, int* res, int n) {
    for (int i = 0; i < n; i++)
        res[i] = a[i] + b[i];
}

void sub_poly(int* a, int* b, int* res, int n) {
    for (int i = 0; i < n; i++)
        res[i] = a[i] - b[i];
}

void poly_multiply(int* p, int* q, int* res, int n) {
    if (n == 1) {
        res[0] = p[0] * q[0];
        return;
    }

    int m = n / 2;
    int *low_p = p;
    int *high_p = p + m;
    int *low_q = q;
    int *high_q = q + m;

    int* z0 = calloc(2 * m, sizeof(int));
    int* z1 = calloc(2 * m, sizeof(int));
    int* z2 = calloc(2 * m, sizeof(int));
    int* sum_p = calloc(m, sizeof(int));
    int* sum_q = calloc(m, sizeof(int));
    int* temp1 = calloc(2 * m, sizeof(int));

    poly_multiply(low_p, low_q, z0, m);
    poly_multiply(high_p, high_q, z2, m);

    add_poly(low_p, high_p, sum_p, m);
    add_poly(low_q, high_q, sum_q, m);
    poly_multiply(sum_p, sum_q, temp1, m);
    sub_poly(temp1, z0, temp1, 2 * m);
    sub_poly(temp1, z2, z1, 2 * m);

    memset(res, 0, sizeof(int) * 2 * n);
    for (int i = 0; i < 2 * m; i++) res[i] += z0[i];
    for (int i = 0; i < 2 * m; i++) res[i + m] += z1[i];
    for (int i = 0; i < 2 * m; i++) res[i + 2 * m] += z2[i];

    free(z0); free(z1); free(z2); free(sum_p); free(sum_q); free(temp1);
}