'''
Created on 11/05/2013

@author: Carne
'''

class Kernel():
    
    def getCpu(self):
        return self.cpu
    
    def getIO(self):
        return self.io
    
    def getEnd(self):
        return self.end
    
    def getScheduler(self):
        return self.scheduler
    
    def setKernelMode(self, value):
        self.kernelMode = value
        
    def getKernelMode(self):
        return self.kernelMode
        
    def isUserMode(self):
        return not self.getKernelMode()
    
    def isKernelMode(self):
        return self.getKernelMode()
    
    def getWaiting(self):
        return self.getIO().getWaiting()
    
    def getClock(self):
        return self.clock
    
    def __init__(self, scheduler, cpu, mmu, io, end, clock):
        self.scheduler = scheduler
        self.cpu = cpu
        cpu.setKernel(self)
        self.mmu = mmu
        self.io = io
        io.setKernel(self)
        self.end = end
        self.kernelMode = False
        self.clock = clock
        
    def handle(self, interruption):
        interruption.doIt(self)
        
    def contextSwitch(self):
        self.getScheduler().contextSwitch()
        
    def restartQuantum(self):
        self.getScheduler().restartQuantum()
        
    def restartCPU(self):
        self.getCpu().restart()
        
    def restartIO(self):
        self.getIO().restart()
        
    def sendPCBFromCPUToEnd(self):
        self.getEnd().put(self.getCpu().getPCB())
        
    def sendPCBFromIOToEnd(self):
        self.getEnd().put(self.getIO().getPCB())
        
    def sendPCBToReady(self):
        self.getScheduler().put(self.getIO().getPCB())
        
    def sendPCBToWaiting(self):
        self.getWaiting().put(self.getCpu().getPCB())
        
    def turnToKernelMode(self):
        self.setKernelMode(True)
        
    def turnToUserMode(self):
        self.setKernelMode(False)
        
    def turnOn(self):
        self.getScheduler().contextSwitch()
        self.getClock().startUp()
        self.getIO().startUp()