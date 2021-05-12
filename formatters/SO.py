"""
**Sistemi Operativi 1** – Bruno Crispo, IV semestre 2021 (`SO.py`)
  - *Funziona per*: **elenchi puntati** (maggior parte dei contenuti)
  - *Formato*: **Markdown**
  - *Note*: selezionare l'intera slide, titolo compreso
  - *Problemi noti*: non funziona con elenchi ordinati
  - Marca la prima riga come titolo h3 (`###`)
  - Dispone il testo in un elenco di (soli) due livelli (*)
  - Corregge alcune imprecisioni
"""


REPLACE = {
    'S.O.'  : 'SO',
    'S.O'   : 'SO',
    'S. O.' : 'SO',
    ' à '   : '  `→`  ',
    'á'     : 'à',
    'ú'     : 'ù',
    'o’'    : 'ò',
    ' piu ' : ' più ',
    'Della thread' : 'Del thread',
    'della thread' : 'del thread',
    'sola thread'  : 'solo thread',
    'La thread'    : 'Il thread',
    'la thread'    : 'il thread',
    'Una thread'   : 'Un thread',
    'una thread'   : 'un thread',
    'Le thread'    : 'I threads',
    'le thread'    : 'i threads',
    'hreadss'      : 'hreads'
}


def form(code):
    out = '### '
    misplaced = []
    for line in code.splitlines():
        if line:
            if len(line) == 1:
                misplaced.append(('  ' if line == '–' else '') + '- ')
            elif line[0] == '•' or line[0] == '–':
                line = ('  ' if line[0] == '–' else '') + '- ' + line[2].upper() + line[3:]
            elif len(misplaced):
                line = misplaced.pop(0) + line[0].upper() + line[1:]
            else:
                out = out[:-1] + ' '
            if len(line) > 1:
                out += line + '\n'
    return out
