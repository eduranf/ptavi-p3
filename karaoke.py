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
        parametro = lista[1]
        if parametro.split(':')[0] == "http":
            parametro = parametro.split("/")[-1]
            os.system("wget -q " + parametro)
            print str(parametro)
            
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
                for elemento in dicc.keys():
                    frase = frase + elemento + '="' + dicc[elemento] + '"' + "\t"
                print "Elemento: " + atributos[0] + "\t" + "Atributos: " + frase
