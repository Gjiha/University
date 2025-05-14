
#include <stdio.h>
#include <stdlib.h>

struct array_float {
	float *a;
	int n;
	int c;
};
typedef struct array_float array_float;

array_float array_init (void);
array_float array_delete(array_float v, int pos);
void array_print ( array_float v );

void main() {
	array_float v = array_init();
	float c[4] = {1.5,2.5,3.5,4.5};
	v.a = c;
	v.n = 4;
	v.c = 3;
	
	v = array_delete( v, 1 );
	
    array_print ( v );
	
	
	
}

array_float array_init (void) {
	
	array_float v = {NULL, 0 ,0};
	return v;
}


array_float array_delete ( array_float v, int pos ) {
	
	int i = 0;
	float *a;
	int j = pos+1;
	
	a = malloc( (v.n)*sizeof(float) );
	while ( i < pos ) {
		a[i] = v.a[i];
		i++;
	}
	while ( j < v.n ) {
		a[j-1] = v.a[j];
		j++;
	}
	
	v.a = a;
	v.c = v.n+1;
	v.n--;
	return v;
	
}


void array_print ( array_float v ) {
    
    printf("[");
    
    for ( int i = 0; i < v.n; i++ ){
        printf("%.2f, ",v.a[i]);        
    }
    printf("]\n");
    
}

