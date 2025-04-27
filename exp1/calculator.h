#include <math.h>
#include <stdio.h>

void add(int a, int b) {
    printf("The sum of %d and %d is: %d\n", a, b, a + b);
}

void subtract(int a, int b) {
    printf("The subtraction of %d and %d is: %d\n", a, b, a - b);
}

void multiply(int a, int b) {
    printf("The multiplication of %d and %d is: %d\n", a, b, a * b);
}

void division(int a, int b) {
    
        printf("The division of %d by %d is: %d\n", a, b, a / b);
    }

void square(int a) {
    printf("The square of %d is: %d\n", a, a * a);
}

void sqr_root(int a) {
    
        printf("The square root of %d is: %.2f\n", a, sqrt(a));
    }

void cb_root(double a) {
    printf("The cube root of %.2f is: %.2f\n", a, cbrt(a));
}