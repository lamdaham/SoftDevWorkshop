# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

app.run()  # Q4: Where have you seen similar construcs in other languages?
                

# 0. This syntax reminds me of Java, where we initiate object with a class.
# 1. "/" is how the computer separate path directories and it is easy to see this in the terminal or html websites
# 2. I think it'll print in terminal once the server starts. 3. It says it'll print __name__ so I assume it's the name corresponding to the Flask element.
# 3. I believe it print on the webpage once the server runs because I have prior experience in flask.
# 4. This reminds me of functions that certain objects have in Java