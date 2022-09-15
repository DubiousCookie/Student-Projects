#To find if indiviual numbers are prime
def is_prime (number) :
    if number > 1:
        for num in range (2, int (number**0.5) + 1) :
            if number % num == 0:
                return False
            return True
        return False
print(is_prime (2011))
#To list all prime numbers within a range
prime_numbers = []
for num in range (100, 301):
    if is_prime (num) : #depends on the "is_prime" defined above.
        prime_numbers.append(num)

print (prime_numbers) #If this is indented, will be put into a loop (comedy)

    # Returns all prime numbers
#Let's try that with even numbers
def is_even (number) :
    if number > 1:
        for num in range (1, int(number*0.5)):
            if number % num == 0:
                return False
            return True
        return False
print(is_even (2))
