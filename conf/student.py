# 상속
# 명시성 지켜주기 위하여 .을 찍어서 경로를 보여줌
from .base import Person
class Student(Person):
    def app_for_course(self, course):
        course.student.append(self)




s1 = Student('학생', 23)



    
