#! /usr/bin/env python3
#Github address: https://github.com/tetration
#Github repository: https://github.com/tetration/Simcity3000-HD-patch
#Developer Contact: rafael@theancientscroll.com
import os
import shutil
import binascii
def Welcome():
	print("Welcome to Simcity 3000/Simcity 3000 Unlimited Resolution Fix")
	print("After installing you will be able to change your game's resolution up to 2560x1440") 
	print("Warning: Some resolutions might be unstable and thus may make the game crash.")


def Backup_and_rename_original_file():
	#copy_rename(os.curdir,"'SCU3.exe1")
	#shutil.copy2(os.curdir, "SCU3.exe1")
	#navigate_and_rename(os.curdir)
	currentDir=str(os.getcwd())
	fileTolook="/SC3U.exe"
	finalPath=currentDir+fileTolook
	print(finalPath)
	if os.path.isfile(finalPath)==True:
		src_file=os.path.join(os.curdir,"SC3U.exe")
		dst_file=os.path.join(os.curdir,"SC3U1.exe")
		if os.path.exists(dst_file)!=True:
			shutil.copy2(src_file, dst_file)
		else:
			print("Error: Couldn't create a backup it looks like a file named SC3U1.exe already exists in the current directory")
	else:
		print("Error: Couldn't find SC3U.exe (Simcity 3000 executable) in the current directory. Please, before running this script make sure to put it inside your Simcity 3000/Apps folder and then try again")
		exit()

def logHex_data_of_executable(filename):
	# Open in binary mode (so you don't read two byte line endings on Windows as one byte)
	# and use with statement (always do this to avoid leaked file descriptors, unflushed files)
	with open('SC3U.exe', 'rb') as f:
	    # Slurp the whole file and efficiently convert it to hex all at once
	    hexdata = binascii.hexlify(f.read())
	    #print(hexdata)
	    text_file = open(filename, "wb")
	    text_file.write(hexdata)
	    text_file.close()


def edit_hex():# changes the resolution options avaliable in the binary executable file of the game
	    #replaces hex string to new hex string, thus allowing bigger resolutions in the game
	    logHex_data_of_executable("original_hexdata.txt")# Logs an hex data of the file before the changes
	    oldhexstring="8b4c24048b44240853"
	    newhexstring="c20800908b44240853"
	    replace_hex_chunk(oldhexstring, newhexstring)
	    oldhexstring="8b4c24048b54240881f9"
	    newhexstring="c20800908b54240881f9"
	    replace_hex_chunk(oldhexstring, newhexstring)
	    logHex_data_of_executable("modified_hexdata.txt")# Logs an hex data of the file after the changes

def replace_hex_chunk(oldhexstring, newhexstring):
	oldbinstring=binascii.unhexlify(oldhexstring)
	newbinstring=binascii.unhexlify(newhexstring)
	f = open('SC3U.exe','rb')
	contents = f.read().replace(oldbinstring, newbinstring)
	f.close()
	f = open('SC3U.exe','wb')
	f.write(contents)
	f.close()

def main():#All the steps the program will perform while running and its functions
	Welcome()
	Backup_and_rename_original_file()
	edit_hex()
	print("Patch Complete")
	
# Initializer
main()
print("Exe updated sucessfully! ")
print("original exe was backed up with the name SC3U.exe1")
