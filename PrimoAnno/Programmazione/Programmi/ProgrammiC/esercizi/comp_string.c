
#include <stdio.h>
#include <stdlib.h>

//prototipi

int str_cmp(char *a, char *b);

//funzione

void main(){
	
	char a[] = "programmazione";
	char b[] = "non";
	char *p;
	char *q;
	
	p = a;
	q = b;
	
	int c = str_cmp( p, q );
	printf("%d\n",c);
	
	int f = str_cmp( q, p );
	printf("%d\n",f);
	
}

int str_cmp(char *a, char *b) {
	
	int i = 0;
	int x = 0 ,y = 0;
	
	while (a[i] != '\0' && b[i] != '\0'){
		
		if ( a[i] > b[i] ) {			
			x++;
		}
					
		else {
			y++;
		}
		i++;
	}
	
	if (a[i] == '\0'){
		while (b[i] != '\0'){
			y++;
			i++;
		}
	}
	else{
		while (a[i] != '\0'){
			x++;
			i++;
		}
	}
	
	if ( x > y ) {
		return 1;
	}
	else if ( x < y ) {
		return -1;
	}
	else if ( x == y ) {
		return 0;
	}
}



	
	
		
		
				
	



