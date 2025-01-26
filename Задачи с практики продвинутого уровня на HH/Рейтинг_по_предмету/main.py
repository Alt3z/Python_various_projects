class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}

    def add_courses(self, courses, score):
        self.courses[courses] = score


class CourseManager:
    def __init__(self):
        self.students = {}

    def add_students(self, requested_course, requested_score, student: Student):
        for student_courses in student.courses.keys():
            if student_courses == requested_course and student.courses[student_courses] > requested_score:
                if student.courses[student_courses] not in self.students:
                    self.students[student.courses[student_courses]] = [student.name]
                else:
                    self.students[student.courses[student_courses]] += [student.name]


students_info = input()
scores_info = input().split(",")

course_manager = CourseManager()
for stud in students_info.split(";"):
    student = Student(stud.split(",")[0])
    student.add_courses(stud.split(",")[1], stud.split(",")[2])

    course_manager.add_students(scores_info[0], scores_info[1], student)

if len(course_manager.students) > 0:
    for student in sorted(course_manager.students, reverse=True):
        print(f"{','.join(map(str,sorted(course_manager.students[student])))},{student}")
else:
    print("Никто")

