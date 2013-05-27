'''
Created on 04/05/2013

@author: Carne
'''

class PCB():
    def __init__(self, pid, nInstructions):
        self.setPC(0)
        self.setPID(pid)
        self.setNumberOfInstructions(nInstructions)
        
    def isEnded(self):
        return self.getPC() == self.getNumberOfInstructions()
    
    def setNumberOfInstructions(self, n):
        self.numberOfInstructions = n
        
    def setPC(self, p):
        self.pc = p
        
    def getNumberOfInstructions(self):
        return self.numberOfInstructions
        
    def getPC(self):
        return self.pc

    def setPID(self, p):
        self.pid = p
        
    def getPID(self):
        return self.pid
    
    def nextInstruction(self):
        self.setPC(self.getPC() + 1)
