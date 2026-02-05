import os
from utils import get_marks
from analysis import recommend_career

base_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(base_dir, "reports")
os.makedirs(reports_dir, exist_ok=True)

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

file_name = os.path.join(reports_dir, f"{name.replace(' ', '_')}_report.txt")

with open(file_name, "w") as f:
    f.write("STUDENT PERFORMANCE REPORT\n")
    f.write(f"Name: {name}\n")
    f.write(f"Career Recommendation: {career}\n")

print("Report saved at:", file_name)
