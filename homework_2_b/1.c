#include <stdio.h>
#include <limits.h>

int main() {
    int max = INT_MIN;
    int count = 0;
    int value = 1;

    while (value != 0) {
       scanf("%d", &value);
       if (value > max) {
           max = value;
           count = 0;
       }
       if (max == value) ++count;
    }

    printf("%d\n", count);
}