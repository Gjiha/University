generaListe(_, 0, []).
generaListe(N, M, [H|T]):-
    length(H, N),
    S is M - 1, 
    generaListe(N, S, T),!.

controlloRiga([A,_], [B,_], _):-
    A =\= B.
controlloRiga([A, X], [A, Y], M):-
    M < abs(X-Y).

controlloColonna([_, A], [_, B], _):-
    A =\= B.
controlloColonna([X, B], [Y, B], M):-
    M < abs(X-Y).

controlloDiagonale([A, B], [C, D], _):-
    X is A - C,
    Y is B - D,
    X =\= -Y,
    X =\= Y.

controlloDiagonale([A, B], [C, D], M):-
    X is A - C,
    Y is B - D,
    X == -Y,
    M < abs(X-Y).

controlloDiagonale([A, B], [C, D], M):-
    X is A - C,
    Y is B - D,
    X == Y,
    M < abs(X-Y).

controlloCoppia(_,[], _).

controlloCoppia(H, [A|S], M):-
    controlloRiga(H, A, M),
    controlloColonna(H, A, M),
    controlloDiagonale(H, A, M),
    controlloCoppia(H, S, M).



controlloSoluzione([],_,_).
controlloSoluzione([H|T], S, M):-
    controlloCoppia(H, S, M),
    controlloSoluzione(T, S, M).







