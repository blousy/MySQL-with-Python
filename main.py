import mysql.connector as connector 


class DBhelper:
    def __init__(self):

        self.con = connector.connect(host = 'localhost',
                              user='root',
                              password='mysql',
                              port = '3306',
                              database='pythontest_01')
        query = 'create table if not exists user(userId int primary key, userName varchar(200), phone varchar(200))'
        cur=self.con.cursor()
        cur.execute(query)
        print("created!")



    def into_user(self, userid, usename, phone):
        query = "insert into user(userId, userName, phone) values({},'{}','{}')".format(userid,usename,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")



    def fetch_data(self):
        query = "select * from user"
        con = self.con.cursor()
        con.execute(query)
        for row in con:
            print("User ID : ", row[0])
            print("Username : ", row[1])
            print("Phone : ", row[2])
            print()
            print()



    # def fetch_with_id(self,userid):

	#     query = "select * from user where userId='{}'".format(userid)
		
    #     con = self.con.cursor()
	# 	con.execute(query)
	# 	for row in con:
	# 		print("User Id :",row[0])
	# 		print("User Name :",row[1])
	# 		print("User Phone :",row[2])


helper = DBhelper()
# # helper.into_user(22, "Namyyy",'98765656')
# helper.into_user(23, "Lynnyyyy",'98765656')
helper.fetch_data()
helper.fetch_with_id(1952)

