#include <stdlib.h>
#include <string.h>
#include <stdio.h>

struct array_int{
    int *a;
    int n;
    int c;
};
typedef struct array_int array_int;

void swap_int(int*,int*);
int somma_array_int (array_int);
array_int array_int_init();
array_int array_int_compile(array_int,int);
char* string_copy(char*);

void main(){

    int a = 5;
    int b = 7;
    swap_int(&a,&b);
    printf("%d, %d\n",a,b);

    array_int v = array_int_init();
    v = array_int_compile(v,10);
    int e = somma_array_int(v);
    printf("%d\n",e);

    char m[] = "siumm";
    char *t = string_copy(m);
    printf("%s\n",m);

}

void swap_int(int *x,int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

int somma_array_int(array_int v){

    int i;
    int k = 0;
    for (i = 0;i < v.n;i++){
        k = k + v.a[i];
    }

    return k;
}

array_int array_int_init(){
    array_int v = {NULL,0,0};
    return v;
}


array_int array_int_compile(array_int v,int e){
    v.a = malloc((e+1)*sizeof(int));
    v.c = e+1;
    v.n = e;
    for (int i = 0; i < e; i++){
        v.a[i] = i;
    }
    return v;
}

char* string_copy(char *s){

    int len = strlen(s);
    char *p = realloc(p,sizeof(char)*(len+1));
    int i = 0;
    while ( s[i] != '\0'){
        p[i] = s[i];
        i++;
    }
    p[i] = '\0';
    return p;
}
