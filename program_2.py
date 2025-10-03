# Title: Math Quiz
# Author: Arianna Endres
# Date: 10/03/2025

# Define the math_quiz function, which presents the
# equation and inputs the user's answer.
def math_quiz(number1, number2):
    print('Add the following two numbers:')
    response = float(input(f'{number1} + {number2} = '))
    return response

# Set the number variables equal to the desired values
# and set the correct answer and response variables.
number1 = 17
number2 = 109
correct_answer = number1 + number2
response = math_quiz(number1, number2)

# Determine if the user's answer is correct and display
# a message accordingly.
if response == correct_answer:
    print('Congratulations! Your answer is correct!')
else:
    print(f'Sorry! Your answer is incorrect. The correct answer is {correct_answer}')
