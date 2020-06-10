from Database import Database
from datetime import datetime
from passwordEncrypt import Passwd
class Repo:
    def __init__(self):
        pass

    def activateState(self,username,state):
        try:
            db = Database()
            db.connectDB()
            db.executeQuery('delete from userState where userName="{0}"'.format(username))
            db = Database()
            db.connectDB()
            db.executeQuery('insert into userState values("{0}","{1}","{2}")'.format(username, state,
                                                                                     datetime.now().strftime(
                                                                                         '%Y-%m-%d %H:%M:%S')))
            return True
        except Exception as e:
            print(e)
            return False

    def loginRepo(self, userName, password):
        flag=False
        try:
            db = Database()
            db.connectDB()
            results=db.executeQueryWithResults('select * from userInfo')
            for i in results:
                if(i[0]==userName and Passwd().decrypt(i[2])==password):
                    flag=True
            if(flag==True):
                if(self.activateState(userName,'online')):
                    return "User logged in"
                else:
                    return "User already logged in"
            return "Invalid credentials"
        except Exception as e:
            print(e)
            return "User doesn't exist"

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

    def logoutServiceRepo(self, username):
        try:
            self.activateState(username,'offline')
            return True
        except Exception as e:
            return False
