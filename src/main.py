#!/usr/bin/env python

from os import system
from random import shuffle

def createList(userNumber):
	userNumber = userNumber + 1
	numList = []
	for i in range(1,userNumber):
		numList.append(i)

	shuffle(numList)

	return numList

def sortList(numList):
	sortedList = numList.copy()
	sortedList.sort()
	length = len(numList)
	max = length - 1
	sorted = False
	holder = 0

	while sorted != True:
		swapCount = 0
		system("clear")
		print(f"Sorted:   {sortedList}")
		print(f"Unsorted: {numList}")
		
		for i in range(0, length):
			if i == max:
				if numList[i] > numList[i - 1]:
					pass
				elif numList[i] < numList[i - 1]:
					holder = numList[i]
					numList[i] = numList[i - 1]
					numList[i - 1] = holder
					swapCount = swapCount + 1
			elif numList[i] < numList[i + 1]:
				pass
			elif numList[i] > numList[i + 1]:
				holder = numList[i]
				numList[i] = numList[i + 1]
				numList[i + 1] = holder
				swapCount = swapCount + 1
			else:
				pass

		if swapCount == 0:
			sorted = True
	
	system("clear")
	print(f"Sorted:   {sortedList}")
	print(f"Unsorted: {numList}")
	print("List has been sorted!")

def main():
	system("clear")
	userNumber = input("How many numbers do you want to sort?: ")
	list = createList(int(userNumber))
	sortList(list)

if __name__ == "__main__":
	main()
