# week11_02.py
import datetime

class Test:
    def __init__(self):  # class에서 만든 함수로 메소드임, self는 매개변수로 지역변수임
        name = "a"       # local
        self.name = "b"  # attr.
        self.age = 20    # 상동.
        print(datetime.datetime.now())  # datetime.py 파일안에 datetime클래스에 now메소드

t = Test()
print(t.name)
# 순서
# 1. Test() 생성자 호출
# 2. __new__() 메소드 자동 호츌
#    Test의 인스턴스를 생성
# 3. __init__() 메소드 자동 호출
#    Test의 인스턴스를 초기화
# 4. 생성한 인스턴스의 참조를 반환

t2 = Test()  
print(t2.name)  # t3 = t2라고 선언해도 생성된 Test의 인스턴스는 두 개

t.name = "김인하"
t2.name = "이인하"


print(id(t), id(t2))  # t와 t2의 메모리상의 위치, 같은 Test class지만 서로 다름
print(type(t) == type(t2))
print(t == t2)  # 위치가 달라 false
print(t.name == t2.name)
print(t.age == t2.age)
