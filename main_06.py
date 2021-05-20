import mysql.connector as connector

mydb = connector.connect(host='localhost',
                          port ='3306',
                          user='root',
                          password='mysql',
                          database='zas1')


con = mydb.cursor()

x1 = input("Enter row name you want to delete : ")
x2 = input("Enter the particular item you want to delete : ")

s= f"DELETE FROM test2 WHERE {x1} = '{x2}'"
con.execute(s)
mydb.commit()
