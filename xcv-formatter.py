import os
import pyperclip
from pynput.keyboard import Key, Listener


COMBINATION = {"key.ctrl", "'x'", "'c'"}  # lowercase
current = set()


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


print('\n==== ' + pdf + ' ====')
print(module.__doc__)
print('=' * (10 + len(pdf)) + '\n')
print('Tastiera in ascolto:')
print(' - Ctrl+X+C per copiare e formattare')
print(' - Ctrl+Esc per terminare')
print('\nBuono studio!')


def format(replacements, form):
    clip = pyperclip.paste()
    for old in replacements:
        clip = clip.replace(old, replacements[old])
    pyperclip.copy(form(clip))


def on_press(key):
    try:
        if str(key).lower() in COMBINATION:
            current.add(str(key).lower())
            if all(k in current for k in COMBINATION):
                format(module.REPLACE, module.form)
        elif key == Key.esc and "key.ctrl" in current:
            return False
    except AttributeError:
        pass


def on_release(key):
    try:
        current.remove(str(key).lower())
    except KeyError:
        pass
    

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
