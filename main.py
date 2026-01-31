name = input("Enter student name: ")

marks = []
subjects = ["Math", "Physics", "Programming", "Communication", "Creativity"]

for subject in subjects:
    mark = int(input(f"{subject} marks: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("\n--- RESULT ---")
print("Student Name:", name)
print("Average Marks:", round(average, 2))

