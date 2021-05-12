# XCV formatter
Formatta il testo copiato da slides in PDF per adattarlo ad appunti in Markdown.


## Funzionalità

Gli script qui presenti permettono di formattare il testo presente negli appunti, copiato da slides in formato PDF, per adattarlo alla sintassi del linguaggio Markdown.
Il testo abbellito viene copiato negli appunti in modo da essere subito disponibile per incollarlo a destinazione.


## Utilizzo

1. Eseguire lo script `xcv-formatter.py`
2. Selezionare una porzione di testo
3. Premere la combinazione di tasti <kbd>Ctrl</kbd>+<kbd>X</kbd>+<kbd>C</kbd> per copiare il testo
4. Incollare il testo formattato a destinazione
5. Premere <kbd>Ctrl</kbd>+<kbd>Esc</kbd> quando si vuole terminare l'esecuzione


## Lista dei PDF supportati

Funziona correttamente per le seguenti raccolte di slide, o per porzioni di esse.

#### UniTN – DISI

- **Algoritmi e Strutture Dati** – Alberto Montresor, 2020-2021 (`ASD.py`)
  - <u>Funziona per</u>: **blocchi di pseudocodice**
  - Genera un blocco di codice (`` ```pseudocode ... ``` ``)
  - Corregge le spaziature e altre imperfezioni
  - Intenta tutto il codice con 4 spazi, tranne la prima riga[^*]
- **Sistemi Operativi 1** – Bruno Crispo, 2020-2021 (`SO.py`)
  - <u>Funziona per</u>: **elenchi** (maggior parte dei contenuti)
  - Marca la prima riga come titolo h3 (`###`)
  - Dispone il testo in un elenco di (soli) due livelli[^*]
  - Corregge alcune imperfezioni

[^*]: Non sono presenti informazioni nel testo di origine per definire livelli superiori
