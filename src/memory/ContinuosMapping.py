'''
Created on 10/06/2013

@author: usuario
'''

from MemoryAllocation import MMU
from MemoryBlock import *

class ContinuosMapping(MMU):
    def __init__(self):
        self.freeBlocks = FreeBlock()
        self.occupedBlocks = OccupedBlock()
        
    def getFreeBlocks(self):
        return self.freeBlocks
    
    def getOccupedBlocks(self):
        return self.occupedBlocks
    
    def getFreeSpace(self):
        freeSpace = 0
        
        for b in self.getFreeBlocks():
            freeSpace = freeSpace + b.size()
            
        return freeSpace
    
class FirstFit(ContinuosMapping):
    def swapIn(self, process):
        