import os
import pyperclip
from pynput.keyboard import Key, Listener

COMBINATION = {"key.ctrl", "'x'", "'c'"}  # lowercase
current = set()

pdflist = [file.removesuffix('.py') for file in os.listdir('formatters') if file[-3:] == '.py']
for i in range(len(pdflist)):
    print(str(i + 1) + '. ' + pdflist[i])
pdf = int(input('Cosa studi oggi? ')) - 1
module = __import__('formatters.' + pdflist[pdf], fromlist=[pdflist[pdf]])


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
    

print('\nTastiera in ascolto!')
print(' - Ctrl+X+C per copiare e formattare')
print(' - Ctrl+Esc per terminare')

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
