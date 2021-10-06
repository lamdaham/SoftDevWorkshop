#Gold Medalist: Ivan Lam, Justin Morrill, Ella Krechmer, Naomi Naranjo
#SoftDev
#K10: Putting Little Pieces Together
#2021-10-5


import csv, random

from flask import Flask
app = Flask(__name__) #create instance of class Flask


# reads the file into a 2d list and returns the list
def read(dict):
    with open('occupations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        spamreader = list(spamreader)
        spamreader.pop(0)
        spamreader.pop(-1)
        for row in spamreader:
            dict[row[0]] = float(row[1])*10
        return spamreader




def main():
    dict = {}
    p = read(dict)
    occupationList = "<br>"

    # takes every occupation and puts it into a string with <br> as new lines
    for x in p:
        occupationList += x[0]
        occupationList += "<br>"
    start = 0
    end = 0
    randNum = random.randint(0, 1000)
    for x in dict:
        start = end
        end += dict[x]
        if(randNum>=start and randNum<end):
            return "Gold Medalist: Ivan Lam, Justin Morrill, Ella Krechmer, Naomi Naranjo" + 2* "<br>" + x + "<br>" + occupationList
    return "Gold Medalist: Ivan Lam, Justin Morrill, Ella Krechmer, Naomi Naranjo" + 2* "<br>" + "Other" + "<br>" + occupationList

@app.route("/")       #assign fxn to route
def hello_world():
    return main()

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
