'''
Created on 25/05/2013

@author: Carne
'''

from scheduler import ReadyFIFO, ReadyPriority
from estructuraCpu import Cpu
from temporizador import Clock
from io import IO
from executionPolitic import Simple, RoundRobin
from end import End
from kernel import Kernel
from pcb import PCB, PCBPriority
from programaEInstrucciones import Instruction
from memory import Memory
from process import Process


if __name__ == '__main__':
    ins1p1 = Instruction.Instruction(True, "resultado ins1p1")
    ins2p1 = Instruction.Instruction(True, "resultado ins2p1")
    ins3p1 = Instruction.Instruction(True, "resultado ins3p1")
    ins4p1 = Instruction.Instruction(False, "resultado ins4p1", 10)
    instructionsP1 = [ins1p1, ins2p1, ins3p1, ins4p1]
    p1 = Process.Process(1, instructionsP1)
    
    ins1p2 = Instruction.Instruction(True, "resultado ins1p2")
    ins2p2 = Instruction.Instruction(True, "resultado ins2p2")
    ins3p2 = Instruction.Instruction(True, "resultado ins3p2")
    ins4p2 = Instruction.Instruction(False, "resultado ins4p2", 5)
    instructionsP2 = [ins1p2, ins2p2, ins3p2, ins4p2]
    p2 = Process.Process(2, instructionsP2)
    
    memory = Memory.Memory()
    memory.putProcess(p1)
    memory.putProcess(p2)
    
    pcbP1 = PCB.PCB(1, len(p1.getInstructions()))
    pcbP2 = PCB.PCB(2, len(p2.getInstructions()))
    
    #pcbP1 = PCBPriority.PCBPriority(pcbP1, 10)
    #pcbP2 = PCBPriority.PCBPriority(pcbP2, 3)
    
    cpu = Cpu.Cpu(memory)
    policy = Simple.Simple()
    #policy = RoundRobin.RoundRobin(1)
    scheduler = ReadyFIFO.ReadyFIFO(cpu, policy)
    #scheduler = ReadyPriority.ReadyPriority(cpu, policy)
    scheduler.put(pcbP1)
    scheduler.put(pcbP2)
    io = IO.IO(memory)
    end = End.End()
    
    clock = Clock.Clock()
    clock.addObserver(cpu)
    clock.addObserver(scheduler)
    
    kernel = Kernel.Kernel(scheduler, cpu, memory, io, end, clock)
    
    kernel.turnOn()