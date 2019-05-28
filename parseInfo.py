import xlwt 
from xlwt import Workbook 
import codecs
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
#we start by opening the file so that we can read it
f=codecs.open("homemsilveusDocumentsCernscripts (1)", 'r')
#reads the first line

#establishes a boolean for an end condition for the reading
# of the file for the fir
line = f.readline()

#before starting the first line defenition of a dictionary 
#is useful
statusCodeDict = {-1: 'Final State', 1: 'Initial State', 2: 'Intermediate State'}
#Starting the first while loop to find the start of the event


while True:
	
	if line.__contains__('<event>'):
		break
	else: 
		line = f.readline()
end = True
count=1 # establish a count to keep track of what line in the event we are at

while end:

	#we get the next line of code because we have found an actaul event
	line = f.readline()

	#checks if the last line of the event has been reached
	
	if line.__contains__('</event>'):
		break
	# the first line is different from the rest.
	if count==1:

		#Add the labels for the first row
		sheet1.write(0,0,"number of particles")
		sheet1.write(0,1,"global event info")
		sheet1.write(0,2,"global event info")
		sheet1.write(0,3,"factorization scale")
		sheet1.write(0,4,"alpha")
		sheet1.write(0,5,"alphas")
		#now we must get all the info
		splitline=line.split()
		#splits the line by white space
		
		for i in range(len(splitline)):
			#iterates through a for loop 
			#writes each entry to excell spread sheet
			sheet1.write(1,i,splitline[i])	
	elif(count==2):

		#sets up the labels for the rest of the event
		sheet1.write(3,0,"particle")
		sheet1.write(3,1,"status code")
		sheet1.write(3,2,"parent 1 row number")
		sheet1.write(3,3,"parent 2 row number")
		sheet1.write(3,4,"color flow 1")
		sheet1.write(3,5,"color flow 2")
		sheet1.write(3,6,"E/c")
		sheet1.write(3,7,"px")
		sheet1.write(3,8,"py")
		sheet1.write(3,9,"pz")
		sheet1.write(3,10,"invariant mass")
		sheet1.write(3,11,"mass")
		sheet1.write(3,12,"spin")
		#now to collect all the data from the line we use
		#a for loop to place all of it.  Fortanetly it is 
		#all split by white space
		splitline=line.split()
		for i in range(len(splitline)):
			if i != 1:
				sheet1.write(count+2,i,splitline[i])
				#Writing of the line to the excel sheet
			else:
				print(splitline[i])
				sheet1.write(count+2,i,statusCodeDict[int(splitline[i],10)])
				# getting the status code to write vs the number.   

	else:
		splitline=line.split()
		for i in range(len(splitline)):
			# taking advantage of the dictionary created earlier
			if i != 1:
				sheet1.write(count+2,i,splitline[i])
				#Writing of the line to the excel sheet
			else:
				print(splitline[i])
				sheet1.write(count+2,i,statusCodeDict[int(splitline[i],10)])
				# getting the status code to write vs the number.   
	count+=1

	#increment the count by one after iterating through once
wb.save("event.xls")


