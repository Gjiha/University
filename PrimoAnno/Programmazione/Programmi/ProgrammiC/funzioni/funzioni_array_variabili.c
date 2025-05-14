#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct object{
	void* pointer;
	char type;  // 'i'-> int, 'f'-> float, 'c'-> char, 's'-> stringa
};
typedef struct object object;

struct list{
	object* array;
	int n; // numero di elementi
	int c; // capacità occupata
};
typedef struct list list;

object new_int(int);
object new_char(char);
object new_float(float);
object string_alias(char*);
object string_clone(char*);
list list_init(void);
list list_append_int(list, int);
list list_append_float(list, float);
list list_append_char(list, char);
list list_append_string_alias(list, char*);
list list_append_string_clone(list, char*);
list list_append_object(list, object);
list list_pop(list);
list list_del(list, int);
list list_insert(list, int, object);
void print_list(list);



void main() {
	
	list L = list_init();
	L = list_append_int(L, 6);
	L = list_append_float(L, 7.5);
	L = list_append_char(L, 'o');
	char t[] = "mamma";
	L = list_append_string_alias(L,t);
	object ob = new_int(100);
	L = list_append_object(L,ob);
	L = list_pop(L);
	char s[] = "siummmm";
	object ot = string_clone(s);
	L = list_insert(L,1,ot);
	
	print_list(L);
	
}

object new_int(int e){
	
	object ob = {NULL, 'i'};
	ob.pointer = malloc(sizeof(int));
	*((int*)ob.pointer) = e;
	return ob;
}

object new_char(char c){
	
	object ob = {NULL, 'c'};
	ob.pointer = malloc(sizeof(char));
	*((char*)ob.pointer) = c;
	return ob;
}

object new_float(float f){
	
	object ob = {NULL, 'f'};
	ob.pointer = malloc(sizeof(float));
	*((float*)ob.pointer) = f;
	return ob;
}

object string_alias(char* s){
	
	object ob = {NULL, 's'};
	ob.pointer = s;
	return ob;
}

object string_clone(char* s){
	
	object ob = {NULL, 's'};
	ob.pointer = malloc((strlen(s)+1)*(sizeof(char)));
	ob.pointer = strcpy( ob.pointer, s);
	return ob;	
}

list list_init(void){
	
	list L = {NULL, 0, 0};
	return L;
}

list list_append_int(list L, int e){
	
	object ob = new_int(e);
	
	if (L.n == L.c){
		L.array = realloc(L.array, (L.c*2+1)*sizeof(object));
		L.c = 2*L.c+1;
	}
	
	L.array[L.n] = ob;
	L.n++;
	return L;	
}

list list_append_float(list L, float e){
	
	object ob = new_float(e);
	
	if (L.n == L.c){
		L.array = realloc(L.array, (L.c*2+1)*sizeof(object));
		L.c = 2*L.c+1;
	}
	
	L.array[L.n] = ob;
	L.n++;
	return L;
}

list list_append_char(list L, char e){
	
	object ob = new_char(e);
	
	if (L.n == L.c){
		L.array = realloc(L.array, (L.c*2+1)*sizeof(object));
		L.c = 2*L.c+1;
	}
	
	L.array[L.n] = ob;
	L.n++;
	return L;
}

list list_append_string_alias(list L, char* e){
	
	object ob = string_alias(e);
	
	if (L.n == L.c){
		L.array = realloc(L.array, (L.c*2+1)*sizeof(object));
		L.c = 2*L.c+1;
	}
	
	L.array[L.n] = ob;
	L.n++;
	return L;
}

list list_append_string_clone(list L, char* e){
	
	object ob = string_clone(e);
	
	if (L.n == L.c){
		L.array = realloc(L.array, (L.c*2+1)*sizeof(object));
		L.c = 2*L.c+1;
	}
	
	L.array[L.n] = ob;
	L.n++;
	return L;
}

list list_append_object(list L, object ob){
	
	if (L.n == L.c){
		L.array = realloc(L.array, (L.c*2+1)*sizeof(object));
		L.c = 2*L.c+1;
	}
	
	L.array[L.n] = ob;
	L.n++;
	return L;
}

list list_pop(list L){
	
	L.n--;
	if (L.n == L.c/4){
		L.array = realloc(L.array, (L.c/2+1)*sizeof(object));
		L.c = L.c/2 +1;
	}
	return L;
}

list list_del(list L, int pos){
	
	if (pos < L.n-1){
		for (int i=0; i+pos < L.n-1; i++){
			
		    L.array[pos+i] = L.array[pos+i+1];
		}
			 
		L.n--;
		if (L.n == L.c/4){
			L.array = realloc(L.array, (L.c/2+1)*sizeof(int));
			L.c = L.c/2+1;
		}
	}
	else if (pos == L.n-1){
		L = list_pop(L);
	}
	return L;
}




list list_insert(list L, int pos, object ob){
	
	if (L.n+1 == L.c){
			
		L.array = realloc(L.array, (L.c*2+1)*sizeof(object));
		L.c = 2*L.c+1;
	}
	
	if (pos < L.n){
		
		for (int i=L.n+1; i>pos; i--){
		
		L.array[i] = L.array[i-1];
		} 
		L.array[pos] = ob;
		L.n++;
	}
	
	else if (pos == L.n){
		L = list_append_object(L, ob);
	}
	
	return L;
}

void print_list(list L) {
	
    int i;
	printf("[");
	for(i = 0; i < L.n; i++){
		if( L.array[i].type == 'i' ){
			printf("%d, ", *((int*)L.array[i].pointer));
		}
		else if ( L.array[i].type == 'c' ){
			printf("%c, ", *((char*)L.array[i].pointer));
		}
		else if ( L.array[i].type == 's'){
			printf("\'%s\', ", (char*)L.array[i].pointer );
		}
		else{
			printf("%f, ", *((float*)L.array[i].pointer) );
		}
	}
	printf("]\n");
}




	
	
	










