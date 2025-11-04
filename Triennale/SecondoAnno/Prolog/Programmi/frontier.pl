edge(a,b).
edge(a,c).
edge(c,d).
edge(b,x).
edge(x,y).


path(A,B,[A|B]):-
    edge(A,B).

path(A,B,[A|T]):-
    edge(A,X),
    path(X,B,T).


livello([],[]).

livello([H|T],F):- %-> PF livello raggiungibile da F
	setof(Y, edge(H,Y),YF),
    livello(T,TF),
    append(YF, TF, F).

path_level(F,FR,y):-
    livello(F,FR),
    member(y,FR).
    

path_level(F,FF,y):-
    livello(F,FR),
    path_level(FR,FF,y).
    
