pila(h([X|A],B,C),h(A,B,[X|C])):-
    ordinata([X|A]),
    ordinata([X|B]),
    ordinata([C]).

pila(h([X|A],B,C),h(A,[X|B],C)):-
    ordinata([X|A]),
    ordinata([X|B]),
    ordinata([C]).

pila(h(A,[X|B],C),h(A,B,[X|C])):-
    ordinata([A]),
    ordinata([X|B]),
    ordinata([X|C]).

pila(h(A,[X|B],C),h([X|A],B,C)):-
    ordinata([X|A]),
    ordinata([X|B]),
    ordinata([C]).

pila(h(A,B,[X|C]),h([X|A],B,C)):-
    ordinata([X|A]),
    ordinata([B]),
    ordinata([X|C]).

pila(h(A,B,[X|C]),h(A,[X|B],C)):-
    ordinata([A]),
    ordinata([X|B]),
    ordinata([X|C]).

ordinata([]).
ordinata([_]).
ordinata([H1,H2|T]):-
    H1 < H2,
    ordinata([H2|T]).

hanoi(X, X, 0).

hanoi(X, Y, N):-
	pila(X, Z),
    hanoi(Z, Y, M),!,
    N is M + 1.

    



 
