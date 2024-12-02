# Nathaniel Salan C0547078

import random
from statistics import stdev

#Global Variables
totalValue = 0 #Total Value of each set of Dice toss
log = [] #Recorded log of the total value of each set of Dice toss

tableNum = [] #The Value of a set of Dice toss
tableFreq = [] #The Frequency of a set of Dice toss

#Simulate die roll
def roll(num:int) -> int:
    totalPoints = 0

    #num is the number of die being rolled
    for i in range(num):
        out = random.randint(1,6)

        if out == 6:
            #Roll 6 for +4 points
            totalPoints += 4
        elif out == 5:
            #Roll 5 for +2 points
            totalPoints += 2
        elif out < 4:
            #Roll 3,2,1 for -1 points
            totalPoints -= 1
    
    return totalPoints

#Simulate rolling a set of dice rolls, and then records it into a log.
def rollStack(num:int, times:int):
    global log,totalValue

    #Times is the number of times a set (num) of dice will be rolled.
    for i in range(times):
        points = roll(num)
        totalValue += points
        log.append(points)

#A function that just ask for user input.
def ask():

    try:
        numberOfDice = int(input("Pick how many dice do you want to roll? "))
        numberOfRepeat = int(input("Pick how many times do you want to roll them? "))

        rollStack(numberOfDice, numberOfRepeat)
    except:
        print("Invalid Input")

#A function that creates the frequency tables.
def frequencyTable():
    global log,tableNum,tableFreq
    i = 0

    #Basically just count frequent a number shows up on the list
    for num in log:
        if len(tableNum) == 0:
            tableNum.append(num)
            tableFreq.append(1)
        elif num != tableNum[i]:
            tableNum.append(num)
            tableFreq.append(1)
            i += 1
        else:
            tableFreq[i] += 1

#A function that formats the table into the (Value, Frequency, and Probability) and prints them.
def printTable():
    global log, tableNum, tableFreq
    print("Value","Frequency","Probability", sep="\t")
    print("---------------------------------------------------")
    for i in range(len(tableNum)):
        print(f"{tableNum[i]}",f"{tableFreq[i]}\t",f"{ (tableFreq[i]/len(log))*100.0 }%", sep="\t ")

#A function that calculates the Mean, Median and Standard Deviation of the recorded log.
def statistics():
    global log, tableNum, totalValue


    mean = totalValue/len(log)
    median = log[int((len(log))/2)]
    sd = stdev(log) #Used a library to calculate the S.D :P

    print(f"\nTotal Value: {totalValue}\t Mean: {mean}\t Median: {median}\t Standard Deviation: {sd}")

#Main
def main():
    ask()
    print("Log:")
    print(log, end="\n\n")
    log.sort()

    frequencyTable()
    printTable()
    statistics()

if __name__ == "__main__":
    main()