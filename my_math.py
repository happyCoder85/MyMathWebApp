"""
Description: My Math class that contains a calculate average & calculate standard deviation
Author: Jonathan Spurling
Section Number: ADEV-3005(251409)
Date Created: February 18, 2024

Updates: none
"""

class MyMath():
    """Class that contains a calculate average and calculate standard deviation functions"""
    def __init__(self):
        """Instantiates an empty list"""
        self.num_list = []

    def calculate_average(self):
        """Function that takes a list of numbers and calculates the average."""
        average = sum(self.num_list) / len(self.num_list)

        return round(average, 2)

    def calculate_standard_deviation(self):
        """
        Function that takes a list of numbers and then calculates and returns the 
        standard deviation
        """
        # Calculate the mean of the self
        mean = sum(self.num_list) / len(self.num_list)
        # Calculate the variance
        variance = sum((x - mean) ** 2 for x in self.num_list) / (len(self.num_list) - 1)
        # Calculate the standard deviation
        standard_deviation = round(variance ** 0.5, 2)
        return standard_deviation
