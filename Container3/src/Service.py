from Repository import Repo


class Service:
    def __init__(self):
        pass
    def getOnlineUsersService(self):
        return Repo().getOnlineUsersRepo()

    def logoutService(self,username):
        Repo().logoutServiceRepo(username)