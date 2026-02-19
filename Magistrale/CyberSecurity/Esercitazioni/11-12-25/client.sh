#!/bin/bash
# Modifica con l'IP del tuo server/proxy
TARGET_URL="http://192.168.122.1"

# Elenco delle pagine possibili (HTML e PHP)
PAGES=(
"info_page_1.html" "info_page_1.html" "info_page_1.html" # Più frequente
"login.php" "login.php" # Frequente
"dashboard.php"
"search.php"
"news.php"
"report.php"
"export.php" # Rara
"info_page_2.html" "info_page_3.html" "info_page_4.html"
"profile.php"
)

echo "Avvio simulazione client (Premere CTRL+C per fermare)..."

while true; do
    # Seleziona una pagina a caso dall'array
    RANDOM_PAGE=${PAGES[$RANDOM % ${#PAGES[@]}]}
    
    echo "$(date +%H:%M:%S) - Utente visita: $RANDOM_PAGE"
    
    # Esegue la richiesta (silenziosa ma segue i redirect)
    curl -L -s -o /dev/null "$TARGET_URL/$RANDOM_PAGE" &
    
    # Aspetta un tempo casuale tra 0.1s e 1s prima della prossima richiesta
    sleep 0.$(( ( RANDOM % 9 ) + 1 ))
done
