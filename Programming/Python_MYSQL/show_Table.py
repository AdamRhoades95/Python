import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="shr4l1f3", database="Test")

commander = conn.cursor()
command1 = ("SELECT * FROM accounts")

commander.execute(command1)
titles = commander.description
records = commander.fetchall()
#print (commander.description)
i = 0
for record in titles:
    i = 0
    for field in record:
        if i == 0:
            print (str(field)),
        i+=1
    

for record in records:
    print("\n---------------------")
    for field in record:
        print (str(field)),
print("\n---------------------\n")
    
