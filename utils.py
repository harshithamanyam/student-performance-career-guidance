def get_marks(subject):
    while True:
        try:
            mark = int(input(f"{subject} marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
        except ValueError:
            print("Enter a valid number")

