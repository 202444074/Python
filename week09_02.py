data3 = {
    "김인하": [1, 2],
    "이인하": [10, 20, 30, 40, 50, 60, 70],
    "송인하": [11, 12, 13, 14],
    }

print("-"*30)
for k in data3:  # data3.keys()와 같음
    print(k)

print("-"*30)
for k in data3:
    print(data3[k])  

print("-"*30)
for k in data3:
    print(k,":",data3[k])


print("-"*30)
for k in data3:
    print(f"{k} : ", end="")
    for i, v in enumerate(data3[k]):
        print(f"[{i+1}]{v} ", end="")
    print()
    print("sum", sum(data3[k]))
    print("max", max(data3[k]))
    print("min", min(data3[k]))
    print("avg", sum(data3[k])/len(data3[k]))
'''
# week09_02.py

data2 = [
          [1, 2, 3]
        , [10, 20]
        , [11, 12, 13 ,14]
        ]

data3 = {
    "김인하": [1, 2],
    "이인하": [10, 20, 30, 40, 50, 60, 70],
    "송인하": [11, 12, 13, 14],
    }

def print_info(datas):
    for i2, v2 in enumerate(datas):
        print(f"[{i2}]{v2} ", end="")
    print()
    print("sum", sum(datas))
    print("max", max(datas))
    print("min", min(datas))
    print("avg", sum(datas) / len(datas))
    

    
def analyze_list(datas):
    for i, v in enumerate(datas):
        print(f"{i+1}번째 : ", end="")
        print_info(datas)

def analyze_dict(datas):
    for k in datas:
        print(f"{k} : ", end="")
        print_info(datas[k])

def analyze_score(datas):
    if isinstance(datas, list):
        analyze_list(datas)
    elif isinstance(datas, dict):
        analyze_dict(datas)
    else:
        print("분석 불가")
            

analyze_list(data2)
analyze_dict(data3)
analyze_score(data3)
'''
