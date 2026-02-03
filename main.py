name = input("Enter student name: ")

subjects = ["Math", "Physics", "Programming", "Communication", "Creativity"]
marks = {}

for subject in subjects:
    marks[subject] = int(input(f"{subject} marks: "))

technical_avg = (marks["Math"] + marks["Physics"] + marks["Programming"]) / 3
soft_avg = (marks["Communication"] + marks["Creativity"]) / 2

if technical_avg >= 80:
    career = "Software / IT field"
elif soft_avg >= 80:
    career = "Management / HR"
else:
    career = "General skill-based career"

print("\n--- RESULT ---")
print("Student Name:", name)
print("Technical Average:", technical_avg)
print("Soft Skill Average:", soft_avg)
print("Recommended Career:", career)


