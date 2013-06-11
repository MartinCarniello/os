'''
Created on 10/06/2013

@author: usuario
'''

class Block():
    def __init__(self, base, limit):
        self.base = base
        self.limit = limit
        
    def getBase(self):
        return self.base
    
    def getLimit(self):
        return self.limit
    
    def size(self):
        return self.getLimit() - self.getBase() + 1
    
class FreeBlock():
    def __init__(self):
        self.blocks = []
        
    def getBlocks(self):
        return self.blocks
    
    def put(self, aBlock):
        self.getBlocks().append(aBlock)
        
    def get(self, index):
        return self.getBlocks()[index]
        
    def size(self):
        return len(self.getBlocks())
    
class OccupedBlock():
    def __init__(self, pcb):
        self.blocks = []
        self.pcb = pcb
        
    def getBlocks(self):
        return self.blocks
    
    def getPCB(self):
        return self.pcb
    
    def size(self):
        return len(self.getBlocks())