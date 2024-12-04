import datetime
from datetime import datetime as dt

d1 = datetime.datetime.now()  # 모듈.클래스.매소드()
print(d1,type(d1))

d2 = dt.now()  # 클래스.매소드()

print(d2.year)
print(d2.month)
print(d2.day)
print(d2.hour)
print(d2.minute)
print(d2.second)
print(d2.microsecond) # 밀리세컨드 쓸거면 /1000

print(d2.weekday())  # 월요일부터 0
print(d2.date())
print(d2.time())
