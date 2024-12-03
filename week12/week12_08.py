# week12_08.py

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r**2)


def add(a, b):
    return a + b

if __name__ == "__main__":  # 여기 모듈 안에서만 작동하는 듯함
    print(add(1,2))
    print(type(Math()))
# 그냥 print하면 이걸 불러올때 마다 작동하니까 이름이 main일 때만 작동하도록 
# if문 안에 넣음. 그래서 선생님도 type으로 <class '__main__.Math'> 을 보여준 듯
