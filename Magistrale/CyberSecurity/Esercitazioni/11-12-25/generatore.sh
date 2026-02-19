#!/bin/bash
# File: genera_sito.sh
# Eseguire come root o sudo

# Directory di destinazione (modifica se necessario)
WEB_ROOT="html"

echo "Generazione file in $WEB_ROOT..."

# 1. Generazione 10 Pagine STATICHE (HTML)
for i in {1..10}
do
   cat <<EOF > $WEB_ROOT/info_page_$i.html
<!DOCTYPE html>
<html>
<head><title>Pagina Statica $i</title></head>
<body>
    <h1>Informazioni Sezione $i</h1>
    <p>Questa è una pagina statica di puro contenuto informativo.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <hr>
    <footer>Copyright Azienda finta</footer>
</body>
</html>
EOF
done

# 2. Generazione 10 Pagine DINAMICHE (PHP) con TEMPI DI RISPOSTA DIVERSI
# Array associativo: NomeFile -> Ritardo in microsecondi (1000000 = 1 secondo)
declare -A pages
pages=( 
    ["login.php"]=200000      # 0.2s - Veloce
    ["dashboard.php"]=500000  # 0.5s - Medio
    ["report.php"]=1500000    # 1.5s - Lento (query pesante)
    ["search.php"]=800000     # 0.8s
    ["profile.php"]=300000    # 0.3s
    ["upload.php"]=2000000    # 2.0s - Molto lento
    ["news.php"]=100000       # 0.1s - Velocissimo
    ["api_v1.php"]=400000     # 0.4s
    ["settings.php"]=600000   # 0.6s
    ["export.php"]=2500000    # 2.5s - Il più lento (simula generazione PDF)
)

for page in "${!pages[@]}"
do
   delay=${pages[$page]}
   cat <<EOF > $WEB_ROOT/$page
<?php
// Simulazione carico di lavoro (sleep)
usleep($delay+rand(-$delay/5, $delay/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: $page</title></head>
<body>
    <h1>Modulo Dinamico: $page</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: $(($delay / 1000)) ms</p>
    <p>Richiesta processata dal server: <?php echo \$_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
EOF
done

echo "Fatto! 10 pagine HTML e 10 pagine PHP create in $WEB_ROOT."
