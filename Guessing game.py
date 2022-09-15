RightNumber = 55
print("Hello,", end = "")
while RightNumber == 55:
    GUESS = int(input("I have a number in my code, it is between 0 and 100, can you guess what the number? : "))
    if GUESS > RightNumber:
            print("Too high! Guess something smaller.")
    if GUESS < RightNumber:
            print("Too low! Guess something larger.")
    if GUESS == RightNumber:
            print("Nice job!")
            RightNumber = RightNumber - 1
