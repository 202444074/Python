# week11_03.py

'''
문제 예시
클래스 명 : Point (2d 좌표)
필요 속성 : x 위치(실수), y (실수)
'''

class Point:
    def __init__(self):
        self.x = 0.0  # x = 0.0은 지역변수
        self.y = 0.0

p = Point()
print(p.x, p.y)

'''속성 : x위치, y, 너비, 높이 (모두 실수)'''
class Rectangle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.width = 0.0
        self.height = 0.0

'''속성 : 학수번호(문자열), 과목명(문자열), 교수자(문자열), 학점(실수)''''
class Subject:
    def __init__(self):
        self.number = ""
        self.sub = ""
        self.name = ""
        self.grade = 0.0

''' 문자열 문자열 문자열 정수''''
class Student:
    def __init__(self):
        self.name = ""
        self.num = ""
        self.dept = ""
        self.birth = 0

'''Point 실수 실수'''
class Rectangle2:
    def __init__(self):
        self.spoint = Point()
        self.width = 0.0
        self.height = 0.0

'''Point Point'''
class Rectangle3:
    def __init__(self):
        self.spoint = Poin()
        self.epoint = Point()  # 시작점과 끝점을 설정할 수 있음

r = Rectangle3()
r.spoint.x = 1
r.spoint.y = 1

r.epoint.x = 10
r.epoint.y = 21









