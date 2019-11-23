## CMPT 120 D200
## Final Assignment
## Authors: Ramneet Brar, Lena Nejad
## December 3, 2018


#global variables:
userInputFile = "" #input file that user chooses to gather data
listOfDraws = [] #list of draws, including all information (lall in provided code)
listOfDatesOfDraws = [] #list of dates of draws from listofdraws(lall)
listOfNumsDrawn = [] #list of draw numbers from listofdraws(lall)
listOfDrawJackpots = [] #list of draw jackpots in draws from listofdraws(lall)
listNumWinners = [] #list of number of winners in draws from listofdraws(lall)
userDataInput = "" #user input to determine whether to end, use all or sel data
numDraws = 0 #number of draws, used to determine range of for loops
userOutputFile = "" #output file that user selects to create
listTo49 = [] #list of number of times each number appears in draws
listOfNumsInRange = [] #list of frequency of nums in ranges
listResults = [] #list for output file (lout)

import turtle
def welcomeFunction():
    #this is a void function, its purpose is to welcome the user to the system and to get the names of input files
    print("Welcome to the CMPT 120 6-49 Processing System!")
    print("===============================================")
    print("You will first be asked to provide the INPUT file name; you will be asked to provide the OUTPUT file name later.")
    print("The input file should be in this folder, the output file will be created in this folder.")
    print("You will be able to provide new names for the files or accept the default names. Both files should have the extension  .csv")
    #userInputFile =input("Type x for file 'IN_data_draws3.csv', or type a new file name ==>")
    #if userInputFile == "x":
    #    userInputFile = "IN_data_draws3.csv"
    return

def inputFileSelection():
    #this is a productive function that asks user input for the file of draws to be used, and returns that csv file
    userInputFile =input("Type x for file 'IN_data_draws3.csv', or type a new file name ==>")
    if userInputFile == "x":
        userInputFile = "IN_data_draws3.csv"
    return userInputFile

def read_csv_into_list_of_lists(IN_file):
    '''
    PROVIDED. CMPT 120
    A csv file should be available in the folder (where this program is)
    A string with the name of the file should be passed as argument to this function
    when invoking it
    (the string would include the csv extension, e.g "ID_data.csv")
    '''
    import csv

    lall = []
    print("\n.... TRACE - data read from the file\n")
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for inrow in csv_reader:
            print(".......",inrow)
            lall.append(inrow)
    return lall

def createSeparateLists(listDraws):
    listOfDatesOfDraws = []
    for i in range(len(listDraws)):
        date = (listDraws[i][0])
        listOfDatesOfDraws.append(date)
    listOfNumsDrawn = []
    for i in range(len(listDraws)):
        innerListNums = []
        for k in range(1,8):
            number = listDraws[i][k]
            innerListNums.append(number)
        listOfNumsDrawn.append(innerListNums)
    listOfDrawJackpots = []
    for i in range(len(listDraws)):
        jackpot = listDraws[i][8]
        listOfDrawJackpots.append(jackpot)
    listNumWinners = []
    for i in range(len(listDraws)):
        numWinners = listDraws[i][9]
        listNumWinners.append(numWinners)
    return listOfDatesOfDraws, listOfNumsDrawn, listOfDrawJackpots, listNumWinners

def dataProcess():
    #this is a productive function that asks the user for input to select the draws
    print("Please choose one of three options: \n Type ALL to process all the data. \n Type SEL to process selected draws. \n Type END to end this program.\n")
    validInputs = ["all", "sel", "end",]
    userDataInputLocal = ""
    while not(userDataInputLocal.lower() in validInputs):
        userDataInputLocal = input("\nType ALL, SEL OR END (not case sensitive) ==>")
    return userDataInputLocal

def userSelectAll(numDraws):
    #this function changes the formatting of the list, to create a list of the numbers drawn within the list of Draws
    listOfDraws = []
    innerListDraws = []
    for i in range(numDraws):
        innerListDraws = [listOfDatesOfDraws[i], listOfNumsDrawn[i], listOfDrawJackpots[i], listNumWinners[i]]
        listOfDraws.append(innerListDraws)
        #print("TRACE !!", listOfDraws)
    #print("\nTRACE!!", listOfDraws)
    return listOfDraws

def monthFromDataToNum(dateFromList):
    #this is a productive function that receives parameters. it takes a month written in date notation and turns it into the corresponding number
    months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    dashOne = dateFromList.index("-")
    dashTwo = dashOne + 4
    monthString = dateFromList[dashOne + 1: dashTwo]
    monthNum = months.index(monthString)
    return monthNum

def selectionByMonth(listOfDatesOfDraws, listOfNumsDrawn, listOfDrawJackpots,listNumWinners, numDrawswait ):
    print("Please select a month. \n Only the draws associated to this month will be processed.")
    userSelectedMonth = ""
    validMonthsList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while not(userSelectedMonth in validMonthsList):
        userSelectedMonth = int(input("Please type a month number (1-12) ==>"))
    #validation of user input^^
    listOfMonthsNums = []
    for i in range(len(listOfDatesOfDraws)):
        monthNum = monthFromDataToNum(listOfDatesOfDraws[i])
        #print("Trace !!", monthNum)
        listOfMonthsNums.append(monthNum)
    indicesOfUserInput = []
    for i in range(len(listOfMonthsNums)):
        if userSelectedMonth == listOfMonthsNums[i]:
            indicesOfUserInput.append(i)
            #print("Trace !!", i)
    #print("trace !!", indicesOfUserInput)
    numDraws = len(indicesOfUserInput)
    listOfDraws = []
    innerListDraws = []
    for i in range(len(indicesOfUserInput)):
        indexListDraws = [listOfDatesOfDraws[indicesOfUserInput[i]], listOfNumsDrawn[indicesOfUserInput[i]], listOfDrawJackpots[indicesOfUserInput[i]], listNumWinners[indicesOfUserInput[i]]]

        listOfDraws.append(indexListDraws)
    #print("\nTRACE !!",listOfDraws)
    listOfDatesOfDraws = updateLists(indicesOfUserInput, listOfDatesOfDraws)
    listOfNumsDrawn = updateLists(indicesOfUserInput, listOfNumsDrawn)
    listOfDrawJackpots = updateLists(indicesOfUserInput, listOfDrawJackpots)
    listNumWinners = updateLists(indicesOfUserInput, listNumWinners)
    return listOfDraws, listOfDatesOfDraws, listOfNumsDrawn, listOfDrawJackpots, listNumWinners, numDraws

def updateLists(indicesOfUserInput, listToUpdate):
    print(indicesOfUserInput)
    print(listToUpdate)
    updatedList = []
    for elem in indicesOfUserInput:
        print(elem)
        elem = int(elem)
        updatedList.append(listToUpdate[elem])
        print(updatedList)
    return updatedList

def dataBeingProcessed(listOfDraws):
    for i in range(len(listOfDraws)):
        print("\n\n","Just to TRACE, the draw being processed is:")
        print("Index #", i, "\n Date:", listOfDraws[i][0], "\n Numbers Drawn:", listOfDraws[i][1], "\n Jackpot:", listOfDraws[i][2], "\n Number of Winners", listOfDraws[i][3])
    return

def averageJackpot():
    listOfAverageJackpots = []
    for i in range(len(listOfDrawJackpots)):
        jackpot = int(listOfDrawJackpots[i])
        numWinners = int((listNumWinners[i]))

        if numWinners != 0:
            averageJackpot = jackpot//numWinners
            listOfAverageJackpots.append(averageJackpot)
        else:
            averageJackpot = 0
            listOfAverageJackpots.append(averageJackpot)
    #print("TRACE !!", listOfAverageJackpots)
    return listOfAverageJackpots

def maxJackpot():
    maxJackpot = 0
    indexMax = 0
    for i in range(len(listOfDrawJackpots)):
        if int(listOfDrawJackpots[i]) > maxJackpot:
            maxJackpot = int(listOfDrawJackpots[i])
            indexMax = i
    dateMaxJackpot = listOfDatesOfDraws[indexMax]
    print("\nThe max jackpot was", maxJackpot)
    print("The date of the max jackpot was", dateMaxJackpot)
    return maxJackpot, dateMaxJackpot

def maxAverageJackpot(listOfAverageJackpots):
    maxAverageJackpot = 0
    indexMax = 0
    for i in range(len(listOfAverageJackpots)):
        if int(listOfAverageJackpots[i]) > maxAverageJackpot:
            maxAverageJackpot = int(listOfAverageJackpots[i])
            indexMax = i
    dateMaxAverageJackpot = listOfDatesOfDraws[indexMax]
    print("\nThe max average jackpot was", maxAverageJackpot)
    print("The date of the max average jackpot was", dateMaxAverageJackpot)
    return maxAverageJackpot,dateMaxAverageJackpot

def numTimesDrawn(lst):
    print("Number of times each number was drawn:")
    listTo49 = [0]*50
    for elem in lst:
        for num in elem:
            number = int(num)
            listTo49[number] = listTo49[number] + 1
    return listTo49

def numsInRange(listNums):
    print("number of numbers in each range - all selected draws considered ranges:")
    print(listNums)
    listRanges = [0] * 5
    for i in range(len(listNums)):
        for j in range(len(listNums[i])):
            k = 0
            while (int(listNums[i][j]) > k*10):
                k += 1

            listRanges[(k-1)] += 1
            #print("TRACE !!", listRanges)
    return listRanges

def sixMaxs(listNums):
    print("Six most frequently drawn numbers:")

    res = ""
    for i in range(6):
        maxNum = listNums[0]
        pos = 0
        for j in range(len(listNums)):
            if listNums[j] > maxNum:
                maxNum = listNums[j]
                pos = j
        print("number:", pos, "frequency:", maxNum)
        res += "number:" + str(pos) + "frequency:" + str(maxNum) + "\n"
        listNums[pos] = -1
        maxNum = listNums[0]
        pos = 0
    return res

def turtleRangesDistribution():
    validInputs = ["y", "n"]
    userInput = ""
    while not(userInput.lower() in validInputs):
        userInput = input("Do you want to graph the ranges ranges distribution (Y/N) ==>")
    if userInput.lower() == "y":
        print("yes")
        turtle.penup()
        turtle.goto(-300,-200)
        turtle.pendown()
        turtle.pensize(5)
        turtle.forward(20)
        for i in range(len(listOfNumsInRange)):
            turtle.forward(50)
            turtle.left(90)
            turtle.fillcolor('lightblue')
            turtle.begin_fill()
            turtle.forward(listOfNumsInRange[i]*50)
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.backward(listOfNumsInRange[i]*50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(180)
            turtle.forward(50)
            turtle.end_fill()
        turtle.forward(20)
    else:
        print("no")
    return


## TO WRITE TO CSV OUTPUT FILE

def appendResToOutput(numDraws, listResults, listOfDatesOfDraws, listOfNumsDrawn, averageJackpot):
    print(numDraws)
    for i in range(numDraws):
        listResults.append("'" + listOfDatesOfDraws[i] + "'" + ",")
        newListNumsDrawn = []
        newListNumsDrawn.append(listOfNumsDrawn[i])
        listFrequency = numsInRange(newListNumsDrawn)
        #print("trace!!", listFrequency)
        for elmt in listFrequency:
            listResults.append(str(elmt) + ",")
            #print("trace!!",listResults)

        avgJackpot = averageJackpot()[i]
        listResults.append(str(avgJackpot) + "\n")
    return

def outputFileSelection():
    #this is a productive function that asks user input for the file of draws to be created for output, and returns that csv file
    userOutputFile =input("Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==>")
    if userOutputFile == "x":
        userOutputFile = "OUT_results3.csv"
    return userOutputFile

def writeOutputToFile(listResult,file_name):
    '''
    PROVIDED. CMPT 120
    Assumptions:
    1) lout is the list containing all the lines to be saved in the output file
    2) file_name is the parameter receiving a string with the exact name of the output file
       (with the csv extension, e.g "OUT_results.csv")
    3) after executing this function the output file will be in the same
       directory (folder) as this program
    4) the output file contains just text representing one draw data per line
    5) after each line in the file  there is the character "\n"
       so that the next draw is in the next line, and also
       there is (one single) "\n" character after the last line
    6) after the output file was created you should be able to open it
       with Excell as well
    '''

    fileRef = open(file_name,"w") # opening file to be written
    for line in listResult:
        fileRef.write(line)

    fileRef.close()
    return

##TOP LEVEL
##==============================================================
##==============================================================
welcomeFunction() #introduces user to program
userInputFile = inputFileSelection() #user chooses input file
listOfDraws = read_csv_into_list_of_lists(userInputFile) #input file converted into list of multiple draw lists
print("Trace", listOfDraws)
numDraws = len(listOfDraws)

listOfDatesOfDraws, listOfNumsDrawn, listOfDrawJackpots, listNumWinners = createSeparateLists(listOfDraws)

#print("\nTRACE !!",listOfDatesOfDraws,"\n")
#print("\nTRACE !!",listOfNumsDrawn,"\n")
#print("\nTRACE !!",listOfDrawJackpots,"\n")
#print("\nTRACE !!",listNumWinners,"\n")

userDataInput = dataProcess() #gets input from user about what data to process, then in following if/elif processes selected data.


if userDataInput.lower() == "end":
    print("end")    #trace
    #proceed to end
else:
    if userDataInput.lower() == "all":
        print("\n\n All Data will be processed. \n================================================================")
        #print(listOfDraws)
        listOfDraws = userSelectAll(numDraws)

    elif userDataInput.lower() == "sel":
        print("\n\n Selected Data will be processed. \n================================================================")    #trace
        validInputsSelected = ["m"] #d bonus!!!!!!
        userSelectionMethod = ""
        while not(userSelectionMethod.lower() in validInputsSelected):
            userSelectionMethod = input("Type (m) to select by month ==>") #D BONUS!!!

        listOfDraws, listOfDatesOfDraws, listOfNumsDrawn, listOfDrawJackpots, listNumWinners, numDraws = selectionByMonth(listOfDatesOfDraws, listOfNumsDrawn, listOfDrawJackpots,listNumWinners, numDraws)

        #elif userSelectionMethod.lower() == "d" BONUS!!!!!!
                #listOfDraws =

                #''' OUTPUT STUFF!!! '''

    userOutputFile = outputFileSelection()
    dataBeingProcessed(listOfDraws)


    print("\n\n","STATS:\n================================================================")
    print("Draws Processed:", numDraws)
    maxJackpot()
    maxAverageJackpot(averageJackpot())
    listTo49 = numTimesDrawn(listOfNumsDrawn)
    print(listTo49)
    listOfNumsInRange = numsInRange(listOfNumsDrawn)
    print(listOfNumsInRange)
    sixMaxs(listTo49)

    ##Appending to output
    listResults=[]
    appendResToOutput(numDraws, listResults, listOfDatesOfDraws, listOfNumsDrawn, averageJackpot)


    ##Writing it
    writeOutputToFile(listResults,userOutputFile)
    turtleRangesDistribution()
