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
        for atributos in self.lista:
            dicc = atributos[1]
            frase = ""
            for atrib in dicc.keys():
                if dicc[atrib] != "":
                    frase = frase + atrib + '="' + dicc[atrib] + '"' + "\t"
            print atributos[0] + "\t" + frase

    def do_local(self):
         for atributos in self.lista:
            dicc = atributos[1]
            for atrib in dicc.keys():
                if dicc[atrib].split(':')[0] == "http":
                    os.system("wget -q " + dicc[atrib])
                    dicc[atrib] = dicc[atrib].split("/")[-1]

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
        mi_kar.__str__()
        mi_kar.do_local()
        mi_kar.__str__()
