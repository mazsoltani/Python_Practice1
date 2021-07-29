name = input("Please Enter your Name= ")
family = input("Please Enter your Family= ")

score1 = float(input("Please Enter your Score_1= "))
score2 = float(input("Please Enter your Score_2= "))
score3= float(input("EPlease Enter your Score_3= "))

avg = (score1+score2+score3) / 3
if score1>20 or score2>20 or score3>20:
    print("Error!!!  Scores Can not bigger than 20 ")
elif avg >= 17:
    print(name , family, "= your average is",avg ," and your status is Great")

elif avg >=12 and avg < 17 :
    print(name,family,"=your average is",avg ,"and your status Normal") 

else:
    print(name,family,"= your average is",avg ," and your status is Fail")