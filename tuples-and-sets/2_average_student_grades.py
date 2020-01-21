def avg(numbers):
    return sum(numbers) / len(numbers)


def solve(student_grades_strings):
    student_grades = {}
    for student_grade in student_grades_strings:
        (name, grade_str) = student_grade.split(' ')
        grade = float(grade_str)
        if name not in student_grades:
            student_grades[name] = []

        student_grades[name].append(grade)

    for (name, grades) in student_grades.items():
        grades_str = ' '.join(f'{x:.2f}' for x in grades)
        avg_grade = avg(grades)
        print(f'{name} -> {grades_str} (avg: {round(avg_grade, 3):.2f})')


n = int(input())
student_grades = [input() for _ in range(n)]

solve(student_grades)