import mysql.connector
import os
conn = mysql.connector.connect(host="localhost", user="root", passwd="shr4l1f3", database="Test")

commander = conn.cursor()
#command1 = ("SELECT * FROM accounts")

command2 = ("UPDATE accounts SET email = 'rhoades_c_adam@yahoo.com' WHERE ID = 'rhoades_adam'")
#command2 = ("delete from accounts where age='0'")
commander.execute(command2)
conn.commit()

os.system("python Adv_Show_Table.py")

###commander.execute(command1)
#records = commander.fetchall()
#
#
#for record in records:
#    print("\n---------------------")
#    for field in record:
#        print (str(field)),
#print("\n---------------------\n")

#
