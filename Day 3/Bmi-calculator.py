# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height**2)
diagnosis =''
if  bmi <18.5:
  diagnosis= "are underweight."
elif bmi>=18.5 and bmi <25:
 diagnosis= "have a normal weight."
elif bmi>=25 and bmi <30:
 diagnosis= "are slightly overweight."
elif bmi >= 32:
  diagnosis= "are obese."
print (f"Your BMI is {bmi}, you {diagnosis} ")