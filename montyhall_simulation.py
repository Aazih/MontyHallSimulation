# Online Python - IDE, Editor, Compiler, Interpreter
import random

#This function picks a random door based on number of total overall doors as well as doors that are not to be considered for the newly randomly picked door
def pickNewDoor(numDoors, listDoorsReserved):
    #print ("troubleshoot statement: pickNewDoor called with %s and %s" % (numDoors, listDoorsReserved))
    localcopyListDoorsReserved = listDoorsReserved[:]
    newDoor = random.randint(1,numDoors-len(localcopyListDoorsReserved)) #Randomly pick a number from total number of doors while not considering a list of doors to not be considered.
    #print ("troublehshoot statement: newDoor is %s" % (newDoor))
    while newDoor >= min(localcopyListDoorsReserved): #Looping over list of doors to not be considered until randomly picked door has a smaller number than the list of doors to not be considered to eliminate collisions
        newDoor+=1 #If random door has a number equal to or larger than smallest door number, then increase the door by 1
        localcopyListDoorsReserved.remove(min(localcopyListDoorsReserved)) #Remove smallest door from list as it no longer collides
        if not localcopyListDoorsReserved: #If reserved list is empty then collision no longer possible and loop no longer needed.
            break
    #print ("troubleshoot statement: pickNewDoor called with %s and %s" % (numDoors, listDoorsReserved))
    return(newDoor)
    
#This function creates a random list of doors to eliminate from an original pool while taking special doors into consideration
def createEliminateList(numDoors, numDoorsToEliminate, listDoorsReserved):
    #print ("troubleshoot statement: createEliminateList called with %s %s %s" % (numDoors, numDoorsToEliminate, listDoorsReserved))
    listDoorsEliminated = [] #Variable containing list of doors eliminated to return
    
    for loopNum in range(numDoorsToEliminate): #loop as many times as needed
        listDoorsToNotConsider = listDoorsEliminated + listDoorsReserved #Create overall list of doors to not consider which includes eliminated doors as well as reserved doors
        listDoorsEliminated.append(pickNewDoor(numDoors, listDoorsToNotConsider)) #Call picknew door function with overall list and add randomly chosen door to list of doors eliminated
        #print ("troubleshoot statement: in loop doorstonotconsider is %s and doorseliminated is %s" % (listDoorsToNotConsider, listDoorsEliminated))
    
    return listDoorsEliminated


#Initialize variables
numDoors = int(input('Enter total number of doors to simulate, must be integer 3 or higher: '))
numDoorsToRemove = int(input('Enter total number of doors to eliminate, must be number higher than 1 and less than number of doors-2: '))
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
 
 #numDoorToEliminate = pickNewDoor(numDoors, [numDoorPrize, numDoorFirstPick]) #Randomly pick door to eliminate using helperfunction that is not prize door or first picked door
 
 listofDoorsEliminated = createEliminateList(numDoors,numDoorsToRemove,[numDoorPrize, numDoorFirstPick]) #Randomly pick door(s) to eliminate using helperfunction that is not prize door or first picked door

 numDoorSwapPick = pickNewDoor(numDoors,[numDoorFirstPick]+listofDoorsEliminated) #Figure out swap pick that is not first picked or eliminated door using helper function for swap strategy
 
 numDoorSecondPick = pickNewDoor(numDoors,listofDoorsEliminated) #Randomly pick door that is not one of the eliminated doors for randomly pick from smaller pool strategy.

 print("Run %s : numDoorPrize is %s numDoorFirstPick is %s listofDoorsEliminated is %s numDoorSwapPick is %s numDoorSecondPick is %s" % (loopNum, numDoorPrize, numDoorFirstPick, listofDoorsEliminated, numDoorSwapPick, numDoorSecondPick)) #Publish simulation random choices
 
 #Tally if the two new strategies resulted in a win by comparing to the door with prize.
 if numDoorSwapPick == numDoorPrize:
     numSwapPickWinTally += 1
     
 if numDoorSecondPick == numDoorPrize:
     numSecondPickWinTally += 1

#Publish statistics on the three different strategies and their win rate
print ("Number of times original pick won ", numFirstPickWinTally, "For percent value of", numFirstPickWinTally/numSimRums*100)
print ("Number of times swapped pick won ", numSwapPickWinTally, "For percent value of", numSwapPickWinTally/numSimRums*100)
print ("Number of times random pick from smaller pool won ", numSecondPickWinTally, "For percent value of", numSecondPickWinTally/numSimRums*100)
