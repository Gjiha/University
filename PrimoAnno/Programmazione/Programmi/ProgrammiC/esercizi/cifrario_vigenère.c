#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void cifra (char[], char[]);

void main(){
	char a[] = "rapportoimmeddiato";
	char v[] = "verme";
	cifra(a,v);
	printf("%s\n",a);
}

void cifra(char a[], char v[]){
	
	int i = 0, j = 0;
	int n;
	int r;
	while (a[i] != '\0'){
		
		if (v[j] == '\0'){
			j = 0;
		}
		n = a[i] + v[j];
		r = n/26;
		a[i] = n-(26*r);
	    i++;
	    j++;
	}
}

