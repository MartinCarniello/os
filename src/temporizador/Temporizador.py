'''
Created on 04/05/2013

@author: Carne
'''

from temporizador import Clock

class Temporizador():
    def __init__(self):
        self.clock = Clock.Clock()
        self.observers = []

    def getClock(self):
        return self.clock

    def setClock(self, value):
        self.clock = value
        
    def getObsersvers(self):
        return self.observers
    
    def addObserver(self, observer):
        self.getObsersvers().append(observer)

    def startUp(self):
        self.getClock().startUp(self)
        
    def click(self):
        for observer in self.getObsersvers():
            observer.executionCycle()