import math
chocie=input("if selcet advance function Please Enter 1 else Enter 2= ")
if chocie=="1":
    num1 = float(input("Please Enter frist number="))
    op = input("Please Choice an operator in {sin-cos-tan-radical-factorial}=")

    if op == "sin" or op == "cos" or op == "tan" or op =="radical" or op == "factorial":
        if op == "radical":
            res = math.sqrt(num1)
    
        elif op == "sin":
            res = math.sin(math.radians(num1))
    
        elif op == "cos":
            res = math.cos(math.radians(num1))
   
        elif op == "tan":
            res = math.tan(math.radians(num1))
   
        elif op == "factorial":
            
            res = math.factorial(num1)
        
    
else:
        num2 = int(input("please Enter first number="))
        num3 = int(input("please Enter second number="))
        op = input("Please Choice an operator in {+,-,*,/}=")
if op == "+" or op == "-" or op == "*" or op =="/":
    
    if op == '+':
        es = num2 + num3
    elif op == '-':
        res = num2 - num3

    elif op == '*':
        res = num2 *num3

    elif op =='/':
        if num3 !=0:
             res = num2/num3
        else:
            res="can't divide by zero" 
    else:
        print("Error.")  
print("Your Answer is=",res)