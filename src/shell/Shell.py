'''
Created on 27/04/2013

@author: Carne
'''
from shellAndConsoleExceptions import Exceptions

class Shell():
    def getUsers(self):
        return self.usuarios

    def setUsers(self, users):
        self.usuarios = users

    def getCurrentUser(self):
        return self.currentUser

    def setCurrentUser(self, usuario):
        self.currentUser = usuario

    def __init__(self, nickName, password):

        self.setUsers([])

        u = User(nickName, password)
        u.setIsAdmin(True)

        self.getUsers().append(u)

        self.setCurrentUser(u)


    def login(self, nickName, password):

        exist = False

        for user in self.getUsers():
            if(user.getNickName() == nickName):
                exist = True
                u = user

        if(exist and (u.getPassword() == password)):
            self.setCurrentUser(u)
        else:
            raise Exceptions.IncorrectUserOrPasswordException()

    def whoIAm(self):
        return self.getCurrentUser().getNickName()

    def addUser(self, nickName, password):

        exist = False

        for user in self.getUsers():
            if(user.getNickName() == nickName):
                exist = True

        if(self.getCurrentUser().getIsAdmin() and not exist):
            u = User(nickName, password)

            self.getUsers().append(u)
        elif self.getCurrentUser().getIsAdmin():
            raise Exceptions.UserAlreadyExistException()
        else:
            raise Exceptions.NotAdminException()

    def removeUser(self, nickName):
        exist = False

        for user in self.getUsers():
            if(user.getName() == nickName):
                exist = True
                u = user

        if(exist):
            if(self.getCurrentUser().getIsAdmin()):
                self.getUsuarios().remove(u)
            else:
                raise Exceptions.NotAdminException()
        else:
            raise Exceptions.UserDoesNotExistException()
            

    def setAsAdmin(self, nickName):
        exist = False

        for user in self.getUsuarios():
            if(user.getNickName() == nickName):
                exist = True
                u = user

        if exist:
            if self.getCurrentUser().getIsAdmin():
                u.setAsAdmin()
            else:
                raise Exceptions.NotAdminException()
        else:
            raise Exceptions.UserDoesNotExistException()

    def users(self):
        for user in self.getUsers():
            return user.getNickName()

    def changePassword(self, oldPassword, newPassword):
        self.getCurrentUser().changePassword(oldPassword, newPassword)
        

class User():

    def setNickName(self, nickName):
        self.nickName = nickName

    def getNickName(self):
        return self.nickName

    def getIsAdmin(self):
        return self.isAdmin

    def setIsAdmin(self, boolean):
        self.isAdmin = boolean

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password
    
    def __init__(self, nickName, password):
        self.setNickName(nickName)
        self.setPassword(password)
        self.setIsAdmin(False)

    def setAsAdmin(self):
        self.setIsAdmin(True)

    def changePassword(self, oldPassword, newPassword):
        if(self.getPassword() == oldPassword): 
            if(oldPassword != newPassword):
                self.setPassword(newPassword)
            else:
                raise Exceptions.NewPasswordEqualOldPasswordException()
        else:
            raise Exceptions.IncorrectPasswordException()