:-dynamic appoggio/1.

n(11).
n(1).
n(3).
n(7).
n(11).

appoggio([]).

numeri(L):-
    n(Num),
    appoggio(L),
    append(L,[Num],LN),
    retract(appoggio(L)),
    assert(appoggio(LN)),
    write(Num),nl,
    fail.

numeri(L):-
    appoggio(L),
    retract(appoggio(L)),
    assert(appoggio([])),
    write(fine), nl.

