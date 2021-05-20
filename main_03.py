from os import dup2
import mysql.connector as connector

mydb = connector.connect(host='localhost',
                         port ='3306',
                         user= 'root',
                         password= 'mysql',
                         database = 'zas1'
                         )

se = mydb.cursor()
# se.execute('CREATE DATABASE zas1;')
# se.execute('use zas1')
# se.execute('CREATE TABLE USER32(Userid int Primary Key, Name varchar(20), password varchar(20), age integer)')
a = 'insert into user32(Userid, Name, password, age) VALUES(%s,%s,%s,%s)'
# b = (12,'Namash','Digimon23', 23 )
# c= (13,'Lynn','091275875VB',21)


#insert through user input 

while(True):
    d1 = int(input("Enter the id : "))
    d2 = input("Enter your name : ")
    d3 = input("Enter a password : ")
    d4 = int(input("Enter your age : "))

    d5 = (d1, d2, d3, d4)



    se.execute(a,d5)
    mydb.commit()
    print("done!")
# x = se.execute('select * from user32')


# for row in x:

#     print('User : {name}',row[1])
#     print('User : {password}',row[2])
#     print('User : {age}',row[3])
