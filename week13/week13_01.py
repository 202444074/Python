# 날짜 시간 출력하고 나머지는 연습문제 풀고 남은 문제 과제로 하거나 다음주에 이어서 하고 다음주도 주어진 문제 푸는 방식으로 하신다 함
# week13_01.py
# id: 202444074
# name: 이영희

import datetime
from datetime import datetime as dt

d1 = datetime.datetime.now()  # 모듈.클래스.매소드()
print(d1,type(d1))

d2 = dt.now()  # 클래스.매소드()
print(dt.now())
print(d2,type(d2))


print(d2.year)
print(d2.month)
print(d2.day)
print(d2.hour)
print(d2.minute)
print(d2.second)
print(d2.microsecond) # 밀리세컨드 쓸거면 /1000

print("="*20)

print(d2.weekday())  # 월요일부터 0
print(d2.date(), type(d2.date()))
print(d2.time(), type(d2.time()))
