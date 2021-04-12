import mysql.connector

def Config():
    conn = mysql.connector.connect(
        user= 'root',password='password',host='127.0.0.1',database='MYDATABASE'
    )
    return conn

def Check_table():
    lst_table = []
    conn = Config()
    cur = conn.cursor()
    cur.execute("SHOW TABLES ")
    record = cur.fetchall()
    for row in record:
        lst_table.append(list(row))
    return lst_table

def Create():
    conn = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name]
    lst_table=Check_table()
    if table_lst in lst_table:
        print("Table Already Created!!") 
    
    else:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''CREATE TABLE {table_name} (StudentID INT PRIMARY KEY AUTO_INCREMENT NOT NULL, StudentName CHAR (20), StudentMark FLOAT);''')
            conn.commit()
            print ('Table created successfully')
        except:
            print ('Error in Operation')
            conn.rollback()
    conn.close()

def Insert():
    conn = Config()   
    table_name =input("Enter Table Name: ")
    table_lst = [table_name]
    lst_table=Check_table()
    if table_lst in lst_table:
        no_row_add = int(input("Enter Number of Data to add : "))
        for i in range(no_row_add):
            print(f"\tEnter The Details for Student {i+1}")
            try:
                cur =conn.cursor()
                s_name = input("Student Name:")
                s_mark = float(input("Student Mark:"))
                cur.execute(f"INSERT INTO {table_name} (StudentName,StudentMark) VALUES (%s,%s)",(s_name,s_mark))
                print("Insert Data Successfuly\n")
                conn.commit()

            except:
                conn.rollback()
                print("Error in Operation")
        conn.close()
    else:
        print(f"{table_name} Table Not Found!!" )

def Update():
    conn = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name]
    lst_table=Check_table()
    if table_lst in lst_table:
        up_date = int(input("What you want to update 1.name or 2.mark "))

        if up_date == 1:
            try:
                cur =conn.cursor()
                s_id = int(input("Student id:"))
                s_name = input("Student Name:")
                cur.execute(f"UPDATE {table_name} set StudentName='{s_name}'  WHERE StudentID ={s_id};")
                print("Update Data Successfuly")
                conn.commit()
            except:
                conn.rollback()
                print("Error in Operation")
            conn.close()
        
        elif up_date == 2:
            try:
                cur =conn.cursor()
                s_id = int(input("Student id:"))
                s_mark = input("Student mark:")
                cur.execute(f"UPDATE {table_name} set StudentMark={s_mark}  WHERE StudentID ={s_id};")
                print("Update Data Successfuly")
                conn.commit()

            except:
                conn.rollback()
                print("Error in Operation")
        conn.close()
    else:
        print(f"{table_name} Table Not Found!!" )

def Opretions():
    while True:
        op_choise = int(input(''' Enter from 
            1.Insert
            2.Update
            3.Delete
            4.Exit from Opretions
            Enter the Choise:'''))
            
        if op_choise ==1:
            Insert()
        elif op_choise==2:
            Update() 
        elif op_choise==3:
            Delete()
        elif op_choise==4:
            break

def Delete():
    conn = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name]
    lst_table=Check_table()
    if table_lst in lst_table:
        s_id = int(input("Student Id:"))
        try:
            cur =conn.cursor()
            cur.execute(f"DELETE from {table_name} WHERE StudentId='{s_id}'")
            conn.commit()
            print("Delect Successfuly")

        except:
            conn.rollback()
            print("Error in Operation")
        conn.close()
    else:
        print(f"{table_name} Table Not Found!!" )

def Select():
    conn = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name]
    lst_table=Check_table()
    if table_lst in lst_table:
        try:
            cur =conn.cursor()
            cur.execute(f"SElECT * from {table_name};")
            record = cur.fetchall()
            for row in record:
                print(row)
        except:
            conn.rollback()
            print("Error in Operation")
        conn.close()
    else:
        print(f"{table_name} Table Not Found!!" )

def Drop():
    conn = Config()
    table_name =input("Enter Table Name: ")
    
    try:
        cur = conn.cursor()
        cur.execute(f"DROP TABLE {table_name}")
        print("Table Drop Successfuly")
        conn.commit()
    except:
        conn.rollback()
        print(f"{table_name} Table Not Found!!")
    conn.close()


if __name__ == '__main__':

    print('''-------------MYSQL---------------''')

    while True:
        try:
            choise  = int(input('''\nEnter Form
            1.Create Table
            2.Perform Opretion 
            3.Drop Table
            4.Select Table
            5.Exit
            Enter the choise : '''))

            if choise == 1:
                Create()
            elif choise == 2:
                Opretions()
            elif choise == 3:
                Drop()
            elif choise == 4:
                Select()
            elif choise==5:
                exit()
        except ValueError:
            print("Enter Only numerical value")
