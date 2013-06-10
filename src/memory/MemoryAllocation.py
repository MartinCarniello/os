'''
Created on 08/06/2013

@author: martin
'''

class MemoryAllocation():
    def __init__(self, mem):
        self.memory = mem
        
    def getMemory(self):
        return self.memory
    
    def setMemory(self, memory):
        self.memory = memory
        
    def swapIn(self, process):
        pass
    
    def swapOut(self, process):
        pass
    
class ContinuosMapping(MemoryAllocation):
    def __init__(self):
        
    
class FirstFit(ContinuosMapping):
    def swapIn(self, process):
        
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
    def __init__(self):
        self.blocks = []