# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0       #to get the sum of heights
students = 0    #to get the number of students

for height in student_heights:
  total += height
  students += 1

average = round(total / students)
print(average)
