#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* string_conc(char*, char*);
void  delete_non_alpha(char*);

void main(){
	char a[] = "ciao ";
	char b[] = "mamma";
	printf("%s\n",string_conc( a, b));
}

char* string_conc(char *a, char *b){	
	
	int len_a = strlen(a);
	int len_b = strlen(b);
	int i = 0;
	
    
    while (b[i] != '\0'){
		
		a[len_a+i] = b[i];
		i++;
    }
    a[len_a+len_b] = '\0';
    return a;
}

void delete_non_alpha(char *a){
	
	int i = 0;
	int j = 0;
	while (a[i] != 0 ){
		if ((a[i] >= 'a' && a[i] <= 'z')||(a[i] >= 'A' && a[i] <= 'Z')){
			a[j] = a[i];
			j++;
		}
		i++;
	}
	a[j] = '\0';
}

