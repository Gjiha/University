ord([]).
ord([_]).
ord([A,B|T]):-
    A < B,
    ord([B|T]).

edge(h([X|A],B,C), h(A,[X|B],C)):-
    ord([X|A]),
    ord([X|B]),
    ord(C).

edge(h([X|A],B,C), h(A,B,[X|C])):-
    ord([X|A]),
    ord(B),
    ord([X|C]).

edge(h(A,[X|B],C), h(A,B,[X|C])):-
    ord(A),
    ord([X|B]),
    ord([X|C]).

edge(h(A,[X|B],C), h([X|A],B,C)):-
    ord([X|A]),
    ord([X|B]),
    ord(C).

edge(h(A,B,[X|C]), h([X|A],B,C)):-
    ord([X|A]),
    ord(B),
    ord([X|C]).

edge(h(A,B,[X|C]), h(A,[X|B],C)):-
    ord(A),
    ord([X|B]),
    ord([X|C]).

