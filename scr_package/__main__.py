import sys
from scr_package import translator_en_es as en_es
from scr_package import translator_es_en as es_en

if __name__ == "__main__":
    if sys.argv[1] == 'en_es':
        print(en_es.translate_word(sys.argv[2]))
    elif sys.argv[2]:
        print(es_en.translate_word(sys.argv[2]))