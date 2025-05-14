#include <stdio.h>
#include <stdlib.h>
#include <string.h>

union item{
	int i_val;
	float f_val;
	char c_val;
	char* s_val;
};
typedef union item item;

struct s_item{
	char type;
	item object;
};
typedef struct s_item s_item;

struct node{
	s_item u;
	struct node *next;
};
typedef struct node node;

struct linked_list{
	node *head; //primo elemento della sequenza
	int n; //numero di nodi totali
};
typedef struct linked_list linked_list;

s_item s_init(item, int);
linked_list init(void);
linked_list in0 (linked_list, s_item);
linked_list del0 (linked_list);
node* search(linked_list, int);
linked_list delete(linked_list,int);
linked_list insert (linked_list, s_item, int);
linked_list move_to_tail (linked_list);
void print_llist(linked_list);


void main(){
	
	item a;
	a.i_val = 5;

	item b;
	b.f_val = 9.56;

	item c;
	c.c_val = 'p';
	
	item d;
	d.i_val = 78;
	
	item e;
	e.s_val = "viva la figa";
	
	s_item A;
	A = s_init(a,0);
	s_item B; 
	B = s_init(b,1);
	s_item C; 
	C = s_init(c,2);
	s_item D;
	D = s_init(d,0);
	s_item E;
	E = s_init(e,3);
	
	linked_list L;
	L = init();
	
	L = in0(L,A);
	L = in0(L,B);
	L = in0(L,C);
	L = insert(L,D,2);
	L = del0(L);
	L = insert(L,E,1);
	
	print_llist(L);
	
	L = move_to_tail(L);
	
	print_llist(L);
	
}

s_item s_init(item u,int key){
	
	if (key == 0){
		s_item s = {'i', u};
	
		return s;
	}
	else if (key == 1){
		s_item s = {'f', u};
	
		return s;
	}
	else if (key == 2){
		s_item s = {'c', u};
		
		return s;
	}
	else{
		s_item s = {'s', u};
		
		return s;
	}
}

linked_list init(void){
	
	linked_list L = {NULL,0};
	return L;
}

linked_list in0 ( linked_list L, s_item itm){
	node *p = malloc(sizeof(node));
	
	p->next = L.head;
	L.head = p;
	p->u = itm;
	L.n++; 
	
	return L;
}

linked_list del0 (linked_list L){
	
	node *p;
	if (L.n > 0){
		p = L.head;
		L.head = p->next;
		free(p);
		L.n--;
	}
	return L;
}

node* search(linked_list L, int pos){
	
	node *p = L.head;
	int i = 0;
	
	while (p != NULL && i < pos){
		p = p->next;
		i++;
	}
	return p;
}

linked_list delete (linked_list L, int pos){
	
	node *p, *q;
	
	if (pos < L.n && pos > 0){
		
		p = search(L,pos-1);
		q = p->next;
		p->next = q->next;
		free(q);
		L.n--;
	}
		
	else if (pos == 0){
		L = del0(L);
	}
	
	return L;	
}

linked_list insert (linked_list L, s_item e, int pos){
	node *p,*q;
	if (pos > 0 && pos <= L.n){
		p = malloc(sizeof(node));
		p->u = e;
	
		q = search(L,pos-1);
		p->next = q->next;
		q->next = p;
		L.n++;
	}
	else if (pos == 0){
		L = in0(L,e);
	}
	return L;
}

linked_list move_to_tail (linked_list L){
	
	if (L.n > 1){
		node *p = L.head;
		node *q = search(L,L.n-1);
	
		L.head = L.head->next;
		q->next = p;
		p->next = NULL;
	}
	
	return L;
}

void print_llist(linked_list L){
	node *p = L.head;
	
	while( p != NULL ){
		
		if (p->u.type == 'i'){
			printf("%d\n", p->u.object.i_val);
		}
		else if (p->u.type == 'f'){
			printf("%f\n", p->u.object.f_val);
		}
		else if (p->u.type == 'c') {
			printf("%c\n", p->u.object.c_val);
		}
		else{
			printf("'%s'\n", p->u.object.s_val);
		}
		
		p = p->next; 
	}
}





