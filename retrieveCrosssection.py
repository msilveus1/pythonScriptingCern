import os
from os import path
#This function is meant to retrieve the name of the user
# and to retrieve the file path they desire for saving the file.  
class fileNamePathObject()
	#Overloads the constructor using polymorphism and allows
	#allows programer to not request input from user
	def __init__(self,fileName,filePath):
		# 
		self.fileName = fileName
		self.filePath = filePath
		#TODO: Add functionality to create a .txt file

	#initializes the object by asking for user input
	def __init__(self):
		exists = false 
		#makes sure a valid file path found moving on
		self.fileName = raw_input("Please enter desired name for the file: ")
		while not exists
			self.filePath = raw_input("Please enter the full desired path: ")
			exists = path.exists(filePath)
			if not exists:
				print("Your file path does not exist.  Please try entering your file path again.")
	# Allows programmer to reset the file path if desired
	def resetFilePath(self, filePath=""):
		self.fileName = fileName
	def resetFileName(self, fileName="");
		self.filePath = filePath
	#sets up some gettor methods for the user to access
	def getFilename(self):
		return self.fileName
	def getFilePath(self): 
		return self.filePath
	# might have a validity check that I add here for path name 
def runBashScript():
	exists = false 
	#makes sure a valid file path found moving on
	while not exists
	# This gets the name and file path from user of the bash script to run the monte-carlo simulation
		bashScriptName = raw_input("Please enter Bash Script Name: ")
		bashScriptPath = raw_input("Please enter the path to the Script: ")
		# now we combine the filepath and the file name and run the name
		#Check that it exists first
		exists = os.path.isfile(bashScriptPath+bashScriptName)
		if not exists:
			# Allows user to know that an error happened
			print("The bash script file name/file path you entered either was errant or does not exist please try again.")
	#Now we run the script if it is valid input.
	command = "bash " + bashScriptPath + bashScriptName
	#lets user know that the command is running.
	print(command)
	# runs the actual command
	os.system(command)
	print("The script has been run please check for errors")
	# This ends the need for this def.  
def main():
	#calls the Bash Script necessary for running the Monte carlo simulation
	runBashScript()
	#Then asks the user where he wants the file path output to be for the .txt file for 
	#with the values.
	fileNamePathObject()



