#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* chiave: stringa; valore: float */
struct dict_item {
	char *k;
	float v;
};
typedef struct dict_item dict_item;

struct node {
	dict_item info;
	struct node *next;
};
typedef struct node node;

struct linked_list {
	node *a; /* punta al primo elemento della sequenza*/
	int n;
};
typedef struct linked_list linked_list;

struct dict {
	node **a;
	int n;
	int M;
};
typedef struct dict dict;

dict dict_resize(dict, int);
int dict_del(dict, char*);
dict dict_init(int);
int h(dict, char*);
void dict_set(dict, dict_item);
node *dict_search(dict, char*);
void print_dict(dict);

void print_llist(node*);
node *in0(node*, dict_item);
linked_list init(void);
node *search(linked_list, int);
linked_list insert(linked_list, int, char*);
linked_list delete(linked_list, int);
linked_list del0(linked_list);
linked_list move_to_tail(linked_list L);


void main(int dim, char *args[]){
	dict d = dict_init(5);
	int i;
	dict_item e;
	
	for(i = 1; i < dim; i++){
		e.k = args[i];
		e.v = i;
		dict_set(d, e);
	}
	
	print_dict(d);
	
	d = dict_resize(d,7);
	
	print_dict(d);
}


/* ritorna un indice del dizionario*/

/*
 * questa funzione può essere usata sia per immettere una chiave 
 * nel dizionario sia per cercarla visto che il metodo di ricerca 
 * e immissione è lo stesso
 * 
 * ergo la cerco utilizzando lo stesso metodo con cui la imposto
 * */
int h(dict d, char *k){
	
	int i = 0, hash_val = 0;
	
	while( k[i] != '\0') {
		hash_val = hash_val ^ k[i];
		i += 1;
	}
	
	return hash_val % d.M; //calcola il modulo
	
}

/* imposta un valore per una chiave del dizioario usando e */
void dict_set(dict d, dict_item e){
	int p = h(d, e.k);
	node *nd;
	
	nd = dict_search(d, e.k);
	if( nd != NULL ) {
		nd->info.v = e.v;
	} else {
		d.a[p] = in0(d.a[p], e);
		d.n ++;
	}
	
	if (d.n/d.M > 4){
		/*
		 * ridimensiona d.a
		 * */
		 d = dict_resize(d, d.M*2+1);
	}
}

/* ritorna il puntatore al node contenente l'item del dizionario con
 * chiave k. NULL se tale chiave non è presente nel dizionario */
node *dict_search(dict d, char *k){
	int p = h(d, k); 
	node *q = d.a[p];
	
	while( q != NULL && strcmp(k, q->info.k) != 0){
		q = q->next;
	}
	
	return q;
}

/* Inizializza un dizionario vuoto con M liste*/
dict dict_init(int M){
	dict d;
	int i;
	d.a = malloc(sizeof(node*)*M);
	d.n = 0;
	d.M = M;
	for(i = 0; i < d.M; i++){
		d.a[i] = NULL;
	}
	return d;
}

/* Mostra il dizionario */
void print_dict(dict d){
	int i;
	for (i = 0; i < d.M; i++){
		printf("%d ", i);
		print_llist(d.a[i]);
		printf("\n");
	}
}

/* funzione di cancellazione 
 * 
 * restituisce 1 se è stata eseguita una cancellazione altrimenti 0
 * 
 * */

int dict_del(dict d, char *k) {
	
	int p = h(d, k);
	node *x, *q = dict_search(d, k);
	
	if ( q == NULL) {
		return 0;
	}
	
	if ( d.a[p] == q){  /*è il primo nodo*/
		d.a[p] = q -> next;
		free(q);
	}
	else{
		x = d.a[p];
		while ( x -> next != q){
			x = x -> next;
		}
		x -> next = q -> next;  /* SIUMM */
	}
	free(q);
	d.n--;
	return 1;
}

dict dict_resize(dict d0, int new_M){
	dict d1 = dict_init(new_M);
	int i;
	node *q;
	
	for (i = 0; i < d0.M; i++){
		while (d0.a[i] != NULL){
			dict_set(d1, d0.a[i]->info);
			q = d0.a[i];
			d0.a[i] = q -> next;
			free(q);			
		}
	}
	free(d0.a);
	return d1;
}
		
	



/********************************************************/
/********************************************************/
/********************************************************/
/*
linked_list move_to_tail(linked_list L) {
	node *p, *q;
	if(L.n > 1) {
		p = search(L, L.n-1);
		q = L.a;
		L.a = L.a->next;
		p->next = q;
		q->next = NULL;
	}
	return L;
}
*/
/*
linked_list delete(linked_list L, int pos){
	node *q, *p;
	if (pos > 0 && pos < L.n){
		q = search(L, pos-1);
		p = q->next;
		q->next = p->next;
		free(p->v);
		free(p);
		L.n--;
	} else if ( pos == 0 && L.n > 0) {
		L = del0(L);
	}
	
	return L;
}
* */
/*
linked_list insert(linked_list L, int pos, char *e){
	node *q, *p;
	if (pos > 0 && pos <= L.n) {
		q = search(L, pos-1);
		p = malloc(sizeof(node));
		p->v = malloc(sizeof(char)*(strlen(e)+1));
		p->v = strcpy(p->v, e);
		p->next = q->next;
		q->next = p;
		L.n++;
	} else if ( pos == 0) {
		L = in0(L, e);
	}
	
	return L;
}
*/
node *in0(node *nd, dict_item e){
	node *p = malloc(sizeof(node));
	
	p->info = e;
	p->next = nd;
	nd = p;
		
	return nd;
}
/*
linked_list del0(linked_list L){
	node *p;
	if (L.n > 0 ){
		p = L.a;
		L.a = p->next;
		free(p->v);
		free(p);
		L.n--;
	}
	return L;
}
*/
void print_llist(node *nd){
	node *p = nd;
	
	while( p != NULL ){
		printf("(\"%s\", %f) ", p->info.k, p->info.v);
		p = p->next; /*equivalente a p = (*p).next */
	}
}
/*
linked_list init(void) {
	linked_list L = {NULL, 0};
	return L;
}
*/
/*
 * Restituisce il puntatore al node in posizione pos di L. NULL se
 * la posizione pos non esiste
 * */
/*
node *search(linked_list L, int pos){
	node *p = L.a;
	int c = 0;
	
	while( p != NULL && c < pos ){
		p = p->next;
		c++;
	}
	
	return p;
}
*/

