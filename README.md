


# Simcity3000 HD Resolutions Patch
Python 3 and 2.7 script that patches the game to run in HD resolutions such as 1920x1080 and  4k

#Project Webpage

https://tetration.github.io/Simcity3000_Modding_Revival/scu3HD_patch.html

Developer: Tetration
	Github address: https://github.com/tetration
	
	Github repository: https://github.com/tetration/Simcity3000-HD-patch
	
	Developer Contact: rafael@theancientscroll.com

Simcity 3000 Unlimited HD patch for Windows version:

By using this python script to patch your exe file you will be able to run the game up to 4k resolutions. 
However some resolutions are highly unstable and might crash your game. For example any resolution with a vertical or horizontal component that is not divisible by 8, such as 1366x768 or 1600x900 will crash your game.

Python 3 script tested under Windows 10 64 bit using Simcity 3000 Unlimited GOG Edition for our testing purposes
Python 2.7 script tested under Windows 10 64 bit using Simcity 3000 Unlimited GOG Edition for our testing purposes



Instructions to patch the game:

 1: Make sure python 2.7 is installed in your current Windows system
 
	1.1: You can download Python to your current OS at: https://www.python.org/downloads/
	
 2: Download my script
 
 3:Place this python script in the same folder in which SC3U.exe can be located at.
 
	  3.1Example of possible location --> C:\GOG Games\SimCity 3000 Unlimited\Apps

4: Run the script(SCU3_HD_patch) by left-clicking twice on it

5: Enjoy running the game in HD resolutions or 4K!



FAQ:

 	Why there are two text files called original_hexdata.txt and modified_hexdata.txt in my Simcity 3000 game folder?
 	Before and after patching SC3U.exe executable my python script will save a log of how the data stored in the executable was before modifying it and how it is 	now. You are free to delete it if you want.

 	My game is crashing when I´m activating resolution 1600x900 or X. Why is that? Did your patch broke my game?

 	As stated above resolutions that are not divisible by 8 are likely to make the game unstable thus crashing it. And  No my patch didnt broke your game. You can 	   pick any resolution to play the game as long as both the vertical and horizontal components are a number divisible by 8


 	I cant play my linux version in HD or 4k are you going to make a patch for the Linux version?
 	Its possible to run the game in Full HD through the sc3u.dynamic executable. With it you can play the game in resolutions such as 1080P(1920x1080) or even 	higher 4K. However the sc3u.dynamic is known for being unstable or not run at all in some Debian based distros dont run it well. I´ve just recently made a patch 	   for the Windows version to run in Full HD. When I have some more free time again I will try to dig through the files of the linux version to study them more. And  	     then I will try to make a patch for the standard linux executable of the game to run in Full HD.

 	In the meantime I recommend you to try to use the sc3u.dynamic to try to run it in 1080P or higher resolutions or just wait until I make a patch.

 	Edit: You can find the sc3u.dynamic in the folders of the game which can probably be found in usr/local/games/Simcity3000/sc3u.dynamic


Observations:
	-The Script will make a backup file of the original executable(SC3U1.exe) of the game before making any changes in it
