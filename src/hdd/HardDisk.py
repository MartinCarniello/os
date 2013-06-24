'''
Created on 24/06/2013

@author: usuario
'''

class HDD:
    def __init__(self):
        self.pages = {}
        
    def getPages(self):
        return self.pages
    
    def setPages(self, pages):
        self.pages = pages
        
    def getProcessPages(self, pid):
        return self.getPages()[pid]
        
    
class processPages():
    def __init__(self):
        self.pages = []
        
    def getPages(self):
        return self.pages
    
    def setPages(self, pages):
        self.pages = pages
        
    def getPage(self, nPage):
        return self.getPages()[nPage]
    
    def setPage(self, nPage, page):
        return self.getPages()[nPage].set(page)