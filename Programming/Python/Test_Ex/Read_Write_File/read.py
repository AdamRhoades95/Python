
# find the file move.txt
try:
	movedfile = open('/root/Programming/Python/Test_Ex/Moved_File/move.txt', "r")
except:
	movedfile = open('/root/move.txt', "r")


# assign lines in file to variable "lines"
lines = movedfile.readlines()

# iteration loop to read/print lines in file
for line in lines:
	print(line)



movedfile.close()


