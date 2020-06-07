from src.Database import Database
from src.Repository import Repo
from src.Service import Service

"""Dependency Injection"""

class Injector:
    _instance=False
    def __init__(self):
        self.Repo = Repo()
        self.Service = Service()
        self.Database = Database()
        
    def instance(self):
        # global _instance
        if (self._instance == False):
            _instance = Injector()
        return _instance

    def getRepo(self):
        return self.Repo

    def getService(self):
        return self.Service

    def getDB(self):
        return self.Database

    def setRepo(self,Repo):
        self.Repo = Repo

    def setService(self,Service):
        self.Service = Service

    def setDB(self,Database):
        self.Database = Database