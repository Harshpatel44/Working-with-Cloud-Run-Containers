from Repository import Repo


class Service:
    def __init__(self):
        pass
    def getOnlineUsersService(self):
        return Repo().getOnlineUsersRepo()


    def loginService(self,userName,password):
        return Repo().loginRepo(userName,password)
