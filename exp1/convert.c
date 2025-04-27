#include <stdio.h>
#include "convert.h"

int main() {
    int choice;
    double value, result;

    while (1) {
        printf("\nSelect the conversion you want to perform:\n");
        printf("1. Celsius to Fahrenheit\n");
        printf("2. Fahrenheit to Celsius\n");
        printf("3. Meters to Feet\n");
        printf("4. Feet to Meters\n");
        printf("5. Liters to Cubic Feet\n");
        printf("6. Cubic Feet to Liters\n");
        printf("7. Exit\n");
        printf("Enter your choice (1-7): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the temperature in Celsius: ");
                scanf("%lf", &value);
                result = CONVERT_C_TO_F(value);
                printf("%.2f Celsius = %.2f Fahrenheit\n", value, result);
                break;
            case 2:
                printf("Enter the temperature in Fahrenheit: ");
                scanf("%lf", &value);
                result = CONVERT_F_TO_C(value);
                printf("%.2f Fahrenheit = %.2f Celsius\n", value, result);
                break;

            case 3:
                printf("Enter the length in meters: ");
                scanf("%lf", &value);
                result = CONVERT_METRE_TO_FEET(value);
                printf("%.2f meters = %.2f feet\n", value, result);
                break;

            case 4:
                printf("Enter the length in feet: ");
                scanf("%lf", &value);
                result = CONVERT_FEET_TO_METRE(value);
                printf("%.2f feet = %.2f meters\n", value, result);
                break;

            case 5:
                printf("Enter the volume in liters: ");
                scanf("%lf", &value);
                result = CONVERT_LITRE_TO_CUBIC_FEET(value);
                printf("%.2f liters = %.2f cubic feet\n", value, result);
                break;

            case 6:
                printf("Enter the volume in cubic feet: ");
                scanf("%lf", &value);
                result = CONVERT_CUBIC_FEET_TO_LITRE(value);
                printf("%.2f cubic feet = %.2f liters\n", value, result);
                break;

            case 7:
                printf("Exiting program...\n");
                return 0;

            default:
                printf("Invalid choice! Please select between 1 and 7.\n");
                break;
        }
    }

    return 0;
}

