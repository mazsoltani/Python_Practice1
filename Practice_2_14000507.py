num1 = int(input("Please Enter First of Side of the Triangle= "))
num2= int(input("Please Enter Second of Side of the Triangle= "))
num3 = int(input("Please Enter Third of Side of the Triangle= "))

if num1< num2 + num3 and num2 < num1 + num3 and num3 < num1+ num2:

    print("Triangle is Create.")

else:
    print("Triangle Do Not Create.")