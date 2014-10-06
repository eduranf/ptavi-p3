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
        self.rl_width = ""
        self.rl_height = ""
        self.rl_bgcolor = ""
        self.reg_id = ""
        self.reg_top = ""
        self.reg_bottom = ""
        self.reg_left = ""
        self.reg_right = ""
        self.img_src = ""
        self.img_region = ""
        self.img_begin = ""
        self.img_dur = ""
        self.audio_src = ""
        self.audio_begin = ""
        self.audio_dur = ""
        self.txtstr_src = ""
        self.txtstr_region = ""
        self.inRL = 0
        self.inRegion = 0
        self.inImg = 0
        self.inAudio = 0
        self.inTxtstr = 0
    
    def startElment(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.rl_width = attrs.get('width',"")
            self.rl_height = attrs.get('height',"")
            self.rl_bgcolor = attrs.get('background-color',"")
            self.inRL = 1
        elif name == 'region':
            self.reg_id = attrs.get('id',"")
            self.reg_top = attrs.get('top',"")
            self.reg_bottom = attrs.get('bottom',"")
            self.reg_left = attrs.get('left',"")
            self.reg_right = attrs.get('right',"")
            self.inRegion = 1
        elif name == 'img':
            self.img_src = attrs.get('src',"")
            self.img_region = attrs.get('region',"")
            self.img_begin = attrs.get('begin',"")
            self.img_dur = attrs.get('dur',"")
            self.inImg = 1
        elif name == 'audio':
            self.audio_src = attrs.get('src',"")
            self.audio_begin = attrs.get('begin',"")
            self.audio_dur = attrs.get('dur',"")
            self.inAudio = 1
        elif name == 'textstream':
            self.txtstr_src = attrs.get('src',"")
            self.txtstr_region = attrs.get('region',"")
            self.inTxtstr = 1

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':
            self.rl_width = ""
            self.rl_height = ""
            self.rl_bgcolor = "")
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
