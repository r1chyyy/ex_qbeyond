import json

with open("calc.json", "r") as read_file:
    data = json.load(read_file)

uzd = {
    
    "input1": 2,
    "commment":"accept any number",
    "input2": 3,
    "commment":"accept any number",
    "operator":"+",
    "comment":"options here: '+','-','*','/' "

}

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()

with open("calc.json","w") as write_file:  
    json.dump(uzd,write_file)  
  
with open("calc.json", "r") as read_file:  
    b = json.load(read_file)  
print(b)  
