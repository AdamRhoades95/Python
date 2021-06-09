import mysql.connector
import os
import Argv_Show_Table






conn = mysql.connector.connect(host="localhost", user="root", passwd="shr4l1f3")

commander = conn.cursor()
command = ""

def insert(fieldList):
    global commander, command, conn
    try:
        commander.execute(command, var)
        conn.commit()
    except:
        print("OOPS")

check = ""
i = 0
q = "true"
while q == "true":
    print("1 to quit")
    print("Enter a database: "),
    db = "USE " + str(raw_input())
    if db == "USE 1":
        inDB = "false"
        q = "false"
    else:
        commander.execute(db)
        inDB = "true"
    while inDB == "true":
        command = ""
        sender = ""
        print(sender)
        check = ""
        
        print("1 to quit")
        print("2 to exit database\nor"),
        print("3 for more options")
        print("enter SQL command: "),
        command = str(raw_input())
        for first in command:
            if first == " ":
                i += 1
            if i == 0:
                check += str(first)
        i =0
        if command == "1":
            inDB = "false"
            q = "false"
        elif command == "2":
            inDB = "false"
        elif command == "3":
            os.system("clear")
            print("insert\ndrop\ndelete\nselect\nshow\nupdate")
        elif check.lower() == "create":
            try:
                commander.execute(command)
            except:
                print("OOPS")
        elif check.lower() == "insert":
            try:
                os.system("python insert.py")
            except:
                print("ERROR")
        elif check.lower() == "select":
            try:
                Argv_Show_Table.show(command)
            except:
                print("OOPS")
        elif check.lower() == "show":
            try:
                Argv_Show_Table.show(command)
            except:
                print("OOPS")
        elif check.lower() == "delete":
            insert()
        elif check.lower() == "drop":
            try:
                commander.execute(command)
            except:
                print("OOPS")
        elif check.lower() == "update":
            os.system("python update_file.py")
        elif command =="" or command ==" ":
            print("\#n")
        elif command == "run":
            try:
                print("what is the full linux command for the file to running")
                file = raw_input()
                os.system(str(file))
            except:
                print("Sorry, that command or file was not found")
        elif command == "clear":
            os.system(command)
        else:
            print("that command cannot be completed.")
    
             
                
