#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    float f = 0;

    for (int i = 1; i < argc; i++) {
        float n;
        if (sscanf(argv[i], "%f", &n) == 1) {
            f += n;
        }
    }

    printf("%f\n", f);

    return 0;
}