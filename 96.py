#!/usr/bin/python2.7

import re
import itertools

baseCounter = 0
puzzleNumber = 1

with open('shortSudoku.txt') as my_file:
	full_list = my_file.readlines()
	
def needs(inPuzzle):
	myNeedList = []
	for i in xrange(9):
		checkNum = int(i + 1)
		if checkNum not in inPuzzle:
			myNeedList.append(checkNum)
	return myNeedList
	
def column(inPuzzle, i):
	return [row[i] for row in inPuzzle]	

def columnBuilder(inPuzzle):
	pColumns = []
	for i in xrange(9):
		pColumn = column(inPuzzle,i)
		pColumns.append(pColumn)
	return pColumns

def lineBuilder(inPuzzle):
	pLines = []
	for i in xrange(9):
		pLine= inPuzzle[i][0] + inPuzzle[i][1] + inPuzzle[i][2]
		pLines.append(pLine)
	return pLines
			#for i in xrange(9):
				#pColumn = []
			#for j in xrange(9):
				# pColumn.append(inPuzzle[j][i])
			# pColumns.append(pColumn)
	# print("Lines:")
	# print(pLines)
	# print("Columns")
	# print(pColumns)

def allBlockPossibilities(inPuzzle, inNeeds):
    possList = list(itertools.permutations(inNeeds))
    return possList
    
    
    
	
for line in full_list:
	line = line.rstrip()
	if (re.match(r"Grid", line)):
		print(line)
		puzzleLines = 0
		thisBase = baseCounter + 1
		puzzle = []
		while puzzleLines < 9:
			lineNumber = thisBase + puzzleLines;
			thisCharString = full_list[lineNumber]
			thisCharString = thisCharString.rstrip()
			p = list(thisCharString)
			box1 = [p[0],p[1],p[2]]
			box1 = map(int, box1)
			box2 = [p[3],p[4],p[5]]
			box2 = map(int, box2)
			box3 = [p[6],p[7],p[8]]
			box3 = map(int, box3)
			puzzle.append([])
			puzzle[puzzleLines].append(box1)
			puzzle[puzzleLines].append(box2)
			puzzle[puzzleLines].append(box3)
			# puzzle[puzzleLines].append(box1,box2,box3)
			puzzleLines += 1
		#for i in xrange(9):
		#	print(puzzle[i])
		print("Puzzle: ")
		print(puzzle)
		lineBuilder(puzzle)
		print("Lines: ")
		myLines = lineBuilder(puzzle)
		for line in myLines:
			print(line)
		print("Columns: ")
		myColumns = columnBuilder(myLines)
		for line in myColumns:
			print(line)
		block1 = puzzle[0][0] + puzzle[1][0] + puzzle[2][0]
		print("block1")
		print(block1)
		block1needs = needs(block1)
		print("block1needs")
		print(block1needs)
		block2 = puzzle[0][1] + puzzle[1][1] + puzzle[2][1]
		print("block2")
		print(block2)
		block2needs = needs(block2)
		print("block2needs")
		print(block2needs)
		block3 = puzzle[0][2] + puzzle[1][2] + puzzle[2][2]
		print("block3")
		print(block3)
		block3needs = needs(block3)
		print("block3eeds")
		print(block3needs)
		block4 = puzzle[3][0] + puzzle[4][0] + puzzle[5][0]
		print("block4")
		print(block4)
		block4needs = needs(block4)
		print("block4needs")
		print(block4needs)
		block5 = puzzle[3][1] + puzzle[4][1] + puzzle[5][1]
		print("block5")
		print(block5)
		block5needs = needs(block5)
		print("block5needs")
		print(block5needs)
		block6 = puzzle[3][2] + puzzle[4][2] + puzzle[5][2]
		print("block6")
		print(block6)
		block6needs = needs(block6)
		print("block6needs")
		print(block6needs)
		block7 = puzzle[6][0] + puzzle[7][0] + puzzle[8][0]
		print("block7")
		print(block7)
		block7needs = needs(block7)
		print("block7needs")
		print(block7needs)
		block8 = puzzle[6][1] + puzzle[7][1] + puzzle[8][1]
		print("block8")
		print(block8)
		block8needs = needs(block8)
		print("block8needs")
		print(block8needs)
		block9 = puzzle[6][2] + puzzle[7][2] + puzzle[8][2]
		print("block9")
		print(block9)
		block9needs = needs(block9)
		print("block9needs")
		print(block9needs)
		
#		blockPoss = allBlockPossibilities(block9, block9needs)
#		print(blockPoss)
	baseCounter += 1




#def process
#def process
		
	
