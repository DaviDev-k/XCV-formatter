"""
**Algoritmi e Strutture Dati** – Alberto Montresor, III-IV semestre 2020-2021 (`ASD.py`)
  - *Funziona per*: **blocchi di pseudocodice**
  - *Formato*: **Markdown**
  - Genera un blocco di codice (`` ```pseudocode {...} ``` ``)
  - Corregge le spaziature e altre imprecisioni
  - Indenta tutto il codice con 4 spazi, tranne la prima riga (*)
"""


REPLACE = {
    '( '      : '(',
    ' )'      : ')',
    ' ['      : '[',
    '[ '      : '[',
    ' ]'      : ']',
    '{ '      : '{',
    ' }'      : '}',
    ' ,'      : ',',
    ' .'      : '.',
    '. '      : '.',
    '−'       : '-',
    '·'       : '*',
    '≤'       : '<=',
    '≥'       : '>=',
    '6='      : '!=',
    'boolean' : 'bool'
}


def form(code):
    # surround operators with spaces
    for op in {'+', '-', '*', '/', '=', '<', '>', '∧', 'V', '∈'}:
        code = code.replace(op, ' ' + op + ' ')
        code = code.replace('  ' + op, ' ' + op)
        code = code.replace(op + '  ', op + ' ')
        code = code.replace(op + ' ' + op, op + op)
    
    # remove spaces between operators and '='
    for op in {'+', '-', '*', '/', '!', '<', '>'}:
        code = code.replace(op + ' =', op + '=')
    
    first = True  # do not indent first line
    out = '\n'
    for line in code.splitlines():
        if len(line) > 0 and line[0] == '%':  # comment
            line = '/*' + line[1:] + ' */'
        if not first:                         # indent
            line = '    ' + line
        if first and len(line) > 0:           # do not indent
            first = False
        out += line + '\n'
    
    return '```pseudocode' + out + '```'
