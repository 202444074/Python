class Subject:
    def setGrade(self, grade):
        if grade != None and (grade < 0 or grade > 4.5):
            grade = None
        self.grade = grade

    def __init__(self, number, name, teacher=None, grade=None):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.setGrade(grade)

    def __str__(self):
        return f"[{self.number}] {self.name}"

class Student:
    def totalGrade(self):
        if self.subjects:
            grades = [ sub.grade for sub in self.subjects if sub.grade != None]
            if grades:
                return sum(grades) / len(grades)
        else:
            return None
          
    def __init__(self, number, name, dept, birthyear, *subjects):
        self.number = number
        self.name = name
        self.dept = dept
        self.birthyear = birthyear
        if subjects:
            self.subjects = list(subjects)
        else:
            self.subjects = list()
          
st = Student("2", "김영희", "컴정", 2024
             , Subject("001", "파이썬", "김인하", grade=4.5)
             , Subject("002", "자바스크립트", "전혜경"))
