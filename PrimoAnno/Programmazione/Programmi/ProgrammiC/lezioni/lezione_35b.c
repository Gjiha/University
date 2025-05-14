#include <stdio.h>

//prototipi

void incrementa_int(int*);

//main

void main(){
	int n = 1, m = 10, x = 10;
	int d;
	char s[256] = "(123, 456)";
	
	incrementa_int(&x);
	
	printf("%d\n", x);
	
	/*d = scanf("(%d,%d)",&n,&m);		
	printf("%d, %d, %d\n", n, m, d);*/
	
	/*scanf("%s", s);
	printf("%s\n",s);*/
	
	d = sscanf(s, "(%d,%d)",&n,&m); 
	
	printf("%d, %d, %d\n", n, m, d);
}

//funzioni

void incrementa_int(int *z){
	(*z)++;
}



