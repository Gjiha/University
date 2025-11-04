% --- dati del problema ---
A = [  1   -1/4   1/3    0
      -1    2     0    1/2
       2    1     3   -1/3
      -1   -2    -4     7 ];
b = [1; 0; -2; 0];

D = diag(diag(A)); %parte diagonale di A

E = tril(A); %parte triangolare inferiore di A

omega = linspace(0.001, 2, 2000); %creo il vettore di omega su cui poi richiamare l'algoritmo SOR per generare G_omega

rhoG = zeros(1, length(omega)); %vettore di zeri in cui andare a salvare i vari raggi spettrali

for i = 1:length(omega)
    M = (1/omega(i))*D + E - D; % mi calcolo il precondizionatore M
    G = M\(M - A); %mi calcolo la matrice d'iterazione G_omega
    rho = max(abs(eig(G))); % mi calcolo il raggio spettrale di G_omega
    rhoG(i) = rho; %mi salvo rho nel vettore rhoG
end

plot(omega, rhoG);
xlabel('omega');
ylabel('rho(G-omega)');
grid on;
[minRho, idx] = min(rhoG);
omega_opt = omega(idx);

fprintf('omega_opt = %.6f\n', omega_opt);

%ora mi calcolo G con omega = 1
M1 = D + E - D;
G1 = M1\(M1 - A);
rho_G1 = max(abs(eig(G1))); 

%ora mi calcolo G con omega = omega_opt
M_opt = ((1/omega_opt)*D) + E - D;
G_opt = M_opt\(M_opt - A);
rho_Gopt = max(abs(eig(G_opt)));

fprintf('rhoG_omega1: %.10f\n', rho_G1);
fprintf('rhoG_omegaOpt: %.10f\n', rho_Gopt);

%creo la tabella per il punto c

GS_classico =  zeros(4,10);
GS_rilassato =  zeros(4,10);
erroreGS_classico =  zeros(10,1);
erroreGS_rilassato =  zeros(10,1);

x_exact = A\b; %calcolo la soluzione esatta di x

for i = 1:10
    GS_classico(:, i) = sor_solver_M(A, b, 1, 1e-6, [0;0;0;0], i); %utilizzo la funzione sor_solver_M creata per l'esercizio 1.1 per ottenere le varie iterazione del metodo di GS classico
    GS_rilassato(:, i) = sor_solver_M(A, b, omega_opt, 1e-6, [0;0;0;0], i); %utilizzo la funzione sor_solver_M creata per l'esercizio 1.1 per ottenere le varie iterazione del metodo di GS rilassato

    erroreGS_classico(i) = norm(GS_classico(:,i) - x_exact, Inf); %mi calcolo la norma infinito fra l'i-esima iterazione di GS classico e la soluzione esatta per calcolare l'errore
    erroreGS_rilassato(i) = norm(GS_rilassato(:,i) - x_exact, Inf); %mi calcolo la norma infinito fra l'i-esima iterazione di GS rilassato e la soluzione esatta per calcolare l'errore
end

% for k = 1:10
%     xk = GS_classico(:, k);
%     fprintf('k=%2d | x1=%.8f x2=%.8f x3=%.8f x4=%.8f | err_inf=%.3e\n', k, xk(1), xk(2), xk(3), xk(4), erroreGS_classico(k));
% end
% 
% for k = 1:10
%     xk = GS_rilassato(:, k);
%     fprintf('k=%2d | x1=%.8f x2=%.8f x3=%.8f x4=%.8f | err_inf=%.3e\n', k, xk(1), xk(2), xk(3), xk(4), erroreGS_rilassato(k));
% end

for k = 1:10
    xk = GS_rilassato(:, k);
    fprintf('%d & %.8f & %.8f & %.8f & %.8f & %.3e \\\\ \n',k, xk(1), xk(2), xk(3), xk(4), erroreGS_rilassato(k));
end