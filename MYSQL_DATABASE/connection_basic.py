import mysql.connector as con

# fist step
# mydb=con.connect(host="localhost",user="root",passwd="159159")
# print("success..")

# # create cursor
# mycursor=mydb.cursor()

# mycursor.execute("show databases")

# for db in mycursor:
#     print(db)
# to connect with specific database
mydb=con.connect(host="localhost",user="root",passwd="159159",database="raghu")
print("Connection SUccess..")
cursor=mydb.cursor()
#cursor.execute("insert into students values ('ABHIJIT','NIT-H')")
name=input("ENter name:")
college=input("Enter college name:")

sql="insert into students(name,college)\
    values('{}','{}')".format(name,college)

cursor.execute(sql)
mydb.commit()
cursor.execute("select * from students")

for record in cursor:
    print(record)

