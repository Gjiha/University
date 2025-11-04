controlloFatti(P1, P2):-
    P1 =.. [_|X],
    P2 =.. [_|Y],
    
    length(X, Z),
    length(Y, Z).

controlloPredicati([H1|[T1]], [H2|[T2]]):-
    controlloFatti(H1, H2),
    controlloPredicati(T1, T2).

controlloPredicati([X], [Y]):-
    controlloFatti(X, Y).

haStessaStruttura([H1|[T1]], [H2|[T2]]):-
    length(T1, Z),
    length(T2, Z),
    controlloPredicati([H1|[T1]], [H2|[T2]]).

haStessaStruttura([P1], [P2]):-
    controlloFatti(P1, P2).
