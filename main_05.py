from os import dup2
import mysql.connector as connector

mydb = connector.connect(host='localhost',
                          port ='3306',
                          user='root',
                          password='mysql',
                          database='zas1')


con = mydb.cursor()
# con.execute('CREATE TABLE test2(Userid int Primary Key, ProductName varchar(20), price float(7,2))')

# a = "INSERT INTO test2(Userid, ProductName, price) VALUES(%s,%s,%s)"
# # con.execute(a)

# while(True):

#     d1 = int(input("Enter your ID: "))
#     d2 = input("Enter your product name : ")
#     d3 = float(input("Set your price : "))
#     d4 = (d1,d2,d3)

#     con.execute(a,d4)
#     mydb.commit()

#     z = input("Do you want to enter more products? Yes or No?")
#     if z == "No":
#         break

q = "Update test2 set price = price + 30 where price>300"
con.execute(q)
mydb.commit()