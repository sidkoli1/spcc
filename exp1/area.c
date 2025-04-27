#include <stdio.h>
#include "Area.h"  // Assuming AREA_SQUARE, AREA_RECTANGLE, AREA_TRIANGLE, and AREA_CIRCLE are defined in this file.

int main() {
    int choice;
    int side, length, breadth, base, height, radius;

    while (1) {
        printf("\nSelect the shape to calculate the area:\n");
        printf("1. Square\n");
        printf("2. Rectangle\n");
        printf("3. Triangle\n");
        printf("4. Circle\n");
        printf("5. Exit\n");
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1: {
                printf("Enter the side length of the square: ");
                scanf("%d", &side);
                printf("Area of Square: %d\n", AREA_SQUARE(side));
                break;
            }
            
            case 2: {
                printf("Enter the length and breadth of the rectangle: ");
                scanf("%d %d", &length, &breadth);
                printf("Area of Rectangle: %d\n", AREA_RECTANGLE(length, breadth));
                break;
            }
            
            case 3: {
                printf("Enter the base and height of the triangle: ");
                scanf("%d %d", &base, &height);
                printf("Area of Triangle: %.2f\n", AREA_TRIANGLE(base, height));
                break;  // This break was missing
            }
            
            case 4: {
                printf("Enter the radius of the circle: ");
                scanf("%d", &radius);
                printf("Area of Circle: %.2f\n", AREA_CIRCLE(radius));
                break;
            }
            
            case 5: {
                printf("Exiting program...\n");
                return 0;
            }
            
            default: {
                printf("Invalid choice! Please enter a number between 1 and 5.\n");
                break;
            }
        }
    }

    return 0;
}
