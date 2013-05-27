'''
Created on 04/05/2013

@author: Carne
'''

import unittest
from scheduler import ReadyFIFO
from pcb import PCB

class TestReadyFIFO(unittest.TestCase):
    def testGetPCB(self):
        p1 = PCB.PCB(0, 3)
        p2 = PCB.PCB(1, 3)
        p3 = PCB.PCB(2, 3)
        queue = ReadyFIFO.ReadyFIFO(None, None)
        queue.put(p1)
        queue.put(p2)
        queue.put(p3)
        self.assertEqual(0, queue.get().getPID())
        self.assertEqual(1, queue.get().getPID())
        self.assertEqual(2, queue.get().getPID())
        
if __name__ == '__main__':
    unittest.main()