from src.Database import Database
from src.passwordEncrypt import Passwd

class Repo:
    def __init__(self):
        pass

    def registerRepo(self, registerUserName, registerEmail, registerPassword, registerTopic):
        encrypted_password=Passwd().encrypt(registerPassword)
        try:
            db = Database()
            db.connectDB()
            db.executeQuery('insert into userInfo values("{0}","{1}","{2}","{3}")'.format(registerUserName, registerEmail,
                                                                                          encrypted_password, registerTopic))
            return True
        except Exception as e:
            print(e)
            return False

    def getOnlineUsersRepo(self):
        list=[]
        try:
            db = Database()
            db.connectDB()
            results = db.executeQueryWithResults('select * from userState where state="online"')
            for i in results:
                list.append(i[0])
            return list
        except Exception as e:
            print(e)
            return list


