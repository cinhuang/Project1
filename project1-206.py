import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	
	infile = open(file, 'r')
	line = infile.readline()

	
	theList = []
	row1 = line.split(",")

	# Create the keys 
	first = row1[0]
	last = row1[1]
	email = row1[2]
	gradeClass = row1[3]
	dob = row1[4].split("\n")[0]


	line = infile.readline()

	while line:
		dictionary = {}
	
		info = line.split(",")
		firstName = info[0]
		lastName = info[1]
		emailAddress = info[2]
		grade = info[3]
		birthday = info[4].split("\n")[0]


		dictionary[first] = firstName
		dictionary[last] = lastName
		dictionary[email] = emailAddress
		dictionary[gradeClass] = grade
		dictionary[dob] = birthday

		theList.append(dictionary)
		

		line = infile.readline()

	infile.close()

	#return myList
	return theList


def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	
	sortedList = []
	dictionary = {}
	first = ""
	last = ""
	firstLast = ""

	# Creates a list of values based on the key
	for i in data:
		sortedList.append(i.get(col))


	# creates a list of the sorted values 
	for i in sortedList:
		sortedList.sort()

	value = sortedList[0]
	firstLast = first + last

	
	for i in data:
		if value in i.values():
			dictionary = i

		first = dictionary.get("First")
		last = dictionary.get("Last")

	firstLast = first + " " + last
		
	return firstLast


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	sortedList = []
	for i in data:
		sortedList.append(i.get('Class'))

	freshmanCount = 0
	sophomoreCount = 0
	juniorCount = 0
	seniorCount = 0

	# Count how many students in each class 
	for i in sortedList:
		if i == 'Freshman':
			freshmanCount += 1
		elif i == 'Sophomore':
			sophomoreCount += 1
		elif i == 'Junior':
			juniorCount += 1
		else:
			seniorCount += 1
 
	a = ["Freshman", "Sophomore", "Junior", "Senior"]
	b = [freshmanCount, sophomoreCount, juniorCount, seniorCount]
	c = list(zip(a, b))
	c.sort(key=lambda x: x[1], reverse = True)
	
	return c

def findMonth(a):
# Find the most common birth month from this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	
	monthList = {}

	for i in a:
		#extracts all the dobs from the list
		dobList = i["DOB"]
		# extracts all the months from the dobs 
		month = dobList[:2].rstrip('/')

		if month in monthList:
			monthList[month]  += 1 

		else:
			monthList[month] = 1

		mostCommonList = sorted(monthList.items(), key = lambda x: x[1], reverse = True)
		mostCommonBirthMonth = int(mostCommonList[0][0])

	return mostCommonBirthMonth

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()