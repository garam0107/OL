class Person:
    # class 변수
    population = 0
    # 생성자 함수
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.increase()
    # 인스턴스 메서드
    def eat(self,name):
        print(f"{name}이 밥을 먹는다.")

    # 클래스 메서드
    # 데코레이터
    @classmethod
    def increase(cls):
        cls.population += 1

    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
# instance
p1 = Person('가람', 27)
p2 = Person('사람', 10)
# print(Person.population)
# p1.eat(p1.name)



    