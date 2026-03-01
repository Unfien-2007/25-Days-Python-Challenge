#Constant
MILES_TO_KILOMETERS = 1.60934
KILOMETERS_TO_MILES = 0.62137

#user inputs
miles_input = float(input("Enter miles: "))
kilometers_input = float(input("Enter kilometers: "))

#Conversion
miles_result = miles_input * MILES_TO_KILOMETERS
kilometers_result = kilometers_input * KILOMETERS_TO_MILES

#Display Result
print(f"{miles_input} miles is equivalent to {miles_result} in kilometers.")
print(f"{kilometers_input} kilometers is equivalent to {kilometers_result} in miles.")