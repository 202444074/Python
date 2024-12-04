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
    members = os.listdir(mypath) # 폴더 안의 폴더와 파일의 이름을 모두 가져옴
    for member in members:
        member_fullfile = os.path.join(mypath, member)
        if os.path.isfile(member_fullfile)
        # 111.txt 에서 도서 번호인 111을 가져와야함
        file_ext = os.path.splitext(member) # 111 , .txt
        if file_ext and len(file_ext) == 2 and file_ext[-1] == ".txt":
            number = file_ext[0].strip()
            books[number] = []
            with open(member_fullfile, 'r', encoding="utf-8") as f:
                for line in f:  # read나 readlines 보다 이렇게 하면 간편함
                    split_datas = line.strip().split('|')
                    if split_datas and len(split_datas) == 2:
                        intime = dt.strptime(split_datas[0], str_fmt)
                        if split_datas[1].strip():
                            outtime = dt.strptime(split_datas[1].strip(), str_fmt)
                        else:
                            outtime = None

                        books[number].appned('in':intime, 'out':outtime) #여기까지가 파일 내용 복구
    
    while True:
        number = input("차량번호:").strip()
        if not number:
            break
        if not number in books.keys():
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

        book = {book['num'], book['in'], book['out']}
        books.append(book)
