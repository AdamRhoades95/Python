
#ERROR this code is not opperational

# need to pass unknown array size to
# query to insert the data into the position using unknown field title







# python code
# mix with mysql (sql) code
# Adam Rhoades
import mysql.connector
import os
# establish mysql connection to table
conn = mysql.connector.connect(host="localhost", user="root", passwd="shr4l1f3", database="Test")

# create pointer
commander = conn.cursor()

# sql command
command1 = ("SELECT * FROM accounts")
# command1 = ("SELECT age as 'you old',email FROM accounts")
# tells what sql command to do
commander.execute(command1)

# THE ABOVE COMMANDER CAN BE GIVEN A DIFFERENT COMMAND TO CHANGE THE QUERIED DATA
# CHANGE TO COMMAND1 TO QUERY TABLES SHOULD NOT CRASH ANY THING
# IT STILL KEEP THE FORMATTING


# asigns data from above command to variable

# asigns the titles of fields to variable just like records
titles = commander.description
fieldName=[]
fieldValues = []
i = 0
for title in titles:
    for field in title:
        if i == 0:
            fieldName.append(field)
            fieldValues.append("")
        i += 1
    i = 0
#======================
i = 0
for name in fieldName:
    #for name in field:
    print("enter the "+ str(name)+ ":"),
    fieldValues[i] = str(raw_input())
    i += 1


#print(fieldValues)
i = 0
command2 = ("INSERT INTO accounts(")
for name in fieldName:
    command2 +=(str(name))
    if i < (len(fieldName) -1):
        command2 += ", "
    i+=1
command2 += ") VALUES("

i = 0


print(command2)
values = ""
i = 0
for name in fieldValues:
    command2 += ("\'" + str(name)+"\'")
    if i < (len(fieldValues) -1):
        command2 += ", "
    i+=1
command2 += ")"
print(command2)
commander.execute(command2)
conn.commit()
os.system("python Adv_Show_Table.py")



