n(11,a,la).
n(2,m,ka).
n(4,k,jd).
n(5,g,ls).
n(8,l,ks).
n(3,a,ls).

len([],0).

len([_|T], M):-
    len(T,N),
    M is N+1.

numero_lettere_diverse(M):-
    setof(A, (N,L)^n(N,A,L),Lista),
    len(Lista,M).
    

