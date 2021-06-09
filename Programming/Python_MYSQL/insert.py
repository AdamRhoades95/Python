import mysql.connector
import os

conn = mysql.connector.connect(host="localhost", user="root", passwd="shr4l1f3", database="Test")

commander = conn.cursor()

print("User name:"),
ID = raw_input()

print("Email address:"),
email = raw_input()

print("Age:"),
age = raw_input()

print("Language:"),
language = raw_input()

print("First name:"),
FName = raw_input()

print("Last name:"),
LName = raw_input()

command2 = ("INSERT INTO accounts(ID, email, age, language, LName, FName ) VALUES(%s, %s, %s, %s, %s, %s)")
value = (ID, email, age, language, LName, FName)
commander.execute(command2, value)
conn.commit()

os.system("python Adv_Show_Table.py")
