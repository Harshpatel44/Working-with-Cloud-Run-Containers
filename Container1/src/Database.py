import pymysql
import os

class Database:
    def __init__(self):
        pass

    def configureDb(self, host, database, user, password,port):

        if os.environ.get('GAE_ENV') == 'standard':
            unix_socket = '/cloudsql/{}'.format('axial-mercury-279803:us-east4:serverless-a2')
            return pymysql.connect(user=user, password=password,
                                  unix_socket=unix_socket, db=database)
        else:

            return pymysql.connect(user=user, password=password,
                                  host='127.0.0.1', db=database)

    def connectDB(self):
        self.object = self.configureDb("35.236.239.82", "serverless-a2", "root",
                                 "googlecloud",3306)
        print("conneceted")
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
