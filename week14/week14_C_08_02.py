# week14_C_08_2.py
# id:20240000
# name:jang eunmee

from datetime import datetime as dt
import os

dtformat = "%Y-%m-%d %H:%M:%S"


def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.now()
    return (outtime - intime).total_seconds()


if __name__ == "__main__":
    mypath = "c:\\book2_202444074"  # 도서 번호로 파일을 새로 만들거라서 myfile 안만듦

    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    books = {}

    # read 작업해야 할 곳!
    # 파일이 있는지 확인
    # 있으면 파싱, 없으면 그대로 밑으로 떨어지면 됨.

    while True:
        number = input("차량번호:").strip()
        if not number:
            break
        if not number in books.keys(): # 추가한 부분
            books[number] = []
        else:
            for time in books[number]:
                if time['out'] == None:
                    print("반납 안 함")
                    continue

        while True:
            try:
                intime = input("대출시간:").strip()
                if intime:
                    intime = dt.strptime(intime, dtformat)
                    break
            except:
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
                pass

        times = {'in':intime, 'out':outtime}
        books[number].append(times)

        book_fullname = os.path.join(mypath, number + ".txt")
        with open(book_fullnam, 'a', encoding = "utf-8") as f:
            intime = dt.strftime(intime, str_fmt)
            if outtime:
                outtime = dt.strftime(outtime, str_fmt)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|") # \n을 안 하는 이유는 .append로 반납시간을 바로 붙일 수 있어서

    for number, times in books.items():
        print("책번호:", number)
        for time in times:
            print(time["in"], time["out"])
            print(diff_seconds(time["in"], time["out"]))

        book = {book['num'], book['in', book['out']}
        books.append(book)

    for car in cars:
        print(car["num"], car["in"], car["out"])
        print(diff_seconds(car["in"], car["out"]))

