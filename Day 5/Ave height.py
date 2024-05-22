# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total = sum(student_heights)
ave = total / len(student_heights)


print(f"total height = {total}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(ave)}")

