#include <stdlib.h> // only for malloc and free

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
    int* z0 = (int*)calloc(2 * m, sizeof(int));
    int* z1 = (int*)calloc(2 * m, sizeof(int));
    int* z2 = (int*)calloc(2 * m, sizeof(int));
    int* sum_p = (int*)calloc(m, sizeof(int));
    int* sum_q = (int*)calloc(m, sizeof(int));
    int* temp = (int*)calloc(2 * m, sizeof(int));

    poly_multiply(p, q, z0, m);
    poly_multiply(p + m, q + m, z2, m);

    add_poly(p, p + m, sum_p, m);
    add_poly(q, q + m, sum_q, m);
    poly_multiply(sum_p, sum_q, temp, m);
    sub_poly(temp, z0, temp, 2 * m);
    sub_poly(temp, z2, z1, 2 * m);

    for (int i = 0; i < 2 * m; i++) res[i] += z0[i];
    for (int i = 0; i < 2 * m; i++) res[i + m] += z1[i];
    for (int i = 0; i < 2 * m; i++) res[i + 2 * m] += z2[i];

    free(z0);
    free(z1);
    free(z2);
    free(sum_p);
    free(sum_q);
    free(temp);
}