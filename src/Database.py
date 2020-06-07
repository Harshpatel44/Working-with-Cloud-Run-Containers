import mysql.connector

class Database:
    def __init__(self):
        print('db init')

    def configureDb(self, host, database, user, password):
        return mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password)
    def connectDB(self):
        self.object = self.connectRDS("database-1.ceofxztsta8i.us-east-1.rds.amazonaws.com", "sampleDB", "admin",
                                 "amazonrds")

    def executeQuery(self, query):
        cur = self.object.cursor()
        # query = 'INSERT INTO users (userID,Password) VALUES ({0},"{1}")'.format(str(user_id),
        #                                                                         encrypted_password)
        cur.execute(query)
        self.object.commit()
        cur.close()
        self.object.close()

    def executeQueryWithResults(self,query):
        cur = self.object.cursor()
        cur.execute(query)
        results=cur.fetchone()
        self.object.commit()
        cur.close()
        self.object.close()
        return results
