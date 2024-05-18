two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

dig1 = int(int(two_digit_number) /10)

dig2 = int(two_digit_number) %10


print (str(dig2+dig1))