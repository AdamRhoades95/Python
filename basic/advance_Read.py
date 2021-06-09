textFile = "blank"
trigger = "t"
while trigger == "t":
	check = raw_input("do you have a file that exists (y or n): ")
        if check.lower() == 'y' or check.lower() == 'yes':
                print("/root/Programming/Python/Test_Ex/Moved_File/move.txt")
                textFile = raw_input("enter the path then file name: ")
                try:
                        readFile = open(textFile, "r")
                        trigger = "f"
                except:
                        print("Sorry, could not find that file ")

        elif check.lower() == 'n' or check.lower() == 'no':
                try:
			readFile = open('/root/Programming/Python/Test_Ex/Moved_File/move.txt', "r")
                except:
                        readFile = open('/root/move.txt', "r")

                trigger = "f"
                        
        else:
                print("pleasee enter a y or n!")

count = 1
lines = readFile.readlines()
for line in lines:
        print(str(count)+": "+line)
        count+=1




        # find the file move.txt

 #               movedfile = open('/root/Programming/Python/Test_Ex/Moved_File/move.txt', "a")
#                movedfile = open('/root/move.txt', "a")
       


