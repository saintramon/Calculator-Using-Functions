def sumNum(a, b):
    print(a + b)


def difNum(a, b):
    print(a - b)


def mulNum(a, b):
    print(a * b)


def divNum(a, b):
    print(a / b)



userWant = None
while userWant != "0":

    firstNum = int(input("What is your first number? "))
    operator = input("What is your operator (+,-,/,*)? ")
    secNum = int(input("What is your second number? "))

    if operator == "+":
        sumNum(firstNum,secNum)
    elif operator == "-":
        difNum(firstNum,secNum)
    elif operator == "*":
        mulNum(firstNum,secNum)
    elif operator == "/":
        divNum(firstNum,secNum)
    else:
        print("Error, not an operator!")

    userWant = input("Do you want to try again? 1 if yes, 0 if no: ")







