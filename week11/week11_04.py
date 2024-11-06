# week11_04.py


class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birth = 0

lee = Student()
lee.name = input("name: ")
lee.number = input("number: ")
lee.dept = input("dept: ")
lee.birth = int(input("birth: "))  # 정수형 int로 변환
kim = Student()
kim.name = input("name: ")
kim.number = input("number: ")
kim.dept = input("dept: ")
kim.birth = int(input("birth: ")) 

print(lee.name, lee.number, lee.dept, lee.birth)
print(kim.name, kim.number, kim.dept, kim.birth)


students = []
for i in range(3):  # 여러명의 데이터가 들어갈 것이기 때문에 리스트나 딕셔너리를 만들어 놓아야함
    stu = Student()
    stu.name = input("name: ")
    stu.number = input("number: ")
    stu.dept = input("dept: ")
    stu.birth = int(input("birth(yyyy): "))
    students.append(stu)

for i in students:  # type(i) => Student
    print(i.name)

# 고려사항 : 동일한 학번이 들어올 때, list가 아닌 dict로 구성(key -> number), while로 구성하는 것이 더 합리적으로 보이는데 구성한다면 어떻게















