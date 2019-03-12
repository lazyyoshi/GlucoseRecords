import sqlite3
import sys
import datetime



class DBCont:
    def __init__(self, dbname):
        self.sql = 'INSERT INTO BSRecords(BS,DateTime,Type) VALUES(?,?,?);'
        self.dbname = dbname
        try:
            self.conn = sqlite3.connect(dbname)
            self.c = self.conn.cursor()
        except sqlite3.OperationalError as e:
            print(e)

    def addGlucose(self, glucose, tmg):
        self.insrtData = []
        self.insrtData.append(glucose)
        self.insrtData.append(datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        self.insrtData.append(tmg)
        try:
            self.c.execute(self.sql, self.insrtData)
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print(e)
            print(sql, insrtData)

    def __del__(self):
        self.c.close()
        self.conn.close()

