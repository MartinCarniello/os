'''
Created on 04/05/2013

@author: Carne
'''

import executionPolitic
from kernel import TimeOutInterruption

class RoundRobin(executionPolitic.ExecutionPolitic):
    def __init__(self, quantum):
        super(RoundRobin, self).__init__()
        self.quantum = quantum
        self.actual = 0
    
    def getActual(self):
        return self.actual
    
    def setActual(self, value):
        self.actual = value
    
    def getQuantum(self):
        return self.quantum
    
    def nextActual(self):
        self.setActual(self.getActual() + 1)
        
    def restartQuantum(self):
        self.setActual(0)
    
    def executionCycle(self):
        self.nextActual()
        
        if self.getActual() == self.getQuantum():
            self.getKernel().handle(TimeOutInterruption.TimeOutInterruption())