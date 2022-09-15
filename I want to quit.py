import sys
X = 1
while X == 1:
    USER_IN = input('"Hello, would you like to quit?" (Yes/No) :  ')
    if USER_IN == "Yes" or USER_IN == "yes":
        sys.exit("User typed in Yes.")
    else :
            print('"Understood, I will ask you again."')
