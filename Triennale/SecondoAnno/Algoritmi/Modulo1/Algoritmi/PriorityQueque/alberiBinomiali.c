#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
typedef struct arrayOfChar {
    char **array;
    int len;
} arrayOfChar;
*/
typedef struct element {
    int key;
    char *parola;
} element;

typedef struct node {
    element object;
    struct node *child;
    struct node *father;
    int numberOfChild;
} node;
/*
typedef struct arrayOfNode {
    node *array;
    int len;
} arrayOfNode;
*/
typedef struct tree {
    int numberOfNode;
    node *root;
    struct tree *next;
} tree;

typedef struct binomialTree {
    tree *head;
    int numberOfTree;
    int allNode;
} binomialTree;

element elementCreate(int, char *);
node *nodeCreate(element);
// arrayOfNode arrayNodeInit(void);
// void arrayNodeCreation(arrayOfNode *, arrayOfChar *, int[]);
void nodeAllocation(node *, node *);
binomialTree *binomialInit(void);
void treeMerge(binomialTree *);
void binomialAppend(binomialTree *, node *);

void printFatherChild(node);
void printNode(node);
void printElement(element);

int main() {
    char *parola = "mamma";
    int key = 3;
    char *parola2 = "figlio";
    int key2 = 8;
    char *parola3 = "figlia";
    int key3 = 5;
    char *parola4 = "zio";
    int key4 = 7;
    char *parola5 = "zia";
    int key5 = 1;

    element c = elementCreate(key, parola);
    element d = elementCreate(key2, parola2);
    element e = elementCreate(key3, parola3);
    element a = elementCreate(key4, parola4);
    element b = elementCreate(key5, parola5);

    node *C = nodeCreate(c);
    node *D = nodeCreate(d);
    node *E = nodeCreate(e);
    node *A = nodeCreate(a);
    node *B = nodeCreate(b);

    binomialTree *BT = binomialInit();
    binomialAppend(BT, A);
    binomialAppend(BT, B);
    binomialAppend(BT, C);
    binomialAppend(BT, D);
    binomialAppend(BT, E);

    return 0;
}

element elementCreate(int key, char *parola) {
    element object = {0, NULL};
    object.key = key;
    int len = strlen(parola);

    object.parola = malloc(sizeof(char) * (len + 1));
    for (int i = 0; i < len; i++) {
        object.parola[i] = parola[i];
    }
    return object;
}

node *nodeCreate(element object) {
    node *nodo = malloc(sizeof(node));
    nodo->object = object;
    nodo->child = malloc(sizeof(node));
    nodo->father = NULL;
    nodo->numberOfChild = 0;
    return nodo;
}

void nodeAllocation(node *father, node *figlio) {

    father->numberOfChild++;
    father->child = realloc(father->child, (father->numberOfChild) * sizeof(node));

    father->child[father->numberOfChild - 1] = *figlio;
    figlio->father = father;
    return;
}

/*
arrayOfNode arrayNodeInit() {
    arrayOfNode Aon = {malloc(sizeof(node)), 0};
    return Aon;
}

void arrayNodeCreation(arrayOfNode *lista, arrayOfChar *valori, int keys[]) {
    if ((sizeof(&keys) / sizeof(int)) != valori->len) {
        printf("input error");
        return;
    }

    for (int i = 0; i < lista->len; i++) {
        element object = elementCreate(keys[i], valori->array[i]);
        node *nodo = nodeCreate(object);

        lista->array = realloc(lista->array, sizeof(node) * lista->len);
        lista->array[lista->len] = *nodo;
        lista->len++;
    }
    return;
}
*/

binomialTree *binomialInit(void) {
    binomialTree *BT = malloc(sizeof(binomialTree));
    BT->numberOfTree = 0;
    BT->head = NULL;
    BT->allNode = 0;
    return BT;
}

void treeMerge(binomialTree *alberi) {
    int i = 0;
    tree *t = malloc(sizeof(tree));
    t = alberi->head;

    while (i < alberi->numberOfTree) {
        if ((t->next != NULL) && (t->numberOfNode == t->next->numberOfNode)) {
            if (t->root->object.key <= t->next->root->object.key) {
                node *p = malloc(sizeof(node));
                p = t->root;
                t->root = t->next->root;
                t->next->root = p;
                free(p);
            }

            nodeAllocation(t->root, t->next->root);
            t->numberOfNode += t->next->numberOfNode;
            t->next = t->next->next;
            alberi->numberOfTree--;
        } else {
            t = t->next;
            i++;
        }
    }
}

void binomialAppend(binomialTree *alberi, node *nodo) {
    if (alberi->numberOfTree == 0) {
        alberi->head = malloc(sizeof(tree));
        alberi->head->root = nodo;
        alberi->head->numberOfNode++;
        alberi->numberOfTree++;
        alberi->allNode++;
    } else {

        tree *t = malloc(sizeof(tree));
        t->next = alberi->head;
        t->root = nodo;
        t->numberOfNode++;

        alberi->head = t;
        alberi->numberOfTree++;
        alberi->allNode++;

        treeMerge(alberi);
    }

    return;
}

void printFatherChild(node nodo) {
    printf("il padre è [");
    printElement(nodo.object);

    for (int i = 0; i < nodo.numberOfChild; i++) {
        printNode(nodo.child[i]);
    }
    printf("] questo è il figlio\n");
}

void printNode(node nodo) {
    printElement(nodo.object);
    return;
}

void printElement(element object) {
    printf("[ %d, %s ]\n", object.key, object.parola);
    return;
}
