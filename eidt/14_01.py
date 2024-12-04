from week14_c_book import Book2 as Book
from week14_c_book import timeStamp
from datetime import datetime as dt
import os
import random
str_fmt = "%Y-%m-%d %H:%M:%S"

def gen_book_code():  # 도서번호 직접 입력 안 하고 바로 부여하는 방법
    #A1000_00
    class_chars = "ABCDEFG"
    #front_num = random.randrange(1000, 10000, 2) # 1000~9999 2씩
    front_num = f"{random.randint(1000, 9999)}" # 1000~9999
    rear_num = f"{random.randint(10, 99)}"
    class_num = random.choice(class_chars) # 문자열 리스츠 튜플 모두 사용가능
    return f"{class_num}{front_num}_{rear_num}"

def gen_renttime():
    return dt.now() - datetime.timedelta(hours=random.randint(0, 10), minutes=random.randint(0,60)) # days부터 microseconds까지 가능
def gen_returntime():
    return dt.now() + datetime.timedelta(hours=random.randint(0, 48), minutes=random.randint(0,60))

if __name__ == "__main__":
    mypath = "c:\\book2_202444074"

    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    books = []
    members = os.listdir(mypath)    
    for member in members:
        member_fullfile = os.path.join(mypath, member)
        if os.path.isfile(member_fullfile)
        # 111.txt 에서 도서 번호인 111을 가져와야함
        file_ext = os.path.splitext(member) # 111 , .txt
        if file_ext and len(file_ext) == 2 and file_ext[-1] == ".txt":
            number = file_ext[0].strip()
            book = Book(number) # book을 만듦
            with open(member_fullfile, 'r', encoding="utf-8") as f:
                for line in f:
                    split_datas = line.strip().split('|')
                    if split_datas and len(split_datas) == 2:
                        intime = dt.strptime(split_datas[0], str_fmt)
                        if split_datas[1].strip():
                            outtime = dt.strptime(split_datas[1].strip(), str_fmt)
                        else:
                            outtime = None

                        book.add_timestamp(intime, outtime) # history안에 추가됨
            if book.history:
                books.append(book)
    
    while True:
        number = input("신규 도서 입력?").strip()
        if not number:
            break
        else:
            number = gen_book_code()

        search_book = [book for book in books if book.number == number]

        if not search_book:
            book = Book(number)
            books.appned(book)
        else:
            book = search_book[0]
            for timestamp in book.history:
                if timestamp.is_rent():
                    print("반납 안 함")
                    continue

        while True:
            try:
                intime = input("대출시간:").strip()
                if intime:
                    intime = dt.strptime(intime, dtformat)
                    break
                else:
                    intime = gen_renttime()
                    break
            except:
                intime = gen_renttime()
                pass

        while True:
            try:
                outtime = input("반납시간:").strip()
                if not outtime:
                    outtime = None
                    break
                outtime = dt.strptime(outtime, dtformat)
                break
            except:
                outtime = gen_returntime()
                break
              
        book.add_timestamp(intime, outtime)

        book_fullname = os.path.join(mypath, number + ".txt")
        with open(book_fullnam, 'a', encoding = "utf-8") as f:
            intime = dt.strftime(intime, str_fmt)
            if outtime:
                outtime = dt.strftime(outtime, str_fmt)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")

    for book in books:
        print("책번호:", book.number)
        for timestamp in book.history:
            print(timestamp.renttime, timestamp.returntime)
            print(timestamp.diff_seconds)
