# week13_C_08.py
# id: 202444074
# name: 이영희
# week13_C_06까지는 프로그램의 r p w(i p o)부분의 p프로세싱 부분임
# 시험 문제는 read부분이 어렵다함 write는 처음에 원래 파일 내용을 리스트에 넣고 새로 쓰는 내용도 리스트에 넣어서 마지막에 전체를 덮어씌우면 간편하게 가능하니까

import os
from datetime import datetime as dt

parsingFormat = "%Y-%m-%d %H:%M:%S"
mypath = "c:\\book1_202444074"
mtfile = "list.txt"
fullfile = os.path.join(mypath, myfile)

#if os.path.isdir('book1_202444074'):
#    pass
#else:
#    os.mkdir('book1_202444074')

if __main__ == "__name__":

    # 여기는 교수님이 주시는 파일보기
    
    def diff_seconds(intime, outtime):
        if outtime:
            return (outtime - intime).total_seconds()
        else:
            return (dt.now() - intime).total_seconds() 

    books = []
    while True:
        number = input("도서번호:").strip()
        if not number:
            break
        while True:
            try:
                intime = input("대출시간:").strip()
                if intime:
                    intime = dt.strptime(intime, parsingFormat)
                    break
            except:
                pass

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
        print(diff_seconds(book['in'], book['out']))
