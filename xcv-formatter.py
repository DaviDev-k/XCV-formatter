import os
import sys
import pyperclip
from pynput import keyboard


# Keymap
COPY = '<ctrl>+x+c'
EXIT = '<ctrl>+<esc>'


# Formatter selection
print('Formatters disponibili:')
pdflist = [file.removesuffix('.py') for file in os.listdir('formatters') if file[-3:] == '.py']
for i in range(len(pdflist)):
    print(str(i + 1) + '. ' + pdflist[i])
pdf = ''
print()
while pdf not in map(str, range(1, len(pdflist) + 1)):
    pdf = input('Cosa studi oggi? ')
pdf = pdflist[int(pdf) - 1]
module = __import__('formatters.' + pdf, fromlist=[pdf])


# Print info
print('\n==== ' + pdf + ' ====')
print(module.__doc__)
print('=' * (10 + len(pdf)) + '\n')
print('Tastiera in ascolto:')
print(' - Ctrl+X+C per copiare e formattare')
print(' - Ctrl+Esc per terminare')
print('\nBuono studio!')


# Paste, replace, format, copy
def format(replacements, form):
    clip = pyperclip.paste()
    for old in replacements:
        clip = clip.replace(old, replacements[old])
    pyperclip.copy(form(clip))


def format_wrapper():
    format(module.REPLACE, module.form)


# Main: keyboard listener
try:
    with keyboard.GlobalHotKeys({
        COPY: format_wrapper,
        EXIT: sys.exit
    }) as h:
        h.join()
except ValueError:
    pass
