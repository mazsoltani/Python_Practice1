weight = float(input("Please Enter your Weight as kg= "))
height = float(input("Please Enter your Height as cm="))

height = height / 100
bmi = weight / (height*height)

if bmi < 18.5:
    print("your weight is underweight")

elif bmi >= 18.5 and bmi <= 24.9:
    print('your weight is normal')

elif bmi >= 25 and bmi < 29.9:
    print('your weight is overweight')

elif bmi>= 30 and bmi < 34.9:
    print('your weight is obese')

elif bmi>= 35:
    print('your weight is extremely obese')