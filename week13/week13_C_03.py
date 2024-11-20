# week13_C_03.py
# id: 202444074
# name: 이영희


all_data = []
while True:
    number = input("도서번호:").strip()
    if not number:
        break
    intime = input("대출시간:")
    outtime = input("반납시간:")
    data = {}  # 도서번호를 입력 안하면 낭비하는 경우를 방지
    data['num'] = number
    data['in'] = intime
    data['out'] = outtime
    # data = {'num': number, 'in':intime, 'out':outtime} 을 쓰면 딕셔너리를 만듬과 동시에 값을 넣음
    all_data.append(data)

print(all_data)
for data in all_data:
    print(data['num'], data['in'], data['out'])
