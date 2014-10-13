#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
import os
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal():
    """
    Clase para gestionar archivos karaoke
    """
    def __init__(self, fich):
        parser = make_parser()
        KHandler = SmallSMILHandler()
        parser.setContentHandler(KHandler)
        parser.parse(open(fich))
        self.lista = KHandler.get_tags()

    def __str__(self):
        str_total = ""
        for atributos in self.lista:
            dic = atributos[1]
            frase = ""
            for atrib in dic.keys():
                if dic[atrib] != "":
                    frase = frase + atrib + '="' + dic[atrib] + '"' + "\t"
            str_total = str_total + atributos[0] + "\t" + frase
            if atributos != self.lista[-1]:
                str_total = str_total + "\n"
        return str_total

    def do_local(self):
        for atributos in self.lista:
            dic = atributos[1]
            for atrib in dic.keys():
                if dic[atrib].split(':')[0] == "http":
                    os.system("wget -q " + dic[atrib])
                    dic[atrib] = dic[atrib].split("/")[-1]

if __name__ == "__main__":
    """
    Programa principal
    """
    lista = sys.argv
    if len(lista) != 2:
        print "Usage: python karaoke.py file.smil"
    else:
        fichero = lista[1]
        mi_kar = KaraokeLocal(fichero)
        print mi_kar.__str__()
        mi_kar.do_local()
        print mi_kar.__str__()
