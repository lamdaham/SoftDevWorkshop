#Ivan Lam
#SoftDev
#K06: StI/O: Divine your Destiny
#2021-09-28

# SUMMARY OF TRIO DISCUSSION
# I discussed with Ella and Justin to use a dictionary to store the list of the two occupations and percentage.
# We also used sys readfile to create a program that reads from csv file
# DISCOVERIES
# We could multiply each percentage by 10 so that there is no decimal point and we can use randrange
# QUESTIONS
# None
# COMMENTS
# We used two functions to better organize the code.


import csv, random

def read(dict):
    with open('occupations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            dict[row[0]] = float(row[1])*10



def main():
    dict = {}
    read(dict)
    start = 0
    end = 0
    randNum = random.randint(0, 1000)
    for x in dict:
        start = end
        end += dict[x]
        if(randNum>=start and randNum<end):
            print(x)
            return



if __name__ == "__main__":
    main()