#include <stdio.h>
#include <stdlib.h>

struct array_int {
	int *a;  //array di int
	int n;   //numero di elementi
	int c;   //capacità occupata
};
typedef struct array_int array_int;

array_int array_int_init(void);
array_int array_int_append(array_int, int);
array_int array_int_starter(array_int, int, int); 
array_int array_int_pop(array_int);
array_int array_int_del(array_int, int);
array_int array_int_insert(array_int, int, int);
void array_int_print(array_int);

void main() {
	array_int v = array_int_init();
	v = array_int_starter(v,6,10);
	v = array_int_insert(v, 0, 9);
	array_int_print(v);
}

array_int array_int_init(void) {
	
	array_int v = {NULL,0,0};
	
	return v;
}

array_int array_int_append (array_int v, int e) {
	
	if (v.n == v.c){
		v.a = realloc(v.a, ((2*v.c)+1)*sizeof(int));
		v.c = (2*v.c)+1;
	}
	
	v.a[v.n] = e;
	v.n++;
	
	return v;
}


array_int array_int_starter(array_int v, int val, int rip){
	
	v.a = realloc(v.a, (rip+1)*sizeof(int));
	for (int i=0; i<rip; i++){
		v.a[i] = val+i;
		
	} 
	v.n = rip;
	v.c = rip+1;
	
	return v;
	
}


array_int array_int_pop(array_int v){
	
	if (v.n > 0){
		v.n--;
		if (v.n == v.c/4){
			v.a = realloc(v.a, (v.c/2+1)*sizeof(int));
			v.c = v.c/2+1;
		}
	}
	return v;
}


array_int array_int_del(array_int v, int pos){
	
	if (pos < v.n){
		for (int i=0; i+pos < v.n-1; i++){
			
		    v.a[pos+i] = v.a[pos+i+1];
		}
			 
		v.n--;
		if (v.n == v.c/4){
			v.a = realloc(v.a, (v.c/2+1)*sizeof(int));
			v.c = v.c/2+1;
		}	
	}
	return v;
}


array_int array_int_insert(array_int v, int pos, int e){
	
	if (v.n+1 == v.c){
			
		v.a = realloc(v.a, (v.c*2+1)*sizeof(int));
		v.c = 2*v.c+1;
	}
	
	if (pos < v.n){
		
		for (int i=v.n+1; i>pos; i--){
		
		v.a[i] = v.a[i-1];
		} 
		v.a[pos] = e;
		v.n++;
	}
	
	else if (pos == v.n){
		v = array_int_append(v,e);
	}
	
	return v;
}


void array_int_print(array_int v) {
	
	printf("[");
	for (int i=0; i<v.n; i++){
		printf("%d,", v.a[i]);
	}
	printf("]\n");
}
	


