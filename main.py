"""
Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
To each file append a random number between 1 and 100.
Create a summary file (summary.txt) that contains name of the file and number in that fil
"""


import random

#create txt of the al
letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
#open and w create text doc if it doesn't exist yet
all_letters = open("all-letters.txt", "w")
#loop of every element in letters
for l in letters:
    #create a  file for every l
    with open(f'{l}.txt', "w") as files:
        #generate random number
        random_number = random.randint(1, 100)
#write the values from random function
        files.write(f"Random number: {random_number}")
        #write the list and \n starts from the new line
        all_letters.write(f"{l}.txt: {random_number}\n")