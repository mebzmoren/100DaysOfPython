# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest = 0 #initializes highest score to 0

for score in student_scores:
    if highest <= score:
        highest = score #stores the score to the highest score variable if score is more than or equal to the highest score
    else:
        highest = highest   #maintains the highest score value if score is less than the highest score

print(f"The highest score in the class is: {highest}")