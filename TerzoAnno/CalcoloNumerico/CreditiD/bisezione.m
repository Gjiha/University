function [m, K, fx] = bisezione(a, b, f, epsilon)
    %verifica che f(a) e f(b) siano di segno opposto
    if f(a) * f(b) > 0
        warning('f(a) e f(b) devono avere segni opposti');
    end

    %inizializzazione degli estremi dell'intervallo e contare delle
    %iterazioni

    alpha_k = a;
    beta_k = b;
    K = 0;

    %ripeti fintanto che la lunghezza dell'intervallo è maggiore di quella
    %richiesta

    while (beta_k - alpha_k) > epsilon
        %caloclo il punto medio dell'intervallo
        m = (alpha_k + beta_k) / 2;

        %se trovo la radice mi blocco
        if f(m) == 0
            break;
        end

        %aggiorno gli estremi dell'intervallo in base al segno di f(m)
        if f(alpha_k) * f(m) < 0
            beta_k = m;
        else
            alpha_k = m;
        end
        %incrementiamo il contatore delle iterazioni
        K = K + 1;
    end

    %calcolo l'approssimazione finale di m come punto medio dell'ultimo
    %intervallo

    m = (alpha_k + beta_k) / 2;
    fx = f(m);
end