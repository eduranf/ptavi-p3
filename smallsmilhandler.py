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
        self.dicc_RLup = {}
        self.dicc_RL = {}
        self.dicc_region = {}
        self.dicc_img = {}
        self.dicc_audio = {}
        self.dicc_txtstr = {}
        self.dicc_regionup = {}
        self.dicc_imgup = {}
        self.dicc_audioup = {}
        self.dicc_txtstrup = {}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.dicc_RL['width'] = attrs.get('width', "")
            self.dicc_RL['height'] = attrs.get('height', "")
            self.dicc_RL['background-color'] = attrs.get('background-color', "")
            self.dicc_RLup['root-layout'] = self.dicc_RL

        elif name == 'region':
            self.dicc_region['id'] = attrs.get('id', "")
            self.dicc_region['top'] = attrs.get('top', "")
            self.dicc_region['bottom'] = attrs.get('bottom', "")
            self.dicc_region['left'] = attrs.get('left', "")
            self.dicc_region['right'] = attrs.get('right', "")
            self.dicc_regionup['region'] = self.dicc_region

        elif name == 'img':
            self.dicc_img['src'] = attrs.get('src', "")
            self.dicc_img['region'] = attrs.get('region', "")
            self.dicc_img['begin'] = attrs.get('begin', "")
            self.dicc_img['dur'] = attrs.get('dur', "")
            self.dicc_imgup['img'] = self.dicc_img

        elif name == 'audio':
            self.dicc_audio['src'] = attrs.get('src', "")
            self.dicc_audio['begin'] = attrs.get('begin', "")
            self.dicc_audio['dur'] = attrs.get('dur', "")
            self.dicc_audioup['audio'] = self.dicc_audio

        elif name == 'textstream':
            self.dicc_txtstr['src'] = attrs.get('src', "")
            self.dicc_txtstr['region'] = attrs.get('region', "")
            self.dicc_txtstrup['textstream'] = self.dicc_txtstr

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':
            self.rl_width = ""
            self.rl_height = ""
            self.rl_bgcolor = ""
            self.inRL = 0
        elif name == 'region':
            self.reg_id = ""
            self.reg_top = ""
            self.reg_bottom = ""
            self.reg_left = ""
            self.reg_right = ""
            self.inRegion = 0
        elif name == 'img':
            self.img_src = ""
            self.img_region = ""
            self.img_begin = ""
            self.img_dur = ""
            self.inImg = 0
        elif name == 'audio':
            self.audio_src = ""
            self.audio_begin = ""
            self.audio_dur = ""
            self.inAudio = 0
        elif name == 'textstream':
            self.txtstr_src = ""
            self.txtstr_region = ""
            self.inTxtstr = 0

    def get_tags(self):
        """
        Metodo que devuelve una lista de elementos
        """
        self.lista_elem = [self.dicc_RLup, self.dicc_regionup, self.dicc_imgup, self.dicc_audioup, self.dicc_txtstrup]
        return self.lista_elem
    


