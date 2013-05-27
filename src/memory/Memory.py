'''
Created on 25/05/2013

@author: Carne
'''

class Memory():

    def __init__(self):
        self.memory = {}
        
    def fetchInstruction(self, idProcess, pc):
        return self.memory[idProcess][pc]
    
    def putProcess(self, process):
        self.memory[process.getID()] = process.getInstructions()