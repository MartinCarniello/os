'''
Created on 10/06/2013

@author: usuario
'''

from MemoryAllocation import MMU
from MemoryBlock import *
from pcb import PCB

class ContinuosMapping(MMU):
    def __init__(self, freeBlocks, occupedBlocks):
        self.freeBlocks = freeBlocks
        self.occupedBlocks = occupedBlocks
        
    def putFreeBlock(self, aFreeBlock):
        self.getFreeBlocks().put(aFreeBlock)
        
    def putOccupedBlock(self, anOccupedBlock):
        self.getOccupedBlocks().put(anOccupedBlock)
        
    def getFreeBlocks(self):
        return self.freeBlocks.getBlocks()
    
    def getOccupedBlocks(self):
        return self.occupedBlocks.getBlocks()
    
    def getSizeOfBiggestBlock(self):
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
    
    def memoryCompact(self):
        
        firstBlock = self.getOccupedBlocks()[0]
        
        if firstBlock[1].getBase() != 0:
            
            sizeOfFirstBlock = firstBlock[1].size()
            
            base = 0
            limit = sizeOfFirstBlock - 1
            
            firstBlock[1].setBase(base)
            firstBlock[1].setLimit(limit)
            firstBlock[0].setBase(base)
            firstBlock[0].setLimit(limit)
        
        for block in self.getOccupedBlocks()[1:len(self.getOccupedBlocks())]:
            
            movement = block[1].getBase() - limit - 1
            
            newBase = block[1].getBase() - movement
            
            newLimit = block[1].getLimit() - movement
            
            block[1].setBase(newBase)
            
            block[1].setLimit(newLimit)
            
            limit = newLimit
            
            block[0].setBase(newBase)
            block[0].setLimit(newLimit)
            
        #newBlock = Block(limit, self.getMemory().size())
        #newFreeBlock = FreeBlock().put(newBlock)
        #self.setFreeBlocks(newFreeBlock)
                
    
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
                break
                
        return b
    
    
    
    
freeBlock1 = Block(0, 3)
freeBlock2 = Block(6, 7)
freeBlock3 = Block(10, 15)
        
occupedBlock1 = Block(4, 5)
occupedBlock2 = Block(8, 9)
occupedBlock3 = Block(16, 20)
                
freeBlocks = FreeBlock()
freeBlocks.put(freeBlock1)
freeBlocks.put(freeBlock2)
freeBlocks.put(freeBlock3)
                
pcb1 = PCB.PCB(1, 2)
pcb2 = PCB.PCB(2, 2)
pcb3 = PCB.PCB(3, 5)
                
occupedBlocks = OccupedBlock()
occupedBlocks.put(pcb1, occupedBlock1)
occupedBlocks.put(pcb2, occupedBlock2)
occupedBlocks.put(pcb3, occupedBlock3)
            
allocationMethod = FirstFit(freeBlocks, occupedBlocks)
                
allocationMethod.memoryCompact()

print(allocationMethod.getOccupedBlocks()[0][1].getBase())
print(allocationMethod.getOccupedBlocks()[0][1].getLimit())
print(allocationMethod.getOccupedBlocks()[1][1].getBase())
print(allocationMethod.getOccupedBlocks()[1][1].getLimit())
print(allocationMethod.getOccupedBlocks()[2][1].getBase())
print(allocationMethod.getOccupedBlocks()[2][1].getLimit())