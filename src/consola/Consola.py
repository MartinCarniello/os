'''
Created on 27/04/2013

@author: Carne
'''

import re
import sys
from shell import Shell
from shellAndConsoleExceptions import Exceptions

class Console():

    def setCommands(self, comand):
        self.commands = comand

    def getCommands(self):
        return self.commands

    def setRunning(self, run):
        self.running = run

    def getRunning(self):
        return self.running

    def setShell(self, s):
        self.shell = s

    def getShell(self):
        return self.shell
    
    def __init__(self):
        self.commands = [AddUser(), LogIn(), WhoIAm(), RemoveUser(), SetAsAdmin(), Users(), ChangePassword()]
        self.running = True
        self.shell = Shell.Shell("admin", "admin")

    def run(self):
        while(self.getRunning()):
            inp = input("<")
            self.commandExecute(inp)

    def commandExecute(self, inp):
        inpAux = inp.split()
        foundIt = False
        for command in self.getCommands():
            regExpInp = re.compile(r"\A" + command.getName() + "\Z", re.IGNORECASE)
            if(regExpInp.match(inpAux[0])):
                command.execute(self.getShell(), inpAux)
                foundIt = True
                
        if(not foundIt):
            print("Command does not exist")    

class AddUser():
    def __init__(self):
        self.name = "addUser"

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name
    
    def execute(self, shell, inp):
        try:
            shell.addUser(inp[1], inp[2])
            print("User " + inp[1] + " has been created")
        except Exceptions.NotAdminException:
            print("Don't have admin's permission to create a new user")
        except Exceptions.UserAlreadyExistException:
            print("User " + inp[1] + " already exists")

class LogIn():
    def __init__(self):
        self.name = "logIn"

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def execute(self, shell, inp):
        try:
            shell.login(inp[1], inp[2])
            print("You are logged as user " + inp[1])
        except Exceptions.IncorrectUserOrPasswordException:
            print("Nickname or password are incorrect")
        except:
            print("Wrong number of arguments")

class WhoIAm():
    def __init__(self):
        self.name = "whoIAm"

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def execute(self, shell, inp):
            print("You are logged as user " + shell.whoIAm())
            

class RemoveUser():
    def __init__(self):
        self.name = "removeUser"

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def execute(self, shell, inp):
        try:
            shell.removeUser(inp[1])
            print("User " + inp[1] + " has been removed from user's list")
        except Exceptions.UserDoesNotExistException:
            print("User " + inp[1] + " does not exist")
        except Exceptions.NotAdminException:
            print("Don't have admin's permission to remove a user")

class SetAsAdmin():
    def __init__(self):
        self.name = "setAsAdmin"

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def execute(self, shell, inp):
        try:
            shell.setAsAdmin(inp[1])
            print("User " + inp[1] + " has admin's permission from now on")
        except Exceptions.NotAdminException:
            print("Don't have permission to set a user to be admin")
        except Exceptions.UserDoesNotExistException:
            print("User you want to set as admin does not exist")

class Users():
    def __init__(self):
        self.name = "users"

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name
    
    def execute(self, shell, inp):
        for user in shell.getUsers():
            print(user.getNickName())


class ChangePassword():
    def __init__(self):
        self.name = "changePassword"

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def execute(self, shell, inp):
        try:
            shell.changePassword(inp[1], inp[2])
            print("User's password " + inp[1] + " has been succesfully modified")
        except Exceptions.NewPasswordEqualOldPasswordException:
            print("New password have to be different from the old one")
        except  Exceptions.IncorrectPasswordException:
            print("Old password is incorrect")
            
            
console = Console()
console.run()