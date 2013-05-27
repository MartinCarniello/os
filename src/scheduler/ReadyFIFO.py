'''
Created on 04/05/2013

@author: Carne
'''

from scheduler import Scheduler
import Queue

class ReadyFIFO(Scheduler.Scheduler):
    def __init__(self, cpu, politica):
        Scheduler.Scheduler.__init__(self, cpu, politica)
        self.queue = Queue.Queue()

    def setQueue(self, q):
        self.queue = q
        
    def getQueue(self):
        return self.queue
        
    def put(self, pcb):
        self.getQueue().put(pcb)
        
    def get(self):
        return self.getQueue().get()