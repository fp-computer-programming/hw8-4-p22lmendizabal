# author: LM (AMDG) 12/9/21
import random
random.seed(17)
def guessing(number):
    integer = random.randint(0, 50)
    while number != integer:
        if number < integer:
            print("Guess a higher number")
            input("Enter another number:")
        elif number > integer:
            print("Guess a lower number.")
            input("Enter another number.")


number = int(input("Enter a number: "))
guessing(number)