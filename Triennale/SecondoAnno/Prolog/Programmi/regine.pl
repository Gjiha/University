controlloRiga([A, _], [A, _]).

controlloColonna([_, B], [_, B]).

controlloDiagonale([A, B], [C, D]):-
    X is A - C,
    Y is B - D,
    X =\= -Y,
    X =\= Y.

controlloCoppia([_]).

controlloCoppia([A, B|T]):-
    controlloRiga(A, B),
    controlloColonna(A, B),
    controlloDiagonale(A, B),
    controlloCoppia([A|T]).

controlloSoluzione([_]).

controlloSoluzione([H|T]):-
    \+controlloCoppia([H|T]),
    controlloSoluzione([T]).
    
