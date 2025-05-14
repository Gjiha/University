#include <stdlib.h>
#include <stdio.h>

struct array {
  float *a;
  int n;
};

typedef struct array array;

int main() {
  array *p;
  p = malloc(sizeof(array));
  p->n = 0; // Inizializza il numero di elementi a 0
  p->a = NULL; // Inizializza l'array a NULL
  
  for (int i = 0; i < 5; i++) {
    p->a = realloc(p->a, sizeof(float) * i); // Realloca l'array con la nuova dimensione
    p->n = sizeof(p->a);
    printf("%d\n",p->n);
    
  }

  return 0;
}