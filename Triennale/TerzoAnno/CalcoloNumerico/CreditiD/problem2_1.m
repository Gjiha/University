%prima funzione

%f = @(x) x.^3 + 3*x - 1 - exp(-x.^2); a = 0; b = 1;

%seconda funzione

f = @(x) cos(x) - x; a = 0; b = pi;

x = linspace(a,b, 1000);
figure;
plot(x, f(x), 'LineWidth', 1.2);
grid on;
xlabel('x');
ylabel('f(x)');

xi = zeros(10,1);
k = zeros(10,1);
f_xi = zeros(10,1);

%ciclo sulle tolleranze
for i = 1:10
    eps = 10^(-i);
    [xi(i), k(i), f_xi(i)] = bisezione(a, b, f, eps);
end

for i = 1:10
    fprintf('$10^{-%d}$ & $%.10f$ & $%4d$ & $%.3e$ \\\\ \n', i, xi(i), k(i), f_xi(i));
end