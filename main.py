from conf.student import Student
from conf.teacher import Teacher



class Course:
    def __init__(self):
        self.student = []
        self.teacher = None

c1 = Course()
# print(c1.student, c1.teacher)

s1 = Student('학생', 29)
t1 = Teacher('선생', 30)

print(s1)
s1.app_for_course(c1)
c1.teacher = t1

print(c1.student, c1.teacher)


# c1.student = s1
# c1.teacher = t1

# print(c1.student, c1.teacher)
