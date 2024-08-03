# Online Python - IDE, Editor, Compiler, Interpreter
import random
def pickNewDoor(numDoors, arrDoorsReserved):
    #print ("pickNewDoor called with %s and %s" % (numDoors, arrDoorsReserved))
    newDoor = random.randint(1,numDoors-len(arrDoorsReserved))
    #print ("newDoor is %s" % (newDoor))
    while newDoor >= min(arrDoorsReserved):
        newDoor+=1
        arrDoorsReserved.remove(min(arrDoorsReserved))
        if not arrDoorsReserved:
            break
    return(newDoor)

numDoors = int(input('Enter total number of doors to simulate: '))
numSimRums = int(input('Enter total number of runs to simulate: '))
numDoorPrize = -1
numDoorFirstPick = -1
numDoorSwapPick = -1
numDoorSecondPick = -1
numFirstPickWinTally = 0
numSwapPickWinTally = 0
numSecondPickWinTally = 0

for loopNum in range(numSimRums):
 numDoorPrize = random.randint(1,numDoors)
 numDoorFirstPick = random.randint(1,numDoors)
 if numDoorPrize == numDoorFirstPick:
     numFirstPickWinTally+=1
 
 numDoorToEliminate = pickNewDoor(numDoors, [numDoorPrize, numDoorFirstPick])
 
 numDoorSwapPick = pickNewDoor(numDoors,[numDoorFirstPick,numDoorToEliminate])
 
 numDoorSecondPick = pickNewDoor(numDoors,[numDoorToEliminate])
 print("Run %s : numDoorPrize is %s numDoorFirstPick is %s numDoorToEliminate is %s numDoorSwapPick is %s numDoorSeconPick is %s" % (loopNum, numDoorPrize, numDoorFirstPick, numDoorToEliminate, numDoorSwapPick, numDoorSecondPick))
 if numDoorSwapPick == numDoorPrize:
     numSwapPickWinTally += 1
     
 if numDoorSecondPick == numDoorPrize:
     numSecondPickWinTally += 1


print ("numFirstPickWinTally is ", numFirstPickWinTally, "For percent value of", numFirstPickWinTally/numSimRums*100)
print ("numSwapPickWinTally is ", numSwapPickWinTally, "For percent value of", numSwapPickWinTally/numSimRums*100)
print ("numSecondPickWinTally is ", numSecondPickWinTally, "For percent value of", numSecondPickWinTally/numSimRums*100)
