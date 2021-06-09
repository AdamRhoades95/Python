import os
import shutil

# two ways to move the file  "directory1" to "directory2"
try:
	os.rename('/root/Programming/Python/Test_Ex/Moved_File/move.txt','/root/move.txt')
except:
	shutil.move('/root/move.txt','/root/Programming/Python/Test_Ex/Moved_File/move.txt')
