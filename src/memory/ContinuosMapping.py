'''
Created on 10/06/2013

@author: usuario
'''

from MemoryAllocation import MMU
from MemoryBlock import *
from pcb import PCB

class ContinuosMapping(MMU):
    def __init__(self):
        self.freeBlocks = FreeBlock()
        self.occupedBlocks = OccupedBlock()
        
    def getFreeBlocks(self):
        return self.freeBlocks
    
    def getOccupedBlocks(self):
        return self.occupedBlocks
    
    def getBiggestBlog(self):
        blockSize = 0
        
        for block in self.getFreeBlocks():
            if block.size() > blockSize:
                blockSize = block.size()
                
        return blockSize
    
    def getFreeSpace(self):
        freeSpace = 0
        
        for b in self.getFreeBlocks():
            freeSpace = freeSpace + b.size()
            
        return freeSpace
    
    def swapIn(self, blockList, pid):
        memBlock = self.getFreeBlock(blockList.size())
        if memBlock != None:
            self.assignBlock(memBlock, blockList)
        else:
            if self.getFreeSpace() >= blockList.size():
                self.memoryCompact()
                self.assignBlock(memBlock, blockList)
    
class FirstFit(ContinuosMapping):
    def getFreeBlock(self, size):
        for block in self.getFreeBlocks():
            if block.size() >= size:
                return block
            
class BestFit(ContinuosMapping):
    def getFreeBlock(self, blockSize):
        biggestBlockSize = self.getSizeOfBiggestBlock()
        block = None
        
        for b in self.getFreeBlocks():
            if b.size() <= biggestBlockSize and b.size() >= blockSize:
                biggestBlockSize = b.size()
                block = b
                
        return block
            
class WorstFit(ContinuosMapping):
    def getFreeBlock(self, blockSize):
        biggestBlockSize = self.getSizeOfBiggestBlock()
        b = None
        
        for block in self.getFreeBlocks():
            if block.size() == biggestBlockSize and block.size() >= blockSize:
                b = block
                
        return b