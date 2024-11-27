# week13_C_06.py
# id:20240000
# name:jang eunmee
from datetime import datetime

def diff_seconds(intime, outtime):
    if not outtime:
        outtime = datetime.now()
    return (outtime - intime).total_seconds()
    


str_fmt = "%Y-%m-%d %H:%M:%S"

books = []
while True:    
    number = input("도서번호:").strip()
    if not number:
        break
    while True:
        try:
            intime = input("대출시간:").strip()
            if intime:        
                intime = datetime.strptime(intime, str_fmt)
                break
        except:
            pass        

    while True:
        try:
            outtime = input("반납시간:").strip()
            if not outtime:
                outtime = None
            else:
                outtime = datetime.strptime(outtime, str_fmt)
            break
        except:
            pass

    book = {'num':number, 'in':intime, 'out':outtime}
    books.append(book)

for book in books:
    print(book['num'], book['in'], book['out'])
    print(diff_seconds(book['in'], book['out']))


    









    
    
























