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
        self.dicc_RL = {}
        self.dicc_region = {}
        self.dicc_img = {}
        self.dicc_audio = {}
        self.dicc_txtstr = {}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.dicc_RL['width'] = attrs.get('width', "")
            self.dicc_RL['height'] = attrs.get('height', "")
            self.dicc_RL['background-color'] = attrs.get('background-color', "")
            self.lista_elem.append(['root-layout', self.dicc_RL])

        elif name == 'region':
            self.dicc_region['id'] = attrs.get('id', "")
            self.dicc_region['top'] = attrs.get('top', "")
            self.dicc_region['bottom'] = attrs.get('bottom', "")
            self.dicc_region['left'] = attrs.get('left', "")
            self.dicc_region['right'] = attrs.get('right', "")
            self.lista_elem.append(['region', self.dicc_region])

        elif name == 'img':
            self.dicc_img['src'] = attrs.get('src', "")
            self.dicc_img['region'] = attrs.get('region', "")
            self.dicc_img['begin'] = attrs.get('begin', "")
            self.dicc_img['dur'] = attrs.get('dur', "")
            self.lista_elem.append(['img', self.dicc_img])

        elif name == 'audio':
            self.dicc_audio['src'] = attrs.get('src', "")
            self.dicc_audio['begin'] = attrs.get('begin', "")
            self.dicc_audio['dur'] = attrs.get('dur', "")
            self.lista_elem.append(['audio', self.dicc_audio])

        elif name == 'textstream':
            self.dicc_txtstr['src'] = attrs.get('src', "")
            self.dicc_txtstr['region'] = attrs.get('region', "")
            self.lista_elem.append(['textstream', self.dicc_txtstr])

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':
            self.dicc_RL = {}
        elif name == 'region':
            self.dicc_region = {}
        elif name == 'img':
            self.dicc_img = {}
        elif name == 'audio':
            self.dicc_audio = {}         
        elif name == 'textstream':
             self.dicc_txtstr = {}

    def get_tags(self):
        """
        Metodo que devuelve una lista de elementos
        """
        return self.lista_elem
