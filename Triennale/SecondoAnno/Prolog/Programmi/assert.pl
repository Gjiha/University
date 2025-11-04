%assert() -> fa diventare una regola vera
%retract() -> se è vero cancella il fatto
%retractAll() -> cancella tutti quelli che si unificabili con l'input
%dynamic(_/n) -> fa in modo che l'argomento con lunghezza n possa divetare retract o assert
% =.. -> len(0, 1) =.. [len, 0, 1] -> unifica il predicato con una lista contenente la composizione del predicato, può essere usato per modificare i predicati in runtime


primo(a).
funtore(A,Funtore):-
    A =.. [Funtore|_].
    
    
    
    
    
