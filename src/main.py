#!/usr/bin/env python

from os import system
from random import shuffle
from time import sleep

def createList(userNumber):
	userNumber = userNumber + 1
	numList = []
	for i in range(1,userNumber):
		numList.append(i)

	shuffle(numList)

	return numList

def sortList(numList, slowDown): # Thanks dad!
	max = len(numList)
	holder = 0
	swapCount = 1

	while swapCount != 0:
		max = max - 1
		swapCount = 0
		system("clear")
		print(numList)
		
		for i in range(0, max):
			if numList[i] > numList[i + 1]:
				holder = numList[i]
				numList[i] = numList[i + 1]
				numList[i + 1] = holder
				swapCount = swapCount + 1
				if slowDown == 1:
					system("clear")
					print(numList)
					sleep(1)
	
	system("clear")
	print(numList)
	print("List has been sorted!")

def main():
	system("clear")
	slowDown = 0
	userNumber = input("How many numbers do you want to sort?: ")
	slowChoice = input("Do you want the script to run slowly? Y/n: ")
	if slowChoice == "Y" or slowChoice == "y":
		slowDown = 1

	list = createList(int(userNumber))
	sortList(list, slowDown)

if __name__ == "__main__":
	main()
