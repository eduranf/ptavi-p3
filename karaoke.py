#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
import os
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":
    """
    Programa principal
    """
    lista = sys.argv
    if len(lista) != 2:
        print "Usage: python karaoke.py file.smil"
    else:
        fich = lista[1]
        parser = make_parser()
        KHandler = SmallSMILHandler()
        parser.setContentHandler(KHandler)
        parser.parse(open(fich))
        lista = KHandler.get_tags()
        for atributos in lista:
            dicc = atributos[1]
            frase = ""
            for atrib in dicc.keys():
                if dicc[atrib] != "":
                    if dicc[atrib].split(':')[0] == "http":
                        os.system("wget -q " + dicc[atrib])
                        dicc[atrib] = dicc[atrib].split("/")[-1]
                    frase = frase + atrib + '="' + dicc[atrib] + '"' + "\t"
            print atributos[0] + "\t" + frase
