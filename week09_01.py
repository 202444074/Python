
# week09_01.py

data1 = [1, 2, 3, 4]


summary = sum(data1)
maximum = max(data1)
minimum = min(data1)
average = sum(data1) / len(data1)

print(summary)
print(maximum)
print(minimum)
print(average)

print("="*30)
for i in data1:
    print(i)

print("="*30)
for i in range(len(data1)):
    print(i)

print("="*30)
for i in range(len(data1)):
    print(f"data1[{i}]:{data1[i]}")

print("="*30)
for v in enumerate(data1):
    print(f"data1[{v[0]}]:{v[1]}")

print("="*30)
for idx, val in enumerate(data1):
    print(f"data1[{idx}]:{val}")

data2 = [
          [1, 2, 3]
        , [10, 20]
        , [11, 12, 13 ,14]
        ]

print("="*30)
for i in data2:
    print(i)

print("="*30)
for i in data2:  # 리스트
    print("sum", sum(i))
    print("max", max(i))
    print("min", min(i))
    print("avg", sum(i) / len(i))

print("="*30)
for i, v in enumerate(data2):  # 인덱스와 리스트
    print(f"{i+1}번째 : {v}")
    print("sum", sum(v))
    print("max", max(v))
    print("min", min(v))
    print("avg", sum(v) / len(v))

print("="*30)
for i, v in enumerate(data2):
    print(f"{i+1}번째 : ", end="")  # 줄바꿈 관련 부분
    for i2, v2 in enumerate(v):  # data2[i]말고 그냥 v
        print(f"[{i2}]{v2} ", end="")
    print()
    print("sum", sum(v))
    print("max", max(v))
    print("min", min(v))
    print("avg", sum(v) / len(v))













