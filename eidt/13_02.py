import datetime
from datetime import datetime as dt

parsingFormat = "%Y-%m-%d %H:%M:%S.%f"

d1 = dt.now()  # datetime.datetime
d2 = dt.strftime(d1, parsingFormat)  # datetime.datetime -> str
d3 = dt.strptime(d2, parsingFormat)  # str -> datetime.datetime

d4 = datetime. datetime(2030, 10, 2, 18, 0, 2, 200)  # 빌린 시간
d5 = datetime. datetime(2031, 10, 3, 17, 3, 3, 202)  # 돌려준 시간
d6 = datetime. datetime(2030, 10, 2) 

td = d5 - d4 # timedelta

print(td.days)
print(td.seconds)  # days를 제외한 seconds
print(td.microseconds)

print(td.total_seconds())  # 전체의 초단위 / hours 등은 없지만 이 값을 나누면 됨
d10 = d4 + datetime.timedelta(days=29)  # datetime
d11 = d4 + datetime.timedelta(days=-29)
