# Python program to check if the input number is prime or not
while(True):
    num = int(input("\n Enter a Number \t") )

    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(" Flase")
               break
       else:
           print(" True ")
