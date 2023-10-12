

// Instructions
// Using a function in C, find the minimum and the maximum numbers of a set of values (with no more than 15 entries) and return the output in the form of an array. For example:
//
// If your input is the following 6 numbers:
// 46
// 78
// 22
// 13
// 9
// 38
//
// The expected output of your program would be: 
//
// Numbers entered: 6
// Minimum number is: 9
// Maximum number is: 78
//
//   gcc c_skills_programming_lab_5.c -o min_max_program


#include <stdio.h>

#define MAX_ENTRIES 15

void findMinMax(int arr[], int n, int* min, int* max) {
    *min = arr[0];
    *max = arr[0];
    
    for (int i = 1; i < n; ++i) {
        if (arr[i] < *min) {
            *min = arr[i];
        }
        if (arr[i] > *max) {
            *max = arr[i];
        }
    }
}

int main() {
    int n, arr[MAX_ENTRIES], min, max;

    printf("Enter the number of values (no more than 15): ");
    scanf("%d", &n);

    if (n > MAX_ENTRIES || n <= 0) {
        printf("Invalid number of entries!\n");
        return 1;
    }
    
    printf("Enter %d numbers:\n", n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }

    findMinMax(arr, n, &min, &max);
    
    printf("Numbers entered: %d\n", n);
    printf("Minimum number is: %d\n", min);
    printf("Maximum number is: %d\n", max);
    
    return 0;
}
