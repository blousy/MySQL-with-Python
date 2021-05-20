import mysql.connector as connector

class DBinfo:

    def __init__(self):


        con = connector.connect(host = 'localhost',
                                port = '3306',
                                user ='root',
                                password='mysql',
                                database = 'test_02')


        

        query = 'create table if not exists user2(userId int Primary key, age int(22), address varchar(200))'

        cur = con.cursor()
        cur.execute(query)
        print("created!")


c1 = DBinfo()