function [x, K, rnorm, M] = sor_solver_M(A, b, omega, eps, x0, Nmax)
% SOR_SOLVER_M  Metodo SOR con precondizionatore M = (1/omega)D + E - D
%
% Input:
%   A      : matrice quadrata (n x n)
%   b      : termine noto (n x 1)
%   omega  : parametro di rilassamento
%   eps    : tolleranza di arresto
%   x0     : vettore iniziale
%   Nmax   : massimo numero iterazioni
%
% Output:
%   x      : soluzione approssimata
%   K      : iterazioni effettuate
%   rnorm  : norma 2 del residuo all'arresto
%   M      : precondizionatore usato

    % --- decomposizione ---
    D = diag(diag(A));
    E = tril(A);       % parte inferiore con segno (come da definizione)
    
    % precondizionatore
    M = (1/omega)*D + E - D;

    % --- inizializzazione ---
    x = x0(:);
    bnrm = norm(b,2);
    r = b - A*x;
    rnorm = norm(r,2);

    if rnorm <= eps*bnrm
        K = 0;
        return;
    end

    % --- iterazioni ---
    for k = 1:Nmax
        dx = M \ r;      % risolve M*dx = r
        x = x + dx;      % aggiornamento
        r = b - A*x;     % residuo
        rnorm = norm(r,2);

        if rnorm <= eps*bnrm
            K = k;
            return;
        end
    end

    % se non converge entro Nmax
    K = Nmax;
end



