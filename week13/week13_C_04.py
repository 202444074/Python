# week13_C_04.py
# id: 202444074
# name: 이영희
# change: data -> book / all_data -> books

from datetime import datetime as dt


parsingFormat = "%Y-%m-%d %H:%M:%S"
books = []
while True:
    number = input("도서번호:").strip()
    if not number:
        break
    intime = input("대출시간:")
    inT = dt.strptime(intime, parsingFormat)  # 그냥 intime에 바로 넣어도 상관없음

    outtime = input("반납시간:")
    outT = dt.strptime(outtime, parsingFormat)

    book = {'num':number, 'in':inT, 'out':outT}
    books.append(book)

print(books)
for book in books:
    print(book['num'], book['in'], book['out'], type(book['out']))
