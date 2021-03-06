##Programmer: Joselyne Guillen
##File Name: golfScores.py 
##Date: 2/21/21
##Version: 1.4
##Explanation of Program: 
##This program reads each player's name and 
##golf score from the user and saves the data
##in a file called golf.txt.

def main(): #main function

    numPlayers = int(input("How many player's information will you be recording?\n")) #asks the user to input how many player's data will be stored

    outfile = open('golf.txt','a') #opens file for appending. If it doesn't exist, it creates a file

    for i in range(1,numPlayers+1): #loop to write each player's information into a file
        playerName = input("Player's Full Name:\n") #asks user for player's name
        playerScore = int(input("Golf Score:\n")) #asks user for player's golf score

        outfile.write('Name: ' + playerName + '\n') #writes player's name to file
        outfile.write('Golf Score: ' + str(playerScore)+'\n') #writes player's golf score to file
        outfile.write('-----------------------------------\n') #writes a divisor to the file to separate the corresponding data

    outfile.close() #closes the file
    print('Data written to golf.txt') #tells the user the data was put in the correct file successfully
main() #function call for main
