#Ivan Lam
#SoftDev
#NamePrint/Classwork/Print a random name from two lists of students
#2021-09-24

# SUMMARY OF TRIO DISCUSSION
# I discussed with Ella and Christopher to use a dictionary to store the list of the two periods.
# We also used sys readfile to create a program that is more flexiable with the arguments
# DISCOVERIES
# randrange from Random allowed us to pick a random number that is inclusive, which is helpful for picking
# an index in a list
# QUESTIONS
# None
# COMMENTS
# Dictionary is not really effective, but it may be helpful for readability and for scalability.



# Imports random to randomly pick and sys to read from file
from random import *
import sys


# Initialize a dictionary with the list of the two periods
namesDict = {}


# Reads the name of the files and stores it into respective list in namesDict
def readNames(filename, numName):
    filecontents=""
    with open(filename, "r") as f:
        filecontents=f.read()
    names=filecontents.split("\n")

    #remove empty lines
    namesDict[numName]=[name for name in names if name]
    return


# Runs readNames and randomly picks from the combination
def main():
    if len(sys.argv) != 3:
        print("Incorrect arguments. Usage: python names.py pd1_filename pd2_filename")
        return

    readNames(sys.argv[1], "names1")
    readNames(sys.argv[2], "names2")
    names=namesDict["names1"]+namesDict["names2"]

    randname=names[randrange(len(names))]
    print(randname)


if __name__ == "__main__":
    main()
