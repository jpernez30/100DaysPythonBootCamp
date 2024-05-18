print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

lowerName1 = name1.lower()
lowerName2 = name2.lower()

t = lowerName1.count("t")
t = t+ lowerName2.count("t")

r = lowerName1.count("r")
r = r+ lowerName2.count("r")

u = lowerName1.count("u")
u = u+ lowerName2.count("u")

e = lowerName1.count("e")
e = e+ lowerName2.count("e")


l = lowerName1.count("l")
l = l+ lowerName2.count("l")

o = lowerName1.count("o")
o = o+ lowerName2.count("o")

v = lowerName1.count("v")
v = v+ lowerName2.count("v")


total = ((t+r+u+e)*10) + (l+o+v+e)

if total <10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")

elif total >=40 and total <= 50:
  print(f"Your score is {total}, you are alright together.")
else:
   print(f"Your score is {total}.")
