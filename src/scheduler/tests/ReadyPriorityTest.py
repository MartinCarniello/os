'''
Created on 04/05/2013

@author: Carne
'''
import unittest
from scheduler import ReadyPriority
from pcb import PCB, PCBPriority

class TestReadyFIFO(unittest.TestCase):
    def testGetPCB(self):
        queue = ReadyPriority.ReadyPriority("cpu")
        p1 = PCBPriority.PCBPriority(PCB.PCB(0), 2)
        p2 = PCBPriority.PCBPriority(PCB.PCB(1), 5)
        p3 = PCBPriority.PCBPriority(PCB.PCB(2), 1)
        queue.put(p1)
        queue.put(p2)
        queue.put(p3)
        self.assertEqual(2, queue.get().getPID())
        self.assertEqual(0, queue.get().getPID())
        self.assertEqual(1, queue.get().getPID())
        
if __name__ == '__main__':
    unittest.main()