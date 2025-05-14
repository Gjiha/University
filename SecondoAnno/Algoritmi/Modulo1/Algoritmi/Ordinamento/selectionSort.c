#include <stdio.h>
#include <stdlib.h>

typedef struct array_int {
    int *array;
    int len;
} array_int;

void selectionSort(array_int *L) {

    for (int k = 0; k < (L->len - 1); k++) {

        int m = k;
        for (int j = k + 1; j < (L->len); j++) {

            if (L->array[j] < L->array[m]) {

                int p = L->array[m];
                L->array[m] = L->array[j];
                L->array[j] = p;
            }
        }
    }
}

void printArray(array_int L) {
    printf("[");
    for (int i = 0; i < L.len; i++) {
        printf("%d, ", L.array[i]);
    }
    printf("]\n");
}

int main(int argc, char *argv[]) {

    array_int L = {NULL, 10};
    L.array = malloc(sizeof(int) * L.len);

    int init_array[] = {9, 8, 6, 5, 3, 0, 2, 4, 7, 1};
    for (int i = 0; i < 10; i++) {
        L.array[i] = init_array[i];
    }

    selectionSort(&L);
    printArray(L);

    return 0;
}
