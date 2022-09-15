TACO= 5.00
SUNDAE= 8.00
#Above, I established the variables for TACO and SUNDAE, allowing easy calculation for price later on.
#Below, I wrote the intial question that decides whether the customer wants, (print is not needed for input!!!)
USER_IN= input("Hello, do you want Tacos or Sundaes? : " )
print(USER_IN)
#Above is tool to ensure we know if we put spaces anywhere on accident.
if USER_IN == "Tacos": #if they perfectly enter in "Tacos", they will then be asked how many tacos they want
   tacoAmt = int(input("How many Tacos do you want? : "))
   print("Good Choice! The total amount will be:" , int(tacoAmt*TACO*1.55))
#print above then takes the amount they requested, multiplies that with the cost of each Taco, and then adds the tax
   
    
   #Same can be said for below, except if the customer enters in something other than Sundaes or Tacos they'll just get Sundaes     
elif USER_IN == "Sundaes": 
        sunAmt =  int(input("How many Sundaes do you want? : "))
        print("Good Choice! The total amount will be:", int(sunAmt*SUNDAE*1.55))


    
    
