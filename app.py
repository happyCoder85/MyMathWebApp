"""
Description: MyMath Web Application
Author: Jonathan Spurling
Section Number: ADEV-3005 (251409)
Date Created: February 20, 2024

Updates: None
"""
from flask import Flask, render_template, request
from my_math import MyMath

app = Flask(__name__)

@app.route('/')
def index():
    """Loads the index.html page"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def do_calculation():
    """
        Does the calculations to calculate the max, average and standard deviation
        of a list of numbers
    """
    num_list = MyMath()
    numbers_list = request.form['numbers'].split(",")
    title = "Here are your results:"

    for number in numbers_list:
        try:
            num_list.num_list.append(int(number))
        except ValueError:
            print("Must enter numbers")
            break

    try:
        max_number = max(tuple(num_list.num_list))
    except ValueError as e: 
        print("ValueError: ", e)
        max_number = 0
    try:
        average = MyMath.calculate_average(num_list)
    except ZeroDivisionError as e:
        print("Error: ", e)
        num_list.num_list = []
        average = 0
    try:
        std_deviation = MyMath.calculate_standard_deviation(num_list)
    except UnboundLocalError as e:
        print("Error: ", e)
        std_deviation = 0

    return render_template('calculate.html',
                        num_list=num_list.num_list,
                        max=max_number,
                        average=average,
                        std_deviation=std_deviation,)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    