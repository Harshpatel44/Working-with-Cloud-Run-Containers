from src.Repository import Repo


class Service:
    def __init__(self):
        pass
    def getOnlineUsersService(self):
        return Repo().getOnlineUsersRepo()


    def loginService(self,userName,password):
        return Repo().loginRepo(userName,password)


    def registerService(self,registerUserName,registerEmail,registerPassword,registerTopic):
        if(Repo().registerRepo(registerUserName,registerEmail,registerPassword,registerTopic)):
            return True


    def logoutService(self,username):
        Repo().logoutServiceRepo(username)