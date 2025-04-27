#include <stdio.h>
#include "Calculator.h"

int input() {
    int number;
    scanf("%d", &number);
    return number;
}

int main() {
    int a, b;
    int choice;
    double num;

    while (1) {
        printf("\n1. Perform addition\n");
        printf("2. Perform subtraction\n");
        printf("3. Perform multiplication\n");
        printf("4. Perform division\n");
        printf("5. Square a number\n");
        printf("6. Find square root\n");
        printf("7. Find cube root\n");
        printf("8. Exit\n");

        printf("Enter your choice: ");
        choice = input();

        switch (choice) {
            case 1:
                printf("Enter the numbers to be added: ");
                scanf("%d %d", &a, &b);
                add(a, b);
                break;

            case 2:
                printf("Enter the numbers to be subtracted: ");
                scanf("%d %d", &a, &b);
                subtract(a, b);
                break;

            case 3:
                printf("Enter the numbers to be multiplied: ");
                scanf("%d %d", &a, &b);
                multiply(a, b);
                break;

            case 4:
                printf("Enter the numbers to be divided: ");
                scanf("%d %d", &a, &b);
                division(a, b);
                break;

            case 5:
                printf("Enter the number to be squared: ");
                scanf("%d", &a);
                square(a);
                break;

            case 6:
                printf("Enter the number to find the square root: ");
                scanf("%d", &a);
                sqr_root(a);
                break;

            case 7:
                printf("Enter the number to find the cube root: ");
                scanf("%lf", &num);
                cb_root(num);
                break;

            case 8:
                printf("Exiting program...\n");
                return 0;

            default:
                printf("Wrong input! Please enter a number between 1 and 8.\n");
                break;
        }
    }

    return 0;
}







