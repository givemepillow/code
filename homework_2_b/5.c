#include <stdio.h>

int main() {
    int n, max = 0, diplomas = 0, seconds = 0;
    scanf("%d", &n);

    do {
        scanf("%d", &diplomas);
        if (diplomas > max) {
            seconds += max;
            max = diplomas;
        } else {
            seconds += diplomas;
        }
    } while (--n);

    printf("%d\n", seconds);
}