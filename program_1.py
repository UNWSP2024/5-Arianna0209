# Title: Kilometer Converter
# Author: Arianna Endres
# Date: 10/03/2025

# Define the kilometer_conversion function
def kilometer_conversion(kilometers):
    miles = kilometers * 0.6214
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    kilometers = float(input('Enter the distance in kilometers: '))
    print('in main')

    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    miles = kilometer_conversion(kilometers)

    # Display the miles
    print(f'The distance in miles is: {miles:.2f}')

