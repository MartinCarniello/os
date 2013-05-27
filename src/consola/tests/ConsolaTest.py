'''
Created on 28/04/2013

@author: Carne
'''

from unittest import TestCase 
from exceptions import Exceptions
from shell import Shell
from consola import Consola

class TestConsola(TestCase):
    def setUp(self):
        self.consola = Consola.Consola()
        self.consola.getShell().addUser("u1", "123456")
        self.consola.getShell().addUser("u2", "abcdef")