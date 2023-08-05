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
	
	system("clear")
	print(numList)
	print("List has been sorted!")

def main():
	system("clear")
	userNumber = input("How many numbers do you want to sort?: ")
	list = createList(int(userNumber))
	sortList(list)

if __name__ == "__main__":
	main()
