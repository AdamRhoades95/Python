# this will just write a file for the first time
# this will get path and file name
# this will get text from user
# this will continue until text = !1-


# ask user for path and file
print("type \"default\"\nor type out a path followed by the file")
file_Path = raw_input("file path: ")
if file_Path.lower() == "default":
	file_Name = raw_input("file name: ")
	file_Path = ("/root/Programming/Python/Test_Ex/Read_Write_File/Written_Files/" + file_Name)
# open file
text=""
try:
	file = open(file_Path, "w+")
	line = 1
# loop for line of text till text = !1-
	while text != "!1-":
		text = raw_input("Enter line "+str(line)+ ": ")
		if text != "!1-":
			file.write(text+"\n")
		line+=1
# close file
	file.close()
except:
        print("sorry, the path does not exist")

