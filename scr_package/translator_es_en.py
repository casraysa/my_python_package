es_en = {'rojo': 'red', 'azul': 'blue', 'verde': 'green'}

def translate_word(word):
    if word.lower() in es_en:
        return es_en[word.lower()]
    else:
        return 'Palabra no encontrada'