# python code
# mix with mysql (sql) code
# Adam Rhoades
import mysql.connector
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
records = commander.fetchall()

# asigns the titles of fields to variable just like records
titles = commander.description
counter = 0
size=[]
i = 0

# this is to get the number of field
# to initialize the "size" array for command line gui
for title in titles:
    size.append(0)
# ---------------------------------------------------

# check if title is > char size (len())
# set size array accordingly
for title in titles:
    for fieldN in title:
        counter += 1
        if counter <=1:
            if len(str(fieldN))> size[i]:
                size[i]= (len(str(fieldN)))
            i+=1
    counter = 0
# ---------------------------------------------------

# check if the field's data is larger
# set size array accordingly
for record in records:
    i = 0
    for field in record:
        if len(str(field))> size[i]:
            size[i]= (len(str(field)))
        i+=1
# ---------------------------------------------------

# calculate field title border
top = "+"
TTop = 0
inc = 1
for item in size:
    TTop += item+1
    while (len(top)< TTop+inc):
        top += "="
    top += "+"
    inc += 1 
print (top)

# =======================================================

# =======================================================

lineBreaker = "+"
total = 0
# print the titles for each field
i = 0
# iterate
for title in titles:
    for fieldN in title:
        counter += 1
        # take only the name of the field
        if counter <=1:
            # add blank space to field titles to organize
            strField = ("|"+ str(fieldN.upper()))
            while len(strField)<(size[i]+1):
                strField += " "

            # set record line space for organize
            total += len(strField)+1
            while len(lineBreaker) <total:
                lineBreaker += "-"
            lineBreaker += "+"
            i+=1
            print(strField),
    counter = 0
print("|")# end of field titles
print(top)# add bottom border for field titles

# print field's data
i = 0
for record in records:
    i = 0
    # data for one record
    for field in record:
        # add field with blank space to organize
        strField = ("|"+str(field))
        while len(strField)<(size[i]+1):
            strField += " "
        print(strField),# print finished field cell
        i+=1
    print("|")# finish record line
    print(lineBreaker)# add line with + and -- to seperate records


# this code could be set to be a single class if provide acommand variable
# and database info








