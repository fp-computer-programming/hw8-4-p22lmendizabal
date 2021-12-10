# author: LM (AMDG) 12/9/21

import random
def game():
    integer = random.randint(0, 50)
    num = (input("Enter a number: "))
    if (num) == "stop":
        print("The number was {0}".format(integer))
    while int(num) != integer:
        if int(num)< integer:
            print("Enter a higher number: ")
           
        else:
            print("Enter a lower number")
        
        
    if int(num) == integer:
        print("You guessed the number {0}.".format(integer))
    return
game()