name = input("Enter student name: ")

subjects = ["Math", "Physics", "Programming", "Communication", "Creativity"]
marks = {}

for subject in subjects:
    marks[subject] = int(input(f"{subject} marks: "))

strengths = []
weaknesses = []

for subject, score in marks.items():
    if score >= 75:
        strengths.append(subject)
    else:
        weaknesses.append(subject)

average = sum(marks.values()) / len(marks)

print("\n--- RESULT ---")
print("Student Name:", name)
print("Average:", round(average, 2))
print("Strengths:", strengths)
print("Weaknesses:", weaknesses)

