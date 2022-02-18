#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Annah N Mutaya
# Created Date: 2/18/2022
# ---------------------------------------------------------------------------
"""This file contains all the unit tests for the functionality of the cipher.py program"""
# ---------------------------------------------------------------------------

from cipher import *

def generatePad_test():
    assert generatePad() == 1000