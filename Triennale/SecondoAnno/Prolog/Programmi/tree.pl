%t(a,[t(b,[]),t(c,[t(d,[])])])

somma(0,[]).
somma(T, [H|L]):-
    somma(Z,L),
    T is H+Z.

traduzione(T, S):-
    S =.. [_|L],
    somma(T, L).  
 
leaf(t(R,[]),R).
leaf(t(_,Children),L):-
    member(C,Children),
    leaf(C,L).

    
