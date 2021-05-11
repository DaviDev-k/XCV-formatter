import pyperclip
from pynput.keyboard import Key, Listener


# user definitions
COMBINATION = {"key.ctrl", "'x'", "'c'"}  # lowercase
REPLACE = {
    'S.O.'  : 'SO',
    'S.O'   : 'SO',
    'S. O.' : 'SO',
    'á'     : 'à',
    'ú'     : 'ù',
    'o’'    : 'ò',
    ' piu ' : ' più '
}

def prettify():
    code = pyperclip.paste()
    for old in REPLACE:
        code = code.replace(old, REPLACE[old])
    code = code.splitlines()
    out = '### '
    misplaced = []
    for line in code:
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
    pyperclip.copy(out)

current = set()

def on_press(key):
    try:
        if str(key).lower() in COMBINATION:
            current.add(str(key).lower())
            if all(k in current for k in COMBINATION):
                prettify()
        elif key == Key.esc and "key.ctrl" in current:
            return False
    except AttributeError:
        pass

def on_release(key):
    try:
        current.remove(str(key).lower())
    except KeyError:
        pass

print('Keyboard listening!')
print('- Ctrl+X+C to copy and prettify')
print('- Ctrl+Esc to exit')
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

