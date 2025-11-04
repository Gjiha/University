'S'(N) --> [up], 'S'(M),{N is M + 1}.
'S'(N) --> [down], 'S'(M),{N is M + 1}.
'S'(1) --> [up].
'S'(-1) --> [down].

% query 'S'(X,[up,down,up,down,down], []).

'S' --> [maria], 'A'.
'S' --> [mario], 'A'.
'A' --> [ha], 'B'.
'B' --> 'C', [borsa].
'B' --> 'F', [carrello].
'C' --> [una].
'F' --> [un].

'S' --> 'GN' , 'GN'.
'GN' --> 'N' | 'Art', 'N' | 'Art', 'N', [di], 'N'.
'V' --> [ha]
'Art' --> [un] | [una] | [uno] | [il] | [lo] | [la].









