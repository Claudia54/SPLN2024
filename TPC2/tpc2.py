from jjcli import clfilter
from collections import Counter
import re
import sys
from utils import *


cl=clfilter("cinm:", doc=__doc__)
def tokenize(text):
    return re.findall(r'\w+(?:-\w+)?|[.,?!;:—]+', text)

def print_word_freq(counter):
    for word, freq in counter:
        print(f"{word} --> {freq}")



for txt in cl.text(): 
    lista_palavras = tokenize(txt)
    ocorr = Counter(lista_palavras)
    
    lista_palavras_minusculas = set(map(str.lower, lista_palavras))
    ocorr_minusculas = Counter(lista_palavras_minusculas)
    
    if "-n" in cl.opt and "-m" in cl.opt:
        print_word_freq(sorted(ocorr.most_common(int(cl.opt.get("-m")))))
    
    elif "-m" in cl.opt:
        print_word_freq(ocorr.most_common(int(cl.opt.get("-m"))))

    elif "-n" in cl.opt:
        print_word_freq(sorted(ocorr.items()))

    elif "-i" in cl.opt:
        print_word_freq(ocorr_minusculas.items())
    else:
        print_word_freq(ocorr.items())