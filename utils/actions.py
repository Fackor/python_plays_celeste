# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:48:59 2021

@author: DELL
"""
from .keys import Keys
import time

class Actions():
    '''
    This class will define the actions our agent can take. An action object will be 
    used to take any action taken by our agent. We abstract away the complexities of
    sending keys to the game using this class.
    
    The game gives up 8 movement actions - 
        cardinal movements - UP, DOWN, LEFT, RIGHT 
        **diagonal movements - TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT
        
        ** diagonal movements are only used for dashes, so we will not implement them
           yet since we need to access the game state to check if dash is available
    
    We also have 3 special actions -
        JUMP - The most used movement for Madeline.
        **CLIMB - Madeline can scale walls for a small duration of time
        **DASH - Short dash (available only when hair is red). This will only be 
               when we start using the internal Game States. 
               
    ** - currently not implemented
    '''
    def __init__(self):
        self.JUMP_KEY = "C"
        self.UP = "UP"
        self.DOWN = "DOWN"
        self.RIGHT = "RIGHT"
        self.LEFT = "LEFT"
        self.keys = Keys()
    
    def SHORT_JUMP(self):
        self.keys.directKey(self.JUMP_KEY, type=self.keys.virtual_keys)
        time.sleep(0.025)
        self.keys.directKey(self.JUMP_KEY, self.keys.key_release, self.keys.virtual_keys)
        
    def HIGH_JUMP(self):
        self.keys.directKey(self.JUMP_KEY, type=self.keys.virtual_keys)
        time.sleep(0.3)
        self.keys.directKey(self.JUMP_KEY, self.keys.key_release, self.keys.virtual_keys)
        
    def RUN_LEFT(self, duration):
        self.keys.directKey(self.LEFT, type=self.keys.virtual_keys)
        time.sleep(duration)
        self.keys.directKey(self.LEFT, self.keys.key_release, self.keys.virtual_keys)
    
    def RUN_RIGHT(self, duration):
        self.keys.directKey(self.RIGHT, type=self.keys.virtual_keys)
        time.sleep(duration)
        self.keys.directKey(self.RIGHT, self.keys.key_release, self.keys.virtual_keys)
        
        
        
    