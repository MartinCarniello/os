'''
Created on 11/05/2013

@author: Carne
'''

class PCBPriority():
    def __init__(self, pcb, priority):
        self.pcb = pcb
        
        self.priority = priority
        
    def getPCB(self):
        return self.pcb
        
    def getPriority(self):
        return self.priority
    
    def getPID(self):
        return self.getPCB().getPID()