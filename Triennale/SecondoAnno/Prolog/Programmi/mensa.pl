:- dynamic frigorifero/1.
frigorifero(carne).
frigorifero(pesce).
frigorifero(surgelati).

:- dynamic dispensa/1.
dispensa(insalata).
dispensa(pomodoro).
dispensa(pomodoro).
dispensa(patate).
dispensa(patate).
dispensa(fagioli).
dispensa(ceci).
dispensa(lenticchie).

tempoDiPreparazioneMax(5).
tempoDiPreparazioneMax(10).
tempoDiPreparazioneMax(15).
tempoDiPreparazioneMax(20).

numeroDiPersone(1).
numeroDiPersone(2).
numeroDiPersone(3).

controlloTempo(X):-
    tempoDiPreparazioneMax(Y),
    Y >= X,!.

controlloPersone(X):-
    numeroDiPersone(Y),
    Y >= X,!.

controlloIngredienti([]).
controlloIngredienti([[H,N]|T]):-
    rimozioneIngrediente(H,N),
    controlloIngredienti(T).

rimozioneIngrediente(_, 0).
rimozioneIngrediente(H, N):-
    frigorifero(H),
    retract(frigorifero(H)),
    rimozioneIngrediente(H,M),
    N is M + 1.

rimozioneIngrediente(H, N):-
    dispensa(H),
    retract(dispensa(H)),
    rimozioneIngrediente(H,M),
    N is M + 1.

hoPreparato(X,Y):-
    write('ho preparato: '),
    write(X),nl,
    write('con ingredienti: '),
    write(Y).

piattoPerOggi(3, 2, insaltaConPatate, [[insalata, 1], [pomodoro,2]]):-
    controlloTempo(3),
    controlloPersone(2),
    controlloIngredienti([[insalata, 1], [pomodoro,2]]),
    hoPreparato(insalataConPatate, [[insalata, 1], [pomodoro,2]]).

