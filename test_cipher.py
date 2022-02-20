#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Annah N Mutaya
# Created Date: 2/18/2022
# ---------------------------------------------------------------------------
"""This file contains all the unit tests for the functionality of the cipher.py program"""
# ---------------------------------------------------------------------------

from cipher import *

def test_encipher():
    assert encipher("encipher_test.txt", "encipher_test_pad.txt") == "NhN@m!"