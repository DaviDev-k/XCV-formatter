"""Sistemi Operativi 1 – Bruno Crispo, IV semestre 2021"""


REPLACE = {
    'S.O.'  : 'SO',
    'S.O'   : 'SO',
    'S. O.' : 'SO',
    'á'     : 'à',
    'ú'     : 'ù',
    'o’'    : 'ò',
    ' piu ' : ' più '
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
