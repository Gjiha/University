
:- dynamic f/2.
f(0,0).
f(1,1).
f(2,1).

f(X, M):-
    write(n),nl,
    Y is X-1,
    Z is X-2,
    Y > 0,
    Z > 0,
    f(Y, N),!,
    f(Z, V),!, %fa in modo che non si richiami 
    M is N+V,
    asserta(f(X,M) :- !). %li scrive in cima al programma
    %il ! serve per non far riscrivere all'algoritmo il fatto)
