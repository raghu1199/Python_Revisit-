import mysql.connector as connection

try:
    con=connection.connect(host="raghu",user="root",passwd="159159",database="raghu1")
    cursor=con.cursor()
    print("succee connected..")
except Exception as e:
    print("DATABASE Connection error..",e)

def insert():
    name=input("ENter name (MUST):")
    phone=input("enter phone (MUST):")
    email=input("enter email:")
    marks=int(input("enter marks"))
    sql="insert into students_data(name,phone,email,marks) values(%s,%s,%s,%s)"
    val=(name,phone,email,marks)
    try:
        cursor.execute(sql,val)
        con.commit()
    except Exception as e:
        print("Error Occured During Insertion..")
        
    menu()

def read():
    sql="select * from students_data"
    try:
        cursor.execute(sql)
        records=cursor.fetchall()
        for record in records:
            print(record)
    except Exception as e:
        print("Error during Fetchall")
    menu()

def delete():
    
    idd=input("Enter record id")
    sql="delete from students_data where id=%s"
    val=(idd,)
    try:
        cursor.execute(sql,val)
        con.commit()
        print("succesfully deleted..")
    except Exception as e:
        print("Error during deletion..",e)
    menu()
    
def update():
    idd=input("ENter your row id where update need:")
    sql="select * from students_data where id=%s"
    val=(idd,)
    try:
        cursor.execute(sql,val)
        data=cursor.fetchone()
        print(data)
    except Exception as e:
        print("Error occured during fetching data..")
    print("1.Update name\t2. update phone\n")
    ch=int(input("ENter your choice:"))
    if ch==1:
        try:
            name=input("Enter new name:")
            sql="update students_data set name=%s where id=%s"
            val=(name,idd)
            cursor.execute(sql,val)
            con.commit()
            print("Update succes")
        except Exception as e:
            print("Error during Update:",e)
    elif ch==2:
        try:
            phone=input("Enter new phone no:")
            sql="update students_data set phone=%s where id=%s"
            val=(phone,sql)
            cursor.execute(sql,val)
            con.commit()
            print("Update success")
        except Exception as e:
            print("Error occured during update ",e)
    else:
        print("Wrong choice")
        menu()

    menu()


ch=input("\nAre you need to perform more database ops?(yes/no):")

def menu():
    global ch
    while ch=='y':
        ch=input("\nAre you need to perform more database ops?(yes/no):")
        if ch!='y':
            break
        else:
            choice=int(input("Enter choice:1)Insert\t2)Read\t3)Delete\t4)Update\n"))
            if choice==1:
                insert()
            elif choice==2:
                read()
            elif choice==3:
                delete()
            elif choice==4:
                update()
            else:
                print("\nWrong choice.. please select valid choice")
                menu()
        

    cursor.close()
    con.close()
    print("Database Connection is closed")


menu()
