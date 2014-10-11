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
        self.dic_RL = {}
        self.dic_region = {}
        self.dic_img = {}
        self.dic_audio = {}
        self.dic_txtstr = {}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.dic_RL['width'] = attrs.get('width', "")
            self.dic_RL['height'] = attrs.get('height', "")
            self.dic_RL['background-color'] = attrs.get('background-color', "")
            self.lista_elem.append(['root-layout', self.dic_RL])

        elif name == 'region':
            self.dic_region['id'] = attrs.get('id', "")
            self.dic_region['top'] = attrs.get('top', "")
            self.dic_region['bottom'] = attrs.get('bottom', "")
            self.dic_region['left'] = attrs.get('left', "")
            self.dic_region['right'] = attrs.get('right', "")
            self.lista_elem.append(['region', self.dic_region])

        elif name == 'img':
            self.dic_img['src'] = attrs.get('src', "")
            self.dic_img['region'] = attrs.get('region', "")
            self.dic_img['begin'] = attrs.get('begin', "")
            self.dic_img['dur'] = attrs.get('dur', "")
            self.lista_elem.append(['img', self.dic_img])

        elif name == 'audio':
            self.dic_audio['src'] = attrs.get('src', "")
            self.dic_audio['begin'] = attrs.get('begin', "")
            self.dic_audio['dur'] = attrs.get('dur', "")
            self.lista_elem.append(['audio', self.dic_audio])

        elif name == 'textstream':
            self.dic_txtstr['src'] = attrs.get('src', "")
            self.dic_txtstr['region'] = attrs.get('region', "")
            self.lista_elem.append(['textstream', self.dic_txtstr])

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':
            self.dic_RL = {}
        elif name == 'region':
            self.dic_region = {}
        elif name == 'img':
            self.dic_img = {}
        elif name == 'audio':
            self.dic_audio = {}
        elif name == 'textstream':
            self.dic_txtstr = {}

    def get_tags(self):
        """
        Metodo que devuelve una lista de elementos
        """
        return self.lista_elem
