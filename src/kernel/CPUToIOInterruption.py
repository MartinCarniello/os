'''
Created on 18/05/2013

@author: Carne
'''

from kernel import Interruption

class CPUToIOInterruption(Interruption.Interruption):
    def interruptionMethod(self, kernel):
        kernel.sendPCBToWaiting()
        kernel.restartQuantum()
        kernel.restartCPU()
        kernel.contextSwitch()