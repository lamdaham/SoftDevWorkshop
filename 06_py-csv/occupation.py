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