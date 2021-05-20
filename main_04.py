import mysql.connector as connector

mydb = connector.connect(host='localhost',
                          port ='3306',
                          user='root',
                          password='mysql',
                          database='zas1')


con = mydb.cursor()
con.execute("select * from user32")
res = con.fetchall()

for i in res:
    print(i)