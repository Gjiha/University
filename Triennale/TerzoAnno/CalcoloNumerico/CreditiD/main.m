% --- Matrice A e vettore b ---
A = [  4  -1   0   0;
      -1   4  -1   0;
       0  -1   4  -1;
       0   0  -1   3 ];

b = [15; 10; 10; 10];

% --- Parametri SOR ---
omega = 1.25;          % parametro di rilassamento
eps = 1e-6;            % tolleranza residuo
x0 = zeros(4,1);       % vettore iniziale
Nmax = 100;            % massimo numero di iterazioni

% --- Chiamata funzione ---
[x, K, rnorm, M] = sor_solver_M(A, b, omega, eps, x0, Nmax);

% --- Stampa risultati ---
fprintf('Soluzione approssimata:\n');
disp(x);

fprintf('Iterazioni effettuate: %d\n', K);
fprintf('Norma del residuo: %.2e\n', rnorm);
fprintf('Precondizionatore M:\n');
disp(M);
