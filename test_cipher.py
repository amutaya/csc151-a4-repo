#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Annah N Mutaya
# Created Date: 2/18/2022
# ---------------------------------------------------------------------------
"""This file contains all the unit tests for the functionality of the cipher.py program"""
# ---------------------------------------------------------------------------

from asyncore import read
from cipher import *
import pytest
import unittest

"""Class to test the functions in `cipher.py`. """
class UnitTesting(unittest.TestCase):
    def setUp(self):
        pass

    def  test_encryption_decryption(self):
        """Unit test to compare the output of the original encrypted file to the output of the decryption of the same file using
        the same encryption pad."""
        text_file = open('test.txt',"r")
        original_message  = text_file.read()
        text_file.close()
        encrypted_message = encipher("test.txt","test_pad.txt")
        self.assertEqual(original_message,  decipher("test_encipher.txt", "test_pad.txt"))

    def test_uppercase(self):
        """To test if the output of the decrypted message will be the same as the upper cause of the original message. This is
        important in case our original text was all in upper case or lower case."""
        text_file = open('test.txt',"r")
        original_message  = text_file.read()
        text_file.close()
        encrypted_message = encipher("test.txt","test_pad.txt")
        self.assertTrue(original_message, decipher("test_encipher.txt", "test_pad.txt").isupper())

    def test_encipher_invalidFileNames(self):
        """Unit test for when a user inputs a string instead of a file name to encipher(). Program will throw an error.
        decipher() will also throw an error."""
        with pytest.raises(Exception) as exp:
             encipher("Annah", "Mutaya.txt")

if __name__ == '__main__':
    unittest.main()
