# week11_05.py

class Test:
    def __init__(self):
        self.name = None
        self.age = None
        
    def func(self, name, age):
        self.name = name
        print(age)

t = Test()  # 적어도 func를 호출해야 name과 age에 들어가는데 init은 자동으로 호출함
print(t.name)
print(t.age)


t = Test()
t.func("김인하", 20)  # t.func()는 t.func(t)와 같음
print(t.name)
print(t.age)

print('-'*30)

class In:
    def func(self):
        print("In.func()")

class Out:
    def method(self):
        print("Out.method()")
# func()  # 각갂 in out에 소속되어 있기 때문에 func와 method의 존재를 몰라서 오류 발생
# method()

# Out.method()  # self에서 오류 발생
# In.func()

i = In()
o = Out()

# 실제로는 잘 안쓰이는 정석 표현
Out.method(o)
In.func(i)
str.upper('a')

# 많이 쓰는 약식 표현
i.func()
o.method()
'a'.upper()

# In.func(o)  # 지금은 self를 사용하지 않아 오류가 발생하지 않음
# o.func()  # 하지만 이건 무조건 오류가 발생해 오히려 약식이 더 안전함
