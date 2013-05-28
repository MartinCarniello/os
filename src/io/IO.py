'''
Created on 27/04/2013

@author: Carne
'''

import threading
import time
from kernel import IOToReadyInterruption, IOToEndInterruption
from io import Waiting

class IO(threading.Thread):
    def __init__(self, mmu):
        threading.Thread.__init__(self)
        self.pcb = None
        self.kernel = None
        self.waiting = Waiting.Waiting()
        self.running = True
        self.mmu = mmu
        
    def getRunning(self):
        return self.running
    
    def setRunning(self, running):
        self.running = running
    
    def getWaiting(self):
        return self.waiting
    
    def getKernel(self):
        return self.kernel
    
    def setKernel(self, kernel):
        self.kernel = kernel
    
    def getPCB(self):
        return self.pcb
    
    def setPCB(self, pcb):
        self.pcb = pcb
        
    def getMmu(self):
        return self.mmu
    
    def restart(self):
        self.setPCB(None)
        
    def startUp(self):
        self.setRunning(True)
        self.start()
        
    def run(self):
        while(self.getRunning()):
            if self.getKernel().isUserMode() and (not self.getWaiting().isEmpty()):
                self.setPCB(self.getWaiting().get())
    
                pcbID = self.getPCB().getPID()
                pcbPC = self.getPCB().getPC()
                    
                ins = self.getMmu().fetchInstruction(pcbID, pcbPC)
                    
                print("Se esta ejecutando la instruccion " + str(pcbPC) + " del proceso " + str(pcbID) + " en I/O")
                print("El resultado es: " + ins.getResult())
                self.getPCB().nextInstruction()
                
                time.sleep(ins.getTime())
                
                print("Se termino de ejecutar la instruccion " + str(pcbPC) + " del proceso " + str(pcbID) + " en I/O")
                    
                #self.instructionExecute(ins)    
                
                if self.getPCB().isEnded():
                    self.getKernel().handle(IOToEndInterruption())
                else:
                    self.getKernel().handle(IOToReadyInterruption())
            
    def instructionExecute(self, instruction):
        time.sleep(instruction.getTime())