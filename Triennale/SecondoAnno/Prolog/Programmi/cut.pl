
/*tutto ciò che è scritto è vero*/
/*per verificare se è falso bisogna verificare se sia scritto*/

/*controllare l'algoritmo di prolog per far diventare le cose false true*/

amici(mario, maria).
amici(mario, dario).
amici(mario, pino).

/*per funzionare deve controllare tutto quello che è scritto
not(P).
fail -> ci fa guardare un'altro ramo
! -> é sempre vero ed è il cut, taglia un ramo di ricerca

p :- a, !, b, c. -> scritto in questo modo una volta sorpassato 
                    il cut non si può tornare indietro,
                    non posso nemmeno reistanziare p*/

f(b).
f(a).
g(a).
g(b).
g(j).
k(a).

p(A) :-
    f(A),
    write('28: '),write(A),nl, /*write e nl sono il print*/
    !, %senza il cut lui tornerebbe indietro finché non prova tutte le istanzes
    g(A),
    write('31: '),write(A),nl,
    k(A).

fallimento_di_g(A):-
    g(A),
    !,
    fail. %se può essere verificato lo fa diventare il predicato falso 


fallimento_di_g(_). %l'algoritmo esegue prima tutte le istanze di fail_g(A) dando false e successivamente prova fail_g(_)
                    %mettendo il cut nel momento in cui ne trova una si blocca e dà sicuramente false)

%negation as failure -> per prolog è falso ciò che non è scritto
mynot(Predicato) :-
    Predicato,!,fail.
mynot(_).

/*
num_element(_, [], 0).
num_element(X, [X|L], N):-
    num_element(X, T, M),
    N is M+1.
num_element(X, [Y|T], N):-
    \+(X = Y), %\+ -> not -> X non è unificabile con Y
    num_elemnt(X, T, N).
*/

num_element(_, [], 0).
num_element(X, [X|T], N):-
    !, %mettendo il cut possiamo evitare di mettere il not MA se X è variabile allora si bloccherà al primo che trova
    num_element(X, T, M),
    N is M+1.
num_element(X, [_|T], N):-
    num_element(X, T, N).
    
















