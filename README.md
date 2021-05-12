![XCV.png](XCV.png)


## Funzionalità

Gli script qui presenti permettono di formattare il testo presente negli appunti, copiato da slides in formato PDF, per adattarlo alla sintassi desiderata.
Il testo abbellito viene copiato negli appunti in modo da essere subito disponibile per incollarlo a destinazione.


## Utilizzo

1. Eseguire lo script `xcv-formatter.py`
2. Selezionare una porzione di testo dai PDF supportati
3. Premere la combinazione di tasti <kbd>Ctrl</kbd>+<kbd>X</kbd>+<kbd>C</kbd> per copiare il testo
4. Incollare il testo formattato a destinazione
5. Premere <kbd>Ctrl</kbd>+<kbd>Esc</kbd> quando si vuole terminare l'esecuzione


## Lista dei PDF supportati

Funziona correttamente per le seguenti raccolte di slide, o per porzioni di esse.

#### UniTN – DISI

- **Algoritmi e Strutture Dati** – Alberto Montresor, III-IV semestre 2020-2021 (`ASD.py`)
  - *Funziona per*: **blocchi di pseudocodice**
  - *Formato*: **Markdown**
  - Genera un blocco di codice (`` ```pseudocode {...} ``` ``)
  - Corregge le spaziature e altre imprecisioni
  - Indenta tutto il codice con 4 spazi, tranne la prima riga (*)
- **Sistemi Operativi 1** – Bruno Crispo, IV semestre 2021 (`SO.py`)
  - *Funziona per*: **elenchi** (maggior parte dei contenuti)
  - *Formato*: **Markdown**
  - Marca la prima riga come titolo h3 (`###`)
  - Dispone il testo in un elenco di (soli) due livelli (*)
  - Corregge alcune imperfezioni

(*) Non sono presenti informazioni nel testo originale per definire altri livelli


## Collaborazioni

È possibile creare il proprio insieme di regole usando il file `form.py` come template:
1. Copiare il template nella cartella `formatters`
2. Rinominare il file a piacere
3. Modificare il file con il proprio insieme di sostituzioni e regole
