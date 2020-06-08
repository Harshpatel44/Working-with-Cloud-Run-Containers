import mysql.connector

class Database:
    def __init__(self):
        pass

    def configureDb(self, host, database, user, password,port):
        return mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port)
    def connectDB(self):
        self.object = self.configureDb("serverless-a2.cdvxuztseuhu.us-east-1.rds.amazonaws.com", "serverless-A2", "admin",
                                 "amazonrds",3305)

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
        results=cur.fetchall()
        self.object.commit()
        cur.close()
        self.object.close()
        return results
