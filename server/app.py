#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string>")
def print_string(string):
    print(string)
    return string
# ../Flask application in flask_app.py counts through range of parameter in "/count/<parameter" on separate lines. - AssertionError: assert '1<br>2<br>3<...r>9<br>10<br>' == '0\n1\n2\n3\n...n6\n7\n8\n9\n'
# @app.route("/count/<int:num>")
# def count(num):
#     result = ""
#     for i in range(1, num+1):
#         result += str(i) + "<br>"
#     return str(result)
@app.route("/count/<int:num>")
def count(num):
    result = ""
    for i in range(num):
        result += str(i) + "\n"
    return result

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math_operation(num1, operation, num2):
    if operation == "+" or operation == "add":
        result = num1 + num2
    elif operation == "-" or operation == "subtract":
        result = num1 - num2
    elif operation == "*" or operation == "multiply":
        result = num1 * num2
    elif operation == "div" or operation == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Error: Invalid operation. Use add, subtract, multiply, or divide."
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
