"""[Specifica del corso]"""


# Lista delle sostituzioni preliminari
REPLACE = {
    'old': 'new',
    '...': '...'
}


# Funzione per la formattazione
def form(text: str) -> str:
    """Regole per formattare il testo negli appunti

    Parameters
    ----------
    text : str
        Testo copiato

    Returns
    -------
    str
        Testo formattato
    """

    out = ''
    for line in text.splitlines():
        out += line + '\n'
    return out
