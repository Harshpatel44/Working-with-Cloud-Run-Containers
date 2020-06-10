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
        self.object = self.configureDb("35.236.239.82", "serverless-a2", "root",
                                 "googlecloud",3306)

    def executeQuery(self, query):
        cur = self.object.cursor()
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