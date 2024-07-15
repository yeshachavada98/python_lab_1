def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

def main():
    print("Enter marks for 5 subjects:")

    marks = []
    for i in range(5):
        subject_marks = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(subject_marks)

    total_marks = sum(marks)
    average_marks = total_marks / 5
    grade = calculate_grade(average_marks)

    print("\n----- Marksheet -----")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()