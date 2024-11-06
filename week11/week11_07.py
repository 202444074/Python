# base : week11_03.py
# current : week11_07.py

class Point:
    def __init__(self, x=0.0, y=0.0):  # Point()에 다른 값을 넣어도 되고 안 넣으면 초기값이 나옴
        self.x = x
        self.y = y

    def __str__(self):  # 받은 정보를 문자열로 바꾸는 방법
        # 기본적으로는 타입+인스턴스주소를 문자열 반환
        # 조건: 무조건 문자열로 반환(리턴)
        # (0,0) 형태로 만들기
        return f"({self.x},{self.y})"

p = Point()
print(p.x, p.y)
p = Point(1,2)
print(p.x, p.y)
p = Point(y=1)
print(p.x, p.y)
print(p)

class Rectangle:
    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    # 사각형의 둘레를 구해서 반환하는 메소드
    def getRoundLength(self):
        return (self.width * 2) + (self.height * 2)

#여기서 바로 def로 함수를 만들어서 둘레를 구해도 되지만 사각형이나 삼각형의 둘레인지에 대한 소속이 애매해져서 메소드를 만드는 것
r = Rectangle(3,5,10,5)
print(r.getRoundLength())

class Subject:
    def __init__(self, num, sub, nm=None):  # 학번과 과제는 필수적으로 써야한다는 상황
        self.number = num
        self.sub = sub
        self.name = nm
        self.grade = None

#Subject()
Subject('001', '파이선')
#Subject('001', '파이선', 'lee', 4.5)

class Student:
    def __init__(self, nm, num, d, b):
        self.name = nm
        self.num = num
        self.dept = d
        self.birth = b

class Rectangle2:
    def __init__(self, sp=Point(), w=0.0, h=0.0):  # sp=Point() 형식
        self.spoint = sp
        self.width = w
        self.height = h

class Rectangle3:
    def __init__(self, sp=Point(), ep=Point()):
        self.spoint = sp
        self.epoint = ep
        
r = Rectangle3()
r.spoint.x = 1
r.spoint.y = 1

r.epoint.x = 10
r.epoint.y = 21









