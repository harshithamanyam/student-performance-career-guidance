from utils import get_marks
from analysis import recommend_career

name = input("Enter student name: ")

marks = {
    "Math": get_marks("Math"),
    "Physics": get_marks("Physics"),
    "Programming": get_marks("Programming"),
    "Communication": get_marks("Communication"),
    "Creativity": get_marks("Creativity")
}

technical_avg = (marks["Math"] + marks["Physics"] + marks["Programming"]) / 3
soft_avg = (marks["Communication"] + marks["Creativity"]) / 2

career = recommend_career(technical_avg, soft_avg)

with open("report.txt", "w") as f:
    f.write(f"Student Name: {name}\n")
    f.write(f"Recommended Career: {career}\n")

print("Report saved successfully")
