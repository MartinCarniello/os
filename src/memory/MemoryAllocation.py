'''
Created on 08/06/2013

@author: martin
'''

from pcb import PCB

class MMU():
    def __init__(self, mem, disk):
        self.memory = mem
        self.disk = disk
        
    def getMemory(self):
        return self.memory
    
    def setMemory(self, memory):
        self.memory = memory
        
    def getDisk(self):
        return self.disk
    
    def setDisk(self, disk):
        self.disk = disk
        
    def swapIn(self, programInstructions, pcb):
        pass
    
    def swapOut(self, programInstructions, pcb):
        pass
    
    def load(self, pid):
        programInstructions = self.getDisk().getProgramInstructions(pid)
        pcb = PCB(pid, programInstructions.getSize())
        self.swapIn(programInstructions, pcb)