#week10_06.py
#교안에 없는 내용

class Score:
    def __init__(self, k, m, e):  # _두개는 매직 메소드
        self.kor = k
        self.mat = m
        self.eng = e
    def average(self):  # 메소드
        return (self.kor + self.mat + self.eng) / 3

score3 = Score(10, 20, 30)  # self는 Score자체
print(score3.kor, score3.mat, score3.eng)
print(score3.average())
score3.kor = 100
print(score3.kor, score3.mat, score3.eng)
print(score3.average())

scores1 = [10, 20, 30]
scores2 = {'k':10, 'e':20, 'm':30}

def average_list(datas):
    return sum(datas) / len(datas)

def average_dict(datas):
    return sum(datas.values()) / len(datas)

print(average_list(scores1))
print(average_dict(scores2))
