#include <stdio.h>
#include <stdlib.h>

struct array_float {
	float *a;  //array di int
	int n;   //numero di elementi
	int c;   //capacità occupata
};
typedef struct array_float array_float;

array_float array_float_init(void);
array_float array_float_append(array_float, float);
array_float array_float_starter(array_float, float, int);
array_float array_float_pop(array_float);
array_float array_float_del(array_float, int);
array_float array_float_insert(array_float, int, float);
void array_float_print(array_float);

void main() {
	
}

array_float array_float_init(void) {
	
	array_float v = {NULL,0,0};
	
	return v;
}

array_float array_float_append (array_float v, float e) {
	
	if (v.n == v.c){
		v.a = realloc(v.a, ((2*v.c)+1)*sizeof(float));
		v.c = (2*v.c)+1;
	}
	
	v.a[v.n] = e;
	v.n++;
	
	return v;
}


array_float array_float_starter(array_float v, float val, int rip){
	
	v.a = realloc(v.a, (rip+1)*sizeof(float));
	for (int i=0; i<rip; i++){
		v.a[i] = val+i;
		
	} 
	v.n = rip;
	v.c = rip+1;
	
	return v;
	
}


array_float array_float_pop(array_float v){
	
	if (v.n > 0){
		v.n--;
		if (v.n == v.c/4){
			v.a = realloc(v.a, (v.c/2+1)*sizeof(float));
			v.c = v.c/2+1;
		}
	}
	return v;
}


array_float array_float_del(array_float v, int pos){
	
	if (pos < v.n){
		for (int i=0; i+pos < v.n-1; i++){
			
		    v.a[pos+i] = v.a[pos+i+1];
		} 
		v.n--;
		
		if (v.n == v.c/4){
			v.a = realloc(v.a, (v.c/2+1)*sizeof(float));
			v.c = v.c/2+1;
		}	
	}
	return v;
}


array_float array_float_insert(array_float v, int pos, float e){
	
	if (v.n+1 == v.c){
			
		v.a = realloc(v.a, (v.c*2+1)*sizeof(float));
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
		v = array_float_append(v,e);
	}
	
	
	return v;
	
}


void array_float_print(array_float v) {
	
	printf("[");
	for (int i=0; i<v.n; i++){
		printf("%f,", v.a[i]);
	}
	printf("]\n");
}
	
