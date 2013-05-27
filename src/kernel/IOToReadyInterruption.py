'''
Created on 11/05/2013

@author: Carne
'''

from kernel import Interruption

class IOToReadyInterruption(Interruption.Interruption):
    def interruptionMethod(self, kernel):
        kernel.sendPCBToReady()
        kernel.restartIO()