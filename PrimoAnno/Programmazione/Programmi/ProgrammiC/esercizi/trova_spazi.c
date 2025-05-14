#include <stdio.h>
#include <stdlib.h>

//tipi

struct array_int {
	int *a; // puntatore array
	int n; // numero di elementi
	int c; // capacità del puntatore array
};
typedef struct array_int array_int;

//prototipi

void print_array ( array_int v );
array_int array_init (void);
array_int trova_spazi(char *a);  // !!
array_int append_( array_int v, int e );

//funzioni

void main(){
	
	char a[] = "";
	char *p = a;
	array_int c = trova_spazi(p);
	print_array(c);
	
}


array_int append( array_int v, int e ){
	int i;
	int *a;
	
	if (  v.n == v.c ){
		a = malloc((2*v.c+1)*sizeof(int));
		if (a == NULL)
			return v;
		
		for(i = 0; i < v.n; i++){
			a[i] = v.a[i]; 
		}
		v.c = 2*v.c+1;
		free(v.a);
		v.a = a;
	}
	v.a[v.n] = e;
	v.n++;
	
	return v;
}


array_int array_init (void) {
	array_int v = {NULL,0,0};
	return v;
}

	
void print_array ( array_int v ) {
	
	for (int i = 0; i < v.n; i++){
		
		printf(" %d,",v.a[i]);
		
	}
	
	printf("\n");
	
}


array_int trova_spazi(char *a) {
	
	array_int v = {NULL, 0, 0};
	
	int i = 0;
	int b = 0; 
	
	while ( a[i] != '\0' ) {
		if (a[i] == ' ') {
			v = append (v, i);
		}
		b++;
		i++;
	}
	
	if (b != 0) {
		return v;
	}
	else {
		printf("la stringa non contiene nulla");
		return v;
	}
}

	
