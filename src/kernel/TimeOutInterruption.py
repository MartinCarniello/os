'''
Created on 11/05/2013

@author: Carne
'''

from kernel import Interruption

class TimeOutInterruption(Interruption.Interruption):
    def interruptionMethod(self, kernel):
        kernel.contextSwitch()
        kernel.restartQuantum()