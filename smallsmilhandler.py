#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar SMIL
    """

    def __init__(self):
        """
        Constructor
        """
        self.lista_elem = []
        dic_RL = {'width': "", 'height': "", 'background-color': ""}
        dic_reg = {'id': "", 'top': "",
                   'bottom': "", 'left': "", 'right': ""}
        dic_img = {'src': "", 'region': "", 'begin': "", 'dur': ""}
        dic_audio = {'src': "", 'begin': "", 'dur': ""}
        dic_txtstr = {'src': "", 'region': ""}
        self.lista_dic = {'root-layout': dic_RL, 'region': dic_reg,
                          'img': dic_img, 'audio': dic_audio,
                          'textstream': dic_txtstr}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        mi_dic = {}
        if name in self.lista_dic:
            for atrib in self.lista_dic[name].keys():
                mi_dic[atrib] = attrs.get(atrib, "")
            self.lista_dic[name] = mi_dic
            self.lista_elem.append([name, self.lista_dic[name]])

    def get_tags(self):
        """
        Metodo que devuelve una lista de elementos
        """
        return self.lista_elem
