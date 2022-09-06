def calc():
    import math
    print("You have entered CALCULATOR mode ▼")
    oper = input("Kindly provide the operation -→").strip()
    basic = ['+', '-', '*', '/', '//', '%', 'pow']
    advanced = ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', '!', 'asin', 'acos', 'atan']
    if oper in basic:
        first, second = map(float, input('Provide 2 values (seperated by comma) -→ ').split(','))
        match oper:
            case '+': print(first + second)
            case '-': print(first - second)
            case '*': print(first * second)
            case '/': print(first / second)
            case '//': print(int(first // second))
            case '%': print((first*100)/second)
            case 'pow': print(first ** second)
    if oper in advanced:
        first = float(input('Provide value -→ '))
        match oper:
            case 'sin': print(math.sin(first))
            case 'cos': print(math.cos(first))
            case 'tan': print(math.tan(first))
            case 'log': print(math.log10(first))
            case 'ln': print(math.log(first))
            case 'sqrt': print(math.sqrt(first))
            case '!': print(math.factorial(int(first)))
            case 'asin': print(math.asin(first))
            case 'acos': print(math.acos(first))
            case 'atan': print(math.atan(first))
