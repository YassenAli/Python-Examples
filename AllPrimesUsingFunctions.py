# Demo of Creating Functions
# Mohammad El-Ramly
# Nov 2022

import math

def isPrime(num):    
    prime = True
    for i in range (2 ,int(math.sqrt(num)+1)):
        if(num % i == 0):
            prime = False
            break
    if prime:
        print (num ,  " is a prime number")


#################################
max_num = int(input("Enter a number: "))
for num in range (2 , max_num):
    isPrime(num)

    
