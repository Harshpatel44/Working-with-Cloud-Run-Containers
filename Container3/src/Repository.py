from Database import Database
from datetime import datetime

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
