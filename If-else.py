# Program: Program to show if-else and functions len, upper, title, lower
# Author: Mohammad El-Ramly
# Version: 1.0
# Date: 11/11/2022

cars = ["bmw", "audi", "toyota"] 
car = input ("Pls enter car maker: ")

if len(car) <= 4 and car.lower() in cars:
    print(car.upper())
else:
    print(car.title())
