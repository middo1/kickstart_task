import math


diameter = input("Enter diameter of pizza : ")
price = input("Enter price of pizza : ")

try:
    diameter = int(diameter)
    price = int(price)
    area = math.pi * (diameter**2)/4 
    res = area/price
    print(res)
except:
    print("Invalid input")
