
#include <stdio.h>
#include <stdlib.h>

int *append_array( int *x, int n, int e) ;
void change_array(int x[], int n) ;

void main() {

	int d[15] = {0,10,20,30,40};
	
	int i, len_d = sizeof(d)/sizeof(int);
	int *p;
	int b[10] = {1,2};
	int len_b = sizeof(b)/sizeof(int);
	int len_p = len_d ;
	
	
	change_array(d,len_d);
	
	for( i = 0; i < len_d; i++){
		printf("%d ", d[i]);
	}
	printf("\n");
	
	p = append_array( p, len_p, 100);
	if ( p != NULL) {
		
		for( i = 0; i < len_d; i++){
		printf("%d ", p[i]);		
	    }
	    printf("\n");
	    
	}
	else{
		printf("Errore di memoria\n");
		
	}	
	p = append_array(b ,len_b, 100);
}

void change_array(int x[], int n) {
	int i;
	for (i=0; i < n; i++){
		x[i] = 10*i;
	}
		
}

int *append_array( int *x, int n, int e) { 
	int i;
	int *a = malloc((n+1)*sizeof(int));
	
	if ( a != NULL){
		for( i = 0; i < n; i++ ){ //malloc non è andato a buon fine
		a[i] = x[i];
	    }
	    a[n] = e ;
	}
	
	
	free(x); //libera la memoria
	return a;
}


