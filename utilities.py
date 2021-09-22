import mysql.connector as mysql
import datetime


conn = mysql.connect(host="localhost", user="root", password="", db="task2")
#get Function
def getMovie(genre):
    cur = conn.cursor(dictionary=True)
    qry = "SELECT * FROM `movies` WHERE `genre`= '{}'".format(genre)
    cur.execute(qry)
    user = cur.fetchone()
    return user