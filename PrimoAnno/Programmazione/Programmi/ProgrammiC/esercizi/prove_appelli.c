#include <stdlib.h>
#include <string.h>
#include <stdio.h>

struct array_int {
	int *a;  //array di int
	int n;   //numero di elementi
};
typedef struct array_int int_array;

char** punt_vocali (char*);
void remove_non_alpha(char*);
void centering(int*, int, int);
void int_array_cat( int_array* , int_array );
char* 

void main(){
    /*
    char a[] = "programmazione";
    char **t = punt_vocali(a);

    char b[] = "7Ac89d";
    remove_non_alpha(b);
    printf("%s",b);
    
    int c[] = {
        1,1,0,0,0,
        1,0,0,0,0,
        1,1,1,0,0,
        1,1,0,0,0,
        1,1,1,1,0,
        1,1,1,1,1
    };

    centering(c,5,6);

    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", c[i*5 + j]);
        }
        printf("\n");
    }
    */


    int_array v0;
    v0.n = 10;
    v0.a = malloc(sizeof(int) * v0.n);
    for (int i = 0; i < v0.n; i++) {
        v0.a[i] = i;
    }

    int_array v1;
    v1.n = 5;
    v1.a = malloc(sizeof(int) * v1.n);
    for (int i = 0; i < v1.n; i++) {
        v1.a[i] = i + 10;
    }

    int_array *x;
    x = &v0;

    int_array_cat(x,v1);

    printf("[");
	for (int i=0; i<v0.n; i++){
		printf("%d,", v0.a[i]);
	}
	printf("]\n");

    

}
/*
char **punt_vocali (char *a){

    int i=0, j=0;
    char **p;
    p = malloc(sizeof(char*)*(strlen(a)+1));

    while ( a[i]!='\0'){
        if (a[i] == 'a' || a[i] == 'e' || a[i] == 'i' || a[i] == 'o' || a[i] == 'u'){
            p[j] = malloc(sizeof(char*));
            p[j] = &a[i];
            j++;
            i++;
        }
        else{
            i++;
        }      
    }

    p[j] = NULL;

    return p;
}

void remove_non_alpha (char *a){
    int i = 0, j = 0;
    for (i; a[i]!='\0'; i++){
        if ((a[i]>='a' && a[i]<='z') || (a[i]>='A' && a[i]<='Z')){
            a[j] = a[i];
            j++;
        }
    }
    a[j]='\0';
}

void centering(int *a, int r, int c){

    int i = 0,j = 0;
    

    for (i = 0;i<r;i++){
        int t = 0;

        for(j = 0;j<c;j++){

            if (a[(c*i)+j]==1){
                t++;
            }
        }

        if (t<=(c/2)){
            int f = 0;
            int x = c-t;
            while(f < x){
                a[(c*i)+f] = 0;
                f++;
            }
            while (f >= x){
                a[(c*i)+f] = 1;
                f++;
            }
        }

        j = 0;
    }
}
*/

void int_array_cat( int_array *v0, int_array v1 ){

    v0->a = realloc(v0->a, sizeof(int)*(v0->n+v1.n+2));
    
    
    for (int i = 0; i<v1.n;i++){

        v0->a[v0->n+i] = v1.a[i];

    }
    v0->n = v0->n+v1.n;
}