en_es = {'red': 'rojo', 'blue': 'azul', 'green': 'verde'}

def translate_word(word):
    if word.lower() in en_es:
        return en_es[word.lower()]
    else:
        return 'Word not found'