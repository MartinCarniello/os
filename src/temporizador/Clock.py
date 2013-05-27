'''
Created on 04/05/2013

@author: Carne
'''

import threading
import time

class Clock(threading.Thread):

    def getRunning(self):
        return self.running

    def setRunning(self, value):
        self.running = value

    def __init__(self):
        threading.Thread.__init__(self)
        self.setRunning(True)
        
    def run(self, temporizador):
        while(self.getRunning()):
            temporizador.click()
            time.sleep(1)
        
    def startUp(self, temporizador):
        self.run(temporizador)