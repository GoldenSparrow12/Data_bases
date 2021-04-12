import sqlite3

def Config():
    return sqlite3.connect('student_db.db')

def Check_table():
    lst_table = []
    db = Config()
    cur = db.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type = 'table' and name NOT LIKE 'sqlite_%'")
    record = cur.fetchall()
    for row in record:
        lst_table.append(list(row))
    return lst_table

def Create():
    db = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name] 
    lst_table=Check_table()
    if table_lst in lst_table:
        print("Table Already Created!!")
    else:
        try:       
            cur =db.cursor()
            cur.execute(f'''CREATE TABLE {table_name} (StudentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, StudentName TEXT (20), StudentMark REAL);''')
            db.commit()
            print ('Table created successfully')
        except:
            print ('Error in Operation')
            db.rollback()
    db.close()

def Insert():
    db = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name] 
    lst_table=Check_table()
    if table_lst in lst_table:
        no_row_add = int(input("Enter Number of Data to add : "))
        for i in range(no_row_add):
            print(f"\tEnter The Details for Student {i+1}")
            try:
                cur =db.cursor()
                s_name = input("Student Name:")
                s_mark = float(input("Student Mark:"))
                cur.execute(f"INSERT INTO {table_name} (StudentName,StudentMark) VALUES (?,?)",(s_name,s_mark))
                print("Insert Data Successfuly\n")
                db.commit()

            except:
                db.rollback()
                print("Error in Operation")
        db.close()
    else:
        print(f"{table_name} Table Not Found!!" )

def Update():
    db = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name] 
    lst_table=Check_table()
    if table_lst in lst_table:
   
        up_date = int(input("What you want to update 1.name or 2.mark "))

        if up_date == 1:
            try:
                cur =db.cursor()
                s_id = int(input("Student id:"))
                s_name = input("Student Name:")
                cur.execute(f"UPDATE {table_name} set StudentName='{s_name}'  WHERE StudentID ={s_id};")
                print("Update Data Successfuly")
                db.commit()
            except:
                db.rollback()
                print("Error in Operation")
            db.close()
        
        elif up_date == 2:
            try:
                cur =db.cursor()
                s_id = int(input("Student id:"))
                s_mark = input("Student mark:")
                cur.execute(f"UPDATE {table_name} set StudentMark={s_mark}  WHERE StudentID ={s_id};")
                print("Update Data Successfuly")
                db.commit()

            except:
                db.rollback()
                print("Error in Operation")
        db.close()
    else:
        print(f"{table_name} Table Not Found!!" )

def Delete():
    db = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name] 
    lst_table=Check_table()
    if table_lst in lst_table:
        s_id = int(input("Student Id:"))
        try:
            cur =db.cursor()
            cur.execute(f"DELETE from {table_name} WHERE StudentName='{s_id}'")
            db.commit()
            print("Delect Successfuly")

        except:
            db.rollback()
            print("Error in Operation")
        db.close()  
    else:
        print(f"{table_name} Table Not Found!!" )

def Opretions():
    while True:
        op_choise = int(input(''' Enter from 
            1.Insert
            2.Update
            3.Delete
            4.Exit from Opration
            Enter the Choise:'''))
            
        if op_choise ==1:
            Insert()
        elif op_choise==2:
            Update() 
        elif op_choise==3:
            Delete()
        elif op_choise == 4:
            break

def Select():
    db = Config()
    table_name =input("Enter Table Name: ")
    table_lst = [table_name] 
    lst_table=Check_table()
    if table_lst in lst_table:

        try:
            cur =db.cursor()
            cur.execute(f"SElECT * from {table_name};")
            record = cur.fetchall()
            for row in record:
                print(row)
        except:
            db.rollback()
            print("Error in Operation")
        db.close()
    else:
        print(f"{table_name} Table Not Found!!" )
    
def Drop():
    db = Config()
    table_name =input("Enter Table Name: ")
    
    try:
        cur = db.cursor()
        cur.execute(f"DROP TABLE {table_name}")
        print("Table Drop Successfuly")
        db.commit()
    except:
        db.rollback()
        print(f"{table_name} Table Not Found!!" )
    db.close()


if __name__ == '__main__':

    
    print('''-------------SQLITE---------------''')

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
