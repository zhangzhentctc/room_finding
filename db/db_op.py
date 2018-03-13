import sqlite3
import time
import os
import shutil


RET_OK = 0
RET_ERR = -1
KAIYUAN = 'Kaiyuan'

class db_op:
    def __init__(self):
        self.db =KAIYUAN

    def db_connect(self):
        try:
            self.conn = sqlite3.connect(self.db)
        except:
            return RET_ERR
        return RET_OK

    def db_disconnect(self):
        try:
            self.conn.close()
        except:
            return RET_ERR
        return RET_OK

    def db_open_cur(self):
        try:
            self.cursor = self.conn.cursor()
        except:
            return RET_ERR

        return RET_OK

    def db_close_cur(self):
        try:
            self.cursor.close()
        except:
            return RET_ERR

        return RET_OK

    def db_exec_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except:
            return RET_ERR
        return RET_OK

    def db_commit(self):
        try:
            self.conn.commit()
        except:
            return RET_ERR
        return RET_OK

    def db_fetall(self):
        try:
            values = self.cursor.fetchall()
        except:
            return RET_ERR, []
        return RET_OK, values
