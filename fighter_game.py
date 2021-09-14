# -*- coding: utf-8 -*-
from random import randrange

class Fighter:
    """The base class of a Fighter"""
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.agility = randrange (1,9)

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def __repr__(self):
        return self.get_name()

    def get_agility (self):
        return self.__agility
        
