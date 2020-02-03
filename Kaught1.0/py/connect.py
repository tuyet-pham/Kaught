import mysql.connector as sql
import sys, os
from mysql.connector import errorcode
from datetime import date


def connectUser()
    try:
        # Get info from a file.
        self.conx = sql.connect(user='', password='', host='localhost', database='Kaught')
        self.cur = self.conx.cursor()

        print("Setup Done.") 
    except sql.Error as er:
        if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with username or password")
        elif er.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exit")
        else:
            print(er)
        