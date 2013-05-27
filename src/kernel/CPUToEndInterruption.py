'''
Created on 11/05/2013

@author: Carne
'''

from kernel import Interruption

class CPUToEndInterruption(Interruption.Interruption):
    def interruptionMethod(self, kernel):
        kernel.sendPCBFromCPUToEnd()
        kernel.restartQuantum()
        kernel.restartCPU()
        kernel.contextSwitch()