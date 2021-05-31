##Programmer: Joselyne Guillen
##File Name: golfScoreRead.py 
##Date: 2/21/21
##Version: 1.3
##Explanation of Program: 
##This program reads each line in the
##golf.txt file and displays it

def main(): #main function

    infile = open('golf.txt','r') #opens file to be read

    for line in infile: #loop to read each line in the file
        print(line) #prints the read line

    infile.close #closes file

main() #function call for main
        

   

    

        
