#1) Ask the user for their name and their current salary.
#Then, print to the user a message that they
#just got a 20% raise and show them their new salary.
# Example: "Congragulations John Gibbons, you now make 120$"
salary = float(input("Enter your salary:")) #if the salary includes cents we need to represent those too
name = input("Enter your name:")
print('"Congratulations',name,', your new salary is:"', salary*1.2)



