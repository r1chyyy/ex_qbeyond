import json

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

    input1 = int(input('Please enter the first number: '))
    input2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(input1, input2))
        print(input1 + input2)

    elif operation == '-':
        print('{} - {} = '.format(input1, input2))
        print(input1 - input2)

    elif operation == '*':
        print('{} * {} = '.format(input1, input2))
        print(input1 * input2)

    elif operation == '/':
        print('{} / {} = '.format(input1, input2))
        print(input1 / input2)

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
