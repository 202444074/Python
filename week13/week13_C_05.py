# week13_C_05.py
# id: 202444074
# name: 이영희

from datetime import datetime as dt


parsingFormat = "%Y-%m-%d %H:%M:%S"
books = []
while True:
    number = input("도서번호:").strip()
    if not number:
        break
    while True:  # try 못쓰겠으면 while과 if로 먼저 구현 가능한 부분 만들기
        try:
            intime = input("대출시간:").strip()
            if intime:
                intime = dt.strptime(intime, parsingFormat)
                break  # break가 어디를 빠져나가는지 등을 생각하기
        except:
            pass  # continue도 상관없음 / 만약 메세지를 출력할거면 여기서

    while True:
        try:
            outtime = input("반납시간:").strip()
            if not outtime:
                outtime = None
            else:
                outtime = dt.strptime(outtime, parsingFormat)
            break
        except:
            pass

    book = {'num':number, 'in':intime, 'out':outtime}
    books.append(book)

print(books)
for book in books:
    print(book['num'], book['in'], book['out'], type(book['out']))
