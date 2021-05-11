## PSEUDOCODE PRETTIER

import pyperclip
code = pyperclip.paste()  # get code from clipboard

# user definitions
rep = {
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

# user replacements
for old in rep:
    code = code.replace(old, rep[old])

# surround operators with spaces
for op in {'+', '-', '*', '/', '=', '<', '>', '∧', 'V', '∈'}:
    code = code.replace(op, ' ' + op + ' ')
    code = code.replace('  ' + op, ' ' + op)
    code = code.replace(op + '  ', op + ' ')
    code = code.replace(op + ' ' + op, op + op)

# remove spaces between operators and '='
for op in {'+', '-', '*', '/', '!', '<', '>'}:
    code = code.replace(op + ' =', op + '=')

code = code.splitlines()  # generate array of lines
first = True              # do not indent first line

out = '```pseudocode\n'
for line in code:
    if len(line) > 0 and line[0] == '%':  # comment
        line = '/*' + line[1:] + ' */'
    if not first:                         # indent
        line = '    ' + line
    if first and len(line) > 0:           # do not indent
        first = False
    out += line + '\n'
out += '```'

pyperclip.copy(out)  # copy pretty code to clipboard
print(out)
print('\nCopied to clipboard!')

