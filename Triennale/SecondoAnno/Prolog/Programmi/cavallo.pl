:-dynamic mossa/1.

mossa([]).

controlloMossa([X1, Y1], []).

controlloMossa([X1, Y1], [X2, Y2]):-
    1 is abs(X1 - X2),
    2 is abs(Y1 - Y2).

controlloMossa([X1, Y1], [X2, Y2]):-
    1 is abs(Y1 - Y2),
	2 is abs(X1 - X2).


controllo(H, [H1]):-
    controlloMossa(H, H1),
    \+mossa(H1),
    assert(mossa(H1)).

controllo(H, [H1|T]):-
    controlloMossa(H, H1),
    \+mossa(H1),
    assert(mossa(H1)),
    controllo(H1, T).

generale([_]).

generale([H1|T]):-
    retract(mossa([])),
    assert(mossa(H1)),
    
    controllo(H1, T),
    
    listing(mossa),
    
    retractall(mossa(_)).

