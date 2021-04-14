# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:36:41 2021

@author: Ayan Gangopadhyay
"""
from utils.actions import Actions
import time

action_obj = Actions()
time.sleep(3)

for i in range(10):
    action_obj.SHORT_JUMP()
    action_obj.RUN_RIGHT(2)
    action_obj.HIGH_JUMP()

