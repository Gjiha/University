# Per generare tutti i codici e i dati della blockchain

- dopo aver modificato generatore.json,

- Oltre a tutto cuda e nvidia smi, occorre
  - sudo aptitude install nvidia-docker2
  - sudo systemctl daemon-reload
  - sudo systemctl restart docker
- e poi lo puoi provare con
  - docker run -it --rm --gpus all frextva:10 /bin/bash -i
- Ricorda inoltre che nel path ci devono essere i comandi (tools) di fabric, nella release che hai scelto (2.4.9)
  - ./install-fabric.sh -f 2.4.9 docker binary
  - e i bin vanno nel path di sistema
- RICORDA CHE docker-compose ora è senza -
- Infine esegui
  - ./RunMeFirst

## E poi seguire le istruzioni!

1. ./clean-start.sh
2. e, se serve, ./compile-and-deploy-chaincode.sh
   1. ricorda che in questo caso hai bisogno di jq installato!
      oppure
3. simply-start.sh

### To use domain names instead of localhost (ESEMPIO)

- add this string to /etc/hosts peer0.org1.cvbchain.com peer0.org2.cvbchain.com orderer.cvbchain.com orderer2.cvbchain.com

## Modify crontab if you want to restart the blockchain when the system restarts. use the following rule:

- crontab -e
  -- @reboot (sleep 30s ; cd directory_has_simplystart.sh ; ./simplystart.sh )&
  -- Consider that in some cases you have to add a PATH to simplystart

##### Con host[1234...]down usa --remove-orphans, quando necessario per eliminare container che non servono

## Per attivare la blockchain la prima volta

./RunMeFirst

## Poi sufficiente clean-start.sh (per cancellare tutto e rigenerare tutta la blockchain)
./clean-start.sh

### Compilare il chaincode
./compile-and-deploy-chaincode.sh

### questo non serve: è per sapere che internamente il container che compila fa i seguenti step

- cartella del progetto:
  go mod tidy
  go mod vendor
  e poi go build

- il chaincode va compilato con go1.18?
  -- go install golang.org/dl/go1.18@latest
  -- go1.18 download

## Per fare una prova solo della blockchain e per verificare il client lisp

1. accertarsi che la cartella client-lisp sia nella folder corrente
2. Run the complete environment, still without server

```bash
docker run -ti --net host --volume "$PWD":/vapps -v /:/altro dozenapps/frextva:latest /bin/bash -c 'cd /vapps; /bin/bash -i'
```

## e poi eseguire il comando guile

```bash
guile
```

## e poi copia e incolla delle seguenti linee, una per volta.
## NB: la connect teve tornare true e le AddKV devono tornare #t e le GetKV
## devono tornare i valori in formato JSON
```lisp
(use-modules (mtfa bc-client-lisp)) ;;(load-compiled "client-lisp/client.go")
(use-modules (mtfa utils))
(mtfa-bc::Connect "franco" "1" "kvdevel" "kvdevel.com")
(mtfa-bc::AddKV "franco" "TEST" #("a1" "a2" "a3") 12)
(mtfa-bc::AddKV "franco" "TEST" #("a1" "a2" "a3" "a4") '(("a" . 12)))
(mtfa-bc::GetKeys "franco" "TEST" "a1")
(mtfa-bc::GetKV "franco" "TEST" #("a1" "a2" "a3" "a4"))
,time (repeat 100 (mtfa-bc::AddKV "franco" "TEST" (list->vector (list "aa" (mtfa-rand-string 20) "bbb")) (mtfa-rand-ui)))
(mtfa-bc::GetKeys "franco" "TEST" "aa")
(mtfa-bc::Disconnect "franco")
```

- a seguire, per pulire, fare hostxxxdown.sh con --remove-orphans
- oppure clean-all.sh
