# Online Python - IDE, Editor, Compiler, Interpreter
import random

#This function picks a random door based on number of total overall doors as well as doors that are not to be considered for the newly randomly picked door
def pickNewDoor(numDoors, arrDoorsReserved):
    #print ("troubleshoot statement: pickNewDoor called with %s and %s" % (numDoors, arrDoorsReserved))
    newDoor = random.randint(1,numDoors-len(arrDoorsReserved)) #Randomly pick a number from total number of doors while not considering a list of doors to not be considered.
    #print ("troublehshoot statement: newDoor is %s" % (newDoor))
    while newDoor >= min(arrDoorsReserved): #Looping over list of doors to not be considered until randomly picked door has a smaller number than the list of doors to not be considered to eliminate collisions
        newDoor+=1 #If random door has a number equal to or larger than smallest door number, then increase the door by 1
        arrDoorsReserved.remove(min(arrDoorsReserved)) #Remove smallest door from list as it no longer collides
        if not arrDoorsReserved: #If reserved list is empty then collission no longer possible and loop no longer needed.
            break
    return(newDoor)

#Initialize variables
numDoors = int(input('Enter total number of doors to simulate: '))
numSimRums = int(input('Enter total number of runs to simulate: '))

numDoorPrize = -1
numDoorFirstPick = -1
numDoorSwapPick = -1
numDoorSecondPick = -1
numFirstPickWinTally = 0
numSwapPickWinTally = 0
numSecondPickWinTally = 0

for loopNum in range(numSimRums): #Loop as many times as number of simulations requested
 numDoorPrize = random.randint(1,numDoors) #Randomly pick door with prize
 numDoorFirstPick = random.randint(1,numDoors) #Randomly pick first choice
 
 #Tally win if first pick matches prize
 if numDoorPrize == numDoorFirstPick: 
     numFirstPickWinTally+=1
 
 numDoorToEliminate = pickNewDoor(numDoors, [numDoorPrize, numDoorFirstPick]) #Randomly pick door to eliminate using helperfunction that is not prize door or first picked door
 
 numDoorSwapPick = pickNewDoor(numDoors,[numDoorFirstPick,numDoorToEliminate]) #Figure out swap pick that is not first picked or eliminated door using helper function for swap strategy
 
 numDoorSecondPick = pickNewDoor(numDoors,[numDoorToEliminate]) #Randomly pick door that is not one of the eliminated doors for randomly pick from smaller pool strategy.

 print("Run %s : numDoorPrize is %s numDoorFirstPick is %s numDoorToEliminate is %s numDoorSwapPick is %s numDoorSecondPick is %s" % (loopNum, numDoorPrize, numDoorFirstPick, numDoorToEliminate, numDoorSwapPick, numDoorSecondPick)) #Publish simulation random choices
 
 #Tally if the two new strategies resulted in a win by comparing to the door with prize.
 if numDoorSwapPick == numDoorPrize:
     numSwapPickWinTally += 1
     
 if numDoorSecondPick == numDoorPrize:
     numSecondPickWinTally += 1

#Publish statistics on 
print ("Number of times original pick won ", numFirstPickWinTally, "For percent value of", numFirstPickWinTally/numSimRums*100)
print ("Number of times swapped pick won ", numSwapPickWinTally, "For percent value of", numSwapPickWinTally/numSimRums*100)
print ("Nmber of times random pick from smaller pool won ", numSecondPickWinTally, "For percent value of", numSecondPickWinTally/numSimRums*100)
