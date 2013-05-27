'''
Created on 18/05/2013

@author: Carne
'''

from kernel import Interruption

class IOToEndInterruption(Interruption.Interruption):
    def interruptionMethod(self, kernel):
        kernel.sendPCBFromIOToEnd()
        kernel.restartIO()