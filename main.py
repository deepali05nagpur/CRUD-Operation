import mysql.connector as connector


class DBhelper:
    def __init__(self) :
        #  To create table
        
        self.my_db=connector.connect(host='localhost',
                        username='root',
                        password='root',
                        database='pythontest')
        query='create table if not exists user(userID int primary key,userName varchar(200),phone varchar(100))'
        cur=self.my_db.cursor()
        cur.execute(query)
        print("created ")
        #  Insert Data into Table
    def insert_user(self,userID,userName,phone):
        query="insert into user(userID,userName,phone)values({},'{}','{}')".format(userID,userName,phone)
        print(query)
        cur=self.my_db.cursor()
        cur.execute(query)
        self.my_db.commit()
        print("user saved to db")
#  Read data from table
    def fetch_all(self):
        query="select * from user"
        cur=self.my_db.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
#  Delete data from table
    
    def delete(self,userID):
        query='delete from user where userID={}'.format(userID)
        cur=self.my_db.cursor()
        cur.execute(query)
        self.my_db.commit( )
        print("deleted")
#  Update data from table
    def update_user(self,userID,newName,newPhone):
        query="update user set userName='{}',phone='{}'where userID={}".format(newName,newPhone,userID)
        print(query)
        cur=self.my_db.cursor()
        cur.execute(query)
        self.my_db.commit()
        print("updated")


helper=DBhelper()
# helper.insert_user(59,'ewa','12546561')
# helper.insert_user(569,'Sneha','15546561')
helper.insert_user(944,'Rohan','12586561')
helper.insert_user(256,'Piu','12545561')
helper.insert_user(14140,'Sara','12546361')
helper.insert_user(1118,'Sonu','12546521')
helper.insert_user(117,'Monu','32546561')
helper.insert_user(1114,'Rava','12546861')

# helper.delete(19)
helper.update_user(0,"madhuri","42285")
helper.fetch_all()
helper.delete(944)