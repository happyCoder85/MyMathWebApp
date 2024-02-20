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
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def do_calculation():
    num_list = MyMath()
    numbers_list = request.form['numbers'].split(",")
    title = "Here are your results:"

    for number in numbers_list:
        num_list.num_list.append(int(number))

    max_number = max(tuple(num_list.num_list))
    average = MyMath.calculate_average(num_list)
    std_deviation = MyMath.calculate_standard_deviation(num_list)
    return render_template('calculate.html',
                        num_list=num_list.num_list,
                        max=max_number,
                        average=average,
                        std_deviation=std_deviation,
                        the_title=title,)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")